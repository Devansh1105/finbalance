"""Reusable business-scenario factories for industries."""

from __future__ import annotations

import random

from docs_benchmark.doc_schemas import get_doc_schema
from docs_benchmark.generation.helpers import (
    add_months_to_date,
    amount,
    amount_scale,
    bank_row,
    date_plus_days,
    doc_seed,
    due_date,
    line_items,
    pay_period_label,
    pick_date,
    posting,
    quantity_line_items,
)
from docs_benchmark.types import BusinessScenario, BusinessState, ScenarioResult


def _scaled_amount(state: BusinessState, rng: random.Random, lo: float, hi: float, bucket: str = "operating") -> float:
    return round(amount(rng, lo, hi) * amount_scale(state.industry, state.period_spec.period_type, state.difficulty_level, bucket), 2)


def make_service_invoice_scenario(
    *,
    name: str,
    description: str,
    revenue_account: str,
    with_work_order: bool = False,
    cash_sale_rate: float = 0.0,
) -> BusinessScenario:
    doc_types = ("customer_invoice", "work_order") if with_work_order else ("customer_invoice",)

    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        issue_date = pick_date(state.period_spec, rng, "early")
        customer = rng.choice(state.master_data["customers"])
        total = _scaled_amount(state, rng, 1800, 8200, "operating")
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
                    "approved_amount": total,
                },
                metadata={"footer_note": "Approved job scope supporting the related invoice."},
            )
            documents.append(work_order)
            refs.append(work_order.doc_id)

        fields = {
            "number": invoice_number,
            "customer": customer,
            "due_date": due_date(issue_date, rng, 10, 24),
            "total": total,
            "line_items": line_items(total, [rng.choice(state.master_data["services"]), "Follow-up support"], rng),
            "contract_ref": state.next_number("CTR"),
        }
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
            postings.append(posting(refs, "Cash", revenue_account, total, issue_date, name))
            bank_rows.append(bank_row(issue_date, f"Customer payment {invoice_number}", total))
        else:
            postings.append(posting(refs, "Accounts Receivable", revenue_account, total, issue_date, name))
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
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        issue_date = pick_date(state.period_spec, rng, "early")
        vendor = rng.choice(state.master_data["vendors"])
        total = _scaled_amount(state, rng, 420, 5400, "operating")
        descriptions = state.master_data["products"] if quantity_lines else [rng.choice(state.master_data["services"]), "Support fee"]
        rows = quantity_line_items(total, descriptions[:2], rng) if quantity_lines else line_items(total, descriptions[:2], rng)
        fields = {
            "number": state.next_number("BILL"),
            "vendor": vendor,
            "due_date": due_date(issue_date, rng, 10, 21),
            "total": total,
            "line_items": rows,
        }
        if doc_type == "vendor_invoice":
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
        postings = [posting([bill.doc_id], debit_account, credit_account, total, issue_date, name)]
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
                "reason": "The billing desk issued a revised reference after the review copy was withdrawn.",
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
            },
        )
        postings = [posting([invoice.doc_id], asset_account, "Cash", paid_cash, purchase_date, f"{name}_cash")]
        if financed > 0:
            postings.append(posting([invoice.doc_id], asset_account, "Notes Payable", financed, purchase_date, f"{name}_financed"))
        state.asset_register.append(
            {
                "asset_name": asset_name,
                "asset_tag": invoice.fields["asset_tag"],
                "cost": total,
                "useful_life_months": invoice.fields["useful_life_months"],
                "monthly_charge": round(total / invoice.fields["useful_life_months"], 2),
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
        fields = {
            "schedule_id": state.next_number("DEP"),
            "asset_name": asset["asset_name"],
            "asset_tag": asset["asset_tag"],
            "cost": asset["cost"],
            "useful_life_months": asset["useful_life_months"],
            "current_period_charge": charge,
            "accumulated_depreciation": charge,
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


def make_retail_sale_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        sale_date = pick_date(state.period_spec, rng, "mid")
        gross_sales = _scaled_amount(state, rng, 2600, 12400, "inventory")
        returns = round(gross_sales * rng.uniform(0.01, 0.05), 2)
        net_sales = round(gross_sales - returns, 2)
        cash_sales = round(net_sales * rng.uniform(0.15, 0.35), 2)
        card_sales = round(net_sales - cash_sales, 2)
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
                "units_sold": rng.randint(60, 280),
            },
        )
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
        postings = [
            posting(refs, "Cash", "Sales Revenue", cash_sales, sale_date, f"{name}_cash"),
            posting(refs, "Card Settlement Clearing", "Sales Revenue", card_sales, sale_date, f"{name}_card"),
            posting(refs, "Cost of Goods Sold", "Inventory", cogs, sale_date, f"{name}_cogs"),
        ]
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


def make_goods_receipt_purchase_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        receipt_date = pick_date(state.period_spec, rng, "early")
        vendor = rng.choice(state.master_data["vendors"])
        sku = state.next_number("SKU")
        qty = rng.randint(40, 160)
        unit_cost = _scaled_amount(state, rng, 6, 24, "inventory")
        total = round(qty * unit_cost, 2)
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
                "total": total,
                "goods_receipt_ref": grn.fields["grn_number"],
                "line_items": [
                    {
                        "description": grn.fields["items"][0]["description"],
                        "quantity": qty,
                        "unit_cost": unit_cost,
                        "amount": total,
                    }
                ],
            },
            metadata={"counterparty_name": vendor},
        )
        refs = [grn.doc_id, invoice.doc_id]
        postings = [posting(refs, "Inventory", "Accounts Payable", total, invoice_date, name)]
        state.open_payables.append(
            {"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": vendor, "remaining": total, "category": "vendor"}
        )
        return ScenarioResult(documents=[grn, invoice], postings=postings)

    return BusinessScenario(name=name, description=description, doc_types=("goods_receipt_note", "supplier_invoice"), doc_count_hint=2, builder=build, allow_repeat=True)


def make_delivery_sale_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        ship_date = pick_date(state.period_spec, rng, "mid")
        customer = rng.choice(state.master_data["customers"])
        sku = state.next_number("SKU")
        qty = rng.randint(15, 70)
        unit_price = _scaled_amount(state, rng, 24, 70, "inventory")
        billed = round(qty * unit_price, 2)
        cogs = round(billed * rng.uniform(0.52, 0.72), 2)
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
                "items": [{"sku": sku, "description": rng.choice(state.master_data["products"]), "quantity": qty, "unit_price": unit_price}],
                "billed_amount": billed,
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
                "line_items": [{"description": delivery.fields["items"][0]["description"], "amount": billed}],
                "shipment_ref": delivery.fields["shipment_ref"],
            },
            metadata={"counterparty_name": customer},
        )
        refs = [delivery.doc_id, invoice.doc_id]
        postings = [
            posting(refs, "Accounts Receivable", "Sales Revenue", billed, ship_date, f"{name}_sale"),
            posting(refs, "Cost of Goods Sold", "Inventory", cogs, ship_date, f"{name}_cogs"),
        ]
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
                "provider": vendor,
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
        if against_liability and state.metadata.get("deferred_revenue"):
            item = _take_deferred_item(state)
            account = "Unearned Revenue"
            credit = "Accounts Receivable" if item["receivable_open"] else "Cash"
            amount_value = round(item["remaining"] * rng.uniform(0.1, 0.35), 2)
            item["remaining"] = round(item["remaining"] - amount_value, 2)
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
            },
            metadata={"counterparty_name": counterparty},
        )
        refs.append(memo.doc_id)
        postings = [posting(refs, account, credit, amount_value, memo_date, name)]
        bank_rows = [bank_row(memo_date, f"Customer refund {memo.fields['memo_number']}", -amount_value)] if credit == "Cash" else []
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
) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        bill_date = pick_date(state.period_spec, rng, "early")
        customer = rng.choice(state.master_data["customers"])
        months = 12 if state.period_spec.period_type == "year" else rng.choice((3, 6, 12))
        total = _scaled_amount(state, rng, 2400, 16000, "contract")
        monthly_release = total / months
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
                    total,
                    [
                        rng.choice(state.master_data.get("subscription_plans", state.master_data["services"])),
                        "Service coverage under contract",
                    ],
                    rng,
                ),
                "contract_ref": support_doc.fields.get("form_number", support_doc.fields.get("number", state.next_number("CTR"))),
            },
            metadata={"counterparty_name": customer},
        )
        docs.append(invoice)
        refs = [doc.doc_id for doc in docs]
        if rng.random() < cash_collection_rate:
            postings = [posting(refs, "Cash", "Unearned Revenue", total, bill_date, name)]
            bank_rows = [bank_row(bill_date, f"Advance collection {invoice.fields['number']}", total)]
            receivable_open = False
        else:
            postings = [posting(refs, "Accounts Receivable", "Unearned Revenue", total, bill_date, name)]
            state.open_receivables.append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": customer, "remaining": total, "category": "customer"})
            bank_rows = []
            receivable_open = True
        state.metadata.setdefault("deferred_revenue", []).append(
            {
                "reference": invoice.fields["number"],
                "doc_id": invoice.doc_id,
                "counterparty": customer,
                "remaining": total,
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


def make_material_purchase_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        purchase_date = pick_date(state.period_spec, rng, "early")
        vendor = rng.choice(state.master_data["vendors"])
        material = rng.choice(state.master_data["raw_materials"])
        qty = rng.randint(120, 420)
        unit_cost = _scaled_amount(state, rng, 3, 16, "inventory")
        total = round(qty * unit_cost, 2)
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
                "total": total,
                "line_items": [{"description": material, "quantity": qty, "unit_cost": unit_cost, "amount": total}],
            },
            metadata={"counterparty_name": vendor},
        )
        state.metadata.setdefault("raw_material_lots", []).append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "material": material, "qty": qty, "amount": total})
        state.open_payables.append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": vendor, "remaining": total, "category": "vendor"})
        postings = [posting([invoice.doc_id], "Raw Materials Inventory", "Accounts Payable", total, purchase_date, name)]
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


def make_manufacturing_sale_scenario(*, name: str, description: str) -> BusinessScenario:
    def build(state: BusinessState, rng: random.Random) -> ScenarioResult:
        lots = state.metadata.get("finished_goods_lots", [])
        if not lots:
            raise ValueError(f"Scenario '{name}' needs finished goods ready to sell")
        lot = lots.pop(0)
        sale_date = pick_date(state.period_spec, rng, "late")
        customer = rng.choice(state.master_data["customers"])
        sales_amount = round(lot["amount"] * rng.uniform(1.2, 1.7), 2)
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
                "line_items": [{"description": lot["product_name"], "amount": sales_amount}],
                "contract_ref": lot["reference"],
            },
            metadata={"counterparty_name": customer},
        )
        state.open_receivables.append({"reference": invoice.fields["number"], "doc_id": invoice.doc_id, "counterparty": customer, "remaining": sales_amount, "category": "customer"})
        postings = [
            posting([invoice.doc_id, lot["doc_id"]], "Accounts Receivable", "Sales Revenue", sales_amount, sale_date, f"{name}_sale"),
            posting([invoice.doc_id, lot["doc_id"]], "Cost of Goods Sold", "Finished Goods Inventory", lot["amount"], sale_date, f"{name}_cogs"),
        ]
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
