"""
Minimal framework-neutral agent demo for GDG Chennai DevFest 2026.

This example intentionally uses deterministic local tools instead of
requiring an API key. Replace `model_decide()` with Gemini/ADK or another
provider during the live demonstration.
"""

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Tool:
    name: str
    description: str
    handler: Callable[..., Any]
    read_only: bool = True


def public_lookup(query: str) -> dict:
    """Safe read-only example tool."""
    return {
        "query": query,
        "source": "demo-local",
        "result": f"Public information placeholder for: {query}",
    }


def write_record(record: str) -> dict:
    """State-changing tool used only to demonstrate authorization."""
    return {"written": False, "reason": "Demo blocks state-changing operations by default."}


TOOLS = {
    "public_lookup": Tool(
        "public_lookup",
        "Look up public information.",
        public_lookup,
        read_only=True,
    ),
    "write_record": Tool(
        "write_record",
        "Write a record to external state.",
        write_record,
        read_only=False,
    ),
}


def authorize(tool: Tool, approved: bool = False) -> bool:
    """The application—not the model—controls authorization."""
    if tool.read_only:
        return True
    return approved


def execute_tool(name: str, arguments: dict, approved: bool = False) -> dict:
    if name not in TOOLS:
        raise ValueError(f"Unknown tool: {name}")

    tool = TOOLS[name]

    if not authorize(tool, approved=approved):
        return {
            "ok": False,
            "blocked": True,
            "reason": "Authorization/approval required.",
        }

    try:
        result = tool.handler(**arguments)
        return {"ok": True, "blocked": False, "result": result}
    except Exception as exc:
        return {"ok": False, "blocked": False, "error": str(exc)}


def model_decide(task: str) -> dict:
    """
    Deterministic stand-in for a model decision.
    In the live talk, replace this with a real model/tool-calling API.
    """
    return {
        "tool": "public_lookup",
        "arguments": {"query": task},
    }


def run(task: str) -> dict:
    decision = model_decide(task)
    return execute_tool(
        decision["tool"],
        decision["arguments"],
        approved=False,
    )


if __name__ == "__main__":
    print(run("GDG Chennai DevFest 2026"))
