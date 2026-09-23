"""Tool-contract examples for the session."""

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class ToolContract:
    name: str
    purpose: str
    input_schema: dict
    read_only: bool
    requires_approval: bool


PUBLIC_LOOKUP = ToolContract(
    name="public_lookup",
    purpose="Read public information.",
    input_schema={
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
    read_only=True,
    requires_approval=False,
)

WRITE_RECORD = ToolContract(
    name="write_record",
    purpose="Change external state.",
    input_schema={
        "type": "object",
        "properties": {"record": {"type": "string"}},
        "required": ["record"],
    },
    read_only=False,
    requires_approval=True,
)


def validate_string(value: Any) -> bool:
    return isinstance(value, str) and 0 < len(value.strip()) <= 500


def validate_tool_input(contract: ToolContract, arguments: dict) -> tuple[bool, str]:
    required = contract.input_schema.get("required", [])
    for field in required:
        if field not in arguments:
            return False, f"Missing required field: {field}"

    if contract.name == "public_lookup" and not validate_string(arguments["query"]):
        return False, "Invalid query"

    if contract.name == "write_record" and not validate_string(arguments["record"]):
        return False, "Invalid record"

    return True, "valid"
