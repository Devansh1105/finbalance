"""Industry schema for retail businesses."""

from __future__ import annotations

from docs_benchmark.generation.master_data import build_master_data
from docs_benchmark.generation.scenario_factories import (
    make_card_settlement_scenario,
    make_depreciation_scenario,
    make_fixed_asset_purchase_scenario,
    make_inventory_adjustment_scenario,
    make_loan_activity_scenario,
    make_payable_settlement_scenario,
    make_payroll_scenario,
    make_retail_sale_scenario,
    make_return_scenario,
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
        scale_multiplier=opening_balance_scale("retail", period_spec, level),
        asset_rules=(
            OpeningAccountRule("Cash", 14000, 36000),
            OpeningAccountRule("Inventory", 9000, 24000),
            OpeningAccountRule("Card Settlement Clearing", 400, 2200, min_level=2),
            OpeningAccountRule("Store Fixtures", 3500, 9800, min_level=4),
            OpeningAccountRule("Office Supplies", 300, 1300, min_level=2),
        ),
        liability_rules=(
            OpeningAccountRule("Accounts Payable", 2400, 6400),
            OpeningAccountRule("Unearned Revenue", 900, 3600, min_level=3, min_period_rank=1),
            OpeningAccountRule("Accrued Expenses", 500, 1800, min_level=2),
            OpeningAccountRule("Loans Payable", 1600, 7200, min_level=4),
        ),
        equity_rules=(OpeningAccountRule("Retained Earnings", 2600, 9800, min_level=2),),
    )


SCENARIOS = {
    "inventory_purchase": make_vendor_bill_scenario(
        name="inventory_purchase",
        description="Supplier invoice for store stock.",
        doc_type="supplier_invoice",
        debit_account="Inventory",
        quantity_lines=True,
    ),
    "retail_sale": make_retail_sale_scenario(
        name="retail_sale",
        description="Sales summary and POS batch for the period.",
    ),
    "card_settlement": make_card_settlement_scenario(
        name="card_settlement",
        description="Processor settles open card batches into cash.",
    ),
    "supplier_payment": make_payable_settlement_scenario(
        name="supplier_payment",
        description="Store pays an inventory supplier invoice.",
    ),
    "payroll": make_payroll_scenario(
        name="payroll",
        description="Retail payroll run.",
    ),
    "stock_adjustment": make_inventory_adjustment_scenario(
        name="stock_adjustment",
        description="Physical stock count and shrinkage adjustment.",
    ),
    "utilities_bill": make_utilities_bill_scenario(
        name="utilities_bill",
        description="Store utilities bill.",
    ),
    "loan_draw": make_loan_activity_scenario(
        name="loan_draw",
        description="Retail loan draw for equipment or fit-out.",
        mode="draw",
    ),
    "loan_repayment": make_loan_activity_scenario(
        name="loan_repayment",
        description="Retail loan repayment.",
        mode="repayment",
    ),
    "equipment_purchase": make_fixed_asset_purchase_scenario(
        name="equipment_purchase",
        description="Retail fixtures or equipment purchase.",
        asset_account="Store Fixtures",
    ),
    "depreciation": make_depreciation_scenario(
        name="depreciation",
        description="Depreciation for store fixtures.",
    ),
    "return": make_return_scenario(
        name="return",
        description="Customer return against an earlier sale.",
    ),
}

MONTH_PLANS = {
    1: DifficultyPlan(mandatory=("inventory_purchase", "retail_sale"), optional=("retail_sale",)),
    2: DifficultyPlan(mandatory=("inventory_purchase", "retail_sale", "card_settlement", "supplier_payment"), optional=("retail_sale", "inventory_purchase")),
    3: DifficultyPlan(mandatory=("inventory_purchase", "retail_sale", "card_settlement", "supplier_payment", "payroll", "stock_adjustment"), optional=("retail_sale", "stock_adjustment")),
    4: DifficultyPlan(mandatory=("inventory_purchase", "retail_sale", "card_settlement", "supplier_payment", "payroll", "stock_adjustment", "utilities_bill", "loan_draw", "equipment_purchase", "depreciation"), optional=("retail_sale", "inventory_purchase", "stock_adjustment")),
    5: DifficultyPlan(mandatory=("inventory_purchase", "retail_sale", "card_settlement", "supplier_payment", "payroll", "stock_adjustment", "utilities_bill", "loan_draw", "equipment_purchase", "depreciation", "loan_repayment", "return"), optional=("retail_sale", "stock_adjustment", "return")),
}
QUARTER_PLANS = {
    1: copy_plan(MONTH_PLANS[1]),
    2: copy_plan(MONTH_PLANS[2], extra_optional=("utilities_bill",)),
    3: copy_plan(MONTH_PLANS[3], "utilities_bill"),
    4: copy_plan(MONTH_PLANS[4]),
    5: copy_plan(MONTH_PLANS[5], extra_optional=("return",)),
}
YEAR_PLANS = {
    1: copy_plan(QUARTER_PLANS[1]),
    2: copy_plan(QUARTER_PLANS[2]),
    3: copy_plan(QUARTER_PLANS[3]),
    4: copy_plan(QUARTER_PLANS[4], extra_optional=("retail_sale",)),
    5: copy_plan(QUARTER_PLANS[5], extra_optional=("retail_sale",)),
}


INDUSTRY_SCHEMA = IndustrySchema(
    name="retail",
    display_name="Retail",
    description="Store operations with stock, card settlement, and shrinkage.",
    allowed_accounts=[
        "Cash",
        "Inventory",
        "Card Settlement Clearing",
        "Store Fixtures",
        "Office Supplies",
        "Accumulated Depreciation",
        "Accounts Payable",
        "Accrued Expenses",
        "Loans Payable",
        "Notes Payable",
        "Unearned Revenue",
        "Owner's Equity",
        "Retained Earnings",
        "Sales Revenue",
        "Cost of Goods Sold",
        "Maintenance Expense",
        "Utilities Expense",
        "Inventory Shrinkage Expense",
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
