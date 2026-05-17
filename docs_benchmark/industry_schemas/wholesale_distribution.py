"""Industry schema for wholesale and distribution businesses."""

from __future__ import annotations

from docs_benchmark.generation.master_data import build_master_data
from docs_benchmark.generation.scenario_factories import (
    make_bad_debt_review_scenario,
    make_depreciation_scenario,
    make_delivery_sale_scenario,
    make_fixed_asset_purchase_scenario,
    make_goods_receipt_purchase_scenario,
    make_inventory_adjustment_scenario,
    make_jurisdictional_tax_invoice_scenario,
    make_loan_activity_scenario,
    make_payable_settlement_scenario,
    make_payroll_scenario,
    make_receivable_settlement_scenario,
    make_utilities_bill_scenario,
)
from docs_benchmark.industry_schemas.common import OpeningAccountRule, build_opening_balance, copy_plan, opening_balance_scale
from docs_benchmark.types import DifficultyPlan, IndustrySchema


def _opening_balance(rng, level, period_spec):
    return build_opening_balance(
        rng,
        level,
        period_spec,
        scale_multiplier=opening_balance_scale("wholesale_distribution", period_spec, level),
        asset_rules=(
            OpeningAccountRule("Cash", 26000, 62000),
            OpeningAccountRule("Inventory", 16000, 42000),
            OpeningAccountRule("Accounts Receivable", 3000, 8400),
            OpeningAccountRule("Office Supplies", 500, 1800, min_level=2),
            OpeningAccountRule("Equipment", 5200, 15600, min_level=4),
        ),
        liability_rules=(
            OpeningAccountRule("Accounts Payable", 4000, 10800),
            OpeningAccountRule("Accrued Expenses", 700, 2600, min_level=2),
            OpeningAccountRule("Loans Payable", 2800, 9800, min_level=4),
            OpeningAccountRule("Notes Payable", 2200, 7800, min_level=4, min_period_rank=1),
        ),
        equity_rules=(OpeningAccountRule("Retained Earnings", 3600, 14000, min_level=2),),
    )


SCENARIOS = {
    "goods_receipt_purchase": make_goods_receipt_purchase_scenario(
        name="goods_receipt_purchase",
        description="Warehouse receives stock and supplier invoice arrives.",
        apply_indirect_tax=True,
    ),
    "delivery_sale": make_delivery_sale_scenario(
        name="delivery_sale",
        description="Goods are shipped to a customer and invoiced.",
        apply_indirect_tax=True,
    ),
    "customer_payment": make_receivable_settlement_scenario(
        name="customer_payment",
        description="Customer settles a distribution invoice.",
    ),
    "supplier_payment": make_payable_settlement_scenario(
        name="supplier_payment",
        description="Business pays a supplier for stock received.",
    ),
    "inventory_adjustment": make_inventory_adjustment_scenario(
        name="inventory_adjustment",
        description="Warehouse count and stock adjustment.",
    ),
    "utilities_bill": make_utilities_bill_scenario(
        name="utilities_bill",
        description="Warehouse utilities bill.",
    ),
    "payroll": make_payroll_scenario(
        name="payroll",
        description="Warehouse and office payroll.",
    ),
    "bad_debt_review": make_bad_debt_review_scenario(
        name="bad_debt_review",
        description="AR aging review with a partial writeoff.",
    ),
    "loan_draw": make_loan_activity_scenario(
        name="loan_draw",
        description="Working-capital or equipment loan draw.",
        mode="draw",
    ),
    "loan_repayment": make_loan_activity_scenario(
        name="loan_repayment",
        description="Repayment of outstanding loan principal and interest.",
        mode="repayment",
    ),
    "equipment_purchase": make_fixed_asset_purchase_scenario(
        name="equipment_purchase",
        description="Warehouse equipment purchased.",
    ),
    "depreciation": make_depreciation_scenario(
        name="depreciation",
        description="Depreciation on warehouse equipment.",
    ),
    "jurisdictional_tax_invoice": make_jurisdictional_tax_invoice_scenario(
        name="jurisdictional_tax_invoice",
        description="Jurisdictional tax packet with US sales tax, India GST split/input credit, and exemption override evidence.",
    ),
}

MONTH_PLANS = {
    1: DifficultyPlan(mandatory=("goods_receipt_purchase", "delivery_sale"), optional=("delivery_sale",)),
    2: DifficultyPlan(mandatory=("goods_receipt_purchase", "delivery_sale", "customer_payment", "supplier_payment"), optional=("delivery_sale", "goods_receipt_purchase")),
    3: DifficultyPlan(mandatory=("goods_receipt_purchase", "delivery_sale", "customer_payment", "supplier_payment", "inventory_adjustment", "payroll"), optional=("delivery_sale", "inventory_adjustment")),
    4: DifficultyPlan(mandatory=("goods_receipt_purchase", "delivery_sale", "customer_payment", "supplier_payment", "inventory_adjustment", "payroll", "utilities_bill", "loan_draw", "equipment_purchase", "depreciation", "jurisdictional_tax_invoice"), optional=("delivery_sale", "goods_receipt_purchase")),
    5: DifficultyPlan(mandatory=("goods_receipt_purchase", "delivery_sale", "customer_payment", "supplier_payment", "inventory_adjustment", "payroll", "utilities_bill", "loan_draw", "equipment_purchase", "depreciation", "jurisdictional_tax_invoice", "loan_repayment"), optional=("delivery_sale", "goods_receipt_purchase", "inventory_adjustment")),
}
QUARTER_PLANS = {
    1: copy_plan(MONTH_PLANS[1]),
    2: copy_plan(MONTH_PLANS[2]),
    3: copy_plan(MONTH_PLANS[3], "utilities_bill"),
    4: copy_plan(MONTH_PLANS[4], "bad_debt_review"),
    5: copy_plan(MONTH_PLANS[5], "bad_debt_review"),
}
YEAR_PLANS = {
    1: copy_plan(QUARTER_PLANS[1]),
    2: copy_plan(QUARTER_PLANS[2]),
    3: copy_plan(QUARTER_PLANS[3]),
    4: copy_plan(QUARTER_PLANS[4], extra_optional=("delivery_sale",)),
    5: copy_plan(QUARTER_PLANS[5], extra_optional=("delivery_sale", "inventory_adjustment")),
}


INDUSTRY_SCHEMA = IndustrySchema(
    name="wholesale_distribution",
    display_name="Wholesale Distribution",
    description="Businesses that buy, hold, ship, and invoice inventory in larger lots.",
    allowed_accounts=[
        "Cash",
        "Accounts Receivable",
        "Inventory",
        "Equipment",
        "Office Supplies",
        "Input Tax Receivable",
        "Input CGST Receivable",
        "Input SGST Receivable",
        "Input IGST Receivable",
        "Accumulated Depreciation",
        "Accounts Payable",
        "Accrued Expenses",
        "Loans Payable",
        "Notes Payable",
        "Sales Tax Payable",
        "CGST Payable",
        "SGST Payable",
        "IGST Payable",
        "Owner's Equity",
        "Retained Earnings",
        "Sales Revenue",
        "Cost of Goods Sold",
        "Bad Debt Expense",
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
