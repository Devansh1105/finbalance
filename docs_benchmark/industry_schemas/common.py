"""Shared helpers for industry schema definitions."""

from __future__ import annotations

import random
from dataclasses import dataclass

from docs_benchmark.generation.helpers import amount_scale, period_rank
from docs_benchmark.schemas import OpeningBalance
from docs_benchmark.types import DifficultyPlan, PeriodSpec


@dataclass(frozen=True)
class OpeningAccountRule:
    account: str
    low: float
    high: float
    min_level: int = 1
    min_period_rank: int = 0
    probability: float = 1.0


def build_opening_balance(
    rng: random.Random,
    level: int,
    period_spec: PeriodSpec,
    *,
    asset_rules: tuple[OpeningAccountRule, ...],
    liability_rules: tuple[OpeningAccountRule, ...],
    equity_rules: tuple[OpeningAccountRule, ...] = (),
    residual_equity_account: str = "Owner's Equity",
    scale_multiplier: float = 1.0,
) -> OpeningBalance:
    rank = period_rank(period_spec.period_type)
    assets = _select_accounts(rng, level, rank, asset_rules, scale_multiplier)
    liabilities = _select_accounts(rng, level, rank, liability_rules, scale_multiplier)
    equity = _select_accounts(rng, level, rank, equity_rules, scale_multiplier)
    residual = round(sum(assets.values()) - sum(liabilities.values()) - sum(equity.values()), 2)
    if residual <= 0:
        residual = round(abs(residual) + rng.uniform(1800, 6200) * scale_multiplier, 2)
        assets["Cash"] = round(assets.get("Cash", 0.0) + residual, 2)
        residual = round(sum(assets.values()) - sum(liabilities.values()) - sum(equity.values()), 2)
    equity[residual_equity_account] = residual
    return OpeningBalance(date=period_spec.start_date, assets=assets, liabilities=liabilities, equity=equity)


def opening_balance_scale(industry: str, period_spec: PeriodSpec, level: int) -> float:
    return max(1.0, round(amount_scale(industry, period_spec.period_type, level, "capital") * 0.25, 2))


def copy_plan(plan: DifficultyPlan, *extra_mandatory: str, extra_optional: tuple[str, ...] = ()) -> DifficultyPlan:
    return DifficultyPlan(
        mandatory=tuple(list(plan.mandatory) + list(extra_mandatory)),
        optional=tuple(list(plan.optional) + list(extra_optional)),
    )


def _select_accounts(
    rng: random.Random,
    level: int,
    rank: int,
    rules: tuple[OpeningAccountRule, ...],
    scale_multiplier: float,
) -> dict[str, float]:
    selected: dict[str, float] = {}
    for rule in rules:
        if level < rule.min_level or rank < rule.min_period_rank:
            continue
        if rng.random() > rule.probability:
            continue
        selected[rule.account] = round(rng.uniform(rule.low, rule.high) * scale_multiplier, 2)
    return selected
