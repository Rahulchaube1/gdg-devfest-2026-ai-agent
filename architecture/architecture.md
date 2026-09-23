# System Architecture

This document describes the reference architecture used in the **From LLM to Reliable AI Agent** session.

## 1. End-to-end architecture

```mermaid
flowchart TB
    U[User / Application] --> V[Input Validation]
    V --> O[Agent Orchestrator]
    O --> M[Model / Reasoning]
    O --> C[Context Manager]
    O --> P[Policy Engine]
    C --> R[Retrieval]
    C --> MEM[Memory]
    M --> TG[Tool Gateway]
    P --> TG
    TG --> TV[Tool Validation]
    TV --> A{Authorization}
    A -->|Read-only| RT[Read Tool]
    A -->|State-changing| AP[Approval Gate]
    AP -->|Approved| WT[Write Tool]
    AP -->|Denied| B[Blocked Action]
    RT --> X[External API / Runtime]
    WT --> X
    X --> S[External State]
    O --> OBS[Observability]
    X --> OBS
    OBS --> EVAL[Evaluation]
```

### Architectural rule

> **The model proposes; application code authorizes.**

The model can propose a tool and arguments. It should not be the final authority for identity, permissions, irreversible actions, or access to protected state.

---

## 2. Control-plane vs execution-plane

```mermaid
flowchart LR
    subgraph CP[Control Plane]
        POL[Policy]
        AUTH[Authorization]
        EVAL[Evaluation]
        OBS[Observability]
    end

    subgraph EP[Execution Plane]
        MODEL[Model]
        CTX[Context / Retrieval]
        TOOLS[Tool Gateway]
        EXT[External Systems]
    end

    POL --> TOOLS
    AUTH --> TOOLS
    MODEL --> TOOLS
    CTX --> MODEL
    TOOLS --> EXT
    MODEL --> OBS
    TOOLS --> OBS
    EXT --> OBS
    OBS --> EVAL
    EVAL --> POL
```

This separation makes operational controls independent from model behavior.

---

## 3. Tool execution sequence

```mermaid
sequenceDiagram
    participant U as User
    participant A as Application
    participant M as Model
    participant G as Tool Gateway
    participant Z as Authorization
    participant T as Tool
    participant X as External System

    U->>A: Request
    A->>M: Validated context
    M-->>A: Proposed tool + arguments
    A->>G: Structured tool request
    G->>G: Schema + argument validation
    G->>Z: Authorization check
    alt Read-only
        Z-->>G: Allow
        G->>T: Execute
        T->>X: Read
        X-->>T: Result
        T-->>G: Result
    else State-changing
        Z-->>G: Approval required
        G-->>A: Request approval
        A->>Z: Approval decision
        alt Approved
            Z-->>G: Allow
            G->>T: Execute
            T->>X: Write
            X-->>T: Result
            T-->>G: Result
        else Denied
            Z-->>G: Deny
        end
    end
    G-->>A: Structured result
    A->>A: Record trace / evaluation event
```

---

## 4. Trust boundaries

```mermaid
flowchart LR
    U[User Input] -->|TB-1| APP[Application]
    APP -->|TB-2| MODEL[Model]
    RET[External Retrieval] -->|TB-3 Untrusted Content| CTX[Context]
    MODEL -->|TB-4 Proposed Action| GATE[Tool Gateway]
    GATE -->|TB-5 Authorized Action| EXT[External System]
```

Every boundary should have an explicit control rather than relying on the model to enforce it.

| Boundary | Control |
|---|---|
| User → Application | Input validation and identity |
| Application → Model | Context and data minimization |
| Retrieval → Context | Treat content as untrusted |
| Model → Tool Gateway | Structured contracts and validation |
| Tool Gateway → External System | Authorization and least privilege |
| Runtime → Operations | Audit events, traces, metrics, evaluation |

---

## 5. Failure containment

```mermaid
flowchart TD
    REQ[Request] --> DEC[Model Decision]
    DEC --> VAL{Valid tool request?}
    VAL -->|No| BLOCK1[Reject + Log]
    VAL -->|Yes| AUTH{Authorized?}
    AUTH -->|No| BLOCK2[Reject + Log]
    AUTH -->|Approval needed| APR{Approved?}
    APR -->|No| BLOCK3[Reject + Log]
    APR -->|Yes| EXEC[Execute]
    AUTH -->|Yes| EXEC
    EXEC --> RES{Execution result}
    RES -->|Success| TRACE[Trace + Evaluate]
    RES -->|Failure| ERR[Error + Trace + Recover]
```

The objective is not to eliminate every failure. It is to **bound failure, make it visible, and prevent an invalid model output from becoming an uncontrolled external action**.

---

## 6. Evaluation loop

```mermaid
flowchart LR
    CASE[Test Case] --> RUN[Agent Run]
    RUN --> TRACE[Execution Trace]
    TRACE --> MET[Behavior Metrics]
    MET --> REG[Regression Set]
    REG --> DEC{Accept / Investigate}
    DEC -->|Accept| DEPLOY[Deploy]
    DEC -->|Investigate| FIX[Change Model / Prompt / Tool / Policy]
    FIX --> RUN
```

Recommended evaluation dimensions:

- Outcome
- Tool selection
- Tool arguments
- Trajectory
- Grounding
- Safety
- Latency/cost where relevant
- Regression against prior cases

---

## 7. Production path

```mermaid
flowchart LR
    LOCAL[Local Prototype] --> TEST[Deterministic Tests]
    TEST --> EVAL[Behavioral Evaluation]
    EVAL --> STAGE[Staging]
    STAGE --> OBS[Instrumented Deployment]
    OBS --> PROD[Production]
    PROD --> FB[Failures / Feedback]
    FB --> EVAL
```

A prototype becomes production-oriented when the system has explicit controls around **execution, authorization, evaluation, and operations**, not simply when a model API is connected.

## Design principles

1. **Explicit contracts** — every tool has a defined purpose and input shape.
2. **Least privilege** — tools receive only the permissions they need.
3. **External authorization** — permissions are enforced by application code.
4. **Approval for high-impact actions** — risky state changes can require human or policy approval.
5. **Untrusted retrieval** — retrieved text is data, not policy.
6. **Observable execution** — important decisions and tool calls are traceable.
7. **Behavioral evaluation** — evaluate the agent's actions, not only its final prose.
8. **Reproducibility** — examples should be runnable and inspectable locally.
