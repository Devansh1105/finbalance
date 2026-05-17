"""Industry schema for subscription SaaS businesses."""

from __future__ import annotations

from docs_benchmark.generation.master_data import build_master_data
from docs_benchmark.generation.scenario_factories import (
    make_bad_debt_review_scenario,
    make_bundled_contract_allocation_scenario,
    make_customer_credit_memo_scenario,
    make_deferral_invoice_scenario,
    make_deferral_release_scenario,
    make_expense_accrual_scenario,
    make_fx_payable_settlement_scenario,
    make_fx_remeasurement_scenario,
    make_fx_vendor_bill_scenario,
    make_interbank_transfer_scenario,
    make_loan_activity_scenario,
    make_payable_settlement_scenario,
    make_payroll_scenario,
    make_receivable_settlement_scenario,
    make_utilities_bill_scenario,
    make_vendor_bill_scenario,
)
from docs_benchmark.industry_schemas.common import OpeningAccountRule, build_opening_balance, copy_plan, opening_balance_scale
from docs_benchmark.types import DifficultyPlan, IndustrySchema


def _opening_balance(rng, level, period_spec):
    return build_opening_balance(
        rng,
        level,
        period_spec,
        scale_multiplier=opening_balance_scale("subscription_saas", period_spec, level),
        asset_rules=(
            OpeningAccountRule("Cash", 28000, 64000),
            OpeningAccountRule("Accounts Receivable", 2400, 8600, min_level=2),
            OpeningAccountRule("Prepaid Insurance", 800, 2600, min_level=2),
            OpeningAccountRule("Equipment", 4200, 12000, min_level=4),
            OpeningAccountRule("Office Supplies", 300, 1400, min_level=2),
        ),
        liability_rules=(
            OpeningAccountRule("Accounts Payable", 1800, 5200),
            OpeningAccountRule("Accrued Expenses", 600, 2200, min_level=2),
            OpeningAccountRule("Unearned Revenue", 4000, 18000, min_level=2),
            OpeningAccountRule("Loans Payable", 2200, 7600, min_level=4),
        ),
        equity_rules=(OpeningAccountRule("Retained Earnings", 3200, 15000, min_level=2),),
        residual_equity_account="Share Capital",
    )


SCENARIOS = {
    "subscription_invoice": make_deferral_invoice_scenario(
        name="subscription_invoice",
        description="Subscription contract billed before the service period is earned.",
        support_doc_type="subscription_order_form",
        revenue_account="Service Revenue",
        include_renewal_notice=False,
        apply_indirect_tax=True,
    ),
    "subscription_cash_invoice": make_deferral_invoice_scenario(
        name="subscription_cash_invoice",
        description="Subscription billed and collected upfront.",
        support_doc_type="subscription_order_form",
        revenue_account="Service Revenue",
        cash_collection_rate=1.0,
        apply_indirect_tax=True,
    ),
    "renewal_invoice": make_deferral_invoice_scenario(
        name="renewal_invoice",
        description="Renewal invoice supported by a renewal notice.",
        support_doc_type="subscription_order_form",
        revenue_account="Service Revenue",
        include_renewal_notice=True,
        apply_indirect_tax=True,
    ),
    "revenue_release": make_deferral_release_scenario(
        name="revenue_release",
        description="Deferred subscription revenue recognized into earned revenue.",
        revenue_account="Service Revenue",
    ),
    "customer_payment": make_receivable_settlement_scenario(
        name="customer_payment",
        description="Customer pays an open subscription invoice.",
    ),
    "hosting_bill": make_vendor_bill_scenario(
        name="hosting_bill",
        description="Vendor bill for hosting or software support.",
        doc_type="vendor_invoice",
        debit_account="Utilities Expense",
        apply_indirect_tax=True,
    ),
    "fx_hosting_bill": make_fx_vendor_bill_scenario(
        name="fx_hosting_bill",
        description="Hosting or software support bill denominated in a foreign currency.",
        debit_account="Utilities Expense",
        doc_type="vendor_invoice",
    ),
    "fx_vendor_payment": make_fx_payable_settlement_scenario(
        name="fx_vendor_payment",
        description="Settlement of a foreign-currency hosting bill with an FX gain or loss.",
    ),
    "fx_remeasurement": make_fx_remeasurement_scenario(
        name="fx_remeasurement",
        description="Open foreign-currency payable remeasured at the closing rate.",
        target="payable",
    ),
    "vendor_payment": make_payable_settlement_scenario(
        name="vendor_payment",
        description="Business pays hosting or software suppliers.",
    ),
    "payroll": make_payroll_scenario(
        name="payroll",
        description="SaaS payroll run.",
    ),
    "expense_accrual": make_expense_accrual_scenario(
        name="expense_accrual",
        description="Accrual for cloud or support costs incurred but not billed.",
        expense_account="Utilities Expense",
    ),
    "credit_memo": make_customer_credit_memo_scenario(
        name="credit_memo",
        description="Customer contract credit memo against deferred revenue or receivables.",
        against_liability=True,
        revenue_account="Service Revenue",
    ),
    "bad_debt_review": make_bad_debt_review_scenario(
        name="bad_debt_review",
        description="AR aging review for overdue subscription invoices.",
    ),
    "loan_draw": make_loan_activity_scenario(
        name="loan_draw",
        description="Loan draw for scaling operations.",
        mode="draw",
    ),
    "loan_repayment": make_loan_activity_scenario(
        name="loan_repayment",
        description="Loan repayment during the period.",
        mode="repayment",
    ),
    "interbank_transfer": make_interbank_transfer_scenario(
        name="interbank_transfer",
        description="Treasury transfer between the operating account and reserve account.",
    ),
    "bundled_contract_allocation": make_bundled_contract_allocation_scenario(
        name="bundled_contract_allocation",
        description="ASC 606 bundled implementation and platform contract allocated using SSP rather than invoice-line split.",
    ),
}

MONTH_PLANS = {
    1: DifficultyPlan(mandatory=("subscription_invoice", "revenue_release"), optional=("subscription_cash_invoice",)),
    2: DifficultyPlan(mandatory=("subscription_invoice", "revenue_release", "customer_payment", "hosting_bill", "vendor_payment"), optional=("subscription_cash_invoice",)),
    3: DifficultyPlan(mandatory=("subscription_invoice", "revenue_release", "customer_payment", "hosting_bill", "vendor_payment", "payroll"), optional=("subscription_cash_invoice", "renewal_invoice")),
    4: DifficultyPlan(mandatory=("subscription_invoice", "revenue_release", "customer_payment", "hosting_bill", "vendor_payment", "payroll", "loan_draw", "bundled_contract_allocation", "interbank_transfer"), optional=("subscription_cash_invoice", "renewal_invoice")),
    5: DifficultyPlan(mandatory=("subscription_invoice", "revenue_release", "customer_payment", "hosting_bill", "vendor_payment", "payroll", "loan_draw", "loan_repayment", "bundled_contract_allocation", "interbank_transfer"), optional=("subscription_cash_invoice", "renewal_invoice")),
}
QUARTER_PLANS = {
    1: copy_plan(MONTH_PLANS[1], "renewal_invoice"),
    2: copy_plan(MONTH_PLANS[2], "renewal_invoice"),
    3: copy_plan(MONTH_PLANS[3], "expense_accrual"),
    4: copy_plan(MONTH_PLANS[4], "expense_accrual", "credit_memo"),
    5: copy_plan(MONTH_PLANS[5], "expense_accrual", "credit_memo", "bad_debt_review", "fx_hosting_bill", "fx_vendor_payment"),
}
YEAR_PLANS = {
    1: copy_plan(QUARTER_PLANS[1]),
    2: copy_plan(QUARTER_PLANS[2], extra_optional=("revenue_release",)),
    3: copy_plan(QUARTER_PLANS[3], extra_optional=("renewal_invoice",)),
    4: copy_plan(QUARTER_PLANS[4], extra_optional=("revenue_release", "subscription_cash_invoice")),
    5: DifficultyPlan(
        mandatory=(
            "subscription_invoice",
            "revenue_release",
            "customer_payment",
            "hosting_bill",
            "vendor_payment",
            "payroll",
            "loan_draw",
            "loan_repayment",
            "interbank_transfer",
            "bundled_contract_allocation",
            "expense_accrual",
            "credit_memo",
            "bad_debt_review",
            "fx_hosting_bill",
            "fx_remeasurement",
        ),
        optional=("renewal_invoice", "subscription_cash_invoice", "revenue_release"),
    ),
}


INDUSTRY_SCHEMA = IndustrySchema(
    name="subscription_saas",
    display_name="Subscription SaaS",
    description="Software businesses built around subscription billing and deferred revenue release.",
    allowed_accounts=[
        "Cash",
        "Reserve Cash",
        "Accounts Receivable",
        "Prepaid Insurance",
        "Office Supplies",
        "Equipment",
        "Accounts Payable",
        "Accrued Expenses",
        "Input Tax Receivable",
        "Input CGST Receivable",
        "Input SGST Receivable",
        "Input IGST Receivable",
        "Loans Payable",
        "Sales Tax Payable",
        "CGST Payable",
        "SGST Payable",
        "IGST Payable",
        "Unearned Revenue",
        "Share Capital",
        "Retained Earnings",
        "Service Revenue",
        "Utilities Expense",
        "Insurance Expense",
        "Bad Debt Expense",
        "Salaries Expense",
        "Payroll Tax Expense",
        "Interest Expense",
        "Foreign Exchange Gain",
        "Foreign Exchange Loss",
    ],
    opening_builder=_opening_balance,
    master_data_builder=build_master_data,
    scenarios=SCENARIOS,
    period_plans={"month": MONTH_PLANS, "quarter": QUARTER_PLANS, "year": YEAR_PLANS},
    distractor_doc_types=("secondary_copy", "vendor_statement", "memo", "cancellation_note"),
)
