"""Strict JSON parsing for model submissions."""

from __future__ import annotations

import json
import re
from typing import Any

from finbalance.inconsistencies import INCONSISTENCY_CODES
from finbalance.schemas import ParsedSubmission, Posting


class SubmissionParseError(ValueError):
    """Raised when a model response cannot be parsed into the expected schema."""


def _extract_json_blob(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        raise SubmissionParseError("empty model response")
    if stripped.startswith("{") and stripped.endswith("}"):
        return stripped

    fenced = re.findall(r"```(?:json)?\s*(.*?)```", stripped, flags=re.DOTALL | re.IGNORECASE)
    for block in fenced:
        candidate = block.strip()
        if candidate.startswith("{") and candidate.endswith("}"):
            return candidate

    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise SubmissionParseError("could not find a JSON object in model response")
    return stripped[start : end + 1]


def _strip_thousands_separators(blob: str) -> str:
    return re.sub(r"(?<=\d),(?=\d{3}(?:[^\d]|$))", "", blob)


def _coerce_float(value: Any, path: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise SubmissionParseError(f"{path} must be numeric") from exc


def _normalize_doc_refs(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value]
    raise SubmissionParseError("entry.doc_refs must be a string or list of strings")


def _normalize_balance_sheet(payload: Any) -> dict[str, dict[str, float]]:
    if payload is None:
        return {"assets": {}, "liabilities": {}, "equity": {}}
    if not isinstance(payload, dict):
        raise SubmissionParseError("balance_sheet must be an object")

    normalized: dict[str, dict[str, float]] = {}
    for section in ("assets", "liabilities", "equity"):
        raw_section = payload.get(section, {})
        if raw_section is None:
            raw_section = {}
        if not isinstance(raw_section, dict):
            raise SubmissionParseError(f"balance_sheet.{section} must be an object")
        normalized[section] = {
            str(account): _coerce_float(amount, f"balance_sheet.{section}.{account}")
            for account, amount in raw_section.items()
        }
    return normalized


def _normalize_inconsistency_notes(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        text = value.strip()
        return [text] if text else []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    raise SubmissionParseError("inconsistency_notes must be a string or list of strings")


def _normalize_inconsistency_codes(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        codes = [value.strip()] if value.strip() else []
    elif isinstance(value, list):
        codes = [str(item).strip() for item in value if str(item).strip()]
    else:
        raise SubmissionParseError("inconsistency_codes must be a string or list of strings")

    normalized: list[str] = []
    for code in codes:
        if code not in INCONSISTENCY_CODES:
            raise SubmissionParseError(f"inconsistency_codes contains unknown code '{code}'")
        if code not in normalized:
            normalized.append(code)
    return normalized


def parse_submission(text: str) -> ParsedSubmission:
    blob = _extract_json_blob(text)
    try:
        raw = json.loads(blob)
    except json.JSONDecodeError as exc:
        repaired = _strip_thousands_separators(blob)
        if repaired != blob:
            try:
                raw = json.loads(repaired)
            except json.JSONDecodeError:
                raise SubmissionParseError(f"invalid JSON: {exc.msg}") from exc
        else:
            raise SubmissionParseError(f"invalid JSON: {exc.msg}") from exc

    if not isinstance(raw, dict):
        raise SubmissionParseError("top-level response must be a JSON object")

    raw_entries = raw.get("entries", [])
    if raw_entries is None:
        raw_entries = []
    if not isinstance(raw_entries, list):
        raise SubmissionParseError("entries must be a list")

    parsed_entries: list[Posting] = []
    for index, item in enumerate(raw_entries):
        if not isinstance(item, dict):
            raise SubmissionParseError(f"entries[{index}] must be an object")
        parsed_entries.append(
            Posting(
                doc_refs=_normalize_doc_refs(item.get("doc_refs")),
                debit_account=str(item.get("debit_account", "")),
                credit_account=str(item.get("credit_account", "")),
                amount=_coerce_float(item.get("amount"), f"entries[{index}].amount"),
                posting_date=str(item.get("posting_date", "")),
                label=str(item.get("label", "")),
            )
        )

    return ParsedSubmission(
        entries=parsed_entries,
        balance_sheet=_normalize_balance_sheet(raw.get("balance_sheet")),
        has_inconsistency=bool(raw.get("has_inconsistency", False)),
        inconsistency_codes=_normalize_inconsistency_codes(raw.get("inconsistency_codes")),
        inconsistency_notes=_normalize_inconsistency_notes(raw.get("inconsistency_notes")),
        raw=raw,
    )
