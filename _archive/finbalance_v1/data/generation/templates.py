"""
Transaction type templates for each difficulty level.

Each template defines:
  - tx_type:     identifier string
  - description: human-readable label (formatted with amount)
  - debit:       account to debit
  - credit:      account to credit
  - amount_range: (min, max) in round hundreds
  - complexity_factors: tags for metadata
  - requires:    list of (account, min_balance) needed before this tx is valid
  - levels:      which difficulty levels include this type
"""

TX_TEMPLATES = [
    # ── Level 1: pure cash ────────────────────────────────────────────────
    {
        "tx_type": "owner_investment",
        "description": "Owner invested cash",
        "debit": "Cash",
        "credit": "Owner's Equity",
        "amount_range": (5_000, 50_000),
        "complexity_factors": [],
        "requires": [],
        "levels": {1, 2, 3, 4, 5},
    },
    {
        "tx_type": "cash_purchase_equipment",
        "description": "Purchased equipment for cash",
        "debit": "Equipment",
        "credit": "Cash",
        "amount_range": (1_000, 20_000),
        "complexity_factors": ["depreciable_asset"],
        "requires": [("Cash", 1_000)],
        "levels": {1, 2, 3, 4, 5},
    },
    {
        "tx_type": "cash_purchase_inventory",
        "description": "Purchased inventory for cash",
        "debit": "Inventory",
        "credit": "Cash",
        "amount_range": (500, 10_000),
        "complexity_factors": [],
        "requires": [("Cash", 500)],
        "levels": {1, 2, 3, 4, 5},
    },
    {
        "tx_type": "cash_sale",
        "description": "Cash sale of goods",
        "debit": "Cash",
        "credit": "Revenue",
        "amount_range": (500, 15_000),
        "complexity_factors": [],
        "requires": [],
        "levels": {1, 2, 3, 4, 5},
    },
    {
        "tx_type": "cash_expense",
        "description": "Paid operating expenses in cash",
        "debit": "Operating Expenses",
        "credit": "Cash",
        "amount_range": (200, 5_000),
        "complexity_factors": [],
        "requires": [("Cash", 200)],
        "levels": {1, 2, 3, 4, 5},
    },
    {
        "tx_type": "prepaid_rent",
        "description": "Paid rent in advance",
        "debit": "Prepaid Rent",
        "credit": "Cash",
        "amount_range": (1_000, 6_000),
        "complexity_factors": ["prepaid"],
        "requires": [("Cash", 1_000)],
        "levels": {1, 2, 3, 4, 5},
    },

    # ── Level 2: credit transactions ──────────────────────────────────────
    {
        "tx_type": "bank_loan",
        "description": "Received bank loan",
        "debit": "Cash",
        "credit": "Loans Payable",
        "amount_range": (5_000, 100_000),
        "complexity_factors": ["debt"],
        "requires": [],
        "levels": {2, 3, 4, 5},
    },
    {
        "tx_type": "credit_purchase_inventory",
        "description": "Purchased inventory on credit",
        "debit": "Inventory",
        "credit": "Accounts Payable",
        "amount_range": (500, 15_000),
        "complexity_factors": ["credit_transaction"],
        "requires": [],
        "levels": {2, 3, 4, 5},
    },
    {
        "tx_type": "credit_sale",
        "description": "Sold goods on credit",
        "debit": "Accounts Receivable",
        "credit": "Revenue",
        "amount_range": (500, 20_000),
        "complexity_factors": ["credit_transaction"],
        "requires": [],
        "levels": {2, 3, 4, 5},
    },
    {
        "tx_type": "collect_receivable",
        "description": "Collected cash from accounts receivable",
        "debit": "Cash",
        "credit": "Accounts Receivable",
        "amount_range": (200, 15_000),
        "complexity_factors": [],
        "requires": [("Accounts Receivable", 200)],
        "levels": {2, 3, 4, 5},
    },
    {
        "tx_type": "pay_payable",
        "description": "Paid accounts payable in cash",
        "debit": "Accounts Payable",
        "credit": "Cash",
        "amount_range": (200, 10_000),
        "complexity_factors": [],
        "requires": [("Accounts Payable", 200), ("Cash", 200)],
        "levels": {2, 3, 4, 5},
    },
    {
        "tx_type": "pay_loan_principal",
        "description": "Repaid portion of bank loan",
        "debit": "Loans Payable",
        "credit": "Cash",
        "amount_range": (500, 10_000),
        "complexity_factors": ["debt"],
        "requires": [("Loans Payable", 500), ("Cash", 500)],
        "levels": {2, 3, 4, 5},
    },
    {
        "tx_type": "prepaid_insurance",
        "description": "Purchased prepaid insurance",
        "debit": "Prepaid Insurance",
        "credit": "Cash",
        "amount_range": (500, 5_000),
        "complexity_factors": ["prepaid"],
        "requires": [("Cash", 500)],
        "levels": {2, 3, 4, 5},
    },

    # ── Level 3: adjustments-related transactions ─────────────────────────
    {
        "tx_type": "cash_purchase_furniture",
        "description": "Purchased furniture for cash",
        "debit": "Furniture",
        "credit": "Cash",
        "amount_range": (1_000, 15_000),
        "complexity_factors": ["depreciable_asset"],
        "requires": [("Cash", 1_000)],
        "levels": {3, 4, 5},
    },
    {
        "tx_type": "cash_purchase_vehicles",
        "description": "Purchased vehicle for cash",
        "debit": "Vehicles",
        "credit": "Cash",
        "amount_range": (5_000, 50_000),
        "complexity_factors": ["depreciable_asset"],
        "requires": [("Cash", 5_000)],
        "levels": {3, 4, 5},
    },
    {
        "tx_type": "salaries_expense",
        "description": "Paid salaries in cash",
        "debit": "Salaries Expense",
        "credit": "Cash",
        "amount_range": (2_000, 20_000),
        "complexity_factors": [],
        "requires": [("Cash", 2_000)],
        "levels": {3, 4, 5},
    },
    {
        "tx_type": "utilities_expense",
        "description": "Paid utilities in cash",
        "debit": "Utilities Expense",
        "credit": "Cash",
        "amount_range": (100, 2_000),
        "complexity_factors": [],
        "requires": [("Cash", 100)],
        "levels": {3, 4, 5},
    },
    {
        "tx_type": "interest_expense",
        "description": "Paid interest on loan in cash",
        "debit": "Interest Expense",
        "credit": "Cash",
        "amount_range": (100, 3_000),
        "complexity_factors": ["debt"],
        "requires": [("Loans Payable", 1), ("Cash", 100)],
        "levels": {3, 4, 5},
    },

    # ── Level 3+: COGS-paired sales ──────────────────────────────────────
    {
        "tx_type": "cash_sale_with_cogs",
        "description": "Cash sale of goods (with cost recognition)",
        "debit": "Cash",
        "credit": "Revenue",
        "amount_range": (1_000, 15_000),
        "complexity_factors": ["cogs"],
        "requires": [("Inventory", 500)],
        "levels": {3, 4, 5},
        "cogs_ratio": (0.40, 0.70),
    },
    {
        "tx_type": "credit_sale_with_cogs",
        "description": "Credit sale of goods (with cost recognition)",
        "debit": "Accounts Receivable",
        "credit": "Revenue",
        "amount_range": (1_000, 20_000),
        "complexity_factors": ["cogs", "credit_transaction"],
        "requires": [("Inventory", 500)],
        "levels": {3, 4, 5},
        "cogs_ratio": (0.40, 0.70),
    },

    # ── Level 3+: derived interest expense ────────────────────────────────
    {
        "tx_type": "derived_interest_expense",
        "description": "Paid interest on loan (derived from principal)",
        "debit": "Interest Expense",
        "credit": "Cash",
        "amount_range": (100, 5_000),
        "complexity_factors": ["derived_interest", "debt"],
        "requires": [("Loans Payable", 1_000), ("Cash", 100)],
        "levels": {3, 4, 5},
        "interest_rate": (0.05, 0.12),
    },

    # ── Level 4+: mixed-funding purchases ─────────────────────────────────
    {
        "tx_type": "mixed_purchase_equipment",
        "description": "Purchased equipment (partial cash, partial loan)",
        "debit": "Equipment",
        "credit": "Cash",
        "loan_account": "Notes Payable",
        "amount_range": (10_000, 50_000),
        "complexity_factors": ["mixed_funding", "depreciable_asset", "debt"],
        "requires": [("Cash", 3_000)],
        "levels": {4, 5},
        "cash_ratio": (0.30, 0.70),
    },
    {
        "tx_type": "mixed_purchase_vehicles",
        "description": "Purchased vehicle (partial cash, partial loan)",
        "debit": "Vehicles",
        "credit": "Cash",
        "loan_account": "Notes Payable",
        "amount_range": (15_000, 80_000),
        "complexity_factors": ["mixed_funding", "depreciable_asset", "debt"],
        "requires": [("Cash", 5_000)],
        "levels": {4, 5},
        "cash_ratio": (0.30, 0.70),
    },
]

# ── Adjustment templates ───────────────────────────────────────────────────

ADJUSTMENT_TEMPLATES = [
    {
        "adj_type": "depreciation_equipment",
        "description": "Straight-line depreciation on equipment",
        "asset_account": "Equipment",
        "debit": "Depreciation Expense",
        "credit": "Accumulated Depreciation",
        "useful_life": 10,          # years
        "salvage_pct": 0.10,        # 10% of cost
        "levels": {3, 4, 5},
    },
    {
        "adj_type": "depreciation_furniture",
        "description": "Straight-line depreciation on furniture",
        "asset_account": "Furniture",
        "debit": "Depreciation Expense",
        "credit": "Accumulated Depreciation",
        "useful_life": 5,
        "salvage_pct": 0.05,
        "levels": {3, 4, 5},
    },
    {
        "adj_type": "depreciation_vehicles",
        "description": "Straight-line depreciation on vehicles",
        "asset_account": "Vehicles",
        "debit": "Depreciation Expense",
        "credit": "Accumulated Depreciation",
        "useful_life": 5,
        "salvage_pct": 0.10,
        "levels": {3, 4, 5},
    },
    {
        "adj_type": "prepaid_rent_expiry",
        "description": "Recognition of expired prepaid rent",
        "asset_account": "Prepaid Rent",
        "debit": "Rent Expense",
        "credit": "Prepaid Rent",
        "expiry_fraction": 0.5,     # 50% of prepaid expires in period
        "levels": {2, 3, 4, 5},
    },
    {
        "adj_type": "prepaid_insurance_expiry",
        "description": "Recognition of expired prepaid insurance",
        "asset_account": "Prepaid Insurance",
        "debit": "Insurance Expense",
        "credit": "Prepaid Insurance",
        "expiry_fraction": 0.5,
        "levels": {2, 3, 4, 5},
    },
    {
        "adj_type": "accrued_salaries",
        "description": "Accrual of unpaid salaries at period end",
        "debit": "Salaries Expense",
        "credit": "Accrued Expenses",
        "amount_range": (500, 5_000),
        "levels": {3, 4, 5},
    },

    # ── New: contra-account adjustments ───────────────────────────────────
    {
        "adj_type": "bad_debt_provision",
        "description": "Provision for doubtful accounts",
        "debit": "Bad Debt Expense",
        "credit": "Allowance for Doubtful Accounts",
        "provision_rate": (0.02, 0.10),
        "levels": {3, 4, 5},
    },
    {
        "adj_type": "accrued_interest",
        "description": "Accrual of interest payable at period end",
        "debit": "Interest Expense",
        "credit": "Accrued Interest Payable",
        "interest_rate": (0.05, 0.12),
        "time_fraction": (0.25, 0.75),
        "levels": {3, 4, 5},
    },

    # ── New: inventory write-down ─────────────────────────────────────────
    {
        "adj_type": "inventory_write_down",
        "description": "Write-down of obsolete inventory",
        "debit": "Operating Expenses",
        "credit": "Inventory",
        "write_down_rate": (0.05, 0.15),
        "levels": {4, 5},
    },

    # ── New: chained adjustment (must follow bad_debt_provision) ──────────
    {
        "adj_type": "bad_debt_write_off",
        "description": "Write-off of specific uncollectible account",
        "debit": "Allowance for Doubtful Accounts",
        "credit": "Accounts Receivable",
        "write_off_rate": (0.30, 0.60),
        "requires_adjustment": "bad_debt_provision",
        "levels": {4, 5},
    },
]

# ── Difficulty level configuration ────────────────────────────────────────

LEVEL_CONFIG = {
    1: {
        "n_transactions":  (5, 10),
        "with_adjustments": False,
        "adj_count":       0,
        "tx_types": [t for t in TX_TEMPLATES if 1 in t["levels"]
                     and t["tx_type"] in {
                         "owner_investment", "cash_purchase_equipment",
                         "cash_purchase_inventory", "cash_sale",
                         "cash_expense", "prepaid_rent",
                     }],
    },
    2: {
        "n_transactions":  (10, 20),
        "with_adjustments": True,
        "adj_count":       1,
        "tx_types": [t for t in TX_TEMPLATES if 2 in t["levels"]],
    },
    3: {
        "n_transactions":  (20, 35),
        "with_adjustments": True,
        "adj_count":       (1, 3),
        "tx_types": [t for t in TX_TEMPLATES if 3 in t["levels"]],
    },
    4: {
        "n_transactions":  (35, 60),
        "with_adjustments": True,
        "adj_count":       (2, 4),
        "tx_types": [t for t in TX_TEMPLATES if 4 in t["levels"]],
    },
    5: {
        "n_transactions":  (60, 100),
        "with_adjustments": True,
        "adj_count":       (3, 5),
        "tx_types": [t for t in TX_TEMPLATES if 5 in t["levels"]],
    },
}
