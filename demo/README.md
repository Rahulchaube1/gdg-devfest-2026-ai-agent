# Demo

This directory contains the deterministic demonstration used to explain the agent architecture.

## Run

From the demo/agent directory, run: `python agent.py`

No API key is required.

## Components

- `agent/agent.py` — orchestration and authorization example
- `agent/tools.py` — explicit tool contracts and validation
- `evaluation/evaluation_cases.json` — behavioral evaluation cases

## Live integration

A real Gemini/ADK or other model integration can replace the deterministic `model_decide()` function while keeping the same tool boundary and authorization design.

The local version is intentionally deterministic so the talk remains reproducible during rehearsal.
