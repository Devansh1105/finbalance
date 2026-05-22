"""Dataset loading helpers for the document benchmark."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Sequence

from finbalance.schemas import (
    BalanceSheet,
    DocumentAsset,
    DocumentRecord,
    OpeningBalance,
    Posting,
)


def opening_balance_from_dict(payload: dict) -> OpeningBalance:
    return OpeningBalance(
        date=str(payload["date"]),
        assets={str(key): float(value) for key, value in payload.get("assets", {}).items()},
        liabilities={str(key): float(value) for key, value in payload.get("liabilities", {}).items()},
        equity={str(key): float(value) for key, value in payload.get("equity", {}).items()},
    )


def posting_from_dict(payload: dict) -> Posting:
    return Posting(
        doc_refs=[str(value) for value in payload.get("doc_refs", [])],
        debit_account=str(payload["debit_account"]),
        credit_account=str(payload["credit_account"]),
        amount=float(payload["amount"]),
        posting_date=str(payload.get("posting_date", "")),
        label=str(payload.get("label", "")),
    )


def balance_sheet_from_dict(payload: dict) -> BalanceSheet:
    return BalanceSheet(
        date=str(payload["date"]),
        assets={str(key): float(value) for key, value in payload.get("assets", {}).items()},
        liabilities={str(key): float(value) for key, value in payload.get("liabilities", {}).items()},
        equity={str(key): float(value) for key, value in payload.get("equity", {}).items()},
        total_assets=float(payload.get("total_assets", 0.0)),
        total_liabilities=float(payload.get("total_liabilities", 0.0)),
        total_equity=float(payload.get("total_equity", 0.0)),
        balanced=bool(payload.get("balanced", False)),
    )


def document_asset_from_dict(payload: dict) -> DocumentAsset:
    return DocumentAsset(
        doc_id=str(payload["doc_id"]),
        doc_type=str(payload["doc_type"]),
        role=str(payload["role"]),
        title=str(payload["title"]),
        date=str(payload["date"]),
        asset_path=str(payload["asset_path"]),
        ocr_text=str(payload.get("ocr_text", "")),
        metadata=dict(payload.get("metadata", {})),
    )


def document_record_from_dict(payload: dict) -> DocumentRecord:
    return DocumentRecord(
        record_id=str(payload["record_id"]),
        industry=str(payload["industry"]),
        difficulty_level=int(payload["difficulty_level"]),
        period_start=str(payload["period_start"]),
        period_end=str(payload["period_end"]),
        opening_balance=opening_balance_from_dict(payload["opening_balance"]),
        allowed_accounts=[str(account) for account in payload.get("allowed_accounts", [])],
        documents=[document_asset_from_dict(item) for item in payload.get("documents", [])],
        expected_entries=[posting_from_dict(item) for item in payload.get("expected_entries", [])],
        expected_balance_sheet=balance_sheet_from_dict(payload["expected_balance_sheet"]),
        expected_inconsistency=bool(payload.get("expected_inconsistency", False)),
        expected_inconsistency_codes=[str(value) for value in payload.get("expected_inconsistency_codes", [])],
        inconsistency_reasons=[str(value) for value in payload.get("inconsistency_reasons", [])],
        metadata=dict(payload.get("metadata", {})),
    )


def load_records(path: str | Path) -> list[DocumentRecord]:
    records: list[DocumentRecord] = []
    with Path(path).open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(document_record_from_dict(json.loads(line)))
    return records


def filter_records(
    records: Sequence[DocumentRecord],
    *,
    industries: Iterable[str] | None = None,
    period_types: Iterable[str] | None = None,
    levels: Iterable[int] | None = None,
    record_ids: Iterable[str] | None = None,
    max_records: int | None = None,
) -> list[DocumentRecord]:
    industry_set = set(industries or [])
    period_set = set(period_types or [])
    level_set = {int(level) for level in levels or []}
    record_id_set = set(record_ids or [])

    selected: list[DocumentRecord] = []
    for record in records:
        if industry_set and record.industry not in industry_set:
            continue
        if period_set and record.metadata.get("period_type") not in period_set:
            continue
        if level_set and record.difficulty_level not in level_set:
            continue
        if record_id_set and record.record_id not in record_id_set:
            continue
        selected.append(record)
        if max_records is not None and len(selected) >= max_records:
            break
    return selected


def stratified_sample_records(
    records: Sequence[DocumentRecord],
    max_records: int | None,
    *,
    fields: Sequence[str] = ("difficulty_level", "industry"),
) -> list[DocumentRecord]:
    if max_records is None or max_records >= len(records):
        return list(records)
    if max_records <= 0:
        return []

    groups: dict[tuple[str, ...], list[DocumentRecord]] = defaultdict(list)
    for record in records:
        groups[tuple(_record_field(record, field) for field in fields)].append(record)

    selected: list[DocumentRecord] = []
    cursors = {key: 0 for key in groups}
    group_keys = sorted(groups)
    while len(selected) < max_records:
        added = False
        for key in group_keys:
            if len(selected) >= max_records:
                break
            cursor = cursors[key]
            group = groups[key]
            if cursor >= len(group):
                continue
            selected.append(group[cursor])
            cursors[key] = cursor + 1
            added = True
        if not added:
            break
    return selected


def _record_field(record: DocumentRecord, field: str) -> str:
    value = getattr(record, field, None)
    if value is None:
        value = record.metadata.get(field)
    return str(value if value is not None else "unknown")
