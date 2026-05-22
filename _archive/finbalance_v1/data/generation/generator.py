"""
Synthetic accounting problem generator.

Design:
- A Ledger tracks running account balances (always double-entry consistent).
- Transactions are sampled from templates valid at the current ledger state.
- Ground truth is computed by construction — the ledger IS the source of truth.
- Intermediate states are snapshotted after every transaction.
"""

import random
import math
from typing import Optional

from finbalance.data.schemas import (
    ACCOUNT_TYPE,
    Adjustment,
    BalanceSheet,
    IntermediateState,
    JournalEntry,
    OpeningBalance,
    Problem,
    Transaction,
)
from finbalance.data.generation.templates import (
    ADJUSTMENT_TEMPLATES,
    LEVEL_CONFIG,
    TX_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Ledger
# ---------------------------------------------------------------------------

class Ledger:
    """
    Tracks all account balances using natural-sign convention:
      Assets / Expenses  -> balance increases on debit  (stored as positive)
      Liability / Equity / Revenue -> balance increases on credit (stored as positive)

    Net income (Revenue - Expenses) is folded into Retained Earnings
    when building the final balance sheet.
    """

    # contra_asset (e.g. Accumulated Depreciation) has a CREDIT normal balance
    DEBIT_NORMAL = {"asset", "expense"}

    def __init__(self):
        self.balances: dict[str, float] = {}

    def _atype(self, account: str) -> str:
        return ACCOUNT_TYPE.get(account, "asset")

    def credit_effect(self, account: str, amount: float) -> float:
        """Return +amount if credit increases the account, else -amount."""
        return +amount if self._atype(account) not in self.DEBIT_NORMAL else -amount

    def debit_effect(self, account: str, amount: float) -> float:
        return -self.credit_effect(account, amount)

    def apply(self, debit_account: str, credit_account: str, amount: float):
        # Debit increases assets/expenses; credit increases liabilities/equity/revenue
        self.balances[debit_account] = (
            self.balances.get(debit_account, 0.0) + self.debit_effect(debit_account, amount)
        )
        self.balances[credit_account] = (
            self.balances.get(credit_account, 0.0) + self.credit_effect(credit_account, amount)
        )

    def get(self, account: str) -> float:
        return self.balances.get(account, 0.0)

    def total_assets(self) -> float:
        total = 0.0
        for acc, bal in self.balances.items():
            t = self._atype(acc)
            if t == "asset":
                total += bal
            elif t == "contra_asset":
                total -= bal      # contra reduces assets
        return total

    def total_liabilities(self) -> float:
        return sum(
            bal for acc, bal in self.balances.items()
            if self._atype(acc) == "liability"
        )

    def total_equity(self) -> float:
        """Equity = explicit equity accounts + net income (revenue - expense)."""
        explicit = sum(
            bal for acc, bal in self.balances.items()
            if self._atype(acc) == "equity"
        )
        revenue = sum(
            bal for acc, bal in self.balances.items()
            if self._atype(acc) == "revenue"
        )
        expense = sum(
            bal for acc, bal in self.balances.items()
            if self._atype(acc) == "expense"
        )
        return explicit + revenue - expense

    def build_balance_sheet(self, date: str) -> BalanceSheet:
        assets: dict[str, float] = {}
        liabilities: dict[str, float] = {}
        equity: dict[str, float] = {}

        for acc, bal in self.balances.items():
            t = self._atype(acc)
            if t == "asset":
                assets[acc] = round(bal, 2)
            elif t == "contra_asset":
                assets[acc] = round(-bal, 2)   # shown as negative on balance sheet
            elif t == "liability":
                liabilities[acc] = round(bal, 2)
            elif t == "equity":
                equity[acc] = round(bal, 2)
            # revenue / expense -> net income -> retained earnings (see below)

        # Fold net income into Retained Earnings
        revenue = sum(
            bal for acc, bal in self.balances.items()
            if self._atype(acc) == "revenue"
        )
        expense = sum(
            bal for acc, bal in self.balances.items()
            if self._atype(acc) == "expense"
        )
        net_income = revenue - expense
        if abs(net_income) > 0.01:
            existing = equity.get("Retained Earnings", 0.0)
            equity["Retained Earnings"] = round(existing + net_income, 2)

        ta = round(sum(assets.values()), 2)
        tl = round(sum(liabilities.values()), 2)
        te = round(sum(equity.values()), 2)

        return BalanceSheet(
            date=date,
            assets=assets,
            liabilities=liabilities,
            equity=equity,
            total_assets=ta,
            total_liabilities=tl,
            total_equity=te,
            balanced=abs(ta - (tl + te)) < 1.0,
        )


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------

class ProblemGenerator:

    def __init__(self, seed: Optional[int] = None):
        self.rng = random.Random(seed)

    # ── helpers ──────────────────────────────────────────────────────────

    def _round_amount(self, lo: int, hi: int) -> float:
        """Sample an amount rounded to nearest 100."""
        raw = self.rng.randint(lo // 100, hi // 100)
        return float(raw * 100)

    def _opening_balance(self, level: int) -> tuple[Ledger, OpeningBalance]:
        ledger = Ledger()
        # Seed with owner investment so we always start with cash
        seed_amount = self._round_amount(10_000, 50_000)
        ledger.apply("Cash", "Owner's Equity", seed_amount)

        ob = OpeningBalance(
            date="2024-01-01",
            assets={"Cash": ledger.get("Cash")},
            liabilities={},
            equity={"Owner's Equity": ledger.get("Owner's Equity")},
        )
        return ledger, ob

    def _eligible_templates(self, ledger: Ledger, level: int) -> list[dict]:
        """Return templates valid at the current ledger state."""
        eligible = []
        for tmpl in LEVEL_CONFIG[level]["tx_types"]:
            ok = True
            for (req_acc, req_min) in tmpl.get("requires", []):
                if ledger.get(req_acc) < req_min:
                    ok = False
                    break
            if ok:
                eligible.append(tmpl)
        return eligible

    # ── complex transaction builders ─────────────────────────────────────

    def _create_cogs_sale(
        self, tmpl: dict, tx_id: str, date: str, ledger: Ledger,
    ) -> Transaction:
        """Cash or credit sale with paired COGS / inventory reduction."""
        lo, hi = tmpl["amount_range"]
        sale_amount = self._round_amount(lo, hi)

        cogs_lo, cogs_hi = tmpl["cogs_ratio"]
        cogs_frac = self.rng.uniform(cogs_lo, cogs_hi)
        cogs_amount = round(sale_amount * cogs_frac / 100) * 100
        cogs_amount = max(100.0, cogs_amount)

        # Cap COGS to available inventory
        inv_bal = ledger.get("Inventory")
        cogs_amount = min(cogs_amount, round(inv_bal / 100) * 100)
        cogs_amount = max(100.0, cogs_amount)

        entries = [
            JournalEntry(account=tmpl["debit"], debit=sale_amount),
            JournalEntry(account=tmpl["credit"], credit=sale_amount),
            JournalEntry(account="Cost of Goods Sold", debit=cogs_amount),
            JournalEntry(account="Inventory", credit=cogs_amount),
        ]
        ledger.apply(tmpl["debit"], tmpl["credit"], sale_amount)
        ledger.apply("Cost of Goods Sold", "Inventory", cogs_amount)

        return Transaction(
            transaction_id=tx_id,
            date=date,
            description=tmpl["description"],
            entries=entries,
            tx_type=tmpl["tx_type"],
            complexity_factors=list(tmpl.get("complexity_factors", [])),
        )

    def _create_mixed_purchase(
        self, tmpl: dict, tx_id: str, date: str, ledger: Ledger,
    ) -> Transaction:
        """Asset purchase funded partly by cash, partly by a new loan."""
        lo, hi = tmpl["amount_range"]
        total = self._round_amount(lo, hi)

        cash_lo, cash_hi = tmpl["cash_ratio"]
        cash_frac = self.rng.uniform(cash_lo, cash_hi)
        cash_portion = round(total * cash_frac / 100) * 100
        cash_portion = max(100.0, cash_portion)

        # Cap cash to available balance (leave a buffer)
        cash_avail = ledger.get("Cash") - 500
        cash_portion = min(cash_portion, round(cash_avail / 100) * 100)
        cash_portion = max(100.0, cash_portion)

        loan_portion = total - cash_portion

        entries = [
            JournalEntry(account=tmpl["debit"], debit=total),
            JournalEntry(account="Cash", credit=cash_portion),
            JournalEntry(account=tmpl["loan_account"], credit=loan_portion),
        ]
        ledger.apply(tmpl["debit"], "Cash", cash_portion)
        ledger.apply(tmpl["debit"], tmpl["loan_account"], loan_portion)

        desc = (
            f"{tmpl['description']} — ${cash_portion:,.0f} cash"
            f" + ${loan_portion:,.0f} loan"
        )
        return Transaction(
            transaction_id=tx_id,
            date=date,
            description=desc,
            entries=entries,
            tx_type=tmpl["tx_type"],
            complexity_factors=list(tmpl.get("complexity_factors", [])),
        )

    def _create_derived_interest(
        self, tmpl: dict, tx_id: str, date: str, ledger: Ledger,
    ) -> Transaction:
        """Interest expense computed from outstanding loan balance × rate."""
        loan_bal = ledger.get("Loans Payable") + ledger.get("Notes Payable")
        rate_lo, rate_hi = tmpl["interest_rate"]
        annual_rate = self.rng.uniform(rate_lo, rate_hi)

        # Monthly interest (assume one-month period)
        interest = round(loan_bal * annual_rate / 12 / 100) * 100
        interest = max(100.0, interest)

        # Cap to available cash
        cash_avail = ledger.get("Cash") - 500
        interest = min(interest, round(max(100.0, cash_avail) / 100) * 100)
        interest = max(100.0, interest)

        entries = [
            JournalEntry(account="Interest Expense", debit=interest),
            JournalEntry(account="Cash", credit=interest),
        ]
        ledger.apply("Interest Expense", "Cash", interest)

        desc = (
            f"Paid interest on loan"
            f" ({annual_rate * 100:.1f}% p.a. on ${loan_bal:,.0f})"
        )
        return Transaction(
            transaction_id=tx_id,
            date=date,
            description=desc,
            entries=entries,
            tx_type=tmpl["tx_type"],
            complexity_factors=list(tmpl.get("complexity_factors", [])),
        )

    def _generate_transactions(
        self, ledger: Ledger, level: int, n: int, date_offset: int = 0
    ) -> tuple[list[Transaction], list[IntermediateState]]:
        transactions: list[Transaction] = []
        states: list[IntermediateState] = []

        # tx_types that use dedicated multi-entry builders
        COGS_TYPES  = {"cash_sale_with_cogs", "credit_sale_with_cogs"}
        MIXED_TYPES = {"mixed_purchase_equipment", "mixed_purchase_vehicles"}

        for i in range(n):
            eligible = self._eligible_templates(ledger, level)
            if not eligible:
                break  # safety valve
            tmpl = self.rng.choice(eligible)

            tx_id = f"T{date_offset + i + 1:03d}"
            date = f"2024-{((date_offset + i) // 28) + 1:02d}-{((date_offset + i) % 28) + 1:02d}"
            tx_type = tmpl["tx_type"]

            # ── dispatch to specialised builders ──────────────────────────
            if tx_type in COGS_TYPES:
                tx = self._create_cogs_sale(tmpl, tx_id, date, ledger)

            elif tx_type in MIXED_TYPES:
                tx = self._create_mixed_purchase(tmpl, tx_id, date, ledger)

            elif tx_type == "derived_interest_expense":
                tx = self._create_derived_interest(tmpl, tx_id, date, ledger)

            else:
                # ── standard two-entry transaction ────────────────────────
                lo, hi = tmpl["amount_range"]
                amount = self._round_amount(lo, hi)

                # Cap amounts for txs that reduce existing balances
                if tx_type == "collect_receivable":
                    cap = ledger.get("Accounts Receivable")
                    amount = min(amount, max(100.0, cap * 0.6))
                    amount = round(amount / 100) * 100
                elif tx_type == "pay_payable":
                    cap = min(ledger.get("Accounts Payable"), ledger.get("Cash"))
                    amount = min(amount, max(100.0, cap * 0.6))
                    amount = round(amount / 100) * 100
                elif tx_type == "pay_loan_principal":
                    cap = min(ledger.get("Loans Payable"), ledger.get("Cash"))
                    amount = min(amount, max(100.0, cap * 0.6))
                    amount = round(amount / 100) * 100

                entry_debit  = JournalEntry(account=tmpl["debit"],  debit=amount)
                entry_credit = JournalEntry(account=tmpl["credit"], credit=amount)

                tx = Transaction(
                    transaction_id=tx_id,
                    date=date,
                    description=tmpl["description"],
                    entries=[entry_debit, entry_credit],
                    tx_type=tmpl["tx_type"],
                    complexity_factors=list(tmpl.get("complexity_factors", [])),
                )
                ledger.apply(tmpl["debit"], tmpl["credit"], amount)

            transactions.append(tx)

            states.append(IntermediateState(
                after_transaction_id=tx_id,
                assets_total=round(ledger.total_assets(), 2),
                liabilities_total=round(ledger.total_liabilities(), 2),
                equity_total=round(ledger.total_equity(), 2),
            ))

        return transactions, states

    def _generate_adjustments(self, ledger: Ledger, level: int) -> list[Adjustment]:
        adjustments: list[Adjustment] = []
        adj_cfg = LEVEL_CONFIG[level]
        if not adj_cfg["with_adjustments"]:
            return []

        adj_count_cfg = adj_cfg["adj_count"]
        if isinstance(adj_count_cfg, tuple):
            n_adj = self.rng.randint(*adj_count_cfg)
        else:
            n_adj = adj_count_cfg

        eligible_adjs = [a for a in ADJUSTMENT_TEMPLATES if level in a["levels"]]
        self.rng.shuffle(eligible_adjs)

        # Separate base adjustments from chained ones (chained are added
        # automatically when their prerequisite is selected).
        base_adjs    = [a for a in eligible_adjs if not a.get("requires_adjustment")]
        chained_adjs = [a for a in eligible_adjs if a.get("requires_adjustment")]

        selected = base_adjs[:n_adj]

        # Attach chained adjustments whose prerequisite was selected
        for chain in chained_adjs:
            prereq = chain["requires_adjustment"]
            if any(a["adj_type"] == prereq for a in selected):
                selected.append(chain)

        # Sort so provisions process before write-offs (chain ordering)
        _ADJ_PRIORITY = {"bad_debt_write_off": 10}
        selected.sort(key=lambda a: _ADJ_PRIORITY.get(a["adj_type"], 0))

        for i, tmpl in enumerate(selected):
            adj_id = f"A{i + 1:03d}"
            at = tmpl["adj_type"]

            if "depreciation" in at:
                asset_acc = tmpl["asset_account"]
                cost = ledger.get(asset_acc)
                if cost < 1_000:
                    continue
                salvage = cost * tmpl["salvage_pct"]
                annual_depr = round((cost - salvage) / tmpl["useful_life"] / 100) * 100
                annual_depr = max(100.0, annual_depr)

                calc = {
                    "asset": asset_acc,
                    "cost": cost,
                    "salvage_value": salvage,
                    "useful_life": tmpl["useful_life"],
                    "method": "straight_line",
                    "annual_depreciation": annual_depr,
                }
                entries = [
                    JournalEntry(account="Depreciation Expense", debit=annual_depr),
                    JournalEntry(account="Accumulated Depreciation", credit=annual_depr),
                ]
                ledger.apply("Depreciation Expense", "Accumulated Depreciation", annual_depr)

            elif "prepaid" in at:
                asset_acc = tmpl["asset_account"]
                bal = ledger.get(asset_acc)
                if bal < 100:
                    continue
                expire = round(bal * tmpl["expiry_fraction"] / 100) * 100
                expire = max(100.0, expire)
                expense_acc = tmpl["debit"]

                calc = {"balance": bal, "expiry_fraction": tmpl["expiry_fraction"]}
                entries = [
                    JournalEntry(account=expense_acc, debit=expire),
                    JournalEntry(account=asset_acc,   credit=expire),
                ]
                ledger.apply(expense_acc, asset_acc, expire)

            elif at == "accrued_salaries":
                lo, hi = tmpl["amount_range"]
                amount = self._round_amount(lo, hi)
                calc = {"amount": amount}
                entries = [
                    JournalEntry(account=tmpl["debit"],  debit=amount),
                    JournalEntry(account=tmpl["credit"], credit=amount),
                ]
                ledger.apply(tmpl["debit"], tmpl["credit"], amount)

            # ── new adjustment types ──────────────────────────────────────

            elif at == "bad_debt_provision":
                ar_bal = ledger.get("Accounts Receivable")
                if ar_bal < 500:
                    continue
                prov_lo, prov_hi = tmpl["provision_rate"]
                rate = self.rng.uniform(prov_lo, prov_hi)
                provision = round(ar_bal * rate / 100) * 100
                provision = max(100.0, provision)

                calc = {
                    "accounts_receivable": ar_bal,
                    "provision_rate": round(rate, 4),
                    "provision_amount": provision,
                }
                entries = [
                    JournalEntry(account="Bad Debt Expense", debit=provision),
                    JournalEntry(account="Allowance for Doubtful Accounts", credit=provision),
                ]
                ledger.apply("Bad Debt Expense", "Allowance for Doubtful Accounts", provision)

            elif at == "accrued_interest":
                loan_bal = ledger.get("Loans Payable") + ledger.get("Notes Payable")
                if loan_bal < 500:
                    continue
                rate_lo, rate_hi = tmpl["interest_rate"]
                rate = self.rng.uniform(rate_lo, rate_hi)
                tf_lo, tf_hi = tmpl["time_fraction"]
                time_frac = self.rng.uniform(tf_lo, tf_hi)
                interest = round(loan_bal * rate * time_frac / 100) * 100
                interest = max(100.0, interest)

                calc = {
                    "loan_balance": loan_bal,
                    "annual_rate": round(rate, 4),
                    "time_fraction": round(time_frac, 2),
                    "accrued_interest": interest,
                }
                entries = [
                    JournalEntry(account="Interest Expense", debit=interest),
                    JournalEntry(account="Accrued Interest Payable", credit=interest),
                ]
                ledger.apply("Interest Expense", "Accrued Interest Payable", interest)

            elif at == "inventory_write_down":
                inv_bal = ledger.get("Inventory")
                if inv_bal < 500:
                    continue
                wd_lo, wd_hi = tmpl["write_down_rate"]
                rate = self.rng.uniform(wd_lo, wd_hi)
                write_down = round(inv_bal * rate / 100) * 100
                write_down = max(100.0, write_down)

                calc = {
                    "inventory_balance": inv_bal,
                    "write_down_rate": round(rate, 4),
                    "write_down_amount": write_down,
                }
                entries = [
                    JournalEntry(account="Operating Expenses", debit=write_down),
                    JournalEntry(account="Inventory", credit=write_down),
                ]
                ledger.apply("Operating Expenses", "Inventory", write_down)

            elif at == "bad_debt_write_off":
                allowance_bal = ledger.get("Allowance for Doubtful Accounts")
                ar_bal = ledger.get("Accounts Receivable")
                if allowance_bal < 100 or ar_bal < 100:
                    continue
                wo_lo, wo_hi = tmpl["write_off_rate"]
                rate = self.rng.uniform(wo_lo, wo_hi)
                write_off = round(allowance_bal * rate / 100) * 100
                write_off = min(write_off, round(ar_bal / 100) * 100)
                write_off = max(100.0, write_off)

                calc = {
                    "allowance_balance": allowance_bal,
                    "write_off_rate": round(rate, 4),
                    "write_off_amount": write_off,
                }
                entries = [
                    JournalEntry(account="Allowance for Doubtful Accounts", debit=write_off),
                    JournalEntry(account="Accounts Receivable", credit=write_off),
                ]
                ledger.apply("Allowance for Doubtful Accounts", "Accounts Receivable", write_off)

            else:
                continue

            adjustments.append(Adjustment(
                adjustment_id=adj_id,
                date="2024-12-31",
                description=tmpl["description"],
                adj_type=at,
                entries=entries,
                calculation=calc,
            ))

        return adjustments

    # ── public API ────────────────────────────────────────────────────────

    def generate(self, problem_id: str, level: int) -> Problem:
        assert 1 <= level <= 5, "Level must be 1-5"
        cfg = LEVEL_CONFIG[level]
        lo, hi = cfg["n_transactions"]
        n_tx = self.rng.randint(lo, hi)

        ledger, opening = self._opening_balance(level)
        transactions, states = self._generate_transactions(ledger, level, n_tx)
        adjustments = self._generate_adjustments(ledger, level)

        expected = ledger.build_balance_sheet("2024-12-31")
        assert expected.balanced, f"Generator bug: balance sheet not balanced for {problem_id}"

        return Problem(
            problem_id=problem_id,
            difficulty_level=level,
            opening_balance=opening,
            transactions=transactions,
            adjustments=adjustments,
            expected=expected,
            intermediate_states=states,
            metadata={
                "num_transactions": len(transactions),
                "num_accounts": len(expected.assets) + len(expected.liabilities) + len(expected.equity),
                "has_adjustments": len(adjustments) > 0,
                "num_adjustments": len(adjustments),
                "complexity_factors": list({
                    f for tx in transactions for f in tx.complexity_factors
                }),
            },
        )

    def generate_dataset(
        self,
        counts: dict[int, int],
        id_prefix: str = "FB",
    ) -> list[Problem]:
        """Generate a full dataset across difficulty levels.

        Args:
            counts: {level: n_problems}, e.g. {1: 500, 2: 750, 3: 750}
        """
        problems = []
        global_idx = 1
        for level in sorted(counts):
            for _ in range(counts[level]):
                pid = f"{id_prefix}_{level}_{global_idx:05d}"
                problems.append(self.generate(pid, level))
                global_idx += 1
        return problems
