"""Record-level validation for generated records."""

from __future__ import annotations

from finbalance.accounts import ACCOUNT_TYPES
from finbalance.doc_schemas import get_doc_schema
from finbalance.rendering.renderer import format_scalar
from finbalance.schemas import BalanceSheet, DocumentAsset, DocumentSeed, Posting
from finbalance.types import PeriodSpec, ValidationReport
from finbalance.validation.doc_validation import validate_document_seed


def validate_record_bundle(
    industry: str,
    period_spec: PeriodSpec,
    allowed_accounts: list[str],
    documents: list[DocumentSeed],
    rendered_documents: list[DocumentAsset],
    postings: list[Posting],
    balance_sheet: BalanceSheet,
) -> ValidationReport:
    report = ValidationReport()
    allowed_account_set = set(allowed_accounts)
    seen_doc_ids: set[str] = set()
    for seed in documents:
        if seed.doc_id in seen_doc_ids:
            report.add("error", seed.doc_id, "Duplicate document id in record")
        seen_doc_ids.add(seed.doc_id)
        validate_document_seed(seed, industry, report)
        if not (period_spec.start_date <= seed.date <= period_spec.end_date):
            report.add("error", seed.doc_id, "Document date falls outside record period")

    rendered_map = {doc.doc_id: doc for doc in rendered_documents}
    for seed in documents:
        rendered = rendered_map.get(seed.doc_id)
        if not rendered:
            report.add("error", seed.doc_id, "Rendered document missing from record output")
            continue
        for token in _visible_tokens(seed, industry):
            if token and token not in rendered.ocr_text:
                report.add("error", seed.doc_id, f"Rendered OCR text is missing visible token '{token}'")

    doc_ids = {seed.doc_id for seed in documents}
    for posting in postings:
        for ref in posting.doc_refs:
            if ref not in doc_ids:
                report.add("error", "posting", f"Posting references unknown document '{ref}'")
        if posting.amount <= 0:
            report.add("error", "posting", "Posting amount must be positive")
        if posting.debit_account == posting.credit_account:
            report.add("error", "posting", "Posting cannot use the same account on both sides")
        for account in (posting.debit_account, posting.credit_account):
            if account not in ACCOUNT_TYPES:
                report.add("error", "posting", f"Posting uses unknown account '{account}'")
            elif account not in allowed_account_set:
                report.add(
                    "error",
                    "posting",
                    f"Posting uses account '{account}' outside the allowed account list for industry '{industry}'",
                )

    if not balance_sheet.balanced:
        report.add("error", "ledger", "Final balance sheet is not balanced")

    if period_spec.period_type == "year":
        summary_docs = {
            "ar_aging_summary",
            "ap_aging_summary",
            "bank_statement",
            "fixed_asset_rollforward",
            "inventory_rollforward",
            "revenue_recognition_schedule",
        }
        if not any(seed.doc_type in summary_docs for seed in documents):
            report.add("error", "record", "Year records must include at least one summary or close document")
    return report


def _visible_tokens(seed: DocumentSeed, industry: str) -> list[str]:
    schema = get_doc_schema(seed.doc_type)
    tokens: list[str] = []
    field_names = schema.visible_fields or tuple(
        name for name, value in seed.fields.items() if isinstance(value, (str, int, float))
    )
    for key in field_names:
        value = seed.fields.get(key)
        if isinstance(value, (str, int, float)):
            text = format_scalar(value, key, seed.metadata)
            if text:
                tokens.append(text)
    return tokens
