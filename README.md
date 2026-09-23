# From LLM to Reliable AI Agent

### Building, Securing and Scaling Open-Source AI Systems

[![GDG Chennai DevFest 2026](https://img.shields.io/badge/GDG%20Chennai-DevFest%202026-111111?style=flat-square)](https://github.com/Rahulchaube1/gdg-devfest-2026-ai-agent)
[![Level](https://img.shields.io/badge/level-intermediate-111111?style=flat-square)](https://github.com/Rahulchaube1/gdg-devfest-2026-ai-agent)
[![Format](https://img.shields.io/badge/format-general%20technical%20talk-111111?style=flat-square)](https://github.com/Rahulchaube1/gdg-devfest-2026-ai-agent)

> **GDG Chennai DevFest 2026 speaker-session repository** by **Rahul Chaube**, Founder & CEO of EverestQAI.

This repository contains the technical material, reference architecture, live-demo code, evaluation cases, security model, speaker notes, and supporting documentation for:

> **From LLM to Reliable AI Agent: Building, Securing and Scaling Open-Source AI Systems**

The session focuses on the engineering work required to move beyond a basic LLM call and build AI systems that are **observable, evaluable, secure, maintainable, and production-oriented**.

## Session at a glance

| Field | Details |
|---|---|
| Speaker | Rahul Chaube |
| Organisation | EverestQAI |
| Role | Founder & CEO |
| Focus | AI/LLM Systems · Agentic AI · Open Source · AI Infrastructure |
| Format | General Technical Talk |
| Level | Intermediate |
| Duration | 55 minutes |
| Event | GDG Chennai DevFest 2026 |
| Venue | IITM Research Park, Chennai |
| Date | 17 October 2026 |
| Contact | rahulchaube900@gmail.com |

## Why this session

An LLM can generate an answer. A production AI system has to do considerably more.

Once an AI application can call tools, retrieve information, maintain state, interact with APIs, modify external systems, or make multi-step decisions, the engineering problem changes.

The system now needs explicit **tool contracts, authorization boundaries, context management, evaluation, observability, failure handling, and deployment controls**.

This session demonstrates that transition with a practical, code-first workflow.

## Learning outcomes

Attendees will learn to:

1. Understand agent architecture across models, context, memory, retrieval, tools, policy, evaluation, and observability.
2. Build a small tool-using agent around explicit contracts.
3. Apply validation, authorization, least privilege, and approval gates.
4. Evaluate outcomes, tool selection, arguments, grounding, safety, and regressions.
5. Understand the path from local prototype to observable production service.

## Core engineering principle

> **The model proposes; application code authorizes.**

LLM output should not be treated as an authorization decision. A reliable architecture separates probabilistic reasoning from deterministic validation, authorization, execution, and observability.

## Reference architecture

The repository includes Mermaid diagrams for the end-to-end system, control/execution planes, tool execution sequence, trust boundaries, failure containment, evaluation loop, and production path. GitHub renders these diagrams directly.

```text
                         USER / APPLICATION
                                |
                         Input Validation
                                |
                                v
                       AGENT ORCHESTRATOR
                    _________/ | \\_________
                   /           |            \\
                MODEL       CONTEXT        POLICY
                              /  \\
                         MEMORY  RETRIEVAL
                              |
                              v
                         TOOL GATEWAY
                       /      |       \\
                    READ     WRITE   EXTERNAL API
                              |
                    AUTHORIZATION / APPROVAL
                              |
                              v
                     EXTERNAL STATE / RUNTIME
                              |
                       +------+------+
                       |             |
                 OBSERVABILITY    EVALUATION
```

### Design boundaries

| Boundary | Principle |
|---|---|
| User → Application | Validate inputs and establish identity/context |
| Application → Model | Control model-visible context |
| Retrieval → Context | Treat external content as untrusted |
| Model → Tools | Validate structured tool requests |
| Tools → External systems | Enforce authorization outside the model |
| Runtime → Operations | Log, trace, monitor, and evaluate behavior |

## Live demonstration

The demo intentionally shows failure before success so the audience can see why each engineering control exists.

1. Minimal LLM-style request
2. Read-only tool
3. Structured tool contract
4. Context/retrieval
5. Malformed arguments
6. Unsafe state-changing request
7. Authorization / approval gate
8. Behavioral evaluation
9. Structured observability
10. Production deployment path

The repository includes a deterministic local demo so the workflow can be rehearsed without an API key or external model service.

## Evaluation approach

The session does not treat final generated prose as the only quality signal.

- **Outcome** — Did the task succeed?
- **Tool selection** — Was the appropriate tool selected?
- **Tool arguments** — Were inputs valid and constrained?
- **Trajectory** — Did the system follow an acceptable execution path?
- **Grounding** — Did it use the required evidence?
- **Safety** — Did it block or escalate unsafe actions?
- **Regression** — Did a model, prompt, or tool change break previous behavior?

See [`demo/evaluation/evaluation_cases.json`](demo/evaluation/evaluation_cases.json).

## Security model

The session covers prompt injection, excessive agency, unsafe tool execution, sensitive-data exposure, weak authorization, and untraceable failures.

Controls include least privilege, server-side authorization, typed schemas, argument validation, approval gates, data minimization, structured audit events, and behavioral evaluation.

See [`architecture/threat-model.md`](architecture/threat-model.md) for the threat matrix, trust boundaries, defense-in-depth model, and security review checklist.

## Architecture & technical diagrams

- [`architecture/architecture.md`](architecture/architecture.md) — end-to-end architecture, control plane, execution sequence, trust boundaries, failure containment, evaluation loop, and production path
- [`architecture/threat-model.md`](architecture/threat-model.md) — threat model, security controls, defense-in-depth, and review checklist

## Repository structure

```text
.
├── README.md
├── LICENSE
├── PACKAGE_MANIFEST.txt
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── .gitignore
├── slides/
│   └── presentation-outline.md
├── demo/
│   ├── README.md
│   ├── agent/
│   │   ├── agent.py
│   │   ├── tools.py
│   │   └── requirements.txt
│   └── evaluation/
│       └── evaluation_cases.json
├── architecture/
│   ├── architecture.md
│   └── threat-model.md
├── speaker-notes/
│   └── run-of-show.md
├── docs/
│   ├── CFP-summary.md
│   └── attendee-takeaways.md
└── assets/
    └── README.md
```

## Quick start

Requirements: Python 3.10+. The deterministic demo uses the Python standard library only; no API key is required.

```bash
cd demo/agent
python agent.py
```

Start exploring with:
- [`slides/presentation-outline.md`](slides/presentation-outline.md)
- [`architecture/architecture.md`](architecture/architecture.md)
- [`architecture/threat-model.md`](architecture/threat-model.md)
- [`demo/agent/agent.py`](demo/agent/agent.py)
- [`demo/agent/tools.py`](demo/agent/tools.py)
- [`demo/evaluation/evaluation_cases.json`](demo/evaluation/evaluation_cases.json)
- [`speaker-notes/run-of-show.md`](speaker-notes/run-of-show.md)

## Presentation / CFP link

**Use this repository URL in the CFP “Link to your presentation” field:**

https://github.com/Rahulchaube1/gdg-devfest-2026-ai-agent

A separate speaker proposal PDF can be submitted through the CFP supporting-file upload.

## Speaker

### Rahul Chaube

**Founder & CEO, EverestQAI**

Rahul Chaube is an AI/LLM builder focused on open-source AI systems, agentic applications, model evaluation, AI infrastructure, and practical production engineering.

**Contact:** rahulchaube900@gmail.com

## Session flow

| Time | Section | Focus |
|---:|---|---|
| 00–05 | The agentic shift | Why model calls become systems problems |
| 05–12 | Architecture | Model, context, retrieval, tools, policy |
| 12–25 | Build | Live tool-using agent |
| 25–35 | Secure | Threats, authorization, validation |
| 35–43 | Evaluate | Behavioral evaluation and regression |
| 43–50 | Scale | Telemetry, deployment, failure handling |
| 50–55 | Q&A | Takeaways and discussion |

## Technical positioning

This is not a generic introduction to generative AI, a prompt-engineering-only session, or a product pitch.

It is a **developer-focused engineering session** about the architecture and operational boundaries required when AI systems can act.

## Research and technical basis

The session uses established software-engineering principles for validation, authorization, observability, evaluation, and least-privilege system design. Security topics are presented as engineering controls rather than as claims of guaranteed safety.

The repository avoids unsupported performance claims. Any future benchmark should document its dataset, methodology, model/version, runtime context, and reproducible evaluation procedure.

## Project health and contribution

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing changes and [`SECURITY.md`](SECURITY.md) for responsible vulnerability reporting.

## License

The demo and supporting code are released under the [MIT License](LICENSE).

## Status

**CFP / Speaker Session Repository — GDG Chennai DevFest 2026**

Prepared by Rahul Chaube · September 2026