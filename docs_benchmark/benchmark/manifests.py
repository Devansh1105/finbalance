"""Manifest helpers for dataset generation and benchmark slicing."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from docs_benchmark.benchmark.analysis import ledger_family_for_label
from docs_benchmark.schemas import DocumentRecord, ensure_parent


ROLLFORWARD_DOC_TYPES = frozenset(
    {
        "ar_aging_summary",
        "fixed_asset_rollforward",
        "fx_remeasurement_memo",
        "inventory_rollforward",
        "revenue_recognition_schedule",
        "service_period_memo",
    }
)
FX_DOC_TYPES = frozenset({"exchange_rate_notice", "fx_remeasurement_memo"})
DISTRACTOR_DOC_TYPES = frozenset({"secondary_copy", "vendor_statement", "memo", "cancellation_note"})


def record_feature_flags(record: DocumentRecord) -> dict[str, bool]:
    scenario_sequence = set(record.metadata.get("scenario_sequence", []))
    posting_labels = set(_underlying_posting_labels(record))
    doc_types = {document.doc_type for document in record.documents}
    doc_roles = {document.role for document in record.documents}

    return {
        "has_tax": record.metadata.get("tax_regime", "none") != "none",
        "has_fx": bool(doc_types & FX_DOC_TYPES or any(label.startswith("fx_") for label in posting_labels)),
        "has_distractors": "distractor_doc" in doc_roles,
        "has_multi_invoice_payment": "multi_invoice_payment" in scenario_sequence
        or any(label.startswith("multi_invoice_payment_") for label in posting_labels),
        "has_interbank_transfer": "interbank_transfer" in scenario_sequence or "interbank_transfer" in posting_labels,
        "has_reclassification": "reclassification_correction" in scenario_sequence
        or any(label.startswith("reclassification_correction") for label in posting_labels),
        "has_rollforward": bool(doc_types & ROLLFORWARD_DOC_TYPES),
    }


def _underlying_posting_labels(record: DocumentRecord) -> list[str]:
    labels = list(record.metadata.get("underlying_posting_labels", []))
    if labels:
        return [str(label) for label in labels if str(label)]
    return [posting.label for posting in record.expected_entries if posting.label]


def _counter_to_dict(counter: Counter[str]) -> dict[str, int]:
    return {key: counter[key] for key in sorted(counter)}


def record_manifest_row(record: DocumentRecord) -> dict[str, Any]:
    doc_types = sorted({document.doc_type for document in record.documents})
    doc_roles = sorted({document.role for document in record.documents})
    posting_labels = sorted(set(_underlying_posting_labels(record)))
    ledger_families = sorted({ledger_family_for_label(label) for label in posting_labels})
    feature_flags = record_feature_flags(record)
    return {
        "record_id": record.record_id,
        "industry": record.industry,
        "period_type": record.metadata.get("period_type"),
        "period_label": record.metadata.get("period_label"),
        "difficulty_level": record.difficulty_level,
        "scenario_sequence": list(record.metadata.get("scenario_sequence", [])),
        "doc_types_present": doc_types,
        "doc_roles_present": doc_roles,
        "posting_labels_present": posting_labels,
        "ledger_families_present": ledger_families,
        "document_count": len(record.documents),
        "expected_entry_count": int(record.metadata.get("underlying_expected_entry_count", len(record.expected_entries))),
        "expected_inconsistency": record.expected_inconsistency,
        "expected_inconsistency_codes": list(record.expected_inconsistency_codes),
        "expected_inconsistency_code": record.expected_inconsistency_codes[0] if record.expected_inconsistency_codes else "none",
        "available_inconsistency_codes": list(record.metadata.get("available_inconsistency_codes", [])),
        "tax_regime": record.metadata.get("tax_regime", "none"),
        "currency_code": record.metadata.get("currency_code", "USD"),
        "date_format": record.metadata.get("date_format", "YYYY-MM-DD"),
        **feature_flags,
    }


def dataset_manifest(
    dataset_name: str,
    records: list[DocumentRecord],
    record_rows: list[dict[str, Any]],
    *,
    config: dict[str, Any],
) -> dict[str, Any]:
    industries = Counter(row["industry"] for row in record_rows)
    period_types = Counter(str(row["period_type"]) for row in record_rows)
    difficulty_levels = Counter(str(row["difficulty_level"]) for row in record_rows)
    tax_regimes = Counter(str(row["tax_regime"]) for row in record_rows)
    currency_codes = Counter(str(row["currency_code"]) for row in record_rows)
    date_formats = Counter(str(row["date_format"]) for row in record_rows)
    inconsistency_codes = Counter(
        code
        for row in record_rows
        for code in row["expected_inconsistency_codes"]
    )
    scenario_families = Counter(
        scenario
        for row in record_rows
        for scenario in row["scenario_sequence"]
    )
    records_with_doc_type = Counter(
        doc_type
        for row in record_rows
        for doc_type in row["doc_types_present"]
    )
    documents_by_type = Counter(
        document.doc_type
        for record in records
        for document in record.documents
    )
    records_with_doc_role = Counter(
        doc_role
        for row in record_rows
        for doc_role in row["doc_roles_present"]
    )
    documents_by_role = Counter(
        document.role
        for record in records
        for document in record.documents
    )
    posting_labels = Counter(
        label
        for row in record_rows
        for label in row["posting_labels_present"]
    )
    ledger_families = Counter(
        family
        for row in record_rows
        for family in row["ledger_families_present"]
    )
    feature_flag_counts = Counter(
        key
        for row in record_rows
        for key, value in row.items()
        if key.startswith("has_") and value
    )

    total_documents = sum(len(record.documents) for record in records)
    total_expected_entries = sum(int(row["expected_entry_count"]) for row in record_rows)

    return {
        "dataset_name": dataset_name,
        "dataset_version": records[0].metadata.get("version") if records else "unknown",
        "config": config,
        "summary": {
            "records": len(records),
            "inconsistency_records": sum(1 for record in records if record.expected_inconsistency),
            "total_documents": total_documents,
            "total_expected_entries": total_expected_entries,
            "average_documents_per_record": round(total_documents / len(records), 2) if records else 0.0,
            "average_expected_entries_per_record": round(total_expected_entries / len(records), 2) if records else 0.0,
        },
        "counts": {
            "by_industry": _counter_to_dict(industries),
            "by_period_type": _counter_to_dict(period_types),
            "by_difficulty_level": _counter_to_dict(difficulty_levels),
            "by_tax_regime": _counter_to_dict(tax_regimes),
            "by_currency_code": _counter_to_dict(currency_codes),
            "by_date_format": _counter_to_dict(date_formats),
            "by_inconsistency_code": _counter_to_dict(inconsistency_codes),
            "by_scenario_family": _counter_to_dict(scenario_families),
            "records_with_doc_type": _counter_to_dict(records_with_doc_type),
            "documents_by_type": _counter_to_dict(documents_by_type),
            "records_with_doc_role": _counter_to_dict(records_with_doc_role),
            "documents_by_role": _counter_to_dict(documents_by_role),
            "records_with_posting_label": _counter_to_dict(posting_labels),
            "records_with_ledger_family": _counter_to_dict(ledger_families),
            "records_with_feature_flag": _counter_to_dict(feature_flag_counts),
        },
    }


def write_jsonl(path: str | Path, rows: Iterable[dict[str, Any]]) -> None:
    output = ensure_parent(path)
    with Path(output).open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=True) + "\n")
