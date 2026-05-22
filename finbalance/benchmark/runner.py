"""End-to-end model execution for the document benchmark."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from finbalance.benchmark.analysis import analyze_submission, summarize_results
from finbalance.benchmark.manifests import record_manifest_row
from finbalance.benchmark.model import OpenRouterClient
from finbalance.benchmark.parser import SubmissionParseError, parse_submission
from finbalance.benchmark.prompt import build_prompt
from finbalance.schemas import DocumentRecord, ParsedSubmission


def _empty_submission() -> ParsedSubmission:
    return ParsedSubmission(
        entries=[],
        balance_sheet={"assets": {}, "liabilities": {}, "equity": {}},
        has_inconsistency=False,
        inconsistency_codes=[],
        inconsistency_notes=[],
        raw={},
    )


def run_openrouter_evaluation(
    records: list[DocumentRecord],
    *,
    client: OpenRouterClient,
    dataset_path: str,
    temperature: float = 0.0,
    max_tokens: int = 8192,
    timeout: int = 180,
) -> dict[str, Any]:
    started_at = datetime.now(timezone.utc).isoformat()
    results: list[dict[str, Any]] = []

    for record in records:
        prompt = build_prompt(record)
        error_message = ""
        response_text = ""
        response_payload: dict[str, Any] = {}
        parse_success = False
        parsed = _empty_submission()

        try:
            response_text, response_payload = client.complete(
                prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout,
            )
            parsed = parse_submission(response_text)
            parse_success = True
        except SubmissionParseError as exc:
            error_message = str(exc)
        except Exception as exc:  # pragma: no cover - exercised by integration runs
            error_message = str(exc)

        analysis = analyze_submission(record, parsed, parse_success=parse_success)
        usage = dict(response_payload.get("usage", {})) if isinstance(response_payload, dict) else {}
        results.append(
            {
                "record_id": record.record_id,
                "industry": record.industry,
                "difficulty_level": record.difficulty_level,
                "period_type": record.metadata.get("period_type"),
                "period_label": record.metadata.get("period_label"),
                "document_index": {
                    document.doc_id: {"doc_type": document.doc_type, "role": document.role}
                    for document in record.documents
                },
                "record_features": record_manifest_row(record),
                "metrics": analysis["metrics"],
                "parsed_submission": analysis["parsed_submission"],
                "reconstructed_balance_sheet": analysis["reconstructed_balance_sheet"],
                "entry_diagnostics": analysis["entry_diagnostics"],
                "usage": usage,
                "cost": float(usage.get("cost", 0.0)) if usage else 0.0,
                "prompt_tokens": int(usage.get("prompt_tokens", 0)) if usage else 0,
                "completion_tokens": int(usage.get("completion_tokens", 0)) if usage else 0,
                "total_tokens": int(usage.get("total_tokens", 0)) if usage else 0,
                "error": error_message,
                "raw_response": response_text,
                "raw_provider_payload": response_payload,
            }
        )

    return {
        "dataset_path": dataset_path,
        "model": client.model,
        "run_started_at": started_at,
        "run_completed_at": datetime.now(timezone.utc).isoformat(),
        "temperature": temperature,
        "max_tokens": max_tokens,
        "timeout": timeout,
        "summary": summarize_results(results),
        "results": results,
    }
