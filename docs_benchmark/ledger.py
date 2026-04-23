"""Deterministic ledger used to build the expected balance sheet."""

from __future__ import annotations

from docs_benchmark.accounts import ACCOUNT_TYPES, BALANCE_SHEET_SECTIONS, DEBIT_NORMAL_TYPES
from docs_benchmark.schemas import BalanceSheet, OpeningBalance, Posting


class Ledger:
    def __init__(self, opening_balance: OpeningBalance):
        self.balances: dict[str, float] = {}
        for section in (opening_balance.assets, opening_balance.liabilities, opening_balance.equity):
            for account, value in section.items():
                self.balances[account] = round(float(value), 2)

    def _account_type(self, account: str) -> str:
        if account not in ACCOUNT_TYPES:
            raise KeyError(f"Unknown account '{account}'")
        return ACCOUNT_TYPES[account]

    def debit_effect(self, account: str, amount: float) -> float:
        return amount if self._account_type(account) in DEBIT_NORMAL_TYPES else -amount

    def credit_effect(self, account: str, amount: float) -> float:
        return -self.debit_effect(account, amount)

    def apply_posting(self, posting: Posting) -> None:
        amount = round(float(posting.amount), 2)
        self.balances[posting.debit_account] = round(
            self.balances.get(posting.debit_account, 0.0) + self.debit_effect(posting.debit_account, amount),
            2,
        )
        self.balances[posting.credit_account] = round(
            self.balances.get(posting.credit_account, 0.0) + self.credit_effect(posting.credit_account, amount),
            2,
        )

    def apply_all(self, postings: list[Posting]) -> None:
        for posting in postings:
            self.apply_posting(posting)

    def build_balance_sheet(self, date: str) -> BalanceSheet:
        assets: dict[str, float] = {}
        liabilities: dict[str, float] = {}
        equity: dict[str, float] = {}

        revenue_total = 0.0
        expense_total = 0.0
        for account, balance in self.balances.items():
            account_type = self._account_type(account)
            if account_type == "revenue":
                revenue_total += balance
                continue
            if account_type == "expense":
                expense_total += balance
                continue

            section = BALANCE_SHEET_SECTIONS[account_type]
            rendered = -balance if account_type == "contra_asset" else balance
            if abs(rendered) > 0.004:
                if section == "assets":
                    assets[account] = round(rendered, 2)
                elif section == "liabilities":
                    liabilities[account] = round(rendered, 2)
                else:
                    equity[account] = round(rendered, 2)

        retained_earnings = round(revenue_total - expense_total, 2)
        if abs(retained_earnings) > 0.004:
            equity["Retained Earnings"] = round(equity.get("Retained Earnings", 0.0) + retained_earnings, 2)

        total_assets = round(sum(assets.values()), 2)
        total_liabilities = round(sum(liabilities.values()), 2)
        total_equity = round(sum(equity.values()), 2)
        return BalanceSheet(
            date=date,
            assets=assets,
            liabilities=liabilities,
            equity=equity,
            total_assets=total_assets,
            total_liabilities=total_liabilities,
            total_equity=total_equity,
            balanced=abs(total_assets - (total_liabilities + total_equity)) < 0.01,
        )
