"""Reusable business-scenario factories for industries."""

from __future__ import annotations

import random

from finbalance.doc_schemas import get_doc_schema
from finbalance.generation.helpers import (
    add_months_to_date,
    amount,
    amount_scale,
    bank_row,
    choose_exchange_rate,
    choose_foreign_currency_profile,
    choose_tax_rate,
    convert_to_functional,
    currency_metadata,
    date_plus_days,
    doc_seed,
    due_date,
    line_items,
    merge_currency_metadata,
    pay_period_label,
    pick_date,
    posting,
    quantity_line_items,
    tax_breakdown_from_subtotal,
    tax_label_for_regime,
)
from finbalance.types import BusinessScenario, BusinessState, ScenarioResult


def _scaled_amount(state: BusinessState, rng: random.Random, lo: float, hi: float, bucket: str = "operating") -> float:
    return round(amount(rng, lo, hi) * amount_scale(state.industry, state.period_spec.period_type, state.difficulty_level, bucket), 2)


def _tax_details(state: BusinessState, subtotal: float, rng: random.Random, tax_rate_override: float | None = None) -> dict[str, float | str]:
    tax_label = state.tax_label or tax_label_for_regime(state.tax_regime)
    tax_rate = tax_rate_override if tax_rate_override is not None else choose_tax_rate(state.tax_regime, rng)
    details = tax_breakdown_from_subtotal(subtotal, tax_rate)
    details["tax_label"] = tax_label
    return details


def _india_gst_split(tax_amount: float) -> tuple[float, float]:
    cgst_amount = round(tax_amount / 2, 2)
    return cgst_amount, round(tax_amount - cgst_amount, 2)


def _apply_tax_fields(fields: dict[str, object], tax_details: dict[str, float | str], state: BusinessState | None = None) -> None:
    fields["subtotal"] = tax_details["subtotal"]
    fields["tax_label"] = tax_details["tax_label"]
    fields["tax_rate"] = tax_details["tax_rate"]
    fields["tax_amount"] = tax_details["tax_amount"]
    fields["total"] = tax_details["total"]
    if state and state.tax_regime == "india_gst":
        cgst_amount, sgst_amount = _india_gst_split(float(tax_details["tax_amount"]))
        fields["cgst_amount"] = cgst_amount
        fields["sgst_amount"] = sgst_amount


def _output_tax_postings(
    state: BusinessState,
    refs: list[str],
    debit_account: str,
    tax_amount: float,
    entry_date: str,
    base_label: str,
) -> list:
    if tax_amount <= 0:
        return []
    if state.tax_regime == "india_gst":
        cgst_amount, sgst_amount = _india_gst_split(tax_amount)
        return [
            posting(refs, debit_account, "CGST Payable", cgst_amount, entry_date, f"{base_label}_cgst"),
            posting(refs, debit_account, "SGST Payable", sgst_amount, entry_date, f"{base_label}_sgst"),
        ]
    return [posting(refs, debit_account, "Sales Tax Payable", tax_amount, entry_date, base_label)]


def _input_tax_postings(
    state: BusinessState,
    refs: list[str],
    credit_account: str,
    tax_amount: float,
    entry_date: str,
    base_label: str,
) -> list:
    if tax_amount <= 0:
        return []
    if state.tax_regime == "india_gst":
        cgst_amount, sgst_amount = _india_gst_split(tax_amount)
        return [
            posting(refs, "Input CGST Receivable", credit_account, cgst_amount, entry_date, f"{base_label}_cgst"),
            posting(refs, "Input SGST Receivable", credit_account, sgst_amount, entry_date, f"{base_label}_sgst"),
        ]
    return [posting(refs, "Input Tax Receivable", credit_account, tax_amount, entry_date, base_label)]


def _tax_reversal_postings(
    state: BusinessState,
    refs: list[str],
    credit_account: str,
    tax_amount: float,
    entry_date: str,
    base_label: str,
) -> list:
    if tax_amount <= 0:
        return []
    if state.tax_regime == "india_gst":
        cgst_amount, sgst_amount = _india_gst_split(tax_amount)
        return [
            posting(refs, "CGST Payable", credit_account, cgst_amount, entry_date, f"{base_label}_cgst"),
            posting(refs, "SGST Payable", credit_account, sgst_amount, entry_date, f"{base_label}_sgst"),
        ]
    return [posting(refs, "Sales Tax Payable", credit_account, tax_amount, entry_date, base_label)]


def _foreign_doc_metadata(
    state: BusinessState,
    foreign_profile: dict[str, str],
    functional_profile: dict[str, str],
    extra_overrides: dict[str, dict[str, str]] | None = None,
) -> dict[str, object]:
    metadata = {
        **currency_metadata(foreign_profile),
        "functional_currency_code": functional_profile["currency_code"],
        "functional_currency_symbol": functional_profile["currency_symbol"],
        "functional_currency_format": functional_profile["currency_format"],
    }
    if extra_overrides:
        metadata = merge_currency_metadata(metadata, extra_overrides)
    return metadata


def _functional_profile(state: BusinessState) -> dict[str, str]:
    return {
        "currency_code": state.functional_currency_code,
        "currency_symbol": state.functional_currency_symbol,
        "currency_format": state.functional_currency_format,
    }


def _foreign_profile_for_state(state: BusinessState, rng: random.Random) -> dict[str, str]:
    profile = state.metadata.get("foreign_currency_profile")
    if isinstance(profile, dict):
        return profile
    profile = choose_foreign_currency_profile(state.functional_currency_code, rng)
    state.metadata["foreign_currency_profile"] = profile
    return profile


def make_service_invoice_scenario(
    *,
    name: str,
    description: str,
    revenue_account: str,
    with_work_order: bool = False,
    cash_sale_rate: float = 0.0,
    apply_indirect_tax: bool = False,
) -> BusinessScenario:
    doc_types = ("customer_invoice", "work_order") if with_work_order else ("customer_invoice",)

    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        issue_date = pick_date(state.period_spec, rng, "early")
        customer = rng.choice(state.master_data["customers"])
        subtotal = _scaled_amount(state, rng, 1800, 8200, "operating")
        invoice_number = state.next_number("INV")
        refs: list[str] = []
        documents = []
        if with_work_order:
            work_order = doc_seed(
                state,
                doc_type="work_order",
                title=get_doc_schema("work_order").title,
                date=date_plus_days(issue_date, -1),
                role="support_doc",
                fields={
                    "work_order_number": state.next_number("WO"),
                    "customer": customer,
                    "job_site": rng.choice(state.master_data["job_sites"]),
                    "scope": rng.choice(state.master_data["services"]),
                    "approved_amount": subtotal,
                },
                metadata={"footer_note": "Approved job scope supporting the related invoice."},
            )
            documents.append(work_order)
            refs.append(work_order.doc_id)

        total = subtotal
        fields = {
            "number": invoice_number,
            "customer": customer,
            "due_date": due_date(issue_date, rng, 10, 24),
            "total": total,
            "line_items": line_items(subtotal, [rng.choice(state.master_data["services"]), "Follow-up support"], rng),
            "contract_ref": state.next_number("CTR"),
            "document_currency": state.currency_code,
        }
        tax_amount = 0.0
        if apply_indirect_tax and state.tax_regime != "none":
            tax_details = _tax_details(state, subtotal, rng)
            _apply_tax_fields(fields, tax_details, state)
            total = float(tax_details["total"])
            tax_amount = float(tax_details["tax_amount"])
        if state.industry == "field_services":
            fields["job_code"] = state.next_number("JOB")
        if state.industry == "wholesale_distribution":
            fields["shipment_ref"] = state.next_number("SHP")

        invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=issue_date,
            role="posting_doc",
            fields=fields,
            metadata={"counterparty_name": customer},
        )
        documents.append(invoice)
        refs.append(invoice.doc_id)

        postings = []
        bank_rows = []
        if rng.random() < cash_sale_rate:
            postings.append(posting(refs, "Cash", revenue_account, subtotal, issue_date, name))
            postings.extend(_output_tax_postings(state, refs, "Cash", tax_amount, issue_date, f"{name}_tax"))
            bank_rows.append(bank_row(issue_date, f"Customer payment {invoice_number}", total))
        else:
            postings.append(posting(refs, "Accounts Receivable", revenue_account, subtotal, issue_date, name))
            postings.extend(_output_tax_postings(state, refs, "Accounts Receivable", tax_amount, issue_date, f"{name}_tax"))
            state.open_receivables.append(
                {
                    "reference": invoice_number,
                    "doc_id": invoice.doc_id,
                    "counterparty": customer,
                    "remaining": total,
                    "category": "customer",
                }
            )
        return ScenarioResult(documents=documents, postings=postings, bank_rows=bank_rows)

    return BusinessScenario(name=name, description=description, doc_types=doc_types, doc_count_hint=len(doc_types), builder=build, allow_repeat=True)


def make_vendor_bill_scenario(
    *,
    name: str,
    description: str,
    doc_type: str,
    debit_account: str,
    paid_now_rate: float = 0.0,
    quantity_lines: bool = False,
    apply_indirect_tax: bool = False,
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        issue_date = pick_date(state.period_spec, rng, "early")
        vendor = rng.choice(state.master_data["vendors"])
        subtotal = _scaled_amount(state, rng, 420, 5400, "operating")
        if quantity_lines and state.industry == "field_services" and debit_account == "Repairs Expense":
            descriptions = ["Repair parts for field equipment", "Preventive maintenance service parts"]
        else:
            descriptions = state.master_data["products"] if quantity_lines else [rng.choice(state.master_data["services"]), "Support fee"]
        rows = quantity_line_items(subtotal, descriptions[:2], rng) if quantity_lines else line_items(subtotal, descriptions[:2], rng)
        fields = {
            "number": state.next_number("BILL"),
            "vendor": vendor,
            "due_date": due_date(issue_date, rng, 10, 21),
            "total": subtotal,
            "line_items": rows,
            "document_currency": state.currency_code,
        }
        tax_amount = 0.0
        total = subtotal
        if apply_indirect_tax and state.tax_regime != "none":
            tax_details = _tax_details(state, subtotal, rng)
            _apply_tax_fields(fields, tax_details, state)
            total = float(tax_details["total"])
            tax_amount = float(tax_details["tax_amount"])
        if doc_type == "vendor_invoice":
            fields["expense_account_label"] = debit_account
        if doc_type == "supplier_invoice":
            fields["expense_account_label"] = debit_account
        if doc_type == "supplier_invoice" and state.industry == "wholesale_distribution":
            fields["goods_receipt_ref"] = state.next_number("GRN-LINK")
        bill = doc_seed(
            state,
            doc_type=doc_type,
            title=get_doc_schema(doc_type).title_for(state.industry),
            date=issue_date,
            role="posting_doc",
            fields=fields,
            metadata={"counterparty_name": vendor},
        )
        credit_account = "Cash" if rng.random() < paid_now_rate else "Accounts Payable"
        postings = [posting([bill.doc_id], debit_account, credit_account, subtotal, issue_date, name)]
        postings.extend(_input_tax_postings(state, [bill.doc_id], credit_account, tax_amount, issue_date, f"{name}_tax"))
        bank_rows = []
        if credit_account == "Cash":
            bank_rows.append(bank_row(issue_date, f"{vendor} payment {fields['number']}", -total))
        else:
            state.open_payables.append(
                {
                    "reference": fields["number"],
                    "doc_id": bill.doc_id,
                    "counterparty": vendor,
                    "remaining": total,
                    "category": "vendor",
                }
            )
        return ScenarioResult(documents=[bill], postings=postings, bank_rows=bank_rows)

    return BusinessScenario(name=name, description=description, doc_types=(doc_type,), doc_count_hint=1, builder=build, allow_repeat=True)


def make_expense_receipt_scenario(
    *,
    name: str,
    description: str,
    debit_account: str,
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        receipt_date = pick_date(state.period_spec, rng, "mid")
        merchant = rng.choice(state.master_data["vendors"])
        if rng.random() < 0.2:
            total = _scaled_amount(state, rng, 5, 80, "micro")
        else:
            total = _scaled_amount(state, rng, 60, 780, "small")
        line_labels = [debit_account]
        if debit_account.endswith("Expense"):
            line_labels.append(debit_account.replace("Expense", "Incidentals").strip())
        else:
            line_labels.append(f"{debit_account} Incidentals")
        receipt = doc_seed(
            state,
            doc_type="expense_receipt",
            title=get_doc_schema("expense_receipt").title,
            date=receipt_date,
            role="posting_doc",
            fields={
                "receipt_number": state.next_number("RCPT"),
                "merchant": merchant,
                "total": total,
                "line_items": line_items(total, line_labels, rng),
                "payment_method": rng.choice(["Company card", "Debit card", "Cash"]),
            },
            metadata={"counterparty_name": merchant},
        )
        postings = [posting([receipt.doc_id], debit_account, "Cash", total, receipt_date, name)]
        return ScenarioResult(
            documents=[receipt],
            postings=postings,
            bank_rows=[bank_row(receipt_date, f"{merchant} receipt {receipt.fields['receipt_number']}", -total)],
        )

    return BusinessScenario(name=name, description=description, doc_types=("expense_receipt",), doc_count_hint=1, builder=build, allow_repeat=True)


def make_receivable_settlement_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        item = _take_open_item(state.open_receivables)
        settle_amount = item["remaining"]
        if state.difficulty_level >= 4:
            settle_amount = round(item["remaining"] * rng.uniform(0.55, 1.0), 2)
        pay_date = pick_date(state.period_spec, rng, "late")
        advice = doc_seed(
            state,
            doc_type="payment_advice",
            title=get_doc_schema("payment_advice").title,
            date=pay_date,
            role="support_doc",
            fields={
                "number": state.next_number("PAY"),
                "counterparty": item["counterparty"],
                "amount": settle_amount,
                "reference": item["reference"],
                "payment_method": rng.choice(["Bank transfer", "Card", "Wire"]),
                "payment_for": "Customer settlement",
            },
            metadata={"counterparty_name": item["counterparty"]},
        )
        item["remaining"] = round(item["remaining"] - settle_amount, 2)
        if item["remaining"] > 0.01:
            state.open_receivables.insert(0, item)
        refs = [advice.doc_id, item["doc_id"]]
        postings = [posting(refs, "Cash", "Accounts Receivable", settle_amount, pay_date, name)]
        return ScenarioResult(
            documents=[advice],
            postings=postings,
            bank_rows=[bank_row(pay_date, f"Customer settlement {item['reference']}", settle_amount)],
        )

    return BusinessScenario(name=name, description=description, doc_types=("payment_advice",), doc_count_hint=1, builder=build)


def make_partial_multi_receivable_payment_scenario(
    *,
    name: str,
    description: str,
    revenue_account: str,
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        customer = rng.choice(state.master_data["customers"])
        invoices = []
        postings = []
        created_items: list[dict[str, object]] = []
        issue_dates = sorted(
            [
                pick_date(state.period_spec, rng, "opening"),
                pick_date(state.period_spec, rng, "early"),
                pick_date(state.period_spec, rng, "mid"),
            ]
        )
        for idx, issue_date in enumerate(issue_dates, start=1):
            total = _scaled_amount(state, rng, 1200, 5200, "operating")
            invoice = doc_seed(
                state,
                doc_type="customer_invoice",
                title=get_doc_schema("customer_invoice").title_for(state.industry),
                date=issue_date,
                role="posting_doc",
                fields={
                    "number": state.next_number("INV"),
                    "customer": customer,
                    "due_date": due_date(issue_date, rng, 10, 24),
                    "total": total,
                    "line_items": line_items(
                        total,
                        [rng.choice(state.master_data["services"]), f"Milestone {idx} work"],
                        rng,
                    ),
                    "contract_ref": state.next_number("CTR"),
                },
                metadata={"counterparty_name": customer},
            )
            invoices.append(invoice)
            postings.append(posting([invoice.doc_id], "Accounts Receivable", revenue_account, total, issue_date, f"{name}_invoice_{idx}"))
            created_items.append(
                {
                    "reference": invoice.fields["number"],
                    "doc_id": invoice.doc_id,
                    "counterparty": customer,
                    "remaining": total,
                    "category": "customer",
                }
            )

        partial_amount = round(float(created_items[2]["remaining"]) * rng.uniform(0.35, 0.7), 2)
        allocations = [
            {"reference": created_items[0]["reference"], "allocated_amount": created_items[0]["remaining"], "status": "Closed"},
            {"reference": created_items[1]["reference"], "allocated_amount": created_items[1]["remaining"], "status": "Closed"},
            {"reference": created_items[2]["reference"], "allocated_amount": partial_amount, "status": "Partially paid"},
        ]
        settle_total = round(sum(float(line["allocated_amount"]) for line in allocations), 2)
        pay_date = pick_date(state.period_spec, rng, "late")
        advice = doc_seed(
            state,
            doc_type="payment_advice",
            title=get_doc_schema("payment_advice").title,
            date=pay_date,
            role="support_doc",
            fields={
                "number": state.next_number("PAY"),
                "counterparty": customer,
                "amount": settle_total,
                "reference": "Multiple invoice allocation",
                "payment_method": rng.choice(["Bank transfer", "Wire", "ACH"]),
                "payment_for": "Combined settlement against several invoices",
                "allocations": allocations,
            },
            metadata={"counterparty_name": customer},
        )
        for item, allocation in zip(created_items, allocations):
            settle_amount = round(float(allocation["allocated_amount"]), 2)
            postings.append(
                posting([advice.doc_id, str(item["doc_id"])], "Cash", "Accounts Receivable", settle_amount, pay_date, f"{name}_{item['reference']}")
            )
            remaining = round(float(item["remaining"]) - settle_amount, 2)
            if remaining > 0.01:
                state.open_receivables.append({**item, "remaining": remaining})
        return ScenarioResult(
            documents=[*invoices, advice],
            postings=postings,
            bank_rows=[bank_row(pay_date, f"Combined customer settlement {advice.fields['number']}", settle_total)],
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("customer_invoice", "payment_advice"),
        doc_count_hint=4,
        builder=build,
    )


def make_payable_settlement_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        item = _take_open_item(state.open_payables)
        settle_amount = item["remaining"]
        if state.difficulty_level >= 4:
            settle_amount = round(item["remaining"] * rng.uniform(0.55, 1.0), 2)
        pay_date = pick_date(state.period_spec, rng, "late")
        advice = doc_seed(
            state,
            doc_type="payment_advice",
            title=get_doc_schema("payment_advice").title,
            date=pay_date,
            role="support_doc",
            fields={
                "number": state.next_number("PAY"),
                "counterparty": item["counterparty"],
                "amount": settle_amount,
                "reference": item["reference"],
                "payment_method": rng.choice(["Bank transfer", "ACH", "Wire"]),
                "payment_for": "Supplier settlement",
            },
            metadata={"counterparty_name": item["counterparty"]},
        )
        item["remaining"] = round(item["remaining"] - settle_amount, 2)
        if item["remaining"] > 0.01:
            state.open_payables.insert(0, item)
        refs = [advice.doc_id, item["doc_id"]]
        postings = [posting(refs, "Accounts Payable", "Cash", settle_amount, pay_date, name)]
        return ScenarioResult(
            documents=[advice],
            postings=postings,
            bank_rows=[bank_row(pay_date, f"Supplier settlement {item['reference']}", -settle_amount)],
        )

    return BusinessScenario(name=name, description=description, doc_types=("payment_advice",), doc_count_hint=1, builder=build)


def make_fx_service_invoice_scenario(
    *,
    name: str,
    description: str,
    revenue_account: str,
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        issue_date = pick_date(state.period_spec, rng, "early")
        customer = rng.choice(state.master_data["customers"])
        foreign_profile = _foreign_profile_for_state(state, rng)
        functional_profile = _functional_profile(state)
        source_total = _scaled_amount(state, rng, 1800, 7800, "operating")
        exchange_rate = choose_exchange_rate(functional_profile["currency_code"], foreign_profile["currency_code"], rng)
        functional_total = convert_to_functional(source_total, exchange_rate)
        contract_ref = state.next_number("FXCTR")
        invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=issue_date,
            role="posting_doc",
            fields={
                "number": state.next_number("FXINV"),
                "customer": customer,
                "due_date": due_date(issue_date, rng, 12, 24),
                "total": source_total,
                "line_items": line_items(source_total, [rng.choice(state.master_data["services"]), "Foreign-currency support"], rng),
                "contract_ref": contract_ref,
                "document_currency": foreign_profile["currency_code"],
            },
            metadata=_foreign_doc_metadata(state, foreign_profile, functional_profile),
        )
        fx_notice = doc_seed(
            state,
            doc_type="exchange_rate_notice",
            title=get_doc_schema("exchange_rate_notice").title,
            date=issue_date,
            role="support_doc",
            fields={
                "notice_number": state.next_number("RATE"),
                "reference": invoice.fields["number"],
                "source_currency": foreign_profile["currency_code"],
                "functional_currency": functional_profile["currency_code"],
                "exchange_rate": exchange_rate,
                "source_amount": source_total,
                "functional_amount": functional_total,
                "rate_date": issue_date,
                "rate_type": "Spot rate at invoice date",
            },
            metadata=merge_currency_metadata(
                dict(functional_profile),
                {
                    "source_amount": currency_metadata(foreign_profile),
                    "functional_amount": currency_metadata(functional_profile),
                },
            ),
        )
        refs = [invoice.doc_id, fx_notice.doc_id]
        postings = [posting(refs, "Accounts Receivable", revenue_account, functional_total, issue_date, name)]
        state.open_fx_receivables.append(
            {
                "reference": invoice.fields["number"],
                "doc_id": invoice.doc_id,
                "counterparty": customer,
                "source_currency": foreign_profile["currency_code"],
                "source_symbol": foreign_profile["currency_symbol"],
                "source_format": foreign_profile["currency_format"],
                "source_remaining": source_total,
                "functional_remaining": functional_total,
                "booked_rate": exchange_rate,
                "revenue_account": revenue_account,
                "category": "customer",
            }
        )
        return ScenarioResult(documents=[invoice, fx_notice], postings=postings)

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("customer_invoice", "exchange_rate_notice"),
        doc_count_hint=2,
        builder=build,
        period_types=("quarter", "year"),
    )


def make_fx_receivable_settlement_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        if not state.open_fx_receivables:
            raise ValueError(f"Scenario '{name}' needs an open foreign-currency receivable")
        item = state.open_fx_receivables.pop(0)
        pay_date = pick_date(state.period_spec, rng, "late")
        functional_profile = _functional_profile(state)
        settlement_rate = round(item["booked_rate"] * rng.uniform(0.94, 1.08), 4)
        source_amount = round(float(item["source_remaining"]), 2)
        booked_amount = round(float(item["functional_remaining"]), 2)
        settled_amount = convert_to_functional(source_amount, settlement_rate)
        fx_difference = round(settled_amount - booked_amount, 2)
        advice = doc_seed(
            state,
            doc_type="payment_advice",
            title=get_doc_schema("payment_advice").title,
            date=pay_date,
            role="posting_doc",
            fields={
                "number": state.next_number("FXPAY"),
                "counterparty": item["counterparty"],
                "amount": settled_amount,
                "reference": item["reference"],
                "payment_method": rng.choice(["Wire", "Bank transfer"]),
                "payment_for": "Foreign-currency receivable settlement",
                "document_currency": functional_profile["currency_code"],
                "source_amount": source_amount,
                "source_currency": item["source_currency"],
                "functional_currency": functional_profile["currency_code"],
                "functional_amount": settled_amount,
                "exchange_rate": settlement_rate,
                "fx_difference": abs(fx_difference),
            },
            metadata=merge_currency_metadata(
                dict(functional_profile),
                {
                    "source_amount": {
                        "currency_symbol": item["source_symbol"],
                        "currency_format": item["source_format"],
                        "currency_code": item["source_currency"],
                    },
                    "functional_amount": currency_metadata(functional_profile),
                    "amount": currency_metadata(functional_profile),
                    "fx_difference": currency_metadata(functional_profile),
                },
            ),
        )
        refs = [advice.doc_id, item["doc_id"]]
        postings = [posting(refs, "Cash", "Accounts Receivable", min(settled_amount, booked_amount), pay_date, name)]
        if fx_difference > 0:
            postings.append(posting(refs, "Cash", "Foreign Exchange Gain", fx_difference, pay_date, f"{name}_gain"))
        elif fx_difference < 0:
            postings.append(posting(refs, "Foreign Exchange Loss", "Accounts Receivable", abs(fx_difference), pay_date, f"{name}_loss"))
        return ScenarioResult(
            documents=[advice],
            postings=postings,
            bank_rows=[bank_row(pay_date, f"Foreign receipt {item['reference']}", settled_amount)],
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("payment_advice",),
        doc_count_hint=1,
        builder=build,
        period_types=("quarter", "year"),
    )


def make_fx_vendor_bill_scenario(
    *,
    name: str,
    description: str,
    debit_account: str,
    doc_type: str = "vendor_invoice",
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        issue_date = pick_date(state.period_spec, rng, "early")
        vendor = rng.choice(state.master_data["vendors"])
        foreign_profile = _foreign_profile_for_state(state, rng)
        functional_profile = _functional_profile(state)
        source_total = _scaled_amount(state, rng, 850, 6200, "operating")
        exchange_rate = choose_exchange_rate(functional_profile["currency_code"], foreign_profile["currency_code"], rng)
        functional_total = convert_to_functional(source_total, exchange_rate)
        bill = doc_seed(
            state,
            doc_type=doc_type,
            title=get_doc_schema(doc_type).title_for(state.industry),
            date=issue_date,
            role="posting_doc",
            fields={
                "number": state.next_number("FXBILL"),
                "vendor": vendor,
                "due_date": due_date(issue_date, rng, 12, 24),
                "total": source_total,
                "line_items": line_items(source_total, [rng.choice(state.master_data["services"]), "Foreign-currency support"], rng),
                "document_currency": foreign_profile["currency_code"],
            },
            metadata=_foreign_doc_metadata(state, foreign_profile, functional_profile),
        )
        if doc_type == "vendor_invoice":
            bill.fields["expense_account_label"] = debit_account
        fx_notice = doc_seed(
            state,
            doc_type="exchange_rate_notice",
            title=get_doc_schema("exchange_rate_notice").title,
            date=issue_date,
            role="support_doc",
            fields={
                "notice_number": state.next_number("RATE"),
                "reference": bill.fields["number"],
                "source_currency": foreign_profile["currency_code"],
                "functional_currency": functional_profile["currency_code"],
                "exchange_rate": exchange_rate,
                "source_amount": source_total,
                "functional_amount": functional_total,
                "rate_date": issue_date,
                "rate_type": "Spot rate at bill date",
            },
            metadata=merge_currency_metadata(
                dict(functional_profile),
                {
                    "source_amount": currency_metadata(foreign_profile),
                    "functional_amount": currency_metadata(functional_profile),
                },
            ),
        )
        refs = [bill.doc_id, fx_notice.doc_id]
        postings = [posting(refs, debit_account, "Accounts Payable", functional_total, issue_date, name)]
        state.open_fx_payables.append(
            {
                "reference": bill.fields["number"],
                "doc_id": bill.doc_id,
                "counterparty": vendor,
                "source_currency": foreign_profile["currency_code"],
                "source_symbol": foreign_profile["currency_symbol"],
                "source_format": foreign_profile["currency_format"],
                "source_remaining": source_total,
                "functional_remaining": functional_total,
                "booked_rate": exchange_rate,
                "debit_account": debit_account,
                "category": "vendor",
            }
        )
        return ScenarioResult(documents=[bill, fx_notice], postings=postings)

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=(doc_type, "exchange_rate_notice"),
        doc_count_hint=2,
        builder=build,
        period_types=("quarter", "year"),
    )


def make_fx_payable_settlement_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        if not state.open_fx_payables:
            raise ValueError(f"Scenario '{name}' needs an open foreign-currency payable")
        item = state.open_fx_payables.pop(0)
        pay_date = pick_date(state.period_spec, rng, "late")
        functional_profile = _functional_profile(state)
        settlement_rate = round(item["booked_rate"] * rng.uniform(0.94, 1.08), 4)
        source_amount = round(float(item["source_remaining"]), 2)
        booked_amount = round(float(item["functional_remaining"]), 2)
        paid_amount = convert_to_functional(source_amount, settlement_rate)
        fx_difference = round(paid_amount - booked_amount, 2)
        advice = doc_seed(
            state,
            doc_type="payment_advice",
            title=get_doc_schema("payment_advice").title,
            date=pay_date,
            role="posting_doc",
            fields={
                "number": state.next_number("FXPAY"),
                "counterparty": item["counterparty"],
                "amount": paid_amount,
                "reference": item["reference"],
                "payment_method": rng.choice(["Wire", "Bank transfer"]),
                "payment_for": "Foreign-currency payable settlement",
                "document_currency": functional_profile["currency_code"],
                "source_amount": source_amount,
                "source_currency": item["source_currency"],
                "functional_currency": functional_profile["currency_code"],
                "functional_amount": paid_amount,
                "exchange_rate": settlement_rate,
                "fx_difference": abs(fx_difference),
            },
            metadata=merge_currency_metadata(
                dict(functional_profile),
                {
                    "source_amount": {
                        "currency_symbol": item["source_symbol"],
                        "currency_format": item["source_format"],
                        "currency_code": item["source_currency"],
                    },
                    "functional_amount": currency_metadata(functional_profile),
                    "amount": currency_metadata(functional_profile),
                    "fx_difference": currency_metadata(functional_profile),
                },
            ),
        )
        refs = [advice.doc_id, item["doc_id"]]
        postings = [posting(refs, "Accounts Payable", "Cash", min(booked_amount, paid_amount), pay_date, name)]
        if fx_difference > 0:
            postings.append(posting(refs, "Foreign Exchange Loss", "Cash", fx_difference, pay_date, f"{name}_loss"))
        elif fx_difference < 0:
            postings.append(posting(refs, "Accounts Payable", "Foreign Exchange Gain", abs(fx_difference), pay_date, f"{name}_gain"))
        return ScenarioResult(
            documents=[advice],
            postings=postings,
            bank_rows=[bank_row(pay_date, f"Foreign payment {item['reference']}", -paid_amount)],
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("payment_advice",),
        doc_count_hint=1,
        builder=build,
        period_types=("quarter", "year"),
    )


def make_fx_remeasurement_scenario(
    *,
    name: str,
    description: str,
    target: str = "receivable",
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        pool = state.open_fx_receivables if target == "receivable" else state.open_fx_payables
        if not pool:
            raise ValueError(f"Scenario '{name}' needs an open foreign-currency {target}")
        item = pool[0]
        functional_profile = _functional_profile(state)
        closing_rate = round(float(item["booked_rate"]) * rng.uniform(0.95, 1.1), 4)
        source_amount = round(float(item["source_remaining"]), 2)
        booked_amount = round(float(item["functional_remaining"]), 2)
        remeasured_amount = convert_to_functional(source_amount, closing_rate)
        difference = round(remeasured_amount - booked_amount, 2)
        memo = doc_seed(
            state,
            doc_type="fx_remeasurement_memo",
            title=get_doc_schema("fx_remeasurement_memo").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "memo_id": state.next_number("FXREM"),
                "reference": item["reference"],
                "source_currency": item["source_currency"],
                "functional_currency": functional_profile["currency_code"],
                "source_amount": source_amount,
                "booked_amount": booked_amount,
                "closing_rate": closing_rate,
                "remeasured_amount": remeasured_amount,
                "difference_amount": abs(difference),
                "narrative": "Open foreign-currency balance remeasured at the closing rate.",
            },
            metadata=merge_currency_metadata(
                dict(functional_profile),
                {
                    "source_amount": {
                        "currency_symbol": item["source_symbol"],
                        "currency_format": item["source_format"],
                        "currency_code": item["source_currency"],
                    },
                    "booked_amount": currency_metadata(functional_profile),
                    "remeasured_amount": currency_metadata(functional_profile),
                    "difference_amount": currency_metadata(functional_profile),
                },
            ),
        )
        if target == "receivable":
            if difference > 0:
                postings = [posting([memo.doc_id, item["doc_id"]], "Accounts Receivable", "Foreign Exchange Gain", difference, state.period_end, name)]
            else:
                postings = [posting([memo.doc_id, item["doc_id"]], "Foreign Exchange Loss", "Accounts Receivable", abs(difference), state.period_end, name)]
        else:
            if difference > 0:
                postings = [posting([memo.doc_id, item["doc_id"]], "Foreign Exchange Loss", "Accounts Payable", difference, state.period_end, name)]
            else:
                postings = [posting([memo.doc_id, item["doc_id"]], "Accounts Payable", "Foreign Exchange Gain", abs(difference), state.period_end, name)]
        item["functional_remaining"] = remeasured_amount
        item["booked_rate"] = closing_rate
        return ScenarioResult(documents=[memo], postings=postings)

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("fx_remeasurement_memo",),
        doc_count_hint=1,
        builder=build,
        period_types=("year",),
    )


def make_interbank_transfer_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        transfer_date = pick_date(state.period_spec, rng, "late")
        transfer_amount = _scaled_amount(state, rng, 1800, 14000, "financing")
        state.bank_accounts.setdefault(
            "Reserve Cash",
            {"account_number": f"1002-{state.record_id[-2:]}99", "display_name": "Reserve Account"},
        )
        advice = doc_seed(
            state,
            doc_type="transfer_advice",
            title=get_doc_schema("transfer_advice").title,
            date=transfer_date,
            role="support_doc",
            fields={
                "transfer_number": state.next_number("TRF"),
                "from_account": "Cash",
                "to_account": "Reserve Cash",
                "amount": transfer_amount,
                "transfer_date": transfer_date,
                "reference": state.next_number("TRX"),
            },
            metadata={"footer_note": "Treasury desk transfer between company-controlled bank accounts."},
        )
        postings = [posting([advice.doc_id], "Reserve Cash", "Cash", transfer_amount, transfer_date, name)]
        bank_rows = [
            bank_row(transfer_date, f"Transfer out {advice.fields['reference']}", -transfer_amount, account="Cash"),
            bank_row(transfer_date, f"Transfer in {advice.fields['reference']}", transfer_amount, account="Reserve Cash"),
        ]
        return ScenarioResult(documents=[advice], postings=postings, bank_rows=bank_rows)

    return BusinessScenario(name=name, description=description, doc_types=("transfer_advice",), doc_count_hint=1, builder=build)


def make_reclassification_correction_scenario(
    *,
    name: str,
    description: str,
    from_account: str,
    to_account: str,
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        original_date = pick_date(state.period_spec, rng, "mid")
        merchant = rng.choice(state.master_data["vendors"])
        total = _scaled_amount(state, rng, 110, 780, "small")
        receipt = doc_seed(
            state,
            doc_type="expense_receipt",
            title=get_doc_schema("expense_receipt").title,
            date=original_date,
            role="posting_doc",
            fields={
                "receipt_number": state.next_number("RCPT"),
                "merchant": merchant,
                "total": total,
                "line_items": line_items(total, [from_account, f"{from_account.replace('Expense', '').strip()} follow-up"], rng),
                "payment_method": rng.choice(["Company card", "Debit card"]),
            },
            metadata={"counterparty_name": merchant},
        )
        memo = doc_seed(
            state,
            doc_type="reclassification_memo",
            title=get_doc_schema("reclassification_memo").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "memo_id": state.next_number("RECLASS"),
                "original_reference": receipt.fields["receipt_number"],
                "from_account": from_account,
                "to_account": to_account,
                "amount": total,
                "narrative": "Review of the card packet showed the spend belonged in a different expense category.",
            },
            metadata={"footer_note": "Approved during the period-end account review."},
        )
        postings = [
            posting([receipt.doc_id], from_account, "Cash", total, original_date, f"{name}_original"),
            posting([memo.doc_id, receipt.doc_id], to_account, from_account, total, state.period_end, f"{name}_correction"),
        ]
        return ScenarioResult(
            documents=[receipt, memo],
            postings=postings,
            bank_rows=[bank_row(original_date, f"{merchant} receipt {receipt.fields['receipt_number']}", -total)],
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("expense_receipt", "reclassification_memo"),
        doc_count_hint=2,
        builder=build,
    )


def make_reissued_invoice_scenario(
    *,
    name: str,
    description: str,
    revenue_account: str,
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        customer = rng.choice(state.master_data["customers"])
        original_date = pick_date(state.period_spec, rng, "early")
        replacement_date = date_plus_days(original_date, rng.randint(2, 9))
        original_total = _scaled_amount(state, rng, 1800, 7200, "operating")
        replacement_total = round(original_total * rng.uniform(0.94, 1.08), 2)
        original_ref = state.next_number("INV")
        replacement_ref = state.next_number("INV")
        original_invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=original_date,
            role="distractor_doc",
            fields={
                "number": original_ref,
                "customer": customer,
                "due_date": due_date(original_date, rng, 10, 22),
                "total": original_total,
                "line_items": line_items(original_total, [rng.choice(state.master_data["services"]), "Draft billing copy"], rng),
                "contract_ref": state.next_number("CTR"),
            },
            metadata={"counterparty_name": customer, "footer_note": "Billing office archive copy retained with the packet."},
        )
        note = doc_seed(
            state,
            doc_type="cancellation_note",
            title=get_doc_schema("cancellation_note").title,
            date=replacement_date,
            role="support_doc",
            fields={
                "note_number": state.next_number("CNCL"),
                "withdrawn_reference": original_ref,
                "replacement_reference": replacement_ref,
                "reason": f"{original_ref} is withdrawn and must not be posted. Use {replacement_ref} as the only valid invoice.",
            },
            metadata={"counterparty_name": customer},
        )
        replacement_invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=replacement_date,
            role="posting_doc",
            fields={
                "number": replacement_ref,
                "customer": customer,
                "due_date": due_date(replacement_date, rng, 10, 22),
                "total": replacement_total,
                "line_items": line_items(replacement_total, [rng.choice(state.master_data["services"]), "Reissued billing"], rng),
                "contract_ref": original_invoice.fields["contract_ref"],
            },
            metadata={"counterparty_name": customer},
        )
        state.open_receivables.append(
            {
                "reference": replacement_ref,
                "doc_id": replacement_invoice.doc_id,
                "counterparty": customer,
                "remaining": replacement_total,
                "category": "customer",
            }
        )
        postings = [
            posting(
                [original_invoice.doc_id, note.doc_id, replacement_invoice.doc_id],
                "Accounts Receivable",
                revenue_account,
                replacement_total,
                replacement_date,
                name,
            )
        ]
        return ScenarioResult(documents=[original_invoice, note, replacement_invoice], postings=postings)

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("customer_invoice", "cancellation_note"),
        doc_count_hint=3,
        builder=build,
    )


def make_payroll_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        gross = _scaled_amount(state, rng, 2400, 9200, "payroll")
        employer_tax = round(gross * rng.uniform(0.08, 0.14), 2)
        cash = round(gross + employer_tax, 2)
        pay_date = pick_date(state.period_spec, rng, "late")
        headcount = rng.randint(3, min(12, len(state.master_data["employees"]) + 4))
        payroll = doc_seed(
            state,
            doc_type="payroll_summary",
            title=get_doc_schema("payroll_summary").title,
            date=pay_date,
            role="posting_doc",
            fields={
                "run_number": state.next_number("PAYRUN"),
                "pay_period": pay_period_label(state.period_spec),
                "headcount": headcount,
                "gross_pay": gross,
                "employer_tax": employer_tax,
                "cash_outflow": cash,
            },
        )
        postings = [
            posting([payroll.doc_id], "Salaries Expense", "Cash", gross, pay_date, f"{name}_gross"),
            posting([payroll.doc_id], "Payroll Tax Expense", "Cash", employer_tax, pay_date, f"{name}_tax"),
        ]
        return ScenarioResult(
            documents=[payroll],
            postings=postings,
            bank_rows=[bank_row(pay_date, f"Payroll {payroll.fields['run_number']}", -cash)],
        )

    return BusinessScenario(name=name, description=description, doc_types=("payroll_summary",), doc_count_hint=1, builder=build, allow_repeat=True)


def make_prepaid_expense_scenario(
    *,
    name: str,
    description: str,
    notice_doc_type: str,
    vendor_label: str,
    prepaid_account: str,
    expense_account: str,
    service_label: str,
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        notice_date = pick_date(state.period_spec, rng, "opening")
        total = _scaled_amount(state, rng, 1800, 6400, "operating")
        monthly = round(total / 3, 2)
        end_date = add_months_to_date(notice_date, 3)
        notice = doc_seed(
            state,
            doc_type=notice_doc_type,
            title=get_doc_schema(notice_doc_type).title,
            date=notice_date,
            role="posting_doc",
            fields={
                "number": state.next_number("PRE"),
                "vendor": rng.choice(state.master_data[vendor_label]),
                "property_name": rng.choice(state.master_data.get("properties", state.master_data["customers"])),
                "service_start": notice_date,
                "service_end": date_plus_days(end_date, -1),
                "total": total,
                "monthly_amount": monthly,
            },
            metadata={"footer_note": f"{service_label} paid in advance and tracked for later release."},
        )
        memo = doc_seed(
            state,
            doc_type="service_period_memo",
            title=get_doc_schema("service_period_memo").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "memo_id": state.next_number("MEMO"),
                "subject": f"{service_label} release",
                "reference": notice.fields["number"],
                "recognized_amount": monthly,
                "narrative": f"One month of {service_label.lower()} has expired and should be expensed this period.",
            },
        )
        purchase_refs = [notice.doc_id]
        release_refs = [notice.doc_id, memo.doc_id]
        postings = [
            posting(purchase_refs, prepaid_account, "Cash", total, notice_date, f"{name}_purchase"),
            posting(release_refs, expense_account, prepaid_account, monthly, state.period_end, f"{name}_release"),
        ]
        return ScenarioResult(
            documents=[notice, memo],
            postings=postings,
            bank_rows=[bank_row(notice_date, f"{service_label} prepayment {notice.fields['number']}", -total)],
        )

    return BusinessScenario(name=name, description=description, doc_types=(notice_doc_type, "service_period_memo"), doc_count_hint=2, builder=build)


def make_prepaid_rent_scenario(*, name: str, description: str) -> BusinessScenario:
    return make_prepaid_expense_scenario(
        name=name,
        description=description,
        notice_doc_type="rent_notice",
        vendor_label="vendors",
        prepaid_account="Prepaid Rent",
        expense_account="Rent Expense",
        service_label="Rent",
    )


def make_prepaid_insurance_scenario(*, name: str, description: str) -> BusinessScenario:
    return make_prepaid_expense_scenario(
        name=name,
        description=description,
        notice_doc_type="insurance_notice",
        vendor_label="insurance_carriers",
        prepaid_account="Prepaid Insurance",
        expense_account="Insurance Expense",
        service_label="Insurance coverage",
    )


def make_loan_activity_scenario(*, name: str, description: str, mode: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        activity_date = pick_date(state.period_spec, rng, "mid" if mode == "draw" else "late")
        lender = rng.choice(state.master_data["lenders"])
        opening_principal = _scaled_amount(state, rng, 0, 12000, "financing") if mode == "repayment" else _scaled_amount(state, rng, 0, 2500, "financing")
        draw_amount = _scaled_amount(state, rng, 2800, 14000, "financing") if mode == "draw" else 0.0
        principal_paid = _scaled_amount(state, rng, 800, 2600, "financing") if mode == "repayment" else 0.0
        interest_paid = round(principal_paid * rng.uniform(0.06, 0.15), 2) if mode == "repayment" else 0.0
        ending_principal = round(opening_principal + draw_amount - principal_paid, 2)
        statement = doc_seed(
            state,
            doc_type="loan_statement",
            title=get_doc_schema("loan_statement").title,
            date=activity_date,
            role="posting_doc",
            fields={
                "loan_number": state.next_number("LOAN"),
                "lender": lender,
                "opening_principal": opening_principal,
                "draw_amount": draw_amount,
                "principal_paid": principal_paid,
                "interest_paid": interest_paid,
                "ending_principal": ending_principal,
                "note": "Scheduled lender activity for the selected period.",
            },
            metadata={"counterparty_name": lender},
        )
        postings = []
        bank_rows = []
        if draw_amount > 0:
            postings.append(posting([statement.doc_id], "Cash", "Loans Payable", draw_amount, activity_date, name))
            bank_rows.append(bank_row(activity_date, f"Loan draw {statement.fields['loan_number']}", draw_amount))
        if principal_paid > 0:
            postings.append(posting([statement.doc_id], "Loans Payable", "Cash", principal_paid, activity_date, f"{name}_principal"))
            postings.append(posting([statement.doc_id], "Interest Expense", "Cash", interest_paid, activity_date, f"{name}_interest"))
            bank_rows.append(bank_row(activity_date, f"Loan payment {statement.fields['loan_number']}", -(principal_paid + interest_paid)))
        return ScenarioResult(documents=[statement], postings=postings, bank_rows=bank_rows)

    return BusinessScenario(name=name, description=description, doc_types=("loan_statement",), doc_count_hint=1, builder=build)


def make_fixed_asset_purchase_scenario(*, name: str, description: str, asset_account: str = "Equipment") -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        purchase_date = pick_date(state.period_spec, rng, "mid")
        total = _scaled_amount(state, rng, 4200, 18500, "capital")
        paid_cash = round(total * rng.uniform(0.2, 0.5), 2)
        financed = round(total - paid_cash, 2)
        asset_name = rng.choice(state.master_data["asset_names"])
        invoice = doc_seed(
            state,
            doc_type="equipment_invoice",
            title=get_doc_schema("equipment_invoice").title,
            date=purchase_date,
            role="posting_doc",
            fields={
                "number": state.next_number("ASSET"),
                "vendor": rng.choice(state.master_data["vendors"]),
                "asset_name": asset_name,
                "asset_tag": state.next_number("TAG"),
                "useful_life_months": rng.choice([24, 36, 48, 60]),
                "total": total,
                "paid_cash": paid_cash,
                "financed_amount": financed,
                "note_reference": state.next_number("NOTE"),
                "financing_instrument": "Promissory note payable for financed portion.",
            },
        )
        postings = [posting([invoice.doc_id], asset_account, "Cash", paid_cash, purchase_date, f"{name}_cash")]
        if financed > 0:
            postings.append(posting([invoice.doc_id], asset_account, "Notes Payable", financed, purchase_date, f"{name}_financed"))
        state.asset_register.append(
            {
                "asset_name": asset_name,
                "asset_account": asset_account,
                "asset_tag": invoice.fields["asset_tag"],
                "cost": total,
                "useful_life_months": invoice.fields["useful_life_months"],
                "monthly_charge": round(total / invoice.fields["useful_life_months"], 2),
                "accumulated_depreciation": 0.0,
                "book_depreciation_current_period": 0.0,
            }
        )
        return ScenarioResult(
            documents=[invoice],
            postings=postings,
            bank_rows=[bank_row(purchase_date, f"Asset purchase {invoice.fields['number']}", -paid_cash)],
        )

    return BusinessScenario(name=name, description=description, doc_types=("equipment_invoice",), doc_count_hint=1, builder=build)


def make_depreciation_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        if not state.asset_register:
            raise ValueError(f"Scenario '{name}' needs an asset in the register")
        asset = rng.choice(state.asset_register)
        charge = round(asset["monthly_charge"] * state.period_spec.month_count, 2)
        asset["accumulated_depreciation"] = round(float(asset.get("accumulated_depreciation", 0.0)) + charge, 2)
        asset["book_depreciation_current_period"] = round(float(asset.get("book_depreciation_current_period", 0.0)) + charge, 2)
        fields = {
            "schedule_id": state.next_number("DEP"),
            "asset_name": asset["asset_name"],
            "asset_tag": asset["asset_tag"],
            "cost": asset["cost"],
            "useful_life_months": asset["useful_life_months"],
            "current_period_charge": charge,
            "accumulated_depreciation": asset["accumulated_depreciation"],
        }
        doc_type = "depreciation_schedule"
        if state.period_spec.period_type == "year":
            doc_type = "fixed_asset_rollforward"
            fields.update(
                {
                    "opening_balance": asset["cost"],
                    "additions": 0.0,
                    "disposals": 0.0,
                    "ending_balance": asset["cost"],
                }
            )
        schedule = doc_seed(
            state,
            doc_type=doc_type,
            title=get_doc_schema(doc_type).title,
            date=state.period_end,
            role="adjustment_doc",
            fields=fields,
        )
        postings = [posting([schedule.doc_id], "Depreciation Expense", "Accumulated Depreciation", charge, schedule.date, name)]
        return ScenarioResult(documents=[schedule], postings=postings)

    doc_type = ("fixed_asset_rollforward",) if name.endswith("_year") else ("depreciation_schedule", "fixed_asset_rollforward")
    return BusinessScenario(name=name, description=description, doc_types=doc_type, doc_count_hint=1, builder=build)


def make_jurisdictional_tax_invoice_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        purchase_date = pick_date(state.period_spec, rng, "early")
        sale_date = pick_date(state.period_spec, rng, "mid")
        vendor = rng.choice(state.master_data["vendors"])
        customer = rng.choice(state.master_data["customers"])
        tax_regime = state.tax_regime if state.tax_regime in {"us_sales_tax", "india_gst"} else rng.choice(("us_sales_tax", "india_gst"))
        tax_rate = choose_tax_rate(tax_regime, rng)
        subtotal = _scaled_amount(state, rng, 2200, 9800, "inventory")
        tax_amount = round(subtotal * tax_rate, 2)
        total = round(subtotal + tax_amount, 2)
        company_jurisdiction = rng.choice(("California", "New York")) if tax_regime == "us_sales_tax" else rng.choice(("Karnataka", "Maharashtra"))
        counterparty_jurisdiction = company_jurisdiction if rng.random() < 0.5 else ("Texas" if tax_regime == "us_sales_tax" else "Tamil Nadu")
        same_state = company_jurisdiction == counterparty_jurisdiction
        treatment = "US purchase sales tax capitalized into inventory cost"
        if tax_regime == "india_gst":
            treatment = "India GST same-state CGST+SGST input credit" if same_state else "India GST different-state IGST input credit"
        notice = doc_seed(
            state,
            doc_type="tax_regime_notice",
            title=get_doc_schema("tax_regime_notice").title,
            date=purchase_date,
            role="support_doc",
            fields={
                "notice_number": state.next_number("TAX"),
                "tax_regime": tax_regime,
                "company_jurisdiction": company_jurisdiction,
                "counterparty_jurisdiction": counterparty_jurisdiction,
                "tax_rate": tax_rate,
                "jurisdiction_tax_amount": tax_amount,
                "treatment": treatment,
            },
        )
        invoice_fields = {
            "number": state.next_number("TAXSUP"),
            "vendor": vendor,
            "due_date": due_date(purchase_date, rng, 10, 21),
            "total": total,
            "goods_receipt_ref": state.next_number("GRN-TAX"),
            "document_currency": state.currency_code,
            "subtotal": subtotal,
            "tax_label": tax_label_for_regime(tax_regime),
            "tax_rate": tax_rate,
            "tax_amount": tax_amount,
            "line_items": [{"description": rng.choice(state.master_data["products"]), "quantity": 1, "unit_cost": subtotal, "amount": subtotal}],
        }
        purchase_postings = []
        if tax_regime == "india_gst":
            if same_state:
                cgst_amount = round(tax_amount / 2, 2)
                sgst_amount = round(tax_amount - cgst_amount, 2)
                invoice_fields["cgst_amount"] = cgst_amount
                invoice_fields["sgst_amount"] = sgst_amount
                purchase_postings.extend(
                    [
                        posting([], "Inventory", "Accounts Payable", subtotal, purchase_date, f"{name}_purchase_inventory"),
                        posting([], "Input CGST Receivable", "Accounts Payable", cgst_amount, purchase_date, f"{name}_input_cgst"),
                        posting([], "Input SGST Receivable", "Accounts Payable", sgst_amount, purchase_date, f"{name}_input_sgst"),
                    ]
                )
            else:
                invoice_fields["igst_amount"] = tax_amount
                purchase_postings.extend(
                    [
                        posting([], "Inventory", "Accounts Payable", subtotal, purchase_date, f"{name}_purchase_inventory"),
                        posting([], "Input IGST Receivable", "Accounts Payable", tax_amount, purchase_date, f"{name}_input_igst"),
                    ]
                )
        else:
            purchase_postings.append(posting([], "Inventory", "Accounts Payable", total, purchase_date, f"{name}_us_purchase_cost_includes_tax"))
        supplier_invoice = doc_seed(
            state,
            doc_type="supplier_invoice",
            title=get_doc_schema("supplier_invoice").title_for(state.industry),
            date=purchase_date,
            role="posting_doc",
            fields=invoice_fields,
            metadata={"counterparty_name": vendor},
        )
        for entry in purchase_postings:
            entry.doc_refs[:] = [notice.doc_id, supplier_invoice.doc_id]

        cert = doc_seed(
            state,
            doc_type="tax_exemption_certificate",
            title=get_doc_schema("tax_exemption_certificate").title,
            date=sale_date,
            role="support_doc",
            fields={
                "certificate_number": state.next_number("EXEMPT"),
                "counterparty": customer,
                "tax_regime": tax_regime,
                "effective_date": state.period_start,
                "expiration_date": state.period_end,
                "exemption_status": "Valid",
                "exempt_reason": "Resale exemption certificate overrides default invoice tax treatment.",
            },
            metadata={"counterparty_name": customer},
        )
        profile = doc_seed(
            state,
            doc_type="customer_tax_profile",
            title=get_doc_schema("customer_tax_profile").title,
            date=sale_date,
            role="support_doc",
            fields={
                "profile_id": state.next_number("TAXPROF"),
                "customer": customer,
                "customer_jurisdiction": counterparty_jurisdiction,
                "company_jurisdiction": company_jurisdiction,
                "same_state": same_state,
                "exemption_certificate": cert.fields["certificate_number"],
            },
            metadata={"counterparty_name": customer},
        )
        sale_subtotal = round(subtotal * rng.uniform(1.15, 1.45), 2)
        sale_invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=sale_date,
            role="posting_doc",
            fields={
                "number": state.next_number("INV"),
                "customer": customer,
                "due_date": due_date(sale_date, rng, 10, 21),
                "total": sale_subtotal,
                "subtotal": sale_subtotal,
                "tax_label": tax_label_for_regime(tax_regime),
                "tax_rate": 0.0,
                "tax_amount": 0.0,
                "exemption_certificate": cert.fields["certificate_number"],
                "shipment_ref": state.next_number("SHP"),
                "document_currency": state.currency_code,
                "line_items": [{"description": rng.choice(state.master_data["products"]), "amount": sale_subtotal}],
            },
            metadata={"counterparty_name": customer},
        )
        refs = [cert.doc_id, profile.doc_id, sale_invoice.doc_id]
        sale_postings = [posting(refs, "Accounts Receivable", "Sales Revenue", sale_subtotal, sale_date, f"{name}_exempt_sale")]
        state.open_payables.append({"reference": supplier_invoice.fields["number"], "doc_id": supplier_invoice.doc_id, "counterparty": vendor, "remaining": total, "category": "vendor"})
        state.open_receivables.append({"reference": sale_invoice.fields["number"], "doc_id": sale_invoice.doc_id, "counterparty": customer, "remaining": sale_subtotal, "category": "customer"})
        state.jurisdiction_profile = {
            "company_jurisdiction": company_jurisdiction,
            "counterparty_jurisdiction": counterparty_jurisdiction,
            "same_state": same_state,
        }
        state.tax_context = {
            "tax_regime": tax_regime,
            "tax_rate": tax_rate,
            "purchase_tax_amount": tax_amount,
            "exemption_certificate": cert.fields["certificate_number"],
        }
        state.metadata["has_tax_exemption"] = True
        state.metadata.setdefault("tax_treatments", []).append(treatment)
        return ScenarioResult(
            documents=[notice, supplier_invoice, cert, profile, sale_invoice],
            postings=[*purchase_postings, *sale_postings],
            notes={"tax_regime": tax_regime, "same_state": same_state, "exempt_sale": True},
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("tax_regime_notice", "supplier_invoice", "tax_exemption_certificate", "customer_tax_profile", "customer_invoice"),
        doc_count_hint=5,
        builder=build,
    )


def make_bundled_contract_allocation_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        contract_date = pick_date(state.period_spec, rng, "early")
        acceptance_date = date_plus_days(contract_date, min(14, max(1, state.period_spec.month_count * 3)))
        customer = rng.choice(state.master_data["customers"])
        contract_ref = state.next_number("ASC606")
        implementation_ssp = _scaled_amount(state, rng, 9000, 18000, "contract")
        platform_ssp = _scaled_amount(state, rng, 24000, 52000, "contract")
        total_ssp = round(implementation_ssp + platform_ssp, 2)
        transaction_price = round(total_ssp * rng.uniform(0.82, 0.92), 2)
        implementation_allocated = round(transaction_price * implementation_ssp / total_ssp, 2)
        platform_allocated = round(transaction_price - implementation_allocated, 2)
        invoice_implementation_line = round(transaction_price * 0.15, 2)
        invoice_platform_line = round(transaction_price - invoice_implementation_line, 2)
        term_months = 12
        platform_months_released = min(state.period_spec.month_count, term_months)
        platform_release = round(platform_allocated * platform_months_released / term_months, 2)
        released_this_period = round(implementation_allocated + platform_release, 2)
        ending_deferred = round(transaction_price - released_this_period, 2)
        order_form = doc_seed(
            state,
            doc_type="subscription_order_form",
            title=get_doc_schema("subscription_order_form").title,
            date=contract_date,
            role="support_doc",
            fields={
                "form_number": contract_ref,
                "customer": customer,
                "plan_name": rng.choice(state.master_data["subscription_plans"]),
                "term_months": term_months,
                "contract_start": contract_date,
                "total_contract_value": transaction_price,
            },
            metadata={"counterparty_name": customer},
        )
        invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=contract_date,
            role="posting_doc",
            fields={
                "number": state.next_number("INV"),
                "customer": customer,
                "due_date": due_date(contract_date, rng, 7, 18),
                "total": transaction_price,
                "line_items": [
                    {"description": "Implementation invoice line", "amount": invoice_implementation_line},
                    {"description": "Platform access invoice line", "amount": invoice_platform_line},
                ],
                "contract_ref": contract_ref,
                "document_currency": state.currency_code,
            },
            metadata={"counterparty_name": customer},
        )
        rate_card = doc_seed(
            state,
            doc_type="ssp_rate_card",
            title=get_doc_schema("ssp_rate_card").title,
            date=contract_date,
            role="support_doc",
            fields={
                "rate_card_id": state.next_number("SSP"),
                "contract_reference": contract_ref,
                "effective_date": contract_date,
                "total_ssp": total_ssp,
                "obligations": [
                    {"obligation": "Implementation", "ssp_amount": implementation_ssp},
                    {"obligation": "Platform access", "ssp_amount": platform_ssp},
                ],
            },
            metadata={"counterparty_name": customer},
        )
        acceptance = doc_seed(
            state,
            doc_type="implementation_acceptance_memo",
            title=get_doc_schema("implementation_acceptance_memo").title,
            date=acceptance_date,
            role="support_doc",
            fields={
                "memo_id": state.next_number("ACCEPT"),
                "contract_reference": contract_ref,
                "customer": customer,
                "acceptance_date": acceptance_date,
                "accepted_obligation": "Implementation",
                "accepted_amount": implementation_allocated,
                "narrative": "Customer accepted implementation. Only the implementation performance obligation is released on acceptance.",
            },
            metadata={"counterparty_name": customer},
        )
        schedule = doc_seed(
            state,
            doc_type="performance_obligation_schedule",
            title=get_doc_schema("performance_obligation_schedule").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "schedule_id": state.next_number("POB"),
                "contract_reference": contract_ref,
                "transaction_price": transaction_price,
                "total_ssp": total_ssp,
                "allocation_total": round(implementation_allocated + platform_allocated, 2),
                "released_this_period": released_this_period,
                "ending_deferred": ending_deferred,
                "obligations": [
                    {
                        "obligation": "Implementation",
                        "ssp_amount": implementation_ssp,
                        "invoice_line_amount": invoice_implementation_line,
                        "allocated_transaction_price": implementation_allocated,
                        "release_pattern": "On acceptance",
                        "released_this_period": implementation_allocated,
                    },
                    {
                        "obligation": "Platform access",
                        "ssp_amount": platform_ssp,
                        "invoice_line_amount": invoice_platform_line,
                        "allocated_transaction_price": platform_allocated,
                        "release_pattern": f"Ratable over {term_months} months",
                        "released_this_period": platform_release,
                    },
                ],
            },
            metadata={"counterparty_name": customer},
        )
        refs = [order_form.doc_id, invoice.doc_id, rate_card.doc_id]
        release_refs = [invoice.doc_id, rate_card.doc_id, acceptance.doc_id, schedule.doc_id]
        postings = [
            posting(refs, "Accounts Receivable", "Unearned Revenue", transaction_price, contract_date, f"{name}_invoice"),
            posting(release_refs, "Unearned Revenue", "Service Revenue", implementation_allocated, acceptance_date, f"{name}_implementation_release"),
            posting(release_refs, "Unearned Revenue", "Service Revenue", platform_release, state.period_end, f"{name}_platform_release"),
        ]
        state.open_receivables.append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": customer, "remaining": transaction_price, "category": "customer"})
        state.contract_subledger.append(
            {
                "contract_reference": contract_ref,
                "transaction_price": transaction_price,
                "implementation_allocated": implementation_allocated,
                "platform_allocated": platform_allocated,
                "platform_release": platform_release,
                "ending_deferred": ending_deferred,
            }
        )
        state.metadata["has_asc606"] = True
        return ScenarioResult(
            documents=[order_form, invoice, rate_card, acceptance, schedule],
            postings=postings,
            notes={
                "transaction_price": transaction_price,
                "invoice_implementation_line": invoice_implementation_line,
                "implementation_allocated": implementation_allocated,
                "platform_allocated": platform_allocated,
                "platform_release": platform_release,
            },
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("subscription_order_form", "customer_invoice", "ssp_rate_card", "implementation_acceptance_memo", "performance_obligation_schedule"),
        doc_count_hint=5,
        builder=build,
    )


def make_asset_disposal_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        eligible = [asset for asset in state.asset_register if float(asset.get("accumulated_depreciation", 0.0)) > 0.0 and not asset.get("disposed")]
        if not eligible:
            raise ValueError(f"Scenario '{name}' needs an asset with accumulated depreciation")
        asset = max(eligible, key=lambda item: float(item.get("accumulated_depreciation", 0.0)))
        disposal_date = pick_date(state.period_spec, rng, "late")
        cost = round(float(asset["cost"]), 2)
        asset_account = str(asset.get("asset_account", "Equipment"))
        accumulated = min(cost - 0.01, round(float(asset.get("accumulated_depreciation", 0.0)), 2))
        nbv = round(cost - accumulated, 2)
        proceeds = round(max(1.0, nbv * rng.choice((0.82, 1.18))), 2)
        gain_loss = round(proceeds - nbv, 2)
        gain_loss_type = "Gain" if gain_loss >= 0 else "Loss"
        buyer = rng.choice(state.master_data["customers"])
        notice = doc_seed(
            state,
            doc_type="asset_disposal_notice",
            title=get_doc_schema("asset_disposal_notice").title,
            date=disposal_date,
            role="adjustment_doc",
            fields={
                "notice_number": state.next_number("DISP"),
                "asset_name": asset["asset_name"],
                "asset_tag": asset["asset_tag"],
                "original_cost": cost,
                "accumulated_depreciation": accumulated,
                "net_book_value": nbv,
                "proceeds_amount": proceeds,
                "gain_loss_amount": abs(gain_loss),
                "gain_loss_type": gain_loss_type,
            },
        )
        proceeds_doc = doc_seed(
            state,
            doc_type="sale_proceeds_advice",
            title=get_doc_schema("sale_proceeds_advice").title,
            date=disposal_date,
            role="support_doc",
            fields={
                "advice_number": state.next_number("DSPPAY"),
                "buyer": buyer,
                "asset_tag": asset["asset_tag"],
                "proceeds_amount": proceeds,
                "settlement_date": disposal_date,
                "payment_reference": state.next_number("BNK"),
            },
            metadata={"counterparty_name": buyer},
        )
        refs = [notice.doc_id, proceeds_doc.doc_id]
        postings = [
            posting(refs, "Cash", asset_account, proceeds, disposal_date, f"{name}_proceeds"),
            posting(refs, "Accumulated Depreciation", asset_account, accumulated, disposal_date, f"{name}_remove_accumulated_depreciation"),
        ]
        if gain_loss >= 0:
            postings.append(posting(refs, asset_account, "Gain on Disposal", abs(gain_loss), disposal_date, f"{name}_gain"))
        else:
            postings.append(posting(refs, "Loss on Disposal", asset_account, abs(gain_loss), disposal_date, f"{name}_loss"))
        asset["disposed"] = True
        state.metadata["has_asset_disposal"] = True
        state.metadata["last_asset_disposal"] = {
            "asset_tag": asset["asset_tag"],
            "book_gain_loss": gain_loss,
            "net_book_value": nbv,
            "proceeds": proceeds,
            "doc_refs": refs,
        }
        return ScenarioResult(
            documents=[notice, proceeds_doc],
            postings=postings,
            bank_rows=[bank_row(disposal_date, f"Asset sale {asset['asset_tag']}", proceeds)],
            notes={"net_book_value": nbv, "proceeds": proceeds, "gain_loss": gain_loss},
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("asset_disposal_notice", "sale_proceeds_advice"),
        doc_count_hint=2,
        builder=build,
    )


def make_deferred_tax_depreciation_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        eligible = [asset for asset in state.asset_register if float(asset.get("book_depreciation_current_period", 0.0)) > 0.0]
        if not eligible:
            raise ValueError(f"Scenario '{name}' needs current-period book depreciation")
        asset = max(eligible, key=lambda item: float(item.get("book_depreciation_current_period", 0.0)))
        book_dep = round(float(asset.get("book_depreciation_current_period", asset["monthly_charge"])), 2)
        tax_dep = round(book_dep * rng.uniform(1.45, 1.9), 2)
        temporary_difference = round(tax_dep - book_dep, 2)
        tax_rate = 0.25
        movement = round(temporary_difference * tax_rate, 2)
        schedule = doc_seed(
            state,
            doc_type="tax_depreciation_schedule",
            title=get_doc_schema("tax_depreciation_schedule").title,
            date=state.period_end,
            role="support_doc",
            fields={
                "schedule_id": state.next_number("TAXDEP"),
                "asset_tag": asset["asset_tag"],
                "book_depreciation_amount": book_dep,
                "tax_depreciation_amount": tax_dep,
                "temporary_difference_amount": temporary_difference,
                "tax_rate": tax_rate,
            },
        )
        memo = doc_seed(
            state,
            doc_type="deferred_tax_memo",
            title=get_doc_schema("deferred_tax_memo").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "memo_id": state.next_number("DTAX"),
                "asset_tag": asset["asset_tag"],
                "opening_deferred_tax_liability": 0.0,
                "current_period_deferred_tax_movement": movement,
                "deferred_tax_liability_ending": movement,
                "deferred_tax_expense_amount": movement,
                "narrative": "Tax depreciation exceeds book depreciation, creating a taxable temporary difference.",
            },
        )
        state.metadata["has_deferred_tax"] = True
        state.tax_context["deferred_tax_rate"] = tax_rate
        return ScenarioResult(
            documents=[schedule, memo],
            postings=[posting([schedule.doc_id, memo.doc_id], "Deferred Tax Expense", "Deferred Tax Liability", movement, state.period_end, name)],
            notes={"book_depreciation": book_dep, "tax_depreciation": tax_dep, "movement": movement},
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("tax_depreciation_schedule", "deferred_tax_memo"),
        doc_count_hint=2,
        builder=build,
    )


def make_baseline_lease_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        commencement_date = pick_date(state.period_spec, rng, "early")
        payment_date = pick_date(state.period_spec, rng, "late")
        term_months = rng.choice((24, 36, 48))
        monthly_payment = _scaled_amount(state, rng, 1200, 2600, "operating")
        annual_rate = rng.choice((0.06, 0.075, 0.09))
        monthly_rate = annual_rate / 12
        liability = round(sum(monthly_payment / ((1 + monthly_rate) ** month) for month in range(1, term_months + 1)), 2)
        payment_amount = round(monthly_payment * min(state.period_spec.month_count, 3), 2)
        interest = round(liability * monthly_rate * min(state.period_spec.month_count, 3), 2)
        principal = round(payment_amount - interest, 2)
        ending_liability = round(liability - principal, 2)
        amortization = round(liability / term_months * state.period_spec.month_count, 2)
        lessor = rng.choice(state.master_data["vendors"])
        agreement = doc_seed(
            state,
            doc_type="lease_agreement",
            title=get_doc_schema("lease_agreement").title,
            date=commencement_date,
            role="posting_doc",
            fields={
                "agreement_number": state.next_number("LEASE"),
                "lessor": lessor,
                "commencement_date": commencement_date,
                "term_months": term_months,
                "monthly_payment_amount": monthly_payment,
                "incremental_borrowing_rate": annual_rate,
                "rou_asset_amount": liability,
                "lease_liability_amount": liability,
            },
            metadata={"counterparty_name": lessor},
        )
        schedule = doc_seed(
            state,
            doc_type="lease_amortization_schedule",
            title=get_doc_schema("lease_amortization_schedule").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "schedule_id": state.next_number("LEASESCH"),
                "agreement_number": agreement.fields["agreement_number"],
                "opening_liability_balance": liability,
                "payment_amount": payment_amount,
                "interest_amount": interest,
                "principal_amount": principal,
                "ending_liability_balance": ending_liability,
                "rou_amortization_amount": amortization,
            },
        )
        payment_doc = doc_seed(
            state,
            doc_type="lease_payment_notice",
            title=get_doc_schema("lease_payment_notice").title,
            date=payment_date,
            role="support_doc",
            fields={
                "notice_number": state.next_number("LEASEPAY"),
                "agreement_number": agreement.fields["agreement_number"],
                "payment_date": payment_date,
                "payment_amount": payment_amount,
                "interest_amount": interest,
                "principal_amount": principal,
            },
        )
        refs = [agreement.doc_id, schedule.doc_id, payment_doc.doc_id]
        postings = [
            posting([agreement.doc_id], "Right-of-Use Asset", "Lease Liability", liability, commencement_date, f"{name}_initial_recognition"),
            posting(refs, "Lease Liability", "Cash", principal, payment_date, f"{name}_principal"),
            posting(refs, "Lease Interest Expense", "Cash", interest, payment_date, f"{name}_interest"),
            posting([agreement.doc_id, schedule.doc_id], "Lease Amortization Expense", "Right-of-Use Asset", amortization, state.period_end, f"{name}_amortization"),
        ]
        state.lease_subledger.append(
            {
                "agreement_number": agreement.fields["agreement_number"],
                "doc_id": agreement.doc_id,
                "liability_balance": ending_liability,
                "rou_asset_balance": round(liability - amortization, 2),
                "term_months": term_months,
                "monthly_payment": monthly_payment,
            }
        )
        state.metadata["has_lease"] = True
        return ScenarioResult(
            documents=[agreement, schedule, payment_doc],
            postings=postings,
            bank_rows=[bank_row(payment_date, f"Lease payment {agreement.fields['agreement_number']}", -payment_amount)],
            notes={"liability": liability, "principal": principal, "interest": interest, "amortization": amortization},
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("lease_agreement", "lease_amortization_schedule", "lease_payment_notice"),
        doc_count_hint=3,
        builder=build,
    )


def make_lease_modification_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        if not state.lease_subledger:
            raise ValueError(f"Scenario '{name}' needs an existing lease")
        lease = state.lease_subledger[0]
        modification_date = pick_date(state.period_spec, rng, "closing")
        old_liability = round(float(lease["liability_balance"]), 2)
        delta = round(old_liability * rng.uniform(0.08, 0.18), 2)
        remeasured = round(old_liability + delta, 2)
        notice = doc_seed(
            state,
            doc_type="lease_modification_notice",
            title=get_doc_schema("lease_modification_notice").title,
            date=modification_date,
            role="adjustment_doc",
            fields={
                "modification_number": state.next_number("LEASEMOD"),
                "agreement_number": lease["agreement_number"],
                "modification_date": modification_date,
                "old_liability_balance": old_liability,
                "remeasured_liability_balance": remeasured,
                "liability_remeasurement_delta_amount": delta,
                "rou_asset_adjustment_amount": delta,
                "narrative": "Lease term extension remeasures the liability; the ROU asset is adjusted by the same amount.",
            },
        )
        schedule = doc_seed(
            state,
            doc_type="lease_amortization_schedule",
            title=get_doc_schema("lease_amortization_schedule").title,
            date=modification_date,
            role="support_doc",
            fields={
                "schedule_id": state.next_number("LEASESCH"),
                "agreement_number": lease["agreement_number"],
                "opening_liability_balance": remeasured,
                "payment_amount": 0.0,
                "interest_amount": 0.0,
                "principal_amount": 0.0,
                "ending_liability_balance": remeasured,
                "rou_amortization_amount": 0.0,
            },
        )
        lease["liability_balance"] = remeasured
        lease["rou_asset_balance"] = round(float(lease["rou_asset_balance"]) + delta, 2)
        state.metadata["has_lease"] = True
        return ScenarioResult(
            documents=[notice, schedule],
            postings=[posting([notice.doc_id, schedule.doc_id], "Right-of-Use Asset", "Lease Liability", delta, modification_date, name)],
            notes={"liability_delta": delta, "rou_asset_delta": delta},
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("lease_modification_notice", "lease_amortization_schedule"),
        doc_count_hint=2,
        builder=build,
    )


def make_asset_disposal_with_deferred_tax_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        disposal = state.metadata.get("last_asset_disposal")
        if not disposal:
            raise ValueError(f"Scenario '{name}' needs a prior asset disposal")
        tax_rate = 0.25
        book_gain_loss = round(float(disposal["book_gain_loss"]), 2)
        tax_basis_difference = round(abs(book_gain_loss) * rng.uniform(0.2, 0.45), 2)
        movement = round(tax_basis_difference * tax_rate, 2)
        schedule = doc_seed(
            state,
            doc_type="tax_depreciation_schedule",
            title=get_doc_schema("tax_depreciation_schedule").title,
            date=state.period_end,
            role="support_doc",
            fields={
                "schedule_id": state.next_number("TAXDSP"),
                "asset_tag": str(disposal["asset_tag"]),
                "book_depreciation_amount": round(float(disposal["net_book_value"]), 2),
                "tax_depreciation_amount": round(float(disposal["net_book_value"]) + tax_basis_difference, 2),
                "temporary_difference_amount": tax_basis_difference,
                "tax_rate": tax_rate,
            },
        )
        memo = doc_seed(
            state,
            doc_type="deferred_tax_memo",
            title=get_doc_schema("deferred_tax_memo").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "memo_id": state.next_number("DTAX"),
                "asset_tag": str(disposal["asset_tag"]),
                "opening_deferred_tax_liability": 0.0,
                "current_period_deferred_tax_movement": movement,
                "deferred_tax_liability_ending": movement,
                "deferred_tax_expense_amount": movement,
                "narrative": "Deferred tax movement recorded after combining disposal proceeds with the tax-basis difference.",
            },
        )
        state.metadata["has_asset_disposal"] = True
        state.metadata["has_deferred_tax"] = True
        return ScenarioResult(
            documents=[schedule, memo],
            postings=[posting([*disposal["doc_refs"], schedule.doc_id, memo.doc_id], "Deferred Tax Expense", "Deferred Tax Liability", movement, state.period_end, name)],
            notes={"deferred_tax_movement": movement},
        )

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("tax_depreciation_schedule", "deferred_tax_memo"),
        doc_count_hint=2,
        builder=build,
    )


def make_retail_sale_scenario(*, name: str, description: str, apply_indirect_tax: bool = False) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        sale_date = pick_date(state.period_spec, rng, "mid")
        gross_sales = _scaled_amount(state, rng, 2600, 12400, "inventory")
        returns = round(gross_sales * rng.uniform(0.01, 0.05), 2)
        net_sales = round(gross_sales - returns, 2)
        tax_amount = 0.0
        if apply_indirect_tax and state.tax_regime != "none":
            tax_amount = float(_tax_details(state, net_sales, rng)["tax_amount"])
        gross_receipts = round(net_sales + tax_amount, 2)
        cash_sales = round(gross_receipts * rng.uniform(0.15, 0.35), 2)
        card_sales = round(gross_receipts - cash_sales, 2)
        cogs = round(net_sales * rng.uniform(0.48, 0.67), 2)
        sales_doc = doc_seed(
            state,
            doc_type="sales_summary",
            title=get_doc_schema("sales_summary").title,
            date=sale_date,
            role="posting_doc",
            fields={
                "report_id": state.next_number("SALES"),
                "store_name": state.entity_name,
                "gross_sales": gross_sales,
                "returns": returns,
                "net_sales": net_sales,
                "cash_sales": cash_sales,
                "card_sales": card_sales,
                "tax_label": state.tax_label or tax_label_for_regime(state.tax_regime),
                "tax_amount": tax_amount,
                "cogs_amount": cogs,
                "cogs_source": "POS inventory cost layer for items sold in this sales summary.",
                "units_sold": rng.randint(60, 280),
            },
        )
        if state.tax_regime == "india_gst" and tax_amount > 0:
            cgst_amount, sgst_amount = _india_gst_split(tax_amount)
            sales_doc.fields["cgst_amount"] = cgst_amount
            sales_doc.fields["sgst_amount"] = sgst_amount
        batch_doc = doc_seed(
            state,
            doc_type="pos_batch_report",
            title=get_doc_schema("pos_batch_report").title,
            date=sale_date,
            role="support_doc",
            fields={
                "batch_id": state.next_number("BATCH"),
                "processor": rng.choice(state.master_data["processors"]),
                "batch_total": card_sales,
                "fee_amount": round(card_sales * 0.018, 2),
                "expected_deposit": round(card_sales * 0.982, 2),
                "terminal_id": state.next_number("TERM"),
            },
        )
        refs = [sales_doc.doc_id, batch_doc.doc_id]
        cash_revenue = round(cash_sales * (net_sales / gross_receipts), 2) if gross_receipts else 0.0
        card_revenue = round(net_sales - cash_revenue, 2)
        postings = [
            posting(refs, "Cash", "Sales Revenue", cash_revenue, sale_date, f"{name}_cash"),
            posting(refs, "Card Settlement Clearing", "Sales Revenue", card_revenue, sale_date, f"{name}_card"),
            posting(refs, "Cost of Goods Sold", "Inventory", cogs, sale_date, f"{name}_cogs"),
        ]
        if tax_amount > 0:
            cash_tax = round(cash_sales * (tax_amount / gross_receipts), 2) if gross_receipts else 0.0
            card_tax = round(tax_amount - cash_tax, 2)
            postings.extend(_output_tax_postings(state, refs, "Cash", cash_tax, sale_date, f"{name}_cash_tax"))
            postings.extend(_output_tax_postings(state, refs, "Card Settlement Clearing", card_tax, sale_date, f"{name}_card_tax"))
        state.metadata.setdefault("card_batches", []).append(
            {
                "batch_id": batch_doc.fields["batch_id"],
                "doc_id": batch_doc.doc_id,
                "gross_amount": card_sales,
                "fee_amount": batch_doc.fields["fee_amount"],
                "expected_deposit": batch_doc.fields["expected_deposit"],
            }
        )
        return ScenarioResult(
            documents=[sales_doc, batch_doc],
            postings=postings,
            bank_rows=[bank_row(sale_date, f"Cash till {sales_doc.fields['report_id']}", cash_sales)],
        )

    return BusinessScenario(name=name, description=description, doc_types=("sales_summary", "pos_batch_report"), doc_count_hint=2, builder=build, allow_repeat=True)


def make_card_settlement_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        batches = state.metadata.get("card_batches", [])
        if not batches:
            raise ValueError(f"Scenario '{name}' needs an open card batch")
        batch = batches.pop(0)
        settlement_date = pick_date(state.period_spec, rng, "late")
        settlement = doc_seed(
            state,
            doc_type="card_settlement_report",
            title=get_doc_schema("card_settlement_report").title,
            date=settlement_date,
            role="posting_doc",
            fields={
                "settlement_id": state.next_number("SETTLE"),
                "processor": rng.choice(state.master_data["processors"]),
                "batch_refs": [batch["batch_id"]],
                "gross_amount": batch["gross_amount"],
                "fees": batch["fee_amount"],
                "net_deposit": batch["expected_deposit"],
                "deposit_date": settlement_date,
            },
        )
        refs = [settlement.doc_id, batch["doc_id"]]
        postings = [
            posting(refs, "Cash", "Card Settlement Clearing", batch["expected_deposit"], settlement_date, f"{name}_deposit"),
            posting(refs, "Maintenance Expense", "Card Settlement Clearing", batch["fee_amount"], settlement_date, f"{name}_fees"),
        ]
        return ScenarioResult(
            documents=[settlement],
            postings=postings,
            bank_rows=[bank_row(settlement_date, f"Card settlement {settlement.fields['settlement_id']}", batch["expected_deposit"])],
        )

    return BusinessScenario(name=name, description=description, doc_types=("card_settlement_report",), doc_count_hint=1, builder=build)


def make_inventory_adjustment_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        adjust_date = state.period_end
        sheet_id = state.next_number("COUNT")
        sku = state.next_number("SKU")
        unit_cost = _scaled_amount(state, rng, 8, 40, "small")
        shrink_units = rng.randint(2, 12)
        shrink_amount = round(unit_cost * shrink_units, 2)
        count_sheet = doc_seed(
            state,
            doc_type="stock_count_sheet",
            title=get_doc_schema("stock_count_sheet").title,
            date=adjust_date,
            role="support_doc",
            fields={
                "sheet_id": sheet_id,
                "location": rng.choice(["Front store", "Back room", "Warehouse A"]),
                "items": [
                    {
                        "sku": sku,
                        "description": rng.choice(state.master_data["products"]),
                        "system_qty": 100,
                        "counted_qty": 100 - shrink_units,
                        "unit_cost": unit_cost,
                    }
                ],
            },
        )
        note_doc_type = "inventory_adjustment_note"
        note_fields = {
            "note_id": state.next_number("ADJ"),
            "reason": "Shrinkage found during physical count",
            "amount": shrink_amount,
            "reference_sheet_id": sheet_id,
        }
        if state.period_spec.period_type == "year":
            note_doc_type = "inventory_rollforward"
            note_fields = {
                "rollforward_id": state.next_number("INVROLL"),
                "opening_balance": round(shrink_amount * rng.uniform(8, 20), 2),
                "additions": round(shrink_amount * rng.uniform(10, 24), 2),
                "usage_or_sales": round(shrink_amount * rng.uniform(7, 18), 2),
                "write_down": shrink_amount,
                "ending_balance": 0.0,
            }
            note_fields["ending_balance"] = round(note_fields["opening_balance"] + note_fields["additions"] - note_fields["usage_or_sales"] - note_fields["write_down"], 2)
        note = doc_seed(
            state,
            doc_type=note_doc_type,
            title=get_doc_schema(note_doc_type).title,
            date=adjust_date,
            role="adjustment_doc",
            fields=note_fields,
        )
        refs = [count_sheet.doc_id, note.doc_id]
        postings = [posting(refs, "Inventory Shrinkage Expense", "Inventory", shrink_amount, adjust_date, name)]
        return ScenarioResult(documents=[count_sheet, note], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("stock_count_sheet", "inventory_adjustment_note"), doc_count_hint=2, builder=build, allow_repeat=True)


def make_return_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        return_date = pick_date(state.period_spec, rng, "late")
        amount_value = _scaled_amount(state, rng, 80, 640, "small")
        note = doc_seed(
            state,
            doc_type="return_note",
            title=get_doc_schema("return_note").title,
            date=return_date,
            role="posting_doc",
            fields={
                "return_id": state.next_number("RTN"),
                "reason": rng.choice(["Damaged item", "Customer return", "Shelf defect"]),
                "amount": amount_value,
                "reference": state.next_number("SALE-REF"),
            },
        )
        postings = [posting([note.doc_id], "Sales Revenue", "Cash", amount_value, return_date, name)]
        return ScenarioResult(documents=[note], postings=postings, bank_rows=[bank_row(return_date, f"Return {note.fields['return_id']}", -amount_value)])

    return BusinessScenario(name=name, description=description, doc_types=("return_note",), doc_count_hint=1, builder=build, allow_repeat=True)


def make_goods_receipt_purchase_scenario(*, name: str, description: str, apply_indirect_tax: bool = False) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        receipt_date = pick_date(state.period_spec, rng, "early")
        vendor = rng.choice(state.master_data["vendors"])
        sku = state.next_number("SKU")
        qty = rng.randint(40, 160)
        unit_cost = _scaled_amount(state, rng, 6, 24, "inventory")
        subtotal = round(qty * unit_cost, 2)
        grn = doc_seed(
            state,
            doc_type="goods_receipt_note",
            title=get_doc_schema("goods_receipt_note").title,
            date=receipt_date,
            role="support_doc",
            fields={
                "grn_number": state.next_number("GRN"),
                "supplier": vendor,
                "purchase_ref": state.next_number("PO"),
                "items": [{"sku": sku, "description": rng.choice(state.master_data["products"]), "quantity": qty, "unit_cost": unit_cost}],
                "total_quantity": qty,
            },
            metadata={"counterparty_name": vendor},
        )
        invoice_date = date_plus_days(receipt_date, 2)
        invoice = doc_seed(
            state,
            doc_type="supplier_invoice",
            title=get_doc_schema("supplier_invoice").title_for(state.industry),
            date=invoice_date,
            role="posting_doc",
            fields={
                "number": state.next_number("SUP"),
                "vendor": vendor,
                "due_date": due_date(invoice_date, rng, 10, 21),
                "total": subtotal,
                "goods_receipt_ref": grn.fields["grn_number"],
                "document_currency": state.currency_code,
                "line_items": [
                    {
                        "description": grn.fields["items"][0]["description"],
                        "quantity": qty,
                        "unit_cost": unit_cost,
                        "amount": subtotal,
                    }
                ],
            },
            metadata={"counterparty_name": vendor},
        )
        tax_amount = 0.0
        total = subtotal
        if apply_indirect_tax and state.tax_regime != "none":
            tax_details = _tax_details(state, subtotal, rng)
            _apply_tax_fields(invoice.fields, tax_details, state)
            total = float(tax_details["total"])
            tax_amount = float(tax_details["tax_amount"])
        refs = [grn.doc_id, invoice.doc_id]
        postings = [posting(refs, "Inventory", "Accounts Payable", subtotal, invoice_date, name)]
        postings.extend(_input_tax_postings(state, refs, "Accounts Payable", tax_amount, invoice_date, f"{name}_tax"))
        state.open_payables.append(
            {"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": vendor, "remaining": total, "category": "vendor"}
        )
        return ScenarioResult(documents=[grn, invoice], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("goods_receipt_note", "supplier_invoice"), doc_count_hint=2, builder=build, allow_repeat=True)


def make_delivery_sale_scenario(*, name: str, description: str, apply_indirect_tax: bool = False) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        ship_date = pick_date(state.period_spec, rng, "mid")
        customer = rng.choice(state.master_data["customers"])
        sku = state.next_number("SKU")
        qty = rng.randint(15, 70)
        unit_price = _scaled_amount(state, rng, 24, 70, "inventory")
        subtotal = round(qty * unit_price, 2)
        billed = subtotal
        tax_amount = 0.0
        if apply_indirect_tax and state.tax_regime != "none":
            tax_amount = float(_tax_details(state, subtotal, rng)["tax_amount"])
            billed = round(subtotal + tax_amount, 2)
        cogs = round(subtotal * rng.uniform(0.52, 0.72), 2)
        unit_cost = round(cogs / qty, 2)
        extended_cost = cogs
        delivery = doc_seed(
            state,
            doc_type="delivery_note",
            title=get_doc_schema("delivery_note").title,
            date=ship_date,
            role="support_doc",
            fields={
                "delivery_number": state.next_number("DLV"),
                "customer": customer,
                "shipment_ref": state.next_number("SHP"),
                "items": [
                    {
                        "sku": sku,
                        "description": rng.choice(state.master_data["products"]),
                        "quantity": qty,
                        "unit_price": unit_price,
                        "unit_cost": unit_cost,
                        "extended_cost": extended_cost,
                    }
                ],
                "billed_amount": billed,
                "cost_basis_amount": cogs,
                "cost_basis_source": "Perpetual inventory cost layer for shipped SKU.",
            },
            metadata={"counterparty_name": customer},
        )
        invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=ship_date,
            role="posting_doc",
            fields={
                "number": state.next_number("INV"),
                "customer": customer,
                "due_date": due_date(ship_date, rng, 10, 20),
                "total": billed,
                "line_items": [{"description": delivery.fields["items"][0]["description"], "amount": subtotal}],
                "shipment_ref": delivery.fields["shipment_ref"],
                "document_currency": state.currency_code,
            },
            metadata={"counterparty_name": customer},
        )
        if tax_amount > 0:
            tax_details = _tax_details(state, subtotal, rng, tax_amount / subtotal if subtotal else 0.0)
            _apply_tax_fields(invoice.fields, tax_details, state)
        refs = [delivery.doc_id, invoice.doc_id]
        postings = [
            posting(refs, "Accounts Receivable", "Sales Revenue", subtotal, ship_date, f"{name}_sale"),
            posting(refs, "Cost of Goods Sold", "Inventory", cogs, ship_date, f"{name}_cogs"),
        ]
        postings.extend(_output_tax_postings(state, refs, "Accounts Receivable", tax_amount, ship_date, f"{name}_tax"))
        state.open_receivables.append(
            {"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": customer, "remaining": billed, "category": "customer"}
        )
        return ScenarioResult(documents=[delivery, invoice], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("delivery_note", "customer_invoice"), doc_count_hint=2, builder=build, allow_repeat=True)


def make_patient_billing_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        service_date = pick_date(state.period_spec, rng, "mid")
        patient = rng.choice(state.master_data["patients"])
        insurer = rng.choice(state.master_data["insurers"])
        total = _scaled_amount(state, rng, 400, 2400, "operating")
        patient_portion = round(total * rng.uniform(0.15, 0.35), 2)
        insurer_portion = round(total - patient_portion, 2)
        invoice = doc_seed(
            state,
            doc_type="patient_invoice",
            title=get_doc_schema("patient_invoice").title,
            date=service_date,
            role="posting_doc",
            fields={
                "invoice_number": state.next_number("PTINV"),
                "patient_name": patient,
                "service_date": service_date,
                "total": total,
                "patient_due": patient_portion,
                "insurer_due": insurer_portion,
                "payer_name": insurer,
            },
            metadata={"counterparty_name": patient},
        )
        postings = [posting([invoice.doc_id], "Accounts Receivable", "Service Revenue", total, service_date, name)]
        state.metadata.setdefault("clinic_claims", []).append(
            {
                "reference": invoice.fields["invoice_number"],
                "doc_id": invoice.doc_id,
                "patient": patient,
                "payer_name": insurer,
                "patient_due": patient_portion,
                "insurer_due": insurer_portion,
            }
        )
        state.open_receivables.append({"reference": invoice.fields["invoice_number"], "doc_id": invoice.doc_id, "counterparty": patient, "remaining": total, "category": "patient"})
        return ScenarioResult(documents=[invoice], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("patient_invoice",), doc_count_hint=1, builder=build, allow_repeat=True)


def make_copay_collection_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        claims = state.metadata.get("clinic_claims", [])
        if not claims:
            raise ValueError(f"Scenario '{name}' needs an open clinic claim")
        claim = claims[0]
        pay_date = pick_date(state.period_spec, rng, "late")
        receipt = doc_seed(
            state,
            doc_type="copay_receipt",
            title=get_doc_schema("copay_receipt").title,
            date=pay_date,
            role="posting_doc",
            fields={
                "receipt_number": state.next_number("COPAY"),
                "patient_name": claim["patient"],
                "amount": claim["patient_due"],
                "reference": claim["reference"],
                "payment_method": rng.choice(["Card", "Cash", "Online"]),
            },
            metadata={"counterparty_name": claim["patient"]},
        )
        _reduce_receivable(state, claim["reference"], claim["patient_due"])
        postings = [posting([receipt.doc_id, claim["doc_id"]], "Cash", "Accounts Receivable", claim["patient_due"], pay_date, name)]
        return ScenarioResult(
            documents=[receipt],
            postings=postings,
            bank_rows=[bank_row(pay_date, f"Copay receipt {receipt.fields['receipt_number']}", claim["patient_due"])],
        )

    return BusinessScenario(name=name, description=description, doc_types=("copay_receipt",), doc_count_hint=1, builder=build)


def make_insurer_remittance_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        claims = state.metadata.get("clinic_claims", [])
        if not claims:
            raise ValueError(f"Scenario '{name}' needs an open clinic claim")
        claim = claims.pop(0)
        remit_date = pick_date(state.period_spec, rng, "late")
        remittance = doc_seed(
            state,
            doc_type="insurer_remittance",
            title=get_doc_schema("insurer_remittance").title,
            date=remit_date,
            role="posting_doc",
            fields={
                "remittance_number": state.next_number("REM"),
                "payer_name": claim["payer_name"],
                "claim_reference": claim["reference"],
                "approved_amount": claim["insurer_due"],
                "paid_amount": claim["insurer_due"],
                "payment_date": remit_date,
            },
            metadata={"counterparty_name": claim["payer_name"]},
        )
        _reduce_receivable(state, claim["reference"], claim["insurer_due"])
        postings = [posting([remittance.doc_id, claim["doc_id"]], "Cash", "Accounts Receivable", claim["insurer_due"], remit_date, name)]
        return ScenarioResult(
            documents=[remittance],
            postings=postings,
            bank_rows=[bank_row(remit_date, f"Insurer remittance {claim['reference']}", claim["insurer_due"])],
        )

    return BusinessScenario(name=name, description=description, doc_types=("insurer_remittance",), doc_count_hint=1, builder=build)


def make_rent_roll_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        bill_date = pick_date(state.period_spec, rng, "opening")
        tenant = rng.choice(state.master_data["tenants"])
        unit = rng.choice(state.master_data["units"])
        amount_value = _scaled_amount(state, rng, 1800, 4200, "operating")
        rent_roll = doc_seed(
            state,
            doc_type="rent_roll",
            title=get_doc_schema("rent_roll").title,
            date=bill_date,
            role="posting_doc",
            fields={
                "roll_number": state.next_number("ROLL"),
                "property_name": rng.choice(state.master_data["properties"]),
                "period_label": state.period_spec.label,
                "lines": [{"unit": unit, "tenant": tenant, "amount": amount_value}],
                "total_amount": amount_value,
            },
            metadata={"counterparty_name": tenant},
        )
        postings = [posting([rent_roll.doc_id], "Accounts Receivable", "Rental Revenue", amount_value, bill_date, name)]
        state.open_receivables.append({"reference": rent_roll.fields["roll_number"], "doc_id": rent_roll.doc_id, "counterparty": tenant, "remaining": amount_value, "category": "tenant"})
        return ScenarioResult(documents=[rent_roll], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("rent_roll",), doc_count_hint=1, builder=build, allow_repeat=True)


def make_security_deposit_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        notice_date = pick_date(state.period_spec, rng, "early")
        tenant = rng.choice(state.master_data["tenants"])
        amount_value = _scaled_amount(state, rng, 900, 3200, "operating")
        notice = doc_seed(
            state,
            doc_type="security_deposit_notice",
            title=get_doc_schema("security_deposit_notice").title,
            date=notice_date,
            role="posting_doc",
            fields={
                "notice_number": state.next_number("DEP"),
                "tenant_name": tenant,
                "unit_id": rng.choice(state.master_data["units"]),
                "amount": amount_value,
                "due_date": due_date(notice_date, rng, 3, 10),
            },
            metadata={"counterparty_name": tenant},
        )
        state.metadata.setdefault("security_deposits", []).append({"reference": notice.fields["notice_number"], "doc_id": notice.doc_id, "tenant": tenant, "amount": amount_value})
        postings = [posting([notice.doc_id], "Cash", "Security Deposits Payable", amount_value, notice_date, name)]
        return ScenarioResult(
            documents=[notice],
            postings=postings,
            bank_rows=[bank_row(notice_date, f"Security deposit {notice.fields['notice_number']}", amount_value)],
        )

    return BusinessScenario(name=name, description=description, doc_types=("security_deposit_notice",), doc_count_hint=1, builder=build, allow_repeat=True)


def make_security_deposit_refund_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        deposits = state.metadata.get("security_deposits", [])
        if not deposits:
            raise ValueError(f"Scenario '{name}' needs an existing deposit")
        deposit = deposits.pop(0)
        refund_amount = round(deposit["amount"] * rng.uniform(0.7, 1.0), 2)
        refund_date = pick_date(state.period_spec, rng, "late")
        notice = doc_seed(
            state,
            doc_type="security_deposit_notice",
            title=get_doc_schema("security_deposit_notice").title,
            date=refund_date,
            role="adjustment_doc",
            fields={
                "notice_number": state.next_number("DEPREF"),
                "tenant_name": deposit["tenant"],
                "unit_id": rng.choice(state.master_data["units"]),
                "amount": refund_amount,
                "due_date": refund_date,
            },
            metadata={"counterparty_name": deposit["tenant"], "footer_note": f"Refund of previously collected security deposit {deposit['reference']}."},
        )
        postings = [posting([notice.doc_id, deposit["doc_id"]], "Security Deposits Payable", "Cash", refund_amount, refund_date, name)]
        return ScenarioResult(
            documents=[notice],
            postings=postings,
            bank_rows=[bank_row(refund_date, f"Security deposit refund {deposit['reference']}", -refund_amount)],
        )

    return BusinessScenario(name=name, description=description, doc_types=("security_deposit_notice",), doc_count_hint=1, builder=build, period_types=("quarter", "year"))


def make_utilities_bill_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        bill_date = pick_date(state.period_spec, rng, "late")
        vendor = rng.choice(state.master_data["utility_providers"])
        total = _scaled_amount(state, rng, 180, 1100, "operating")
        stmt = doc_seed(
            state,
            doc_type="utilities_statement",
            title=get_doc_schema("utilities_statement").title,
            date=bill_date,
            role="posting_doc",
            fields={
                "statement_number": state.next_number("UTIL"),
                "invoice_number": state.next_number("UTILINV"),
                "provider": vendor,
                "pay_to": vendor,
                "service_period": state.period_spec.label,
                "due_date": due_date(bill_date, rng, 7, 18),
                "total": total,
                "line_items": line_items(total, ["Electricity", "Water"], rng),
            },
            metadata={"counterparty_name": vendor},
        )
        state.open_payables.append({"reference": stmt.fields["statement_number"], "doc_id": stmt.doc_id, "counterparty": vendor, "remaining": total, "category": "utility"})
        postings = [posting([stmt.doc_id], "Utilities Expense", "Accounts Payable", total, bill_date, name)]
        return ScenarioResult(documents=[stmt], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("utilities_statement",), doc_count_hint=1, builder=build, allow_repeat=True)


def make_expense_accrual_scenario(*, name: str, description: str, expense_account: str = "Utilities Expense") -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        accrual_amount = _scaled_amount(state, rng, 220, 1800, "operating")
        memo = doc_seed(
            state,
            doc_type="service_period_memo",
            title=get_doc_schema("service_period_memo").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "memo_id": state.next_number("ACCR"),
                "subject": "Month-end expense accrual",
                "reference": state.period_spec.label,
                "recognized_amount": accrual_amount,
                "narrative": f"Accrue unpaid {expense_account.lower()} incurred before period end.",
            },
        )
        postings = [posting([memo.doc_id], expense_account, "Accrued Expenses", accrual_amount, state.period_end, name)]
        return ScenarioResult(documents=[memo], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("service_period_memo",), doc_count_hint=1, builder=build, period_types=("quarter", "year"))


def make_bad_debt_review_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        candidate = _take_open_item(state.open_receivables)
        writeoff = round(candidate["remaining"] * rng.uniform(0.2, 0.6), 2)
        summary = doc_seed(
            state,
            doc_type="ar_aging_summary",
            title=get_doc_schema("ar_aging_summary").title,
            date=state.period_end,
            role="support_doc",
            fields={
                "summary_id": state.next_number("AGING"),
                "period_label": state.period_spec.label,
                "lines": [
                    {
                        "customer": candidate["counterparty"],
                        "reference": candidate["reference"],
                        "current": round(candidate["remaining"] - writeoff, 2),
                        "past_due": writeoff,
                    }
                ],
                "total_amount": candidate["remaining"],
            },
            metadata={"footer_note": "Accounts receivable review prepared for collectability assessment."},
        )
        memo = doc_seed(
            state,
            doc_type="credit_memo",
            title=get_doc_schema("credit_memo").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "memo_number": state.next_number("CM"),
                "counterparty": candidate["counterparty"],
                "reference": candidate["reference"],
                "reason": "Bad debt writeoff approved after aging review",
                "amount": writeoff,
            },
            metadata={"counterparty_name": candidate["counterparty"]},
        )
        candidate["remaining"] = round(candidate["remaining"] - writeoff, 2)
        if candidate["remaining"] > 0.01:
            state.open_receivables.insert(0, candidate)
        postings = [posting([summary.doc_id, memo.doc_id, candidate["doc_id"]], "Bad Debt Expense", "Accounts Receivable", writeoff, state.period_end, name)]
        return ScenarioResult(documents=[summary, memo], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("ar_aging_summary", "credit_memo"), doc_count_hint=2, builder=build, period_types=("quarter", "year"))


def make_customer_credit_memo_scenario(
    *,
    name: str,
    description: str,
    against_liability: bool = False,
    revenue_account: str = "Service Revenue",
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        tax_value = 0.0
        if against_liability and state.metadata.get("deferred_revenue"):
            item = _take_deferred_item(state)
            account = "Unearned Revenue"
            credit = "Accounts Receivable" if item["receivable_open"] else "Cash"
            amount_value = round(item["remaining"] * rng.uniform(0.1, 0.35), 2)
            tax_value = round(float(item.get("tax_remaining", 0.0)) * (amount_value / max(float(item["remaining"]), 0.01)), 2)
            item["remaining"] = round(item["remaining"] - amount_value, 2)
            item["tax_remaining"] = round(float(item.get("tax_remaining", 0.0)) - tax_value, 2)
            if item["remaining"] > 0.01:
                state.metadata.setdefault("deferred_revenue", []).insert(0, item)
            refs = [item["doc_id"]]
            counterparty = item["counterparty"]
        else:
            item = _take_open_item(state.open_receivables)
            account = revenue_account
            credit = "Accounts Receivable"
            amount_value = round(item["remaining"] * rng.uniform(0.1, 0.35), 2)
            item["remaining"] = round(item["remaining"] - amount_value, 2)
            if item["remaining"] > 0.01:
                state.open_receivables.insert(0, item)
            refs = [item["doc_id"]]
            counterparty = item["counterparty"]
        memo_date = pick_date(state.period_spec, rng, "late")
        memo = doc_seed(
            state,
            doc_type="credit_memo",
            title=get_doc_schema("credit_memo").title,
            date=memo_date,
            role="posting_doc",
            fields={
                "memo_number": state.next_number("CM"),
                "counterparty": counterparty,
                "reference": item["reference"],
                "reason": rng.choice(["Pricing adjustment", "Service issue", "Contract revision"]),
                "amount": amount_value,
                "document_currency": state.currency_code,
            },
            metadata={"counterparty_name": counterparty},
        )
        refs.append(memo.doc_id)
        postings = [posting(refs, account, credit, amount_value, memo_date, name)]
        if against_liability and tax_value > 0:
            memo.fields["tax_label"] = state.tax_label or tax_label_for_regime(state.tax_regime)
            memo.fields["tax_rate"] = 0.0
            memo.fields["tax_amount"] = tax_value
            postings.extend(_tax_reversal_postings(state, refs, credit, tax_value, memo_date, f"{name}_tax"))
        bank_rows = [bank_row(memo_date, f"Customer refund {memo.fields['memo_number']}", -amount_value)] if credit == "Cash" else []
        if against_liability and tax_value > 0 and credit == "Cash":
            bank_rows = [bank_row(memo_date, f"Customer refund {memo.fields['memo_number']}", -(amount_value + tax_value))]
        return ScenarioResult(documents=[memo], postings=postings, bank_rows=bank_rows)

    return BusinessScenario(name=name, description=description, doc_types=("credit_memo",), doc_count_hint=1, builder=build, period_types=("quarter", "year"))


def make_deferral_invoice_scenario(
    *,
    name: str,
    description: str,
    support_doc_type: str,
    revenue_account: str = "Service Revenue",
    cash_collection_rate: float = 0.0,
    include_renewal_notice: bool = False,
    apply_indirect_tax: bool = False,
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        bill_date = pick_date(state.period_spec, rng, "early")
        customer = rng.choice(state.master_data["customers"])
        months = 12 if state.period_spec.period_type == "year" else rng.choice((3, 6, 12))
        subtotal = _scaled_amount(state, rng, 2400, 16000, "contract")
        total = subtotal
        tax_amount = 0.0
        if apply_indirect_tax and state.tax_regime != "none":
            tax_amount = float(_tax_details(state, subtotal, rng)["tax_amount"])
            total = round(subtotal + tax_amount, 2)
        monthly_release = subtotal / months
        support_doc = doc_seed(
            state,
            doc_type=support_doc_type,
            title=get_doc_schema(support_doc_type).title,
            date=bill_date,
            role="support_doc",
            fields=_support_fields_for_deferral(state, support_doc_type, customer, total, months, bill_date, rng),
            metadata={"counterparty_name": customer},
        )
        docs = [support_doc]
        if include_renewal_notice:
            renewal_date = max(state.period_start, date_plus_days(bill_date, -15))
            renewal = doc_seed(
                state,
                doc_type="renewal_notice",
                title=get_doc_schema("renewal_notice").title,
                date=renewal_date,
                role="support_doc",
                fields={
                    "notice_number": state.next_number("RENEW"),
                    "customer": customer,
                    "contract_reference": support_doc.fields.get("form_number", support_doc.fields.get("number", state.next_number("CTR"))),
                    "renewal_start": bill_date,
                    "renewal_amount": total,
                },
                metadata={"counterparty_name": customer},
            )
            docs.insert(0, renewal)
        invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=bill_date,
            role="posting_doc",
            fields={
                "number": state.next_number("INV"),
                "customer": customer,
                "due_date": due_date(bill_date, rng, 7, 18),
                "total": total,
                "line_items": line_items(
                    subtotal,
                    [
                        rng.choice(state.master_data.get("subscription_plans", state.master_data["services"])),
                        "Service coverage under contract",
                    ],
                    rng,
                ),
                "contract_ref": support_doc.fields.get("form_number", support_doc.fields.get("number", state.next_number("CTR"))),
                "document_currency": state.currency_code,
            },
            metadata={"counterparty_name": customer},
        )
        if tax_amount > 0:
            tax_details = _tax_details(state, subtotal, rng, tax_amount / subtotal if subtotal else 0.0)
            _apply_tax_fields(invoice.fields, tax_details, state)
        docs.append(invoice)
        refs = [doc.doc_id for doc in docs]
        if rng.random() < cash_collection_rate:
            postings = [posting(refs, "Cash", "Unearned Revenue", subtotal, bill_date, name)]
            postings.extend(_output_tax_postings(state, refs, "Cash", tax_amount, bill_date, f"{name}_tax"))
            bank_rows = [bank_row(bill_date, f"Advance collection {invoice.fields['number']}", total)]
            receivable_open = False
        else:
            postings = [posting(refs, "Accounts Receivable", "Unearned Revenue", subtotal, bill_date, name)]
            postings.extend(_output_tax_postings(state, refs, "Accounts Receivable", tax_amount, bill_date, f"{name}_tax"))
            state.open_receivables.append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": customer, "remaining": total, "category": "customer"})
            bank_rows = []
            receivable_open = True
        state.metadata.setdefault("deferred_revenue", []).append(
            {
                "reference": invoice.fields["number"],
                "doc_id": invoice.doc_id,
                "counterparty": customer,
                "remaining": subtotal,
                "tax_remaining": tax_amount,
                "monthly_release": monthly_release,
                "revenue_account": revenue_account,
                "receivable_open": receivable_open,
            }
        )
        return ScenarioResult(documents=docs, postings=postings, bank_rows=bank_rows)

    doc_types = [support_doc_type, "customer_invoice"]
    if include_renewal_notice:
        doc_types.insert(0, "renewal_notice")
    return BusinessScenario(name=name, description=description, doc_types=tuple(doc_types), doc_count_hint=len(doc_types), builder=build)


def make_deferral_release_scenario(*, name: str, description: str, revenue_account: str = "Service Revenue") -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        item = _take_deferred_item(state)
        release_amount = round(min(item["remaining"], item["monthly_release"] * state.period_spec.month_count), 2)
        schedule = doc_seed(
            state,
            doc_type="revenue_recognition_schedule",
            title=get_doc_schema("revenue_recognition_schedule").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "schedule_id": state.next_number("REVREC"),
                "contract_reference": item["reference"],
                "period_label": state.period_spec.label,
                "opening_deferred": item["remaining"],
                "added_deferred": 0.0,
                "released_this_period": release_amount,
                "ending_deferred": round(item["remaining"] - release_amount, 2),
            },
            metadata={"counterparty_name": item["counterparty"]},
        )
        item["remaining"] = round(item["remaining"] - release_amount, 2)
        if item["remaining"] > 0.01:
            state.metadata.setdefault("deferred_revenue", []).insert(0, item)
        postings = [posting([schedule.doc_id, item["doc_id"]], "Unearned Revenue", revenue_account, release_amount, state.period_end, name)]
        return ScenarioResult(documents=[schedule], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("revenue_recognition_schedule",), doc_count_hint=1, builder=build)


def make_material_purchase_scenario(*, name: str, description: str, apply_indirect_tax: bool = False) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        purchase_date = pick_date(state.period_spec, rng, "early")
        vendor = rng.choice(state.master_data["vendors"])
        material = rng.choice(state.master_data["raw_materials"])
        qty = rng.randint(120, 420)
        unit_cost = _scaled_amount(state, rng, 3, 16, "inventory")
        subtotal = round(qty * unit_cost, 2)
        total = subtotal
        invoice = doc_seed(
            state,
            doc_type="supplier_invoice",
            title=get_doc_schema("supplier_invoice").title_for(state.industry),
            date=purchase_date,
            role="posting_doc",
            fields={
                "number": state.next_number("MAT"),
                "vendor": vendor,
                "due_date": due_date(purchase_date, rng, 12, 24),
                "total": subtotal,
                "document_currency": state.currency_code,
                "line_items": [{"description": material, "quantity": qty, "unit_cost": unit_cost, "amount": subtotal}],
            },
            metadata={"counterparty_name": vendor},
        )
        tax_amount = 0.0
        if apply_indirect_tax and state.tax_regime != "none":
            tax_details = _tax_details(state, subtotal, rng)
            _apply_tax_fields(invoice.fields, tax_details, state)
            total = float(tax_details["total"])
            tax_amount = float(tax_details["tax_amount"])
        state.metadata.setdefault("raw_material_lots", []).append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "material": material, "qty": qty, "amount": subtotal})
        state.open_payables.append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": vendor, "remaining": total, "category": "vendor"})
        postings = [posting([invoice.doc_id], "Raw Materials Inventory", "Accounts Payable", subtotal, purchase_date, name)]
        postings.extend(_input_tax_postings(state, [invoice.doc_id], "Accounts Payable", tax_amount, purchase_date, f"{name}_tax"))
        return ScenarioResult(documents=[invoice], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("supplier_invoice",), doc_count_hint=1, builder=build, allow_repeat=True)


def make_material_issue_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        lots = state.metadata.get("raw_material_lots", [])
        if not lots:
            raise ValueError(f"Scenario '{name}' needs purchased raw materials")
        lot = lots.pop(0)
        issue_amount = round(lot["amount"] * rng.uniform(0.45, 0.8), 2)
        issue_qty = max(1, int(lot["qty"] * (issue_amount / lot["amount"])))
        issue_date = pick_date(state.period_spec, rng, "mid")
        batch_id = state.next_number("BATCH")
        requisition = doc_seed(
            state,
            doc_type="material_requisition_slip",
            title=get_doc_schema("material_requisition_slip").title,
            date=issue_date,
            role="posting_doc",
            fields={
                "slip_number": state.next_number("REQ"),
                "batch_id": batch_id,
                "material": lot["material"],
                "quantity_issued": issue_qty,
                "issue_value": issue_amount,
                "warehouse": rng.choice(state.master_data["warehouses"]),
            },
        )
        batch_sheet = doc_seed(
            state,
            doc_type="production_batch_sheet",
            title=get_doc_schema("production_batch_sheet").title,
            date=issue_date,
            role="support_doc",
            fields={
                "batch_id": batch_id,
                "product_name": rng.choice(state.master_data["finished_goods"]),
                "planned_units": rng.randint(20, 80),
                "material_value": issue_amount,
                "labor_value": 0.0,
                "overhead_value": 0.0,
            },
        )
        state.metadata.setdefault("manufacturing_batches", []).append({"batch_id": batch_id, "doc_id": batch_sheet.doc_id, "product_name": batch_sheet.fields["product_name"], "wip_value": issue_amount})
        remaining_amount = round(lot["amount"] - issue_amount, 2)
        remaining_qty = max(0, lot["qty"] - issue_qty)
        if remaining_amount > 0.01 and remaining_qty > 0:
            state.metadata.setdefault("raw_material_lots", []).insert(0, {**lot, "amount": remaining_amount, "qty": remaining_qty})
        postings = [posting([requisition.doc_id, batch_sheet.doc_id, lot["doc_id"]], "Work In Process", "Raw Materials Inventory", issue_amount, issue_date, name)]
        return ScenarioResult(documents=[requisition, batch_sheet], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("material_requisition_slip", "production_batch_sheet"), doc_count_hint=2, builder=build)


def make_wip_cost_scenario(*, name: str, description: str, source: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        batches = state.metadata.get("manufacturing_batches", [])
        if not batches:
            raise ValueError(f"Scenario '{name}' needs an open production batch")
        batch = batches.pop(0)
        add_value = _scaled_amount(state, rng, 600, 3200, "capital")
        post_date = pick_date(state.period_spec, rng, "mid" if source == "labor" else "closing")
        if source == "labor":
            doc_type = "direct_labor_record"
            role = "posting_doc"
            fields = {
                "batch_id": batch["batch_id"],
                "product_name": batch["product_name"],
                "planned_units": rng.randint(20, 80),
                "labor_value": add_value,
                "cash_paid": add_value,
            }
        else:
            doc_type = "overhead_accrual_memo"
            role = "adjustment_doc"
            fields = {
                "batch_id": batch["batch_id"],
                "product_name": batch["product_name"],
                "planned_units": rng.randint(20, 80),
                "overhead_value": add_value,
                "accrued_amount": add_value,
                "narrative": "Factory overhead incurred this period has been accrued into work in process.",
            }
        doc = doc_seed(
            state,
            doc_type=doc_type,
            title=get_doc_schema(doc_type).title,
            date=post_date,
            role=role,
            fields=fields,
        )
        batch["wip_value"] = round(batch["wip_value"] + add_value, 2)
        state.metadata.setdefault("manufacturing_batches", []).insert(0, batch)
        credit_account = "Cash" if source == "labor" else "Accrued Expenses"
        label = f"{name}_{source}"
        postings = [posting([doc.doc_id, batch["doc_id"]], "Work In Process", credit_account, add_value, post_date, label)]
        bank_rows = [bank_row(post_date, f"Direct labor {batch['batch_id']}", -add_value)] if source == "labor" else []
        return ScenarioResult(documents=[doc], postings=postings, bank_rows=bank_rows)

    return BusinessScenario(
        name=name,
        description=description,
        doc_types=("direct_labor_record",) if source == "labor" else ("overhead_accrual_memo",),
        doc_count_hint=1,
        builder=build,
    )


def make_finished_goods_transfer_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        batches = state.metadata.get("manufacturing_batches", [])
        if not batches:
            raise ValueError(f"Scenario '{name}' needs an open production batch")
        batch = batches.pop(0)
        transfer_date = pick_date(state.period_spec, rng, "late")
        transfer = doc_seed(
            state,
            doc_type="finished_goods_transfer_note",
            title=get_doc_schema("finished_goods_transfer_note").title,
            date=transfer_date,
            role="posting_doc",
            fields={
                "transfer_number": state.next_number("FGT"),
                "batch_id": batch["batch_id"],
                "product_name": batch["product_name"],
                "units_completed": rng.randint(18, 70),
                "transfer_value": batch["wip_value"],
            },
        )
        state.metadata.setdefault("finished_goods_lots", []).append({"reference": transfer.fields["transfer_number"], "doc_id": transfer.doc_id, "product_name": batch["product_name"], "amount": batch["wip_value"]})
        postings = [posting([transfer.doc_id, batch["doc_id"]], "Finished Goods Inventory", "Work In Process", batch["wip_value"], transfer_date, name)]
        return ScenarioResult(documents=[transfer], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("finished_goods_transfer_note",), doc_count_hint=1, builder=build)


def make_manufacturing_sale_scenario(*, name: str, description: str, apply_indirect_tax: bool = False) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        lots = state.metadata.get("finished_goods_lots", [])
        if not lots:
            raise ValueError(f"Scenario '{name}' needs finished goods ready to sell")
        lot = lots.pop(0)
        sale_date = pick_date(state.period_spec, rng, "late")
        customer = rng.choice(state.master_data["customers"])
        subtotal = round(lot["amount"] * rng.uniform(1.2, 1.7), 2)
        sales_amount = subtotal
        tax_amount = 0.0
        if apply_indirect_tax and state.tax_regime != "none":
            tax_amount = float(_tax_details(state, subtotal, rng)["tax_amount"])
            sales_amount = round(subtotal + tax_amount, 2)
        invoice = doc_seed(
            state,
            doc_type="customer_invoice",
            title=get_doc_schema("customer_invoice").title_for(state.industry),
            date=sale_date,
            role="posting_doc",
            fields={
                "number": state.next_number("FGINV"),
                "customer": customer,
                "due_date": due_date(sale_date, rng, 12, 24),
                "total": sales_amount,
                "line_items": [{"description": lot["product_name"], "amount": subtotal}],
                "contract_ref": lot["reference"],
                "document_currency": state.currency_code,
            },
            metadata={"counterparty_name": customer},
        )
        if tax_amount > 0:
            tax_details = _tax_details(state, subtotal, rng, tax_amount / subtotal if subtotal else 0.0)
            _apply_tax_fields(invoice.fields, tax_details, state)
        state.open_receivables.append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": customer, "remaining": sales_amount, "category": "customer"})
        postings = [
            posting([invoice.doc_id, lot["doc_id"]], "Accounts Receivable", "Sales Revenue", subtotal, sale_date, f"{name}_sale"),
            posting([invoice.doc_id, lot["doc_id"]], "Cost of Goods Sold", "Finished Goods Inventory", lot["amount"], sale_date, f"{name}_cogs"),
        ]
        postings.extend(_output_tax_postings(state, [invoice.doc_id, lot["doc_id"]], "Accounts Receivable", tax_amount, sale_date, f"{name}_tax"))
        return ScenarioResult(documents=[invoice], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("customer_invoice",), doc_count_hint=1, builder=build)


def make_scrap_report_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        pools = state.metadata.get("finished_goods_lots", []) or state.metadata.get("manufacturing_batches", [])
        if not pools:
            opening_fg = round(float(state.opening_balance.assets.get("Finished Goods Inventory", 0.0)), 2)
            opening_wip = round(float(state.opening_balance.assets.get("Work In Process", 0.0)), 2)
            if opening_fg > 0:
                pools = [{"reference": "OPEN-FG", "doc_id": "D001", "product_name": "Opening finished goods", "amount": opening_fg}]
            elif opening_wip > 0:
                pools = [{"batch_id": "OPEN-WIP", "doc_id": "D001", "product_name": "Opening work in process", "wip_value": opening_wip, "amount": opening_wip}]
            else:
                raise ValueError(f"Scenario '{name}' needs inventory to write down")
        item = pools[0]
        write_down = round(item["amount"] * rng.uniform(0.08, 0.2), 2)
        doc = doc_seed(
            state,
            doc_type="scrap_report",
            title=get_doc_schema("scrap_report").title,
            date=state.period_end,
            role="adjustment_doc",
            fields={
                "report_number": state.next_number("SCRAP"),
                "batch_or_lot_ref": item["reference"] if "reference" in item else item["batch_id"],
                "reason": rng.choice(["Damage in production", "Failed quality test", "Obsolete units"]),
                "write_down_amount": write_down,
            },
        )
        credit_account = "Finished Goods Inventory" if "reference" in item else "Work In Process"
        postings = [posting([doc.doc_id, item["doc_id"]], "Inventory Shrinkage Expense", credit_account, write_down, state.period_end, name)]
        return ScenarioResult(documents=[doc], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("scrap_report",), doc_count_hint=1, builder=build, period_types=("quarter", "year"))


def _take_open_item(items: list[dict[str, object]]) -> dict[str, object]:
    if not items:
        raise ValueError("Scenario needs an open item but none are available")
    return items.pop(0)


def _reduce_receivable(state: BusinessState, reference: str, amount_value: float) -> None:
    updated: list[dict[str, object]] = []
    for item in state.open_receivables:
        if item["reference"] == reference:
            item["remaining"] = round(float(item["remaining"]) - amount_value, 2)
        if float(item["remaining"]) > 0.01:
            updated.append(item)
    state.open_receivables[:] = updated


def _take_deferred_item(state: BusinessState) -> dict[str, object]:
    items = state.metadata.get("deferred_revenue", [])
    if not items:
        raise ValueError("Scenario needs deferred revenue but none is available")
    return items.pop(0)


def _support_fields_for_deferral(
    state: BusinessState,
    support_doc_type: str,
    customer: str,
    total: float,
    months: int,
    bill_date: str,
    rng: random.Random,
) -> dict[str, object]:
    if support_doc_type == "subscription_order_form":
        return {
            "form_number": state.next_number("SOF"),
            "customer": customer,
            "plan_name": rng.choice(state.master_data["subscription_plans"]),
            "term_months": months,
            "contract_start": bill_date,
            "total_contract_value": total,
        }
    if support_doc_type == "retainer_agreement_memo":
        return {
            "memo_id": state.next_number("RET"),
            "subject": "Retainer engagement",
            "reference": state.next_number("RET-CTR"),
            "contract_months": months,
            "total_contract_value": total,
            "narrative": f"Customer {customer} agreed to a service package spanning {months} months.",
        }
    return {
        "memo_id": state.next_number("RET"),
        "subject": "Retainer engagement",
        "reference": state.next_number("RET-CTR"),
        "recognized_amount": round(total / months, 2),
        "narrative": f"Customer {customer} agreed to a service package spanning {months} months.",
    }
