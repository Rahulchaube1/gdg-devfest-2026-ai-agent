# Speaker Run-of-Show

## 0–5 minutes
Introduce the problem. Do not spend time explaining generic AI history.

Opening:
> “An LLM can generate an answer in milliseconds. The engineering challenge starts when we allow that answer to influence real actions.”

## 5–12 minutes
Walk through the architecture. Emphasize boundaries.

## 12–25 minutes
Live build:
1. minimal model interaction
2. read-only tool
3. context
4. failure case
5. controlled execution

## 25–35 minutes
Security:
- prompt injection
- excessive agency
- authorization
- approval

## 35–43 minutes
Evaluation:
- outcomes
- trajectories
- grounding
- safety
- regression

## 43–50 minutes
Production:
- telemetry
- deployment
- retries
- state
- rollout

## 50–55 minutes
Takeaways and Q&A.

## Demo fallback
If live APIs fail:
- run the deterministic local demo
- show the architecture
- show evaluation JSON
- explain where Gemini/ADK integration plugs in

Never claim a live external API succeeded if it did not.
