"""Simple benchmark metrics for predicted entries and balance sheets."""

from __future__ import annotations

from collections import Counter
from typing import Any

from docs_benchmark.schemas import BalanceSheet, DocumentRecord, ParsedSubmission, Posting


def _amount_key(posting: Posting, amount_tol: float) -> int:
    if amount_tol <= 0:
        return int(round(posting.amount * 100))
    return int(round(posting.amount / amount_tol))


def _balance_sheet_sections(balance_sheet: BalanceSheet | dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    if isinstance(balance_sheet, BalanceSheet):
        return {
            "assets": dict(balance_sheet.assets),
            "liabilities": dict(balance_sheet.liabilities),
            "equity": dict(balance_sheet.equity),
        }
    return {
        "assets": {str(key): float(value) for key, value in balance_sheet.get("assets", {}).items()},
        "liabilities": {str(key): float(value) for key, value in balance_sheet.get("liabilities", {}).items()},
        "equity": {str(key): float(value) for key, value in balance_sheet.get("equity", {}).items()},
    }


def _rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 1.0
    return round(numerator / denominator, 4)


def _code_match(expected_codes: list[str], predicted_codes: list[str]) -> bool:
    return set(expected_codes) == set(predicted_codes)


def _entry_key_with_refs(posting: Posting, amount_tol: float) -> tuple[Any, ...]:
    return posting.key(amount_tol)


def _entry_key_without_refs(posting: Posting, amount_tol: float) -> tuple[Any, ...]:
    return (posting.debit_account, posting.credit_account, _amount_key(posting, amount_tol))


def _normalize_balance_section(accounts: dict[str, float], balance_tol: float) -> dict[str, float]:
    return {
        account: round(float(amount), 2)
        for account, amount in accounts.items()
        if abs(float(amount)) > balance_tol
    }


def _balance_sheet_exact_match(
    expected: BalanceSheet | dict[str, dict[str, float]],
    predicted: BalanceSheet | dict[str, dict[str, float]],
    balance_tol: float,
) -> bool:
    expected_sections = _balance_sheet_sections(expected)
    predicted_sections = _balance_sheet_sections(predicted)
    for section in ("assets", "liabilities", "equity"):
        expected_section = _normalize_balance_section(expected_sections[section], balance_tol)
        predicted_section = _normalize_balance_section(predicted_sections[section], balance_tol)
        if set(expected_section) != set(predicted_section):
            return False
        for account, amount in expected_section.items():
            if abs(predicted_section.get(account, 0.0) - amount) > balance_tol:
                return False
    return True


def score_submission(
    record: DocumentRecord,
    parsed: ParsedSubmission,
    *,
    parse_success: bool,
    amount_tol: float = 0.01,
    balance_tol: float = 0.01,
) -> dict[str, Any]:
    if record.expected_inconsistency:
        predicted_balance_sheet = _balance_sheet_sections(parsed.balance_sheet)
        output_clean = not parsed.entries and all(not section for section in predicted_balance_sheet.values())
        code_match = _code_match(record.expected_inconsistency_codes, parsed.inconsistency_codes)
        return {
            "parse_success": bool(parse_success),
            "expected_inconsistency": True,
            "inconsistency_flag_matches": bool(parsed.has_inconsistency),
            "inconsistency_code_matches": bool(parsed.has_inconsistency and code_match),
            "inconsistency_empty_answer": bool(parsed.has_inconsistency and output_clean),
            "final_balance_sheet_matches": False,
            "final_balance_sheet_and_journal_entries_match": False,
            "final_journal_entries_match": False,
            "final_journal_entries_match_no_doc_refs": False,
        }

    expected_entries = record.expected_entries
    predicted_entries = parsed.entries
    exact_entry_match = Counter(_entry_key_with_refs(posting, amount_tol) for posting in expected_entries) == Counter(
        _entry_key_with_refs(posting, amount_tol) for posting in predicted_entries
    )
    account_amount_match = Counter(_entry_key_without_refs(posting, amount_tol) for posting in expected_entries) == Counter(
        _entry_key_without_refs(posting, amount_tol) for posting in predicted_entries
    )
    balance_sheet_match = _balance_sheet_exact_match(record.expected_balance_sheet, parsed.balance_sheet, balance_tol)

    return {
        "parse_success": bool(parse_success),
        "expected_inconsistency": False,
        "inconsistency_flag_matches": not parsed.has_inconsistency,
        "inconsistency_code_matches": not parsed.inconsistency_codes,
        "inconsistency_empty_answer": not parsed.has_inconsistency,
        "final_balance_sheet_matches": balance_sheet_match,
        "final_balance_sheet_and_journal_entries_match": bool(balance_sheet_match and exact_entry_match),
        "final_journal_entries_match": exact_entry_match,
        "final_journal_entries_match_no_doc_refs": account_amount_match,
    }


def summarize_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    summary = _summarize_subset(results)
    summary["by_difficulty"] = _grouped_summary(results, "difficulty_level")
    summary["by_period_type"] = _grouped_summary(results, "period_type")
    summary["by_industry"] = _grouped_summary(results, "industry")
    return summary


def _grouped_summary(results: list[dict[str, Any]], key: str) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for result in results:
        raw_value = result.get(key)
        group_key = str(raw_value) if raw_value is not None else "unknown"
        groups.setdefault(group_key, []).append(result)
    return {group_key: _summarize_subset(group_results) for group_key, group_results in sorted(groups.items())}


def _summarize_subset(results: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(results)
    scored_results = [result for result in results if not result["metrics"]["expected_inconsistency"]]
    inconsistency_results = [result for result in results if result["metrics"]["expected_inconsistency"]]

    parse_success_count = sum(1 for result in results if result["metrics"]["parse_success"])
    final_balance_sheet_matches_count = sum(1 for result in scored_results if result["metrics"]["final_balance_sheet_matches"])
    final_balance_sheet_and_journal_entries_match_count = sum(
        1 for result in scored_results if result["metrics"]["final_balance_sheet_and_journal_entries_match"]
    )
    final_journal_entries_match_count = sum(1 for result in scored_results if result["metrics"]["final_journal_entries_match"])
    final_journal_entries_match_no_doc_refs_count = sum(
        1 for result in scored_results if result["metrics"]["final_journal_entries_match_no_doc_refs"]
    )
    inconsistency_flag_match_count = sum(1 for result in inconsistency_results if result["metrics"]["inconsistency_flag_matches"])
    inconsistency_code_match_count = sum(1 for result in inconsistency_results if result["metrics"]["inconsistency_code_matches"])
    inconsistency_empty_answer_count = sum(1 for result in inconsistency_results if result["metrics"]["inconsistency_empty_answer"])

    return {
        "records_evaluated": total,
        "standard_records": len(scored_results),
        "inconsistency_records": len(inconsistency_results),
        "parse_success_count": parse_success_count,
        "parse_success_rate": _rate(parse_success_count, total),
        "final_balance_sheet_matches_rate": _rate(final_balance_sheet_matches_count, len(scored_results)) if scored_results else 0.0,
        "final_balance_sheet_and_journal_entries_match_rate": _rate(
            final_balance_sheet_and_journal_entries_match_count, len(scored_results)
        )
        if scored_results
        else 0.0,
        "final_journal_entries_match_rate": _rate(final_journal_entries_match_count, len(scored_results)) if scored_results else 0.0,
        "final_journal_entries_match_no_doc_refs_rate": _rate(final_journal_entries_match_no_doc_refs_count, len(scored_results))
        if scored_results
        else 0.0,
        "inconsistency_flag_match_rate": _rate(inconsistency_flag_match_count, len(inconsistency_results)),
        "inconsistency_code_match_rate": _rate(inconsistency_code_match_count, len(inconsistency_results)),
        "inconsistency_empty_answer_rate": _rate(inconsistency_empty_answer_count, len(inconsistency_results)),
    }
