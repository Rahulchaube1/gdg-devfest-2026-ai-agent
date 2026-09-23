# Reference Architecture

```text
User / Application
        |
        v
Input Validation
        |
        v
Agent Orchestrator
   |       |       |
 Model   Context  Policy
           |
      +----+----+
      |         |
    Memory   Retrieval
           |
           v
      Tool Gateway
      /    |     \
   Read  Write  External API
           |
    Authorization
     + Approval
           |
           v
 External State / Runtime
           |
    +------+------+
    |             |
 Observability  Evaluation
```

## Boundary principles

1. The model proposes; application code authorizes.
2. Tools have explicit contracts.
3. State-changing tools receive stricter controls than read-only tools.
4. Retrieved content is untrusted input.
5. Logs and evaluations should make behavior inspectable.
