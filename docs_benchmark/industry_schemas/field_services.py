"""Industry schema for field services and contractors."""

from __future__ import annotations

from docs_benchmark.generation.master_data import build_master_data
from docs_benchmark.generation.scenario_factories import (
    make_depreciation_scenario,
    make_expense_accrual_scenario,
    make_expense_receipt_scenario,
    make_fixed_asset_purchase_scenario,
    make_loan_activity_scenario,
    make_payable_settlement_scenario,
    make_payroll_scenario,
    make_receivable_settlement_scenario,
    make_service_invoice_scenario,
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
        scale_multiplier=opening_balance_scale("field_services", period_spec, level),
        asset_rules=(
            OpeningAccountRule("Cash", 22000, 56000),
            OpeningAccountRule("Accounts Receivable", 2200, 8200),
            OpeningAccountRule("Office Supplies", 400, 1800, min_level=2),
            OpeningAccountRule("Vehicles", 6000, 16000, min_level=3),
            OpeningAccountRule("Equipment", 4200, 11000, min_level=4),
            OpeningAccountRule("Prepaid Insurance", 800, 2600, min_level=3, min_period_rank=1),
        ),
        liability_rules=(
            OpeningAccountRule("Accounts Payable", 1800, 5200),
            OpeningAccountRule("Accrued Expenses", 600, 2400, min_level=2),
            OpeningAccountRule("Notes Payable", 2600, 9200, min_level=4),
            OpeningAccountRule("Loans Payable", 2400, 8600, min_level=4, min_period_rank=1),
        ),
        equity_rules=(OpeningAccountRule("Retained Earnings", 2600, 12000, min_level=2),),
    )


SCENARIOS = {
    "job_invoice": make_service_invoice_scenario(
        name="job_invoice",
        description="Job invoice supported by a work order.",
        revenue_account="Service Revenue",
        with_work_order=True,
        apply_indirect_tax=True,
    ),
    "supplier_bill": make_vendor_bill_scenario(
        name="supplier_bill",
        description="Supplier bill for materials or subcontract support.",
        doc_type="supplier_invoice",
        debit_account="Repairs Expense",
        quantity_lines=True,
        apply_indirect_tax=True,
    ),
    "fuel_receipt": make_expense_receipt_scenario(
        name="fuel_receipt",
        description="Fuel or travel purchase tied to field work.",
        debit_account="Fuel Expense",
    ),
    "customer_payment": make_receivable_settlement_scenario(
        name="customer_payment",
        description="Customer pays for a completed job.",
    ),
    "supplier_payment": make_payable_settlement_scenario(
        name="supplier_payment",
        description="Business pays an open supplier invoice.",
    ),
    "payroll": make_payroll_scenario(
        name="payroll",
        description="Crew payroll for the period.",
    ),
    "utilities_bill": make_utilities_bill_scenario(
        name="utilities_bill",
        description="Yard, depot, or office utilities bill.",
    ),
    "expense_accrual": make_expense_accrual_scenario(
        name="expense_accrual",
        description="Accrual for unpaid site costs.",
        expense_account="Repairs Expense",
    ),
    "loan_draw": make_loan_activity_scenario(
        name="loan_draw",
        description="Short-term financing draw for equipment or working capital.",
        mode="draw",
    ),
    "loan_repayment": make_loan_activity_scenario(
        name="loan_repayment",
        description="Loan repayment with principal and interest.",
        mode="repayment",
    ),
    "equipment_purchase": make_fixed_asset_purchase_scenario(
        name="equipment_purchase",
        description="New equipment bought for site operations.",
        asset_account="Equipment",
    ),
    "depreciation": make_depreciation_scenario(
        name="depreciation",
        description="Depreciation for contractor equipment.",
    ),
}

MONTH_PLANS = {
    1: DifficultyPlan(mandatory=("job_invoice", "supplier_bill", "fuel_receipt"), optional=("fuel_receipt", "job_invoice")),
    2: DifficultyPlan(mandatory=("job_invoice", "supplier_bill", "fuel_receipt", "customer_payment", "supplier_payment"), optional=("fuel_receipt", "supplier_bill")),
    3: DifficultyPlan(mandatory=("job_invoice", "supplier_bill", "fuel_receipt", "customer_payment", "supplier_payment", "payroll"), optional=("fuel_receipt", "supplier_bill", "job_invoice")),
    4: DifficultyPlan(mandatory=("job_invoice", "supplier_bill", "fuel_receipt", "customer_payment", "supplier_payment", "payroll", "utilities_bill", "loan_draw", "equipment_purchase", "depreciation"), optional=("fuel_receipt", "supplier_bill")),
    5: DifficultyPlan(mandatory=("job_invoice", "supplier_bill", "fuel_receipt", "customer_payment", "supplier_payment", "payroll", "utilities_bill", "loan_draw", "equipment_purchase", "depreciation", "loan_repayment"), optional=("job_invoice", "supplier_bill", "fuel_receipt", "customer_payment")),
}
QUARTER_PLANS = {
    1: copy_plan(MONTH_PLANS[1]),
    2: copy_plan(MONTH_PLANS[2]),
    3: copy_plan(MONTH_PLANS[3], "expense_accrual"),
    4: copy_plan(MONTH_PLANS[4], "expense_accrual"),
    5: copy_plan(MONTH_PLANS[5], "expense_accrual", extra_optional=("utilities_bill",)),
}
YEAR_PLANS = {
    1: copy_plan(QUARTER_PLANS[1]),
    2: copy_plan(QUARTER_PLANS[2]),
    3: copy_plan(QUARTER_PLANS[3]),
    4: copy_plan(QUARTER_PLANS[4], extra_optional=("job_invoice",)),
    5: copy_plan(QUARTER_PLANS[5], extra_optional=("supplier_bill",)),
}


INDUSTRY_SCHEMA = IndustrySchema(
    name="field_services",
    display_name="Field Services",
    description="Contractors and field operators that invoice jobs and use equipment heavily.",
    allowed_accounts=[
        "Cash",
        "Accounts Receivable",
        "Office Supplies",
        "Prepaid Insurance",
        "Equipment",
        "Vehicles",
        "Input Tax Receivable",
        "Accumulated Depreciation",
        "Accounts Payable",
        "Accrued Expenses",
        "Loans Payable",
        "Notes Payable",
        "Sales Tax Payable",
        "Owner's Equity",
        "Retained Earnings",
        "Service Revenue",
        "Repairs Expense",
        "Fuel Expense",
        "Utilities Expense",
        "Insurance Expense",
        "Salaries Expense",
        "Payroll Tax Expense",
        "Depreciation Expense",
        "Interest Expense",
    ],
    opening_builder=_opening_balance,
    master_data_builder=build_master_data,
    scenarios=SCENARIOS,
    period_plans={"month": MONTH_PLANS, "quarter": QUARTER_PLANS, "year": YEAR_PLANS},
    distractor_doc_types=("secondary_copy", "vendor_statement", "memo", "cancellation_note"),
)
