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

    if seed.doc_type == "performance_obligation_schedule":
        transaction_price = round(float(seed.fields.get("transaction_price", 0.0)), 2)
        allocation_total = round(float(seed.fields.get("allocation_total", 0.0)), 2)
        released = round(float(seed.fields.get("released_this_period", 0.0)), 2)
        ending = round(float(seed.fields.get("ending_deferred", 0.0)), 2)
        obligations = seed.fields.get("obligations", [])
        allocated_total = round(sum(float(item.get("allocated_transaction_price", 0.0)) for item in obligations), 2)
        release_total = round(sum(float(item.get("released_this_period", 0.0)) for item in obligations), 2)
        if abs(allocated_total - allocation_total) >= 0.01 or abs(allocation_total - transaction_price) >= 0.01:
            report.add("error", seed.doc_id, "Performance obligation allocation does not tie to transaction price")
        if abs(release_total - released) >= 0.01:
            report.add("error", seed.doc_id, "Performance obligation release does not tie to schedule total")
        if abs(round(transaction_price - released, 2) - ending) >= 0.01:
            report.add("error", seed.doc_id, "Performance obligation ending deferred amount does not tie")

    if seed.doc_type == "asset_disposal_notice":
        cost = round(float(seed.fields.get("original_cost", 0.0)), 2)
        accumulated = round(float(seed.fields.get("accumulated_depreciation", 0.0)), 2)
        nbv = round(float(seed.fields.get("net_book_value", 0.0)), 2)
        proceeds = round(float(seed.fields.get("proceeds_amount", 0.0)), 2)
        gain_loss = round(float(seed.fields.get("gain_loss_amount", 0.0)), 2)
        if abs(round(cost - accumulated, 2) - nbv) >= 0.01:
            report.add("error", seed.doc_id, "Asset disposal NBV does not equal cost less accumulated depreciation")
        if abs(abs(round(proceeds - nbv, 2)) - gain_loss) >= 0.01:
            report.add("error", seed.doc_id, "Asset disposal gain/loss does not equal proceeds less NBV")

    if seed.doc_type == "tax_depreciation_schedule":
        book = round(float(seed.fields.get("book_depreciation_amount", 0.0)), 2)
        tax = round(float(seed.fields.get("tax_depreciation_amount", 0.0)), 2)
        difference = round(float(seed.fields.get("temporary_difference_amount", 0.0)), 2)
        if abs(round(tax - book, 2) - difference) >= 0.01:
            report.add("error", seed.doc_id, "Tax depreciation schedule temporary difference does not tie")

    if seed.doc_type == "deferred_tax_memo":
        opening = round(float(seed.fields.get("opening_deferred_tax_liability", 0.0)), 2)
        movement = round(float(seed.fields.get("current_period_deferred_tax_movement", 0.0)), 2)
        ending = round(float(seed.fields.get("deferred_tax_liability_ending", 0.0)), 2)
        expense = round(float(seed.fields.get("deferred_tax_expense_amount", 0.0)), 2)
        if abs(round(opening + movement, 2) - ending) >= 0.01:
            report.add("error", seed.doc_id, "Deferred tax memo rollforward does not tie")
        if abs(movement - expense) >= 0.01:
            report.add("error", seed.doc_id, "Deferred tax expense does not equal current-period movement")

    if seed.doc_type == "lease_amortization_schedule":
        opening = round(float(seed.fields.get("opening_liability_balance", 0.0)), 2)
        payment = round(float(seed.fields.get("payment_amount", 0.0)), 2)
        interest = round(float(seed.fields.get("interest_amount", 0.0)), 2)
        principal = round(float(seed.fields.get("principal_amount", 0.0)), 2)
        ending = round(float(seed.fields.get("ending_liability_balance", 0.0)), 2)
        if abs(round(interest + principal, 2) - payment) >= 0.01:
            report.add("error", seed.doc_id, "Lease schedule payment does not equal interest plus principal")
        if abs(round(opening - principal, 2) - ending) >= 0.01:
            report.add("error", seed.doc_id, "Lease schedule ending liability does not tie")

    if seed.doc_type == "lease_modification_notice":
        old = round(float(seed.fields.get("old_liability_balance", 0.0)), 2)
        remeasured = round(float(seed.fields.get("remeasured_liability_balance", 0.0)), 2)
        delta = round(float(seed.fields.get("liability_remeasurement_delta_amount", 0.0)), 2)
        rou_delta = round(float(seed.fields.get("rou_asset_adjustment_amount", 0.0)), 2)
        if abs(round(remeasured - old, 2) - delta) >= 0.01:
            report.add("error", seed.doc_id, "Lease modification remeasurement delta does not tie")
        if abs(delta - rou_delta) >= 0.01:
            report.add("error", seed.doc_id, "Lease modification ROU asset adjustment does not equal liability delta")
