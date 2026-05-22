"""Industry schema for outpatient healthcare clinics."""

from __future__ import annotations

from finbalance.generation.master_data import build_master_data
from finbalance.generation.scenario_factories import (
    make_copay_collection_scenario,
    make_depreciation_scenario,
    make_expense_accrual_scenario,
    make_fixed_asset_purchase_scenario,
    make_insurer_remittance_scenario,
    make_loan_activity_scenario,
    make_payroll_scenario,
    make_patient_billing_scenario,
    make_vendor_bill_scenario,
)
from finbalance.industry_schemas.common import OpeningAccountRule, build_opening_balance, copy_plan, opening_balance_scale
from finbalance.types import DifficultyPlan, IndustrySchema


def _opening_balance(rng, level, period_spec):
    return build_opening_balance(
        rng,
        level,
        period_spec,
        scale_multiplier=opening_balance_scale("healthcare_clinic", period_spec, level),
        asset_rules=(
            OpeningAccountRule("Cash", 24000, 52000),
            OpeningAccountRule("Accounts Receivable", 2600, 8800),
            OpeningAccountRule("Prepaid Insurance", 900, 3200, min_level=2),
            OpeningAccountRule("Office Supplies", 500, 2200, min_level=2),
            OpeningAccountRule("Equipment", 12000, 32000, min_level=4),
        ),
        liability_rules=(
            OpeningAccountRule("Accounts Payable", 1600, 5200),
            OpeningAccountRule("Accrued Expenses", 700, 2400, min_level=2),
            OpeningAccountRule("Loans Payable", 6000, 18000, min_level=4),
        ),
        equity_rules=(OpeningAccountRule("Retained Earnings", 4000, 14000, min_level=2),),
    )


SCENARIOS = {
    "patient_billing": make_patient_billing_scenario(
        name="patient_billing",
        description="Clinic bills a patient visit between patient and insurer responsibility.",
    ),
    "copay_collection": make_copay_collection_scenario(
        name="copay_collection",
        description="Clinic collects the patient copay amount.",
    ),
    "insurer_remittance": make_insurer_remittance_scenario(
        name="insurer_remittance",
        description="Insurer pays the remaining approved amount.",
    ),
    "clinic_supplies_bill": make_vendor_bill_scenario(
        name="clinic_supplies_bill",
        description="Vendor bill for clinic supplies and services.",
        doc_type="vendor_invoice",
        debit_account="Office Supplies Expense",
    ),
    "payroll": make_payroll_scenario(
        name="payroll",
        description="Clinic payroll run.",
    ),
    "expense_accrual": make_expense_accrual_scenario(
        name="expense_accrual",
        description="Accrual for unpaid clinic costs.",
        expense_account="Office Supplies Expense",
    ),
    "loan_draw": make_loan_activity_scenario(
        name="loan_draw",
        description="Loan draw for clinic equipment or working capital.",
        mode="draw",
    ),
    "loan_repayment": make_loan_activity_scenario(
        name="loan_repayment",
        description="Loan repayment for clinic financing.",
        mode="repayment",
    ),
    "equipment_purchase": make_fixed_asset_purchase_scenario(
        name="equipment_purchase",
        description="Medical equipment purchase.",
    ),
    "depreciation": make_depreciation_scenario(
        name="depreciation",
        description="Depreciation on medical equipment.",
    ),
}

MONTH_PLANS = {
    1: DifficultyPlan(mandatory=("patient_billing", "clinic_supplies_bill"), optional=("patient_billing",)),
    2: DifficultyPlan(mandatory=("patient_billing", "clinic_supplies_bill", "copay_collection", "insurer_remittance"), optional=("patient_billing",)),
    3: DifficultyPlan(mandatory=("patient_billing", "clinic_supplies_bill", "copay_collection", "insurer_remittance", "payroll"), optional=("patient_billing", "clinic_supplies_bill")),
    4: DifficultyPlan(mandatory=("patient_billing", "clinic_supplies_bill", "copay_collection", "insurer_remittance", "payroll", "loan_draw", "equipment_purchase", "depreciation"), optional=("patient_billing", "clinic_supplies_bill")),
    5: DifficultyPlan(mandatory=("patient_billing", "clinic_supplies_bill", "copay_collection", "insurer_remittance", "payroll", "loan_draw", "equipment_purchase", "depreciation", "loan_repayment"), optional=("patient_billing", "clinic_supplies_bill")),
}
QUARTER_PLANS = {
    1: copy_plan(MONTH_PLANS[1]),
    2: copy_plan(MONTH_PLANS[2]),
    3: copy_plan(MONTH_PLANS[3], "expense_accrual"),
    4: copy_plan(MONTH_PLANS[4], "expense_accrual"),
    5: copy_plan(MONTH_PLANS[5], "expense_accrual", extra_optional=("patient_billing",)),
}
YEAR_PLANS = {
    1: copy_plan(QUARTER_PLANS[1]),
    2: copy_plan(QUARTER_PLANS[2]),
    3: copy_plan(QUARTER_PLANS[3]),
    4: copy_plan(QUARTER_PLANS[4], extra_optional=("patient_billing",)),
    5: copy_plan(QUARTER_PLANS[5], extra_optional=("patient_billing",)),
}


INDUSTRY_SCHEMA = IndustrySchema(
    name="healthcare_clinic",
    display_name="Healthcare Clinic",
    description="Outpatient clinics with patient billing, insurers, payroll, and equipment.",
    allowed_accounts=[
        "Cash",
        "Accounts Receivable",
        "Prepaid Insurance",
        "Office Supplies",
        "Equipment",
        "Accumulated Depreciation",
        "Accounts Payable",
        "Accrued Expenses",
        "Loans Payable",
        "Notes Payable",
        "Owner's Equity",
        "Retained Earnings",
        "Service Revenue",
        "Office Supplies Expense",
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
