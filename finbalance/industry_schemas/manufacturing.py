"""Industry schema for manufacturing businesses."""

from __future__ import annotations

from finbalance.generation.master_data import build_master_data
from finbalance.generation.scenario_factories import (
    make_depreciation_scenario,
    make_finished_goods_transfer_scenario,
    make_fx_payable_settlement_scenario,
    make_fx_remeasurement_scenario,
    make_fx_vendor_bill_scenario,
    make_interbank_transfer_scenario,
    make_loan_activity_scenario,
    make_manufacturing_sale_scenario,
    make_material_issue_scenario,
    make_material_purchase_scenario,
    make_partial_multi_receivable_payment_scenario,
    make_payable_settlement_scenario,
    make_payroll_scenario,
    make_receivable_settlement_scenario,
    make_reissued_invoice_scenario,
    make_scrap_report_scenario,
    make_wip_cost_scenario,
)
from finbalance.industry_schemas.common import OpeningAccountRule, build_opening_balance, copy_plan, opening_balance_scale
from finbalance.types import DifficultyPlan, IndustrySchema


def _opening_balance(rng, level, period_spec):
    return build_opening_balance(
        rng,
        level,
        period_spec,
        scale_multiplier=opening_balance_scale("manufacturing", period_spec, level),
        asset_rules=(
            OpeningAccountRule("Cash", 32000, 76000),
            OpeningAccountRule("Raw Materials Inventory", 12000, 28000),
            OpeningAccountRule("Work In Process", 6000, 20000, min_level=2),
            OpeningAccountRule("Finished Goods Inventory", 8000, 24000, min_level=2),
            OpeningAccountRule("Accounts Receivable", 3000, 9200, min_level=3),
            OpeningAccountRule("Equipment", 12000, 36000, min_level=4),
        ),
        liability_rules=(
            OpeningAccountRule("Accounts Payable", 5000, 14000),
            OpeningAccountRule("Accrued Expenses", 1200, 3600, min_level=2),
            OpeningAccountRule("Notes Payable", 4000, 12000, min_level=4),
            OpeningAccountRule("Loans Payable", 5000, 18000, min_level=4, min_period_rank=1),
        ),
        equity_rules=(OpeningAccountRule("Retained Earnings", 6000, 18000, min_level=2),),
        residual_equity_account="Share Capital",
    )


SCENARIOS = {
    "raw_material_purchase": make_material_purchase_scenario(
        name="raw_material_purchase",
        description="Raw materials purchased for production.",
        apply_indirect_tax=True,
    ),
    "material_issue": make_material_issue_scenario(
        name="material_issue",
        description="Raw materials moved into production.",
    ),
    "direct_labor": make_wip_cost_scenario(
        name="direct_labor",
        description="Direct labor charged into work in process.",
        source="labor",
    ),
    "overhead_accrual": make_wip_cost_scenario(
        name="overhead_accrual",
        description="Factory overhead accrued into work in process.",
        source="overhead",
    ),
    "finished_goods_transfer": make_finished_goods_transfer_scenario(
        name="finished_goods_transfer",
        description="Completed production transferred into finished goods.",
    ),
    "finished_goods_sale": make_manufacturing_sale_scenario(
        name="finished_goods_sale",
        description="Finished goods sold to a customer.",
        apply_indirect_tax=True,
    ),
    "fx_material_purchase": make_fx_vendor_bill_scenario(
        name="fx_material_purchase",
        description="Imported raw-material bill denominated in a foreign currency.",
        debit_account="Raw Materials Inventory",
        doc_type="supplier_invoice",
    ),
    "fx_supplier_payment": make_fx_payable_settlement_scenario(
        name="fx_supplier_payment",
        description="Settlement of an imported-material bill with an FX gain or loss.",
    ),
    "fx_remeasurement": make_fx_remeasurement_scenario(
        name="fx_remeasurement",
        description="Open foreign-currency supplier payable remeasured at the closing rate.",
        target="payable",
    ),
    "customer_payment": make_receivable_settlement_scenario(
        name="customer_payment",
        description="Customer settles an open finished-goods invoice.",
    ),
    "multi_invoice_payment": make_partial_multi_receivable_payment_scenario(
        name="multi_invoice_payment",
        description="One customer payment settles several finished-goods invoices and only partly closes one of them.",
        revenue_account="Sales Revenue",
    ),
    "supplier_payment": make_payable_settlement_scenario(
        name="supplier_payment",
        description="Business pays for raw materials or plant services.",
    ),
    "payroll": make_payroll_scenario(
        name="payroll",
        description="Plant payroll run.",
    ),
    "loan_draw": make_loan_activity_scenario(
        name="loan_draw",
        description="Loan draw for plant equipment or working capital.",
        mode="draw",
    ),
    "loan_repayment": make_loan_activity_scenario(
        name="loan_repayment",
        description="Loan repayment for plant financing.",
        mode="repayment",
    ),
    "depreciation": make_depreciation_scenario(
        name="depreciation",
        description="Depreciation on factory equipment.",
    ),
    "scrap_report": make_scrap_report_scenario(
        name="scrap_report",
        description="Scrap or write-down adjustment on production output.",
    ),
    "reissued_invoice": make_reissued_invoice_scenario(
        name="reissued_invoice",
        description="Earlier shipping invoice is replaced by a corrected billing reference.",
        revenue_account="Sales Revenue",
    ),
    "interbank_transfer": make_interbank_transfer_scenario(
        name="interbank_transfer",
        description="Treasury transfer between the operating account and reserve account.",
    ),
}

MONTH_PLANS = {
    1: DifficultyPlan(mandatory=("raw_material_purchase", "material_issue", "finished_goods_transfer", "finished_goods_sale"), optional=("raw_material_purchase",)),
    2: DifficultyPlan(mandatory=("raw_material_purchase", "material_issue", "direct_labor", "finished_goods_transfer", "finished_goods_sale", "customer_payment", "supplier_payment"), optional=("raw_material_purchase", "finished_goods_sale")),
    3: DifficultyPlan(mandatory=("raw_material_purchase", "material_issue", "direct_labor", "overhead_accrual", "finished_goods_transfer", "finished_goods_sale", "customer_payment", "supplier_payment", "payroll"), optional=("raw_material_purchase", "finished_goods_sale")),
    4: DifficultyPlan(mandatory=("raw_material_purchase", "material_issue", "direct_labor", "overhead_accrual", "finished_goods_transfer", "finished_goods_sale", "customer_payment", "supplier_payment", "payroll", "loan_draw", "depreciation", "interbank_transfer"), optional=("raw_material_purchase", "material_issue", "multi_invoice_payment")),
    5: DifficultyPlan(mandatory=("raw_material_purchase", "material_issue", "direct_labor", "overhead_accrual", "finished_goods_transfer", "finished_goods_sale", "customer_payment", "supplier_payment", "payroll", "loan_draw", "depreciation", "loan_repayment", "interbank_transfer"), optional=("raw_material_purchase", "finished_goods_sale", "multi_invoice_payment", "reissued_invoice")),
}
QUARTER_PLANS = {
    1: copy_plan(MONTH_PLANS[1]),
    2: copy_plan(MONTH_PLANS[2]),
    3: copy_plan(MONTH_PLANS[3], "scrap_report"),
    4: copy_plan(MONTH_PLANS[4], "scrap_report"),
    5: copy_plan(MONTH_PLANS[5], "scrap_report", "fx_material_purchase", "fx_supplier_payment"),
}
YEAR_PLANS = {
    1: copy_plan(QUARTER_PLANS[1]),
    2: copy_plan(QUARTER_PLANS[2]),
    3: copy_plan(QUARTER_PLANS[3]),
    4: copy_plan(QUARTER_PLANS[4], extra_optional=("finished_goods_sale",)),
    5: DifficultyPlan(
        mandatory=(
            "raw_material_purchase",
            "material_issue",
            "direct_labor",
            "overhead_accrual",
            "finished_goods_transfer",
            "finished_goods_sale",
            "customer_payment",
            "supplier_payment",
            "payroll",
            "loan_draw",
            "depreciation",
            "loan_repayment",
            "interbank_transfer",
            "scrap_report",
            "fx_material_purchase",
            "fx_remeasurement",
        ),
        optional=("finished_goods_sale", "multi_invoice_payment", "reissued_invoice"),
    ),
}


INDUSTRY_SCHEMA = IndustrySchema(
    name="manufacturing",
    display_name="Manufacturing",
    description="Businesses that convert raw materials into finished goods before sale.",
    allowed_accounts=[
        "Cash",
        "Reserve Cash",
        "Accounts Receivable",
        "Raw Materials Inventory",
        "Work In Process",
        "Finished Goods Inventory",
        "Equipment",
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
        "Share Capital",
        "Retained Earnings",
        "Sales Revenue",
        "Cost of Goods Sold",
        "Inventory Shrinkage Expense",
        "Salaries Expense",
        "Payroll Tax Expense",
        "Depreciation Expense",
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
