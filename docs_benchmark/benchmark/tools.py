"""Controlled in-memory tool loop for benchmark ablations."""

from __future__ import annotations

import ast
import json
import re
import time
from dataclasses import dataclass, field
from typing import Any, Protocol

from docs_benchmark.accounts import ACCOUNT_TYPES
from docs_benchmark.benchmark.analysis import serialize_balance_sheet
from docs_benchmark.benchmark.parser import _extract_json_blob, parse_submission
from docs_benchmark.inconsistencies import INCONSISTENCY_CODES
from docs_benchmark.ledger import Ledger
from docs_benchmark.schemas import DocumentRecord, Posting


TOOL_VARIANT_NO_TOOLS = "no_tools"
TOOL_VARIANT_CALCULATOR = "calculator"
TOOL_VARIANT_DOCUMENT_SEARCH = "document_search"
TOOL_VARIANT_LEDGER_CHECK = "ledger_check"
TOOL_VARIANT_FULL_TOOL_AGENT = "full_tool_agent"
TOOL_VARIANTS = (
    TOOL_VARIANT_NO_TOOLS,
    TOOL_VARIANT_CALCULATOR,
    TOOL_VARIANT_DOCUMENT_SEARCH,
    TOOL_VARIANT_LEDGER_CHECK,
    TOOL_VARIANT_FULL_TOOL_AGENT,
)

TOOL_CALCULATOR = "calculator"
TOOL_DOCUMENT_SEARCH = "document_search"
TOOL_LEDGER_CHECK = "ledger_check"
TOOL_INCONSISTENCY_CHECK = "inconsistency_check"

TOOLS_BY_VARIANT = {
    TOOL_VARIANT_NO_TOOLS: (),
    TOOL_VARIANT_CALCULATOR: (TOOL_CALCULATOR,),
    TOOL_VARIANT_DOCUMENT_SEARCH: (TOOL_DOCUMENT_SEARCH,),
    TOOL_VARIANT_LEDGER_CHECK: (TOOL_LEDGER_CHECK,),
    TOOL_VARIANT_FULL_TOOL_AGENT: (
        TOOL_CALCULATOR,
        TOOL_DOCUMENT_SEARCH,
        TOOL_LEDGER_CHECK,
        TOOL_INCONSISTENCY_CHECK,
    ),
}


class ChatClient(Protocol):
    model: str

    def complete(
        self,
        prompt: str,
        *,
        temperature: float = 0.0,
        max_tokens: int = 8192,
        timeout: int = 180,
    ) -> tuple[str, dict[str, Any]]:
        ...


@dataclass
class ToolAgentResult:
    response_text: str = ""
    response_payload: dict[str, Any] = field(default_factory=dict)
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    tool_call_failures: int = 0
    latency_seconds: float = 0.0


def run_no_tool_completion(
    client: ChatClient,
    prompt: str,
    *,
    temperature: float,
    max_tokens: int,
    timeout: int,
) -> ToolAgentResult:
    started = time.monotonic()
    response_text, response_payload = client.complete(
        prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
    )
    return ToolAgentResult(
        response_text=response_text,
        response_payload=response_payload,
        latency_seconds=round(time.monotonic() - started, 4),
    )


def run_tool_agent_completion(
    record: DocumentRecord,
    client: ChatClient,
    prompt: str,
    *,
    allowed_tools: tuple[str, ...],
    agent_max_steps: int = 8,
    temperature: float,
    max_tokens: int,
    timeout: int,
) -> ToolAgentResult:
    started = time.monotonic()
    failures = 0
    tool_calls: list[dict[str, Any]] = []
    payloads: list[dict[str, Any]] = []
    messages = [
        {
            "role": "user",
            "content": prompt + "\n\n" + _tool_protocol_instructions(allowed_tools),
        }
    ]

    for _ in range(agent_max_steps):
        response_text, response_payload = _complete_messages(
            client,
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
        )
        payloads.append(response_payload)
        messages.append({"role": "assistant", "content": response_text})

        response_object = _try_load_json_object(response_text)
        if response_object is not None and _looks_like_submission(response_object):
            return ToolAgentResult(
                response_text=response_text,
                response_payload=_payload_with_combined_usage(response_payload, payloads),
                tool_calls=tool_calls,
                tool_call_failures=failures,
                latency_seconds=round(time.monotonic() - started, 4),
            )

        try:
            tool_name, arguments = _parse_tool_call(response_object)
        except ValueError as exc:
            failures += 1
            messages.append(
                {
                    "role": "user",
                    "content": (
                        f"Tool call error: {exc}. Return either a valid tool call JSON object "
                        "or the final strict benchmark JSON answer."
                    ),
                }
            )
            continue

        if tool_name not in allowed_tools:
            failures += 1
            tool_result = {
                "ok": False,
                "error": f"Tool '{tool_name}' is not available in this ablation.",
                "available_tools": list(allowed_tools),
            }
        else:
            tool_result = execute_tool(tool_name, arguments, record)

        tool_calls.append(
            {
                "tool": tool_name,
                "arguments": arguments,
                "result": tool_result,
            }
        )
        messages.append({"role": "user", "content": "Tool result:\n" + json.dumps(tool_result, sort_keys=True)})

    failures += 1
    messages.append(
        {
            "role": "user",
            "content": (
                "Maximum tool steps reached. Stop calling tools and return the final strict "
                "benchmark JSON answer now."
            ),
        }
    )
    response_text, response_payload = _complete_messages(
        client,
        messages,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
    )
    payloads.append(response_payload)
    return ToolAgentResult(
        response_text=response_text,
        response_payload=_payload_with_combined_usage(response_payload, payloads),
        tool_calls=tool_calls,
        tool_call_failures=failures,
        latency_seconds=round(time.monotonic() - started, 4),
    )


def execute_tool(tool_name: str, arguments: dict[str, Any], record: DocumentRecord) -> dict[str, Any]:
    if tool_name == TOOL_CALCULATOR:
        return calculator_tool(arguments)
    if tool_name == TOOL_DOCUMENT_SEARCH:
        return document_search_tool(arguments, record)
    if tool_name == TOOL_LEDGER_CHECK:
        return ledger_check_tool(arguments, record)
    if tool_name == TOOL_INCONSISTENCY_CHECK:
        return inconsistency_check_tool(arguments)
    return {"ok": False, "error": f"Unknown tool '{tool_name}'"}


def calculator_tool(arguments: dict[str, Any]) -> dict[str, Any]:
    expression = str(arguments.get("expression", "")).strip()
    if not expression:
        return {"ok": False, "error": "calculator requires a non-empty expression"}
    try:
        result = _eval_arithmetic(expression)
    except Exception as exc:
        return {"ok": False, "error": str(exc), "expression": expression}
    return {"ok": True, "expression": expression, "result": round(float(result), 6)}


def document_search_tool(arguments: dict[str, Any], record: DocumentRecord) -> dict[str, Any]:
    query = str(arguments.get("query", "")).strip()
    max_results = _bounded_int(arguments.get("max_results", 5), default=5, low=1, high=20)
    if not query:
        return {"ok": False, "error": "document_search requires a non-empty query"}

    pattern = re.compile(re.escape(query), flags=re.IGNORECASE)
    results: list[dict[str, Any]] = []
    for document in record.documents:
        match = pattern.search(document.ocr_text)
        if not match:
            continue
        start = max(match.start() - 80, 0)
        end = min(match.end() + 120, len(document.ocr_text))
        snippet = document.ocr_text[start:end].replace("\n", " ").strip()
        results.append(
            {
                "doc_id": document.doc_id,
                "doc_type": document.doc_type,
                "title": document.title,
                "snippet": snippet,
            }
        )
        if len(results) >= max_results:
            break
    return {"ok": True, "query": query, "matches": results, "match_count": len(results)}


def ledger_check_tool(arguments: dict[str, Any], record: DocumentRecord) -> dict[str, Any]:
    raw_entries = arguments.get("entries", [])
    if not isinstance(raw_entries, list):
        return {"ok": False, "error": "ledger_check requires entries to be a list"}

    entries: list[Posting] = []
    errors: list[str] = []
    for index, item in enumerate(raw_entries):
        if not isinstance(item, dict):
            errors.append(f"entries[{index}] must be an object")
            continue
        posting = Posting(
            doc_refs=[str(value) for value in item.get("doc_refs", [])],
            debit_account=str(item.get("debit_account", "")),
            credit_account=str(item.get("credit_account", "")),
            amount=_coerce_amount(item.get("amount"), index, errors),
            posting_date=str(item.get("posting_date", "")),
            label=str(item.get("label", "")),
        )
        unknown = [
            account
            for account in (posting.debit_account, posting.credit_account)
            if account not in ACCOUNT_TYPES
        ]
        if unknown:
            errors.append(f"entries[{index}] contains unknown accounts: {', '.join(unknown)}")
            continue
        entries.append(posting)

    ledger = Ledger(record.opening_balance)
    try:
        ledger.apply_all(entries)
        reconstructed = ledger.build_balance_sheet(record.period_end)
    except Exception as exc:
        return {"ok": False, "error": str(exc), "errors": errors}

    serialized = serialize_balance_sheet(reconstructed)
    return {
        "ok": not errors,
        "errors": errors,
        "accepted_entry_count": len(entries),
        "reconstructed_balance_sheet": serialized,
    }


def inconsistency_check_tool(arguments: dict[str, Any]) -> dict[str, Any]:
    raw_codes = arguments.get("inconsistency_codes", arguments.get("codes", []))
    if isinstance(raw_codes, str):
        codes = [raw_codes]
    elif isinstance(raw_codes, list):
        codes = [str(code) for code in raw_codes]
    else:
        return {"ok": False, "error": "inconsistency_check requires a code or list of codes"}
    unknown = [code for code in codes if code not in INCONSISTENCY_CODES]
    return {
        "ok": not unknown,
        "claimed_codes": codes,
        "unknown_codes": unknown,
        "note": "This deterministic check validates code names; document-specific contradiction checks are limited.",
    }


def _tool_protocol_instructions(allowed_tools: tuple[str, ...]) -> str:
    tool_descriptions = {
        TOOL_CALCULATOR: "calculator: arguments {\"expression\": \"1250 * 0.0825\"}",
        TOOL_DOCUMENT_SEARCH: "document_search: arguments {\"query\": \"invoice number\", \"max_results\": 5}",
        TOOL_LEDGER_CHECK: "ledger_check: arguments {\"entries\": [{\"doc_refs\": [\"D003\"], \"debit_account\": \"Cash\", \"credit_account\": \"Revenue\", \"amount\": 100.0}]}",
        TOOL_INCONSISTENCY_CHECK: "inconsistency_check: arguments {\"inconsistency_codes\": [\"bank_closing_mismatch\"]}",
    }
    available = "\n".join(f"- {tool_descriptions[name]}" for name in allowed_tools)
    return (
        "You may use tools before the final answer. To call a tool, return strict JSON only in "
        "this shape: {\"tool\": \"tool_name\", \"arguments\": {...}}.\n"
        "Available tools:\n"
        f"{available}\n"
        "After tool use, return the final benchmark answer as strict JSON with the required top-level keys."
    )


def _complete_messages(
    client: ChatClient,
    messages: list[dict[str, str]],
    *,
    temperature: float,
    max_tokens: int,
    timeout: int,
) -> tuple[str, dict[str, Any]]:
    complete_messages = getattr(client, "complete_messages", None)
    if callable(complete_messages):
        return complete_messages(
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
        )
    transcript = "\n\n".join(f"{message['role'].upper()}:\n{message['content']}" for message in messages)
    return client.complete(
        transcript,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
    )


def _payload_with_combined_usage(final_payload: dict[str, Any], payloads: list[dict[str, Any]]) -> dict[str, Any]:
    combined = dict(final_payload) if isinstance(final_payload, dict) else {}
    usage_totals: dict[str, float] = {}
    for payload in payloads:
        usage = payload.get("usage", {}) if isinstance(payload, dict) else {}
        if not isinstance(usage, dict):
            continue
        for key, value in usage.items():
            if isinstance(value, (int, float)):
                usage_totals[key] = usage_totals.get(key, 0.0) + float(value)
    if usage_totals:
        combined["usage"] = {
            key: int(value) if value.is_integer() and key != "cost" else round(value, 8)
            for key, value in usage_totals.items()
        }
    return combined


def _try_load_json_object(text: str) -> dict[str, Any] | None:
    try:
        blob = _extract_json_blob(text)
        payload = json.loads(blob)
    except Exception:
        return None
    return payload if isinstance(payload, dict) else None


def _looks_like_submission(payload: dict[str, Any]) -> bool:
    if not {"has_inconsistency", "entries", "balance_sheet"}.issubset(payload):
        return False
    try:
        parse_submission(json.dumps(payload))
    except Exception:
        return False
    return True


def _parse_tool_call(payload: dict[str, Any] | None) -> tuple[str, dict[str, Any]]:
    if payload is None:
        raise ValueError("response was not a JSON object")
    if "tool_call" in payload and isinstance(payload["tool_call"], dict):
        payload = payload["tool_call"]
    tool_name = payload.get("tool") or payload.get("name") or payload.get("tool_name")
    if not tool_name:
        raise ValueError("tool call missing 'tool' or 'name'")
    if "arguments" in payload:
        arguments = payload.get("arguments", {})
    else:
        arguments = {
            key: value
            for key, value in payload.items()
            if key not in {"tool", "name", "tool_name"}
        }
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except json.JSONDecodeError as exc:
            raise ValueError("tool call arguments string is not valid JSON") from exc
    if arguments is None:
        arguments = {}
    if not isinstance(arguments, dict):
        raise ValueError("tool call arguments must be an object")
    return str(tool_name), arguments


def _coerce_amount(value: Any, index: int, errors: list[str]) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        errors.append(f"entries[{index}].amount must be numeric")
        return 0.0


def _bounded_int(value: Any, *, default: int, low: int, high: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return default
    return min(max(parsed, low), high)


def _eval_arithmetic(expression: str) -> float:
    tree = ast.parse(expression, mode="eval")
    return float(_eval_node(tree.body))


def _eval_node(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            if right == 0:
                raise ValueError("division by zero")
            return left / right
    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return operand
        if isinstance(node.op, ast.USub):
            return -operand
    raise ValueError("unsupported arithmetic expression")
