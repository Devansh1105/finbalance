"""Document-level validation for schema-driven records."""

from __future__ import annotations

import re
from typing import Any

from docs_benchmark.schemas import DocumentSeed
from docs_benchmark.doc_schemas import get_doc_schema
from docs_benchmark.types import ValidationReport


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate_document_seed(seed: DocumentSeed, industry: str, report: ValidationReport) -> None:
    schema = get_doc_schema(seed.doc_type)
    field_specs = {spec.name: spec for spec in schema.field_specs_for(industry)}
    for field_name in schema.required_field_names_for(industry):
        if field_name not in seed.fields:
            report.add("error", seed.doc_id, f"Missing required field '{field_name}' for {seed.doc_type}")

    for field_name, spec in field_specs.items():
        if field_name not in seed.fields:
            continue
        if not _matches_kind(seed.fields[field_name], spec.kind):
            report.add(
                "error",
                seed.doc_id,
                f"Field '{field_name}' has wrong type for {seed.doc_type}; expected {spec.kind}",
            )

    if not DATE_RE.match(seed.date):
        report.add("error", seed.doc_id, f"Document date '{seed.date}' is not in YYYY-MM-DD form")

    _run_doc_specific_checks(seed, report)


def _matches_kind(value: Any, kind: str) -> bool:
    if kind == "string":
        return isinstance(value, str)
    if kind == "number":
        return isinstance(value, (int, float))
    if kind == "date":
        return isinstance(value, str) and bool(DATE_RE.match(value))
    if kind == "list":
        return isinstance(value, list)
    if kind == "dict":
        return isinstance(value, dict)
    if kind == "bool":
        return isinstance(value, bool)
    return True


def _run_doc_specific_checks(seed: DocumentSeed, report: ValidationReport) -> None:
    if "line_items" in seed.fields and "total" in seed.fields and isinstance(seed.fields["line_items"], list):
        line_total = round(sum(float(item.get("amount", 0.0)) for item in seed.fields["line_items"]), 2)
        expected_line_total = round(float(seed.fields.get("subtotal", seed.fields["total"])), 2)
        if abs(line_total - expected_line_total) >= 0.01:
            report.add(
                "error",
                seed.doc_id,
                f"Line items total {line_total:.2f} does not match expected pre-tax amount {expected_line_total:.2f}",
            )

    if all(name in seed.fields for name in ("subtotal", "tax_rate", "tax_amount", "total")):
        subtotal = round(float(seed.fields["subtotal"]), 2)
        tax_rate = float(seed.fields["tax_rate"])
        tax_amount = round(float(seed.fields["tax_amount"]), 2)
        total = round(float(seed.fields["total"]), 2)
        expected_tax = round(subtotal * tax_rate, 2)
        expected_total = round(subtotal + tax_amount, 2)
        if abs(expected_tax - tax_amount) >= 0.01:
            report.add("error", seed.doc_id, "Document tax amount does not match subtotal multiplied by the shown tax rate")
        if abs(expected_total - total) >= 0.01:
            report.add("error", seed.doc_id, "Document total does not match subtotal plus tax amount")

    if "rows" in seed.fields and seed.doc_type == "bank_statement":
        rows = seed.fields["rows"]
        opening_balance = round(float(seed.fields.get("opening_balance", 0.0)), 2)
        closing_balance = opening_balance
        for row in rows:
            closing_balance = round(closing_balance + float(row.get("amount", 0.0)), 2)
        expected_close = round(float(seed.fields.get("closing_balance", 0.0)), 2)
        if abs(closing_balance - expected_close) >= 0.01:
            report.add(
                "error",
                seed.doc_id,
                f"Bank statement closing balance {expected_close:.2f} does not match row rollforward {closing_balance:.2f}",
            )

    if seed.doc_type == "revenue_recognition_schedule":
        opening_deferred = round(float(seed.fields.get("opening_deferred", 0.0)), 2)
        added_deferred = round(float(seed.fields.get("added_deferred", 0.0)), 2)
        released = round(float(seed.fields.get("released_this_period", 0.0)), 2)
        ending = round(float(seed.fields.get("ending_deferred", 0.0)), 2)
        expected = round(opening_deferred + added_deferred - released, 2)
        if abs(expected - ending) >= 0.01:
            report.add("error", seed.doc_id, "Revenue recognition schedule does not roll forward cleanly")

    if seed.doc_type in {"fixed_asset_rollforward", "inventory_rollforward"}:
        opening_balance = round(float(seed.fields.get("opening_balance", 0.0)), 2)
        additions = round(float(seed.fields.get("additions", 0.0)), 2)
        disposals = round(float(seed.fields.get("disposals", 0.0)), 2)
        usage = round(float(seed.fields.get("usage_or_sales", 0.0)), 2)
        write_down = round(float(seed.fields.get("write_down", 0.0)), 2)
        ending = round(float(seed.fields.get("ending_balance", 0.0)), 2)
        expected = round(opening_balance + additions - disposals - usage - write_down, 2)
        if abs(expected - ending) >= 0.01:
            report.add("error", seed.doc_id, f"{seed.doc_type} does not roll forward cleanly")

    if seed.doc_type == "exchange_rate_notice":
        source_amount = round(float(seed.fields.get("source_amount", 0.0)), 2)
        exchange_rate = float(seed.fields.get("exchange_rate", 0.0))
        functional_amount = round(float(seed.fields.get("functional_amount", 0.0)), 2)
        expected = round(source_amount * exchange_rate, 2)
        if abs(expected - functional_amount) >= 0.01:
            report.add("error", seed.doc_id, "Exchange rate notice does not reconcile source amount into the stated functional amount")

    if seed.doc_type == "payment_advice" and all(name in seed.fields for name in ("source_amount", "exchange_rate", "functional_amount")):
        source_amount = round(float(seed.fields["source_amount"]), 2)
        exchange_rate = float(seed.fields["exchange_rate"])
        functional_amount = round(float(seed.fields["functional_amount"]), 2)
        expected = round(source_amount * exchange_rate, 2)
        if abs(expected - functional_amount) >= 0.01:
            report.add("error", seed.doc_id, "Payment advice FX details do not reconcile source amount and exchange rate to the stated functional amount")

    if seed.doc_type == "fx_remeasurement_memo":
        booked_amount = round(float(seed.fields.get("booked_amount", 0.0)), 2)
        remeasured_amount = round(float(seed.fields.get("remeasured_amount", 0.0)), 2)
        difference_amount = round(float(seed.fields.get("difference_amount", 0.0)), 2)
        source_amount = round(float(seed.fields.get("source_amount", 0.0)), 2)
        closing_rate = float(seed.fields.get("closing_rate", 0.0))
        expected_remeasured = round(source_amount * closing_rate, 2)
        expected_difference = round(abs(remeasured_amount - booked_amount), 2)
        if abs(expected_remeasured - remeasured_amount) >= 0.01:
            report.add("error", seed.doc_id, "FX remeasurement memo does not reconcile the open foreign amount to the stated remeasured amount")
        if abs(expected_difference - difference_amount) >= 0.01:
            report.add("error", seed.doc_id, "FX remeasurement memo difference does not match booked versus remeasured amount")
