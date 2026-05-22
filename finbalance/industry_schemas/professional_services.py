"""Industry schema for professional services."""

from __future__ import annotations

from finbalance.generation.master_data import build_master_data
from finbalance.generation.scenario_factories import (
    make_bad_debt_review_scenario,
    make_asset_disposal_scenario,
    make_asset_disposal_with_deferred_tax_scenario,
    make_baseline_lease_scenario,
    make_deferral_invoice_scenario,
    make_deferral_release_scenario,
    make_deferred_tax_depreciation_scenario,
    make_depreciation_scenario,
    make_expense_accrual_scenario,
    make_expense_receipt_scenario,
    make_fixed_asset_purchase_scenario,
    make_fx_receivable_settlement_scenario,
    make_fx_remeasurement_scenario,
    make_fx_service_invoice_scenario,
    make_interbank_transfer_scenario,
    make_lease_modification_scenario,
    make_loan_activity_scenario,
    make_partial_multi_receivable_payment_scenario,
    make_payable_settlement_scenario,
    make_payroll_scenario,
    make_prepaid_insurance_scenario,
    make_prepaid_rent_scenario,
    make_reclassification_correction_scenario,
    make_receivable_settlement_scenario,
    make_reissued_invoice_scenario,
    make_service_invoice_scenario,
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
        scale_multiplier=opening_balance_scale("professional_services", period_spec, level),
        asset_rules=(
            OpeningAccountRule("Cash", 18000, 42000),
            OpeningAccountRule("Accounts Receivable", 1800, 6800),
            OpeningAccountRule("Prepaid Rent", 900, 3200, min_level=2),
            OpeningAccountRule("Prepaid Insurance", 500, 2400, min_level=2, min_period_rank=1),
            OpeningAccountRule("Office Supplies", 300, 1600, min_level=2),
            OpeningAccountRule("Equipment", 4200, 9800, min_level=4),
            OpeningAccountRule("Furniture", 2400, 7200, min_level=4, min_period_rank=1),
        ),
        liability_rules=(
            OpeningAccountRule("Accounts Payable", 900, 3600),
            OpeningAccountRule("Accrued Expenses", 400, 2100, min_level=2),
            OpeningAccountRule("Unearned Revenue", 900, 4200, min_level=3, min_period_rank=1),
            OpeningAccountRule("Loans Payable", 2000, 7200, min_level=4),
            OpeningAccountRule("Notes Payable", 1800, 5800, min_level=4, min_period_rank=1),
        ),
        equity_rules=(OpeningAccountRule("Retained Earnings", 2200, 11000, min_level=2),),
    )


SCENARIOS = {
    "service_invoice": make_service_invoice_scenario(
        name="service_invoice",
        description="Consulting or advisory invoice billed to a customer.",
        revenue_account="Service Revenue",
        apply_indirect_tax=True,
    ),
    "vendor_bill": make_vendor_bill_scenario(
        name="vendor_bill",
        description="Professional-services overhead bill on credit.",
        doc_type="vendor_invoice",
        debit_account="Office Supplies Expense",
        apply_indirect_tax=True,
    ),
    "expense_receipt": make_expense_receipt_scenario(
        name="expense_receipt",
        description="Small out-of-pocket business expense.",
        debit_account="Travel Expense",
    ),
    "customer_payment": make_receivable_settlement_scenario(
        name="customer_payment",
        description="Customer settles an open service invoice.",
    ),
    "multi_invoice_payment": make_partial_multi_receivable_payment_scenario(
        name="multi_invoice_payment",
        description="One customer payment settles several invoices and only partly closes one of them.",
        revenue_account="Service Revenue",
    ),
    "supplier_payment": make_payable_settlement_scenario(
        name="supplier_payment",
        description="Business pays an open vendor bill.",
    ),
    "payroll": make_payroll_scenario(
        name="payroll",
        description="Payroll run for the period.",
    ),
    "prepaid_rent": make_prepaid_rent_scenario(
        name="prepaid_rent",
        description="Rent paid in advance and partly expensed by period end.",
    ),
    "prepaid_insurance": make_prepaid_insurance_scenario(
        name="prepaid_insurance",
        description="Insurance premium paid in advance and partly expensed.",
    ),
    "retainer_invoice": make_deferral_invoice_scenario(
        name="retainer_invoice",
        description="Client retainer billed ahead of service delivery.",
        support_doc_type="retainer_agreement_memo",
        revenue_account="Service Revenue",
        apply_indirect_tax=True,
    ),
    "retainer_release": make_deferral_release_scenario(
        name="retainer_release",
        description="Release earned value from unearned revenue.",
        revenue_account="Service Revenue",
    ),
    "utilities_bill": make_utilities_bill_scenario(
        name="utilities_bill",
        description="Office utility bill for the period.",
    ),
    "expense_accrual": make_expense_accrual_scenario(
        name="expense_accrual",
        description="Month-end accrual for unpaid office spend.",
        expense_account="Utilities Expense",
    ),
    "bad_debt_review": make_bad_debt_review_scenario(
        name="bad_debt_review",
        description="Receivable aging review with a partial writeoff.",
    ),
    "reclassification_correction": make_reclassification_correction_scenario(
        name="reclassification_correction",
        description="Expense initially coded to office supplies is corrected into travel expense.",
        from_account="Office Supplies Expense",
        to_account="Travel Expense",
    ),
    "reissued_invoice": make_reissued_invoice_scenario(
        name="reissued_invoice",
        description="Earlier billing reference is withdrawn and replaced by a corrected invoice.",
        revenue_account="Service Revenue",
    ),
    "fx_service_invoice": make_fx_service_invoice_scenario(
        name="fx_service_invoice",
        description="Foreign-currency client invoice translated into functional currency at the spot rate.",
        revenue_account="Service Revenue",
    ),
    "fx_customer_payment": make_fx_receivable_settlement_scenario(
        name="fx_customer_payment",
        description="Later settlement of a foreign-currency client invoice with an FX gain or loss.",
    ),
    "fx_remeasurement": make_fx_remeasurement_scenario(
        name="fx_remeasurement",
        description="Open foreign-currency receivable remeasured at the closing rate.",
        target="receivable",
    ),
    "interbank_transfer": make_interbank_transfer_scenario(
        name="interbank_transfer",
        description="Treasury transfer between the operating account and reserve account.",
    ),
    "loan_draw": make_loan_activity_scenario(
        name="loan_draw",
        description="Loan draw used to support business cash needs.",
        mode="draw",
    ),
    "loan_repayment": make_loan_activity_scenario(
        name="loan_repayment",
        description="Loan principal and interest paid during the period.",
        mode="repayment",
    ),
    "equipment_purchase": make_fixed_asset_purchase_scenario(
        name="equipment_purchase",
        description="Office equipment bought partly with financing.",
    ),
    "depreciation": make_depreciation_scenario(
        name="depreciation",
        description="Depreciation on office equipment.",
    ),
    "asset_disposal": make_asset_disposal_scenario(
        name="asset_disposal",
        description="Fixed asset disposal with NBV and gain or loss computation.",
    ),
    "deferred_tax_depreciation": make_deferred_tax_depreciation_scenario(
        name="deferred_tax_depreciation",
        description="Deferred tax movement from book versus tax depreciation.",
    ),
    "baseline_lease": make_baseline_lease_scenario(
        name="baseline_lease",
        description="Baseline lease recognition with ROU asset, liability, interest, principal, and amortization.",
    ),
    "lease_modification": make_lease_modification_scenario(
        name="lease_modification",
        description="Lease liability remeasurement with equal ROU asset adjustment.",
    ),
    "asset_disposal_with_deferred_tax": make_asset_disposal_with_deferred_tax_scenario(
        name="asset_disposal_with_deferred_tax",
        description="Deferred tax effect layered onto an asset disposal.",
    ),
}

MONTH_PLANS = {
    1: DifficultyPlan(mandatory=("service_invoice", "vendor_bill", "expense_receipt"), optional=("service_invoice", "expense_receipt")),
    2: DifficultyPlan(mandatory=("service_invoice", "vendor_bill", "expense_receipt", "customer_payment", "supplier_payment"), optional=("service_invoice", "vendor_bill")),
    3: DifficultyPlan(mandatory=("service_invoice", "vendor_bill", "expense_receipt", "customer_payment", "supplier_payment", "payroll", "prepaid_rent"), optional=("service_invoice", "expense_receipt", "multi_invoice_payment")),
    4: DifficultyPlan(mandatory=("service_invoice", "vendor_bill", "expense_receipt", "customer_payment", "supplier_payment", "payroll", "prepaid_rent", "utilities_bill", "loan_draw", "equipment_purchase", "depreciation", "asset_disposal", "baseline_lease", "interbank_transfer"), optional=("service_invoice", "vendor_bill", "expense_receipt", "reclassification_correction", "reissued_invoice")),
    5: DifficultyPlan(mandatory=("service_invoice", "vendor_bill", "expense_receipt", "customer_payment", "supplier_payment", "payroll", "prepaid_rent", "prepaid_insurance", "utilities_bill", "loan_draw", "equipment_purchase", "depreciation", "asset_disposal", "deferred_tax_depreciation", "asset_disposal_with_deferred_tax", "baseline_lease", "lease_modification", "loan_repayment", "interbank_transfer"), optional=("service_invoice", "vendor_bill", "expense_receipt", "customer_payment", "multi_invoice_payment", "reclassification_correction", "reissued_invoice")),
}

QUARTER_PLANS = {
    1: copy_plan(MONTH_PLANS[1]),
    2: copy_plan(MONTH_PLANS[2], "retainer_invoice"),
    3: copy_plan(MONTH_PLANS[3], "retainer_invoice", "retainer_release", "multi_invoice_payment", "reclassification_correction", extra_optional=("prepaid_insurance",)),
    4: copy_plan(MONTH_PLANS[4], "retainer_invoice", "retainer_release", "expense_accrual", "reissued_invoice", extra_optional=("prepaid_insurance", "utilities_bill")),
    5: copy_plan(MONTH_PLANS[5], "retainer_invoice", "retainer_release", "expense_accrual", "bad_debt_review", "reissued_invoice", "fx_service_invoice", "fx_customer_payment", extra_optional=("prepaid_insurance", "service_invoice", "multi_invoice_payment")),
}

YEAR_PLANS = {
    1: copy_plan(QUARTER_PLANS[1]),
    2: copy_plan(QUARTER_PLANS[2], extra_optional=("retainer_release",)),
    3: copy_plan(QUARTER_PLANS[3], "expense_accrual"),
    4: copy_plan(QUARTER_PLANS[4], "bad_debt_review"),
    5: DifficultyPlan(
        mandatory=(
            "service_invoice",
            "vendor_bill",
            "expense_receipt",
            "customer_payment",
            "supplier_payment",
            "payroll",
            "prepaid_rent",
            "prepaid_insurance",
            "utilities_bill",
            "loan_draw",
            "equipment_purchase",
            "depreciation",
            "asset_disposal",
            "deferred_tax_depreciation",
            "asset_disposal_with_deferred_tax",
            "baseline_lease",
            "lease_modification",
            "loan_repayment",
            "interbank_transfer",
            "retainer_invoice",
            "retainer_release",
            "expense_accrual",
            "bad_debt_review",
            "reissued_invoice",
            "fx_service_invoice",
            "fx_remeasurement",
        ),
        optional=("service_invoice", "multi_invoice_payment", "reclassification_correction"),
    ),
}


INDUSTRY_SCHEMA = IndustrySchema(
    name="professional_services",
    display_name="Professional Services",
    description="Firms that mainly bill for services and carry light overhead.",
    allowed_accounts=[
        "Cash",
        "Reserve Cash",
        "Accounts Receivable",
        "Prepaid Rent",
        "Prepaid Insurance",
        "Office Supplies",
        "Equipment",
        "Furniture",
        "Accumulated Depreciation",
        "Right-of-Use Asset",
        "Accounts Payable",
        "Accrued Expenses",
        "Input Tax Receivable",
        "Input CGST Receivable",
        "Input SGST Receivable",
        "Input IGST Receivable",
        "Loans Payable",
        "Notes Payable",
        "Sales Tax Payable",
        "CGST Payable",
        "SGST Payable",
        "IGST Payable",
        "Deferred Tax Liability",
        "Lease Liability",
        "Unearned Revenue",
        "Owner's Equity",
        "Retained Earnings",
        "Service Revenue",
        "Rent Expense",
        "Insurance Expense",
        "Office Supplies Expense",
        "Travel Expense",
        "Utilities Expense",
        "Bad Debt Expense",
        "Salaries Expense",
        "Payroll Tax Expense",
        "Depreciation Expense",
        "Deferred Tax Expense",
        "Interest Expense",
        "Lease Interest Expense",
        "Lease Amortization Expense",
        "Gain on Disposal",
        "Loss on Disposal",
        "Foreign Exchange Gain",
        "Foreign Exchange Loss",
    ],
    opening_builder=_opening_balance,
    master_data_builder=build_master_data,
    scenarios=SCENARIOS,
    period_plans={"month": MONTH_PLANS, "quarter": QUARTER_PLANS, "year": YEAR_PLANS},
    distractor_doc_types=("secondary_copy", "vendor_statement", "memo", "cancellation_note"),
)
