"""Industry schema for property-management businesses."""

from __future__ import annotations

from finbalance.generation.master_data import build_master_data
from finbalance.generation.scenario_factories import (
    make_depreciation_scenario,
    make_fixed_asset_purchase_scenario,
    make_loan_activity_scenario,
    make_payable_settlement_scenario,
    make_payroll_scenario,
    make_prepaid_insurance_scenario,
    make_receivable_settlement_scenario,
    make_rent_roll_scenario,
    make_security_deposit_refund_scenario,
    make_security_deposit_scenario,
    make_utilities_bill_scenario,
    make_vendor_bill_scenario,
)
from finbalance.industry_schemas.common import OpeningAccountRule, build_opening_balance, copy_plan, opening_balance_scale
from finbalance.types import DifficultyPlan, IndustrySchema


def _opening_balance(rng, level, period_spec):
    return build_opening_balance(
        rng,
        level,
        period_spec,
        scale_multiplier=opening_balance_scale("property_management", period_spec, level),
        asset_rules=(
            OpeningAccountRule("Cash", 22000, 50000),
            OpeningAccountRule("Accounts Receivable", 2400, 7200),
            OpeningAccountRule("Prepaid Insurance", 900, 3200, min_level=2),
            OpeningAccountRule("Equipment", 3000, 9000, min_level=4),
        ),
        liability_rules=(
            OpeningAccountRule("Accounts Payable", 1400, 4200),
            OpeningAccountRule("Accrued Expenses", 500, 2000, min_level=2),
            OpeningAccountRule("Security Deposits Payable", 1800, 5200, min_level=2),
            OpeningAccountRule("Loans Payable", 1500, 6800, min_level=4),
        ),
        equity_rules=(OpeningAccountRule("Retained Earnings", 2600, 9800, min_level=2),),
    )


SCENARIOS = {
    "rent_roll": make_rent_roll_scenario(
        name="rent_roll",
        description="Rent billing across occupied units.",
    ),
    "tenant_payment": make_receivable_settlement_scenario(
        name="tenant_payment",
        description="Tenant rent payment against the rent roll.",
    ),
    "security_deposit": make_security_deposit_scenario(
        name="security_deposit",
        description="Security deposit received from a tenant.",
    ),
    "security_deposit_refund": make_security_deposit_refund_scenario(
        name="security_deposit_refund",
        description="Security deposit refunded at move-out.",
    ),
    "maintenance_bill": make_vendor_bill_scenario(
        name="maintenance_bill",
        description="Maintenance or property service bill.",
        doc_type="vendor_invoice",
        debit_account="Maintenance Expense",
    ),
    "vendor_payment": make_payable_settlement_scenario(
        name="vendor_payment",
        description="Payment of a property-service vendor bill.",
    ),
    "payroll": make_payroll_scenario(
        name="payroll",
        description="Property-management payroll.",
    ),
    "prepaid_insurance": make_prepaid_insurance_scenario(
        name="prepaid_insurance",
        description="Property insurance prepaid and released over time.",
    ),
    "utilities_bill": make_utilities_bill_scenario(
        name="utilities_bill",
        description="Common-area utilities statement.",
    ),
    "loan_draw": make_loan_activity_scenario(
        name="loan_draw",
        description="Loan draw for property operations or equipment.",
        mode="draw",
    ),
    "loan_repayment": make_loan_activity_scenario(
        name="loan_repayment",
        description="Loan repayment during the period.",
        mode="repayment",
    ),
    "equipment_purchase": make_fixed_asset_purchase_scenario(
        name="equipment_purchase",
        description="Equipment purchase for building operations.",
    ),
    "depreciation": make_depreciation_scenario(
        name="depreciation",
        description="Depreciation for property-management equipment.",
    ),
}

MONTH_PLANS = {
    1: DifficultyPlan(mandatory=("rent_roll", "maintenance_bill"), optional=("rent_roll",)),
    2: DifficultyPlan(mandatory=("rent_roll", "maintenance_bill", "tenant_payment", "vendor_payment", "security_deposit"), optional=("rent_roll", "security_deposit")),
    3: DifficultyPlan(mandatory=("rent_roll", "maintenance_bill", "tenant_payment", "vendor_payment", "security_deposit", "payroll", "utilities_bill"), optional=("rent_roll", "maintenance_bill")),
    4: DifficultyPlan(mandatory=("rent_roll", "maintenance_bill", "tenant_payment", "vendor_payment", "security_deposit", "payroll", "utilities_bill", "prepaid_insurance", "loan_draw", "equipment_purchase", "depreciation"), optional=("rent_roll", "security_deposit", "maintenance_bill")),
    5: DifficultyPlan(mandatory=("rent_roll", "maintenance_bill", "tenant_payment", "vendor_payment", "security_deposit", "payroll", "utilities_bill", "prepaid_insurance", "loan_draw", "equipment_purchase", "depreciation", "loan_repayment"), optional=("rent_roll", "security_deposit", "tenant_payment")),
}
QUARTER_PLANS = {
    1: copy_plan(MONTH_PLANS[1]),
    2: copy_plan(MONTH_PLANS[2], "security_deposit_refund"),
    3: copy_plan(MONTH_PLANS[3], "security_deposit_refund"),
    4: copy_plan(MONTH_PLANS[4], "security_deposit_refund"),
    5: copy_plan(MONTH_PLANS[5], "security_deposit_refund"),
}
YEAR_PLANS = {
    1: copy_plan(QUARTER_PLANS[1]),
    2: copy_plan(QUARTER_PLANS[2]),
    3: copy_plan(QUARTER_PLANS[3]),
    4: copy_plan(QUARTER_PLANS[4], extra_optional=("rent_roll",)),
    5: copy_plan(QUARTER_PLANS[5], extra_optional=("maintenance_bill", "rent_roll")),
}


INDUSTRY_SCHEMA = IndustrySchema(
    name="property_management",
    display_name="Property Management",
    description="Property managers billing rent, collecting deposits, and paying vendors.",
    allowed_accounts=[
        "Cash",
        "Accounts Receivable",
        "Prepaid Insurance",
        "Equipment",
        "Accumulated Depreciation",
        "Accounts Payable",
        "Accrued Expenses",
        "Loans Payable",
        "Notes Payable",
        "Security Deposits Payable",
        "Owner's Equity",
        "Retained Earnings",
        "Rental Revenue",
        "Maintenance Expense",
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
