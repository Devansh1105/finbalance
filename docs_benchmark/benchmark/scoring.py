"""Compatibility wrappers around the richer benchmark analysis helpers."""

from __future__ import annotations

from typing import Any

from docs_benchmark.benchmark.analysis import analyze_submission, summarize_results
from docs_benchmark.schemas import DocumentRecord, ParsedSubmission


def score_submission(
    record: DocumentRecord,
    parsed: ParsedSubmission,
    *,
    parse_success: bool,
    amount_tol: float = 0.01,
    balance_tol: float = 0.01,
) -> dict[str, Any]:
    return analyze_submission(
        record,
        parsed,
        parse_success=parse_success,
        amount_tol=amount_tol,
        balance_tol=balance_tol,
    )["metrics"]


__all__ = ["score_submission", "summarize_results"]
