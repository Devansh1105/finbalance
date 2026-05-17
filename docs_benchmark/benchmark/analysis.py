"""Diagnostic benchmark analysis helpers."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from typing import Any, Callable

from docs_benchmark.accounts import ACCOUNT_TYPES
from docs_benchmark.ledger import Ledger
from docs_benchmark.schemas import BalanceSheet, DocumentRecord, ParsedSubmission, Posting


ENTRY_STATUS_EXACT = "exact"
ENTRY_STATUS_DOC_REFS_MISMATCH = "doc_refs_mismatch"
ENTRY_STATUS_WRONG_AMOUNT = "wrong_amount"
ENTRY_STATUS_WRONG_ACCOUNT = "wrong_account"
ENTRY_STATUS_MISSING = "missing"
ENTRY_STATUS_EXTRA = "extra"

ENTRY_STATUS_ORDER = (
    ENTRY_STATUS_EXACT,
    ENTRY_STATUS_DOC_REFS_MISMATCH,
    ENTRY_STATUS_WRONG_AMOUNT,
    ENTRY_STATUS_WRONG_ACCOUNT,
    ENTRY_STATUS_MISSING,
    ENTRY_STATUS_EXTRA,
)

ENTRY_REASONING_SINGLE_DOC_VISIBLE = "single_doc_visible"
ENTRY_REASONING_MULTI_DOC_VISIBLE = "multi_doc_visible"
ENTRY_REASONING_DERIVED_COMPUTATION = "derived_computation"
ENTRY_REASONING_ADJUSTMENT_SUPPORT = "adjustment_support"

ENTRY_ERROR_FAMILY_EXACT = "exact"
ENTRY_ERROR_FAMILY_DOC_REF_LINKING = "doc_ref_linking"
ENTRY_ERROR_FAMILY_PARSE_OUTPUT = "parse_or_output"
ENTRY_ERROR_FAMILY_DIRECT_REASONING = "direct_doc_reasoning"
ENTRY_ERROR_FAMILY_DERIVED_REASONING = "derived_reasoning"
ENTRY_ERROR_FAMILY_EXTRA = "extra_predicted_entry"

DERIVED_LABEL_TOKENS = (
    "_cogs",
    "depreciation",
    "revenue_release",
    "retainer_release",
    "expense_accrual",
    "bad_debt_review",
    "bundled_contract_allocation",
    "fx_remeasurement",
    "asset_disposal",
    "deferred_tax",
    "baseline_lease",
    "lease_modification",
    "stock_adjustment",
    "inventory_adjustment",
    "material_issue",
    "finished_goods_transfer",
    "scrap_report",
    "overhead_accrual",
    "direct_labor",
)

LEDGER_FAMILY_RULES: tuple[tuple[str, Callable[[str], bool]], ...] = (
    ("tax", lambda label: label.endswith("_tax") or "tax" in label),
    ("foreign_exchange", lambda label: label.startswith("fx_")),
    ("payroll", lambda label: label.startswith("payroll_")),
    ("transfers", lambda label: "transfer" in label),
    ("reclassification", lambda label: label.startswith("reclassification_")),
    ("credits_and_returns", lambda label: "credit_memo" in label or label.startswith("return")),
    ("deferred_revenue", lambda label: "subscription_" in label or "retainer_" in label or label == "revenue_release"),
    ("deposits", lambda label: "security_deposit" in label or "deposit" in label),
    (
        "collections",
        lambda label: label in {"customer_payment", "tenant_payment", "copay_collection", "insurer_remittance"}
        or label.startswith("multi_invoice_payment_"),
    ),
    (
        "supplier_settlement",
        lambda label: label in {"supplier_payment", "vendor_payment"}
        or label.startswith("fx_supplier_payment")
        or label.startswith("fx_vendor_payment"),
    ),
    ("financing", lambda label: label.startswith("loan_")),
    ("depreciation", lambda label: label == "depreciation"),
    ("fixed_assets", lambda label: label.startswith("equipment_purchase") or label.startswith("asset_disposal")),
    ("leases", lambda label: label.startswith("baseline_lease") or label.startswith("lease_modification")),
    ("deferred_tax", lambda label: label.startswith("deferred_tax") or label.startswith("asset_disposal_with_deferred_tax")),
    (
        "inventory_and_cogs",
        lambda label: any(
            token in label
            for token in (
                "inventory_purchase",
                "stock_adjustment",
                "goods_receipt_purchase",
                "inventory_adjustment",
                "raw_material_purchase",
                "material_issue",
                "finished_goods_transfer",
                "finished_goods_sale_cogs",
                "overhead_accrual",
                "direct_labor",
                "retail_sale_cogs",
                "delivery_sale_cogs",
                "scrap_report",
            )
        ),
    ),
    (
        "billing",
        lambda label: any(
            token in label
            for token in (
                "service_invoice",
                "job_invoice",
                "patient_billing",
                "rent_roll",
                "delivery_sale_sale",
                "finished_goods_sale_sale",
                "reissued_invoice",
                "retail_sale_cash",
                "retail_sale_card",
                "subscription_invoice",
                "subscription_cash_invoice",
                "renewal_invoice",
                "bundled_contract_allocation",
            )
        ),
    ),
    (
        "accruals_and_prepaids",
        lambda label: any(
            token in label
            for token in (
                "expense_accrual",
                "prepaid_rent",
                "prepaid_insurance",
                "utilities_bill",
                "bad_debt_review",
                "revenue_release",
            )
        ),
    ),
    (
        "operating_expenses",
        lambda label: any(
            token in label
            for token in (
                "vendor_bill",
                "supplier_bill",
                "clinic_supplies_bill",
                "expense_receipt",
                "fuel_receipt",
                "hosting_bill",
                "maintenance_bill",
            )
        ),
    ),
)


def ledger_family_for_label(label: str) -> str:
    normalized = (label or "").strip().lower()
    if not normalized:
        return "unlabeled"
    for family, predicate in LEDGER_FAMILY_RULES:
        if predicate(normalized):
            return family
    return "other"


def posting_to_dict(posting: Posting) -> dict[str, Any]:
    return {
        "doc_refs": list(posting.doc_refs),
        "debit_account": posting.debit_account,
        "credit_account": posting.credit_account,
        "amount": float(posting.amount),
        "posting_date": posting.posting_date,
        "label": posting.label,
    }


def parsed_submission_to_dict(parsed: ParsedSubmission) -> dict[str, Any]:
    return {
        "has_inconsistency": parsed.has_inconsistency,
        "inconsistency_codes": list(parsed.inconsistency_codes),
        "inconsistency_notes": list(parsed.inconsistency_notes),
        "entries": [posting_to_dict(posting) for posting in parsed.entries],
        "balance_sheet": _balance_sheet_sections(parsed.balance_sheet),
    }


def serialize_balance_sheet(balance_sheet: BalanceSheet | dict[str, dict[str, float]]) -> dict[str, Any]:
    sections = _balance_sheet_sections(balance_sheet)
    assets_total = round(sum(sections["assets"].values()), 2)
    liabilities_total = round(sum(sections["liabilities"].values()), 2)
    equity_total = round(sum(sections["equity"].values()), 2)
    return {
        "assets": sections["assets"],
        "liabilities": sections["liabilities"],
        "equity": sections["equity"],
        "total_assets": assets_total,
        "total_liabilities": liabilities_total,
        "total_equity": equity_total,
        "balanced": abs(assets_total - (liabilities_total + equity_total)) < 0.01,
    }


def reconstruct_balance_sheet(record: DocumentRecord, entries: list[Posting]) -> BalanceSheet:
    ledger = Ledger(record.opening_balance)
    ledger.apply_all([entry for entry in entries if not _unknown_entry_accounts(entry)])
    return ledger.build_balance_sheet(record.period_end)


def analyze_submission(
    record: DocumentRecord,
    parsed: ParsedSubmission,
    *,
    parse_success: bool,
    amount_tol: float = 0.01,
    balance_tol: float = 0.01,
) -> dict[str, Any]:
    document_index = {
        document.doc_id: {"doc_type": document.doc_type, "role": document.role}
        for document in record.documents
    }
    predicted_balance_sheet = _balance_sheet_sections(parsed.balance_sheet)
    predicted_balance_sheet_serialized = serialize_balance_sheet(predicted_balance_sheet)
    invalid_account_entries = _invalid_account_entries(parsed.entries)
    invalid_accounts = sorted(
        {
            account
            for item in invalid_account_entries
            for account in item["unknown_accounts"]
        }
    )
    reconstructed_balance_sheet = reconstruct_balance_sheet(record, parsed.entries) if parse_success else reconstruct_balance_sheet(record, [])
    reconstructed_balance_sheet_serialized = serialize_balance_sheet(reconstructed_balance_sheet)

    if record.expected_inconsistency:
        output_clean = not parsed.entries and all(not section for section in predicted_balance_sheet.values())
        code_match = _code_match(record.expected_inconsistency_codes, parsed.inconsistency_codes)
        metrics = {
            "parse_success": bool(parse_success),
            "expected_inconsistency": True,
            "inconsistency_flag_matches": bool(parsed.has_inconsistency),
            "inconsistency_code_matches": bool(parsed.has_inconsistency and code_match),
            "inconsistency_empty_answer": bool(parsed.has_inconsistency and output_clean),
            "journal_entries_matched": False,
            "journal_entries_accounting_matched": False,
            "final_balance_sheet_matches": False,
            "final_balance_sheet_and_journal_entries_match": False,
            "final_journal_entries_match": False,
            "final_journal_entries_match_no_doc_refs": False,
            "entries_correct_but_final_balance_sheet_wrong": False,
            "entries_accounting_correct_but_doc_refs_wrong": False,
            "predicted_balance_sheet_matches_reconstructed_balance_sheet": False,
            "predicted_entries_reconstruct_correct_final_balance_sheet": False,
            "false_inconsistency_alarm": False,
            "missed_inconsistency": not parsed.has_inconsistency,
            "predicted_balance_sheet_balanced": predicted_balance_sheet_serialized["balanced"],
            "reconstructed_balance_sheet_balanced": reconstructed_balance_sheet_serialized["balanced"],
            "exact_entry_match_count": 0,
            "doc_refs_mismatch_count": 0,
            "wrong_amount_count": 0,
            "wrong_account_count": 0,
            "missing_entry_count": 0,
            "extra_entry_count": 0,
            "expected_entry_count": 0,
            "predicted_entry_count": len(parsed.entries),
            "invalid_account_entry_count": len(invalid_account_entries),
            "invalid_accounts": invalid_accounts,
            "entry_exact_posting_rate": 0.0,
            "entry_accounting_posting_rate": 0.0,
        }
        return {
            "metrics": metrics,
            "parsed_submission": parsed_submission_to_dict(parsed),
            "reconstructed_balance_sheet": reconstructed_balance_sheet_serialized,
            "entry_diagnostics": {
                "expected_entries": [],
                "predicted_entries": [],
                "invalid_account_entries": invalid_account_entries,
            },
        }

    expected_details, predicted_details = _match_entries(record.expected_entries, parsed.entries, amount_tol)
    for entry in expected_details:
        reasoning_type = _entry_reasoning_type(entry["posting"], document_index)
        entry["reasoning_type"] = reasoning_type
        entry["error_family"] = _entry_error_family(
            entry["status"],
            reasoning_type=reasoning_type,
            parse_success=parse_success,
        )
    for entry in predicted_details:
        entry["error_family"] = (
            ENTRY_ERROR_FAMILY_EXTRA if entry["status"] == ENTRY_STATUS_EXTRA else ENTRY_ERROR_FAMILY_EXACT
        )
    status_counts = Counter(item["status"] for item in expected_details)
    exact_match_count = status_counts[ENTRY_STATUS_EXACT]
    doc_refs_mismatch_count = status_counts[ENTRY_STATUS_DOC_REFS_MISMATCH]
    wrong_amount_count = status_counts[ENTRY_STATUS_WRONG_AMOUNT]
    wrong_account_count = status_counts[ENTRY_STATUS_WRONG_ACCOUNT]
    missing_entry_count = status_counts[ENTRY_STATUS_MISSING]
    extra_entry_count = sum(1 for item in predicted_details if item["status"] == ENTRY_STATUS_EXTRA)
    expected_entry_count = len(expected_details)
    predicted_entry_count = len(predicted_details)

    exact_entry_match = (
        expected_entry_count == exact_match_count
        and extra_entry_count == 0
        and predicted_entry_count == expected_entry_count
    )
    accounting_match = (
        expected_entry_count == exact_match_count + doc_refs_mismatch_count
        and wrong_amount_count == 0
        and wrong_account_count == 0
        and missing_entry_count == 0
        and extra_entry_count == 0
    )
    balance_sheet_match = _balance_sheet_exact_match(record.expected_balance_sheet, parsed.balance_sheet, balance_tol)
    reconstructed_balance_sheet_match = _balance_sheet_exact_match(record.expected_balance_sheet, reconstructed_balance_sheet, balance_tol)
    predicted_vs_reconstructed_match = _balance_sheet_exact_match(reconstructed_balance_sheet, parsed.balance_sheet, balance_tol)

    metrics = {
        "parse_success": bool(parse_success),
        "expected_inconsistency": False,
        "inconsistency_flag_matches": not parsed.has_inconsistency,
        "inconsistency_code_matches": not parsed.inconsistency_codes,
        "inconsistency_empty_answer": not parsed.has_inconsistency,
        "journal_entries_matched": exact_entry_match,
        "journal_entries_accounting_matched": accounting_match,
        "final_balance_sheet_matches": balance_sheet_match,
        "final_balance_sheet_and_journal_entries_match": bool(balance_sheet_match and exact_entry_match),
        "final_journal_entries_match": exact_entry_match,
        "final_journal_entries_match_no_doc_refs": accounting_match,
        "entries_correct_but_final_balance_sheet_wrong": bool(exact_entry_match and not balance_sheet_match),
        "entries_accounting_correct_but_doc_refs_wrong": bool(accounting_match and not exact_entry_match),
        "predicted_balance_sheet_matches_reconstructed_balance_sheet": predicted_vs_reconstructed_match,
        "predicted_entries_reconstruct_correct_final_balance_sheet": reconstructed_balance_sheet_match,
        "false_inconsistency_alarm": parsed.has_inconsistency,
        "missed_inconsistency": False,
        "predicted_balance_sheet_balanced": predicted_balance_sheet_serialized["balanced"],
        "reconstructed_balance_sheet_balanced": reconstructed_balance_sheet_serialized["balanced"],
        "exact_entry_match_count": exact_match_count,
        "doc_refs_mismatch_count": doc_refs_mismatch_count,
        "wrong_amount_count": wrong_amount_count,
        "wrong_account_count": wrong_account_count,
        "missing_entry_count": missing_entry_count,
        "extra_entry_count": extra_entry_count,
        "expected_entry_count": expected_entry_count,
        "predicted_entry_count": predicted_entry_count,
        "invalid_account_entry_count": len(invalid_account_entries),
        "invalid_accounts": invalid_accounts,
        "entry_exact_posting_rate": _rate(exact_match_count, expected_entry_count),
        "entry_accounting_posting_rate": _rate(exact_match_count + doc_refs_mismatch_count, expected_entry_count),
    }

    return {
        "metrics": metrics,
        "parsed_submission": parsed_submission_to_dict(parsed),
        "reconstructed_balance_sheet": reconstructed_balance_sheet_serialized,
        "entry_diagnostics": {
            "expected_entries": expected_details,
            "predicted_entries": predicted_details,
            "invalid_account_entries": invalid_account_entries,
        },
    }


def summarize_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    summary = summarize_result_subset(results)
    summary["by_difficulty"] = group_results_by_field(results, "difficulty_level")
    summary["by_period_type"] = group_results_by_field(results, "period_type")
    summary["by_industry"] = group_results_by_field(results, "industry")
    return summary


def summarize_result_subset(results: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(results)
    scored_results = [result for result in results if not result["metrics"]["expected_inconsistency"]]
    inconsistency_results = [result for result in results if result["metrics"]["expected_inconsistency"]]

    def _count(field: str, items: list[dict[str, Any]]) -> int:
        return sum(1 for result in items if result["metrics"].get(field))

    parse_success_count = _count("parse_success", results)
    exact_record_match_count = _count("journal_entries_matched", scored_results)
    accounting_record_match_count = _count("journal_entries_accounting_matched", scored_results)
    final_balance_sheet_matches_count = _count("final_balance_sheet_matches", scored_results)
    final_balance_sheet_and_journal_entries_match_count = _count("final_balance_sheet_and_journal_entries_match", scored_results)
    entries_correct_but_balance_sheet_wrong_count = _count("entries_correct_but_final_balance_sheet_wrong", scored_results)
    entries_accounting_correct_but_doc_refs_wrong_count = _count("entries_accounting_correct_but_doc_refs_wrong", scored_results)
    predicted_entries_reconstruct_correct_count = _count("predicted_entries_reconstruct_correct_final_balance_sheet", scored_results)
    predicted_balance_sheet_matches_reconstructed_count = _count("predicted_balance_sheet_matches_reconstructed_balance_sheet", scored_results)
    false_inconsistency_alarm_count = _count("false_inconsistency_alarm", scored_results)
    inconsistency_flag_match_count = _count("inconsistency_flag_matches", inconsistency_results)
    inconsistency_code_match_count = _count("inconsistency_code_matches", inconsistency_results)
    inconsistency_empty_answer_count = _count("inconsistency_empty_answer", inconsistency_results)
    missed_inconsistency_count = _count("missed_inconsistency", inconsistency_results)

    total_expected_entries = sum(result["metrics"]["expected_entry_count"] for result in scored_results)
    total_exact_entry_matches = sum(result["metrics"]["exact_entry_match_count"] for result in scored_results)
    total_doc_refs_mismatches = sum(result["metrics"]["doc_refs_mismatch_count"] for result in scored_results)
    total_wrong_amount = sum(result["metrics"]["wrong_amount_count"] for result in scored_results)
    total_wrong_account = sum(result["metrics"]["wrong_account_count"] for result in scored_results)
    total_missing = sum(result["metrics"]["missing_entry_count"] for result in scored_results)
    total_extra = sum(result["metrics"]["extra_entry_count"] for result in scored_results)
    total_predicted_entries = sum(result["metrics"]["predicted_entry_count"] for result in scored_results)
    total_invalid_account_entries = sum(result["metrics"].get("invalid_account_entry_count", 0) for result in results)
    invalid_accounts = sorted(
        {
            account
            for result in results
            for account in result["metrics"].get("invalid_accounts", [])
        }
    )

    total_cost = round(sum(float(result.get("cost", 0.0)) for result in results), 6)
    prompt_tokens = sum(int(result.get("prompt_tokens", 0)) for result in results)
    completion_tokens = sum(int(result.get("completion_tokens", 0)) for result in results)
    total_tokens = sum(int(result.get("total_tokens", 0)) for result in results)

    return {
        "records_evaluated": total,
        "standard_records": len(scored_results),
        "inconsistency_records": len(inconsistency_results),
        "parse_success_count": parse_success_count,
        "parse_success_rate": _rate(parse_success_count, total),
        "journal_entries_exact_record_match_rate": _rate(exact_record_match_count, len(scored_results)),
        "journal_entries_accounting_record_match_rate": _rate(accounting_record_match_count, len(scored_results)),
        "journal_entries_matched_rate": _rate(exact_record_match_count, len(scored_results)),
        "final_balance_sheet_matches_rate": _rate(final_balance_sheet_matches_count, len(scored_results)),
        "final_balance_sheet_and_journal_entries_match_rate": _rate(
            final_balance_sheet_and_journal_entries_match_count,
            len(scored_results),
        ),
        "final_journal_entries_match_rate": _rate(exact_record_match_count, len(scored_results)),
        "final_journal_entries_match_no_doc_refs_rate": _rate(accounting_record_match_count, len(scored_results)),
        "entry_exact_posting_rate": _rate(total_exact_entry_matches, total_expected_entries),
        "entry_accounting_posting_rate": _rate(total_exact_entry_matches + total_doc_refs_mismatches, total_expected_entries),
        "entries_correct_but_final_balance_sheet_wrong_rate": _rate(
            entries_correct_but_balance_sheet_wrong_count,
            len(scored_results),
        ),
        "entries_accounting_correct_but_doc_refs_wrong_rate": _rate(
            entries_accounting_correct_but_doc_refs_wrong_count,
            len(scored_results),
        ),
        "predicted_entries_reconstruct_correct_final_balance_sheet_rate": _rate(
            predicted_entries_reconstruct_correct_count,
            len(scored_results),
        ),
        "predicted_balance_sheet_matches_reconstructed_balance_sheet_rate": _rate(
            predicted_balance_sheet_matches_reconstructed_count,
            len(scored_results),
        ),
        "false_inconsistency_alarm_rate": _rate(false_inconsistency_alarm_count, len(scored_results)),
        "inconsistency_flag_match_rate": _rate(inconsistency_flag_match_count, len(inconsistency_results)),
        "inconsistency_code_match_rate": _rate(inconsistency_code_match_count, len(inconsistency_results)),
        "inconsistency_empty_answer_rate": _rate(inconsistency_empty_answer_count, len(inconsistency_results)),
        "missed_inconsistency_rate": _rate(missed_inconsistency_count, len(inconsistency_results)),
        "exact_entry_match_count": total_exact_entry_matches,
        "doc_refs_mismatch_count": total_doc_refs_mismatches,
        "wrong_amount_count": total_wrong_amount,
        "wrong_account_count": total_wrong_account,
        "missing_entry_count": total_missing,
        "extra_entry_count": total_extra,
        "expected_entry_count": total_expected_entries,
        "predicted_entry_count": total_predicted_entries,
        "invalid_account_entry_count": total_invalid_account_entries,
        "invalid_accounts": invalid_accounts,
        "average_missing_entries_per_standard_record": round(total_missing / len(scored_results), 2) if scored_results else 0.0,
        "average_extra_entries_per_standard_record": round(total_extra / len(scored_results), 2) if scored_results else 0.0,
        "cost_total": total_cost,
        "cost_average_per_record": round(total_cost / total, 6) if total else 0.0,
        "prompt_tokens_total": prompt_tokens,
        "completion_tokens_total": completion_tokens,
        "total_tokens": total_tokens,
    }


def group_results_by_field(results: list[dict[str, Any]], field: str) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in results:
        raw_value = result.get(field)
        if raw_value is None and "record_features" in result:
            raw_value = result["record_features"].get(field)
        group_key = str(raw_value) if raw_value not in (None, "") else "unknown"
        groups[group_key].append(result)
    return {group: summarize_result_subset(group_results) for group, group_results in sorted(groups.items())}


def group_results_by_membership(results: list[dict[str, Any]], field: str) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in results:
        values = result.get(field)
        if values is None and "record_features" in result:
            values = result["record_features"].get(field, [])
        for value in values or []:
            groups[str(value)].append(result)
    return {group: summarize_result_subset(group_results) for group, group_results in sorted(groups.items())}


def group_results_by_feature_flags(results: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in results:
        record_features = result.get("record_features", {})
        for key, value in record_features.items():
            if key.startswith("has_") and value:
                groups[key].append(result)
    return {group: summarize_result_subset(group_results) for group, group_results in sorted(groups.items())}


def summarize_expected_entry_groups(
    results: list[dict[str, Any]],
    group_name: str,
) -> dict[str, dict[str, Any]]:
    groups: dict[str, Counter[str]] = defaultdict(Counter)

    for result in results:
        document_index = result.get("document_index", {})
        for entry in result.get("entry_diagnostics", {}).get("expected_entries", []):
            status = entry["status"]
            error_family = entry.get(
                "error_family",
                _entry_error_family(
                    status,
                    reasoning_type=_entry_reasoning_type(entry["posting"], document_index),
                    parse_success=bool(result["metrics"].get("parse_success")),
                ),
            )
            posting = entry["posting"]
            keys: list[str]
            if group_name == "posting_label":
                label = posting.get("label") or "unlabeled"
                keys = [str(label)]
            elif group_name == "ledger_family":
                keys = [ledger_family_for_label(str(posting.get("label", "")))]
            elif group_name == "doc_type":
                keys = sorted(
                    {
                        str(document_index.get(doc_ref, {}).get("doc_type", "unknown"))
                        for doc_ref in posting.get("doc_refs", [])
                    }
                ) or ["unknown"]
            else:
                raise ValueError(f"Unsupported expected-entry group '{group_name}'")

            for key in keys:
                groups[key]["expected_entries"] += 1
                groups[key][status] += 1
                groups[key][error_family] += 1

    summary: dict[str, dict[str, Any]] = {}
    for key, counter in sorted(groups.items()):
        expected_entries = counter["expected_entries"]
        exact = counter[ENTRY_STATUS_EXACT]
        accounting = exact + counter[ENTRY_STATUS_DOC_REFS_MISMATCH]
        failure_counts = {
            ENTRY_ERROR_FAMILY_PARSE_OUTPUT: counter[ENTRY_ERROR_FAMILY_PARSE_OUTPUT],
            ENTRY_ERROR_FAMILY_DOC_REF_LINKING: counter[ENTRY_ERROR_FAMILY_DOC_REF_LINKING],
            ENTRY_ERROR_FAMILY_DIRECT_REASONING: counter[ENTRY_ERROR_FAMILY_DIRECT_REASONING],
            ENTRY_ERROR_FAMILY_DERIVED_REASONING: counter[ENTRY_ERROR_FAMILY_DERIVED_REASONING],
        }
        dominant_failure_mode = max(failure_counts.items(), key=lambda item: item[1])[0]
        summary[key] = {
            "expected_entries": expected_entries,
            "exact_entry_rate": _rate(exact, expected_entries),
            "accounting_entry_rate": _rate(accounting, expected_entries),
            "doc_refs_mismatch_rate": _rate(counter[ENTRY_STATUS_DOC_REFS_MISMATCH], expected_entries),
            "wrong_amount_rate": _rate(counter[ENTRY_STATUS_WRONG_AMOUNT], expected_entries),
            "wrong_account_rate": _rate(counter[ENTRY_STATUS_WRONG_ACCOUNT], expected_entries),
            "missing_rate": _rate(counter[ENTRY_STATUS_MISSING], expected_entries),
            "parse_or_output_failure_rate": _rate(counter[ENTRY_ERROR_FAMILY_PARSE_OUTPUT], expected_entries),
            "doc_ref_linking_failure_rate": _rate(counter[ENTRY_ERROR_FAMILY_DOC_REF_LINKING], expected_entries),
            "direct_doc_reasoning_failure_rate": _rate(counter[ENTRY_ERROR_FAMILY_DIRECT_REASONING], expected_entries),
            "derived_reasoning_failure_rate": _rate(counter[ENTRY_ERROR_FAMILY_DERIVED_REASONING], expected_entries),
            "exact_entry_count": exact,
            "doc_refs_mismatch_count": counter[ENTRY_STATUS_DOC_REFS_MISMATCH],
            "wrong_amount_count": counter[ENTRY_STATUS_WRONG_AMOUNT],
            "wrong_account_count": counter[ENTRY_STATUS_WRONG_ACCOUNT],
            "missing_count": counter[ENTRY_STATUS_MISSING],
            "parse_or_output_failure_count": counter[ENTRY_ERROR_FAMILY_PARSE_OUTPUT],
            "doc_ref_linking_failure_count": counter[ENTRY_ERROR_FAMILY_DOC_REF_LINKING],
            "direct_doc_reasoning_failure_count": counter[ENTRY_ERROR_FAMILY_DIRECT_REASONING],
            "derived_reasoning_failure_count": counter[ENTRY_ERROR_FAMILY_DERIVED_REASONING],
            "dominant_failure_mode": dominant_failure_mode if failure_counts[dominant_failure_mode] else "none",
        }
    return summary


def _rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return round(numerator / denominator, 4)


def _unknown_entry_accounts(posting: Posting) -> list[str]:
    return [
        account
        for account in (posting.debit_account, posting.credit_account)
        if account not in ACCOUNT_TYPES
    ]


def _invalid_account_entries(entries: list[Posting]) -> list[dict[str, Any]]:
    invalid_entries = []
    for index, posting in enumerate(entries):
        unknown_accounts = _unknown_entry_accounts(posting)
        if unknown_accounts:
            invalid_entries.append(
                {
                    "index": index,
                    "unknown_accounts": unknown_accounts,
                    "posting": posting_to_dict(posting),
                }
            )
    return invalid_entries


def _amount_key(posting: Posting, amount_tol: float) -> int:
    if amount_tol <= 0:
        return int(round(posting.amount * 100))
    return int(round(posting.amount / amount_tol))


def _entry_key_with_refs(posting: Posting, amount_tol: float) -> tuple[Any, ...]:
    return posting.key(amount_tol)


def _entry_key_without_refs(posting: Posting, amount_tol: float) -> tuple[Any, ...]:
    return (posting.debit_account, posting.credit_account, _amount_key(posting, amount_tol))


def _entry_key_same_accounts(posting: Posting) -> tuple[Any, ...]:
    return (tuple(sorted(posting.doc_refs)), posting.debit_account, posting.credit_account)


def _entry_key_same_doc_amount(posting: Posting, amount_tol: float) -> tuple[Any, ...]:
    return (tuple(sorted(posting.doc_refs)), _amount_key(posting, amount_tol))


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


def _code_match(expected_codes: list[str], predicted_codes: list[str]) -> bool:
    return set(expected_codes) == set(predicted_codes)


def _match_entries(expected_entries: list[Posting], predicted_entries: list[Posting], amount_tol: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    expected = [
        {"index": index, "posting": posting, "status": "unmatched", "matched_predicted_index": None}
        for index, posting in enumerate(expected_entries)
    ]
    predicted = [
        {"index": index, "posting": posting, "status": "unmatched", "matched_expected_index": None}
        for index, posting in enumerate(predicted_entries)
    ]

    _apply_matches(expected, predicted, lambda posting: _entry_key_with_refs(posting, amount_tol), ENTRY_STATUS_EXACT)
    _apply_matches(expected, predicted, lambda posting: _entry_key_without_refs(posting, amount_tol), ENTRY_STATUS_DOC_REFS_MISMATCH)
    _apply_matches(expected, predicted, _entry_key_same_accounts, ENTRY_STATUS_WRONG_AMOUNT)
    _apply_matches(expected, predicted, lambda posting: _entry_key_same_doc_amount(posting, amount_tol), ENTRY_STATUS_WRONG_ACCOUNT)

    for item in expected:
        if item["status"] == "unmatched":
            item["status"] = ENTRY_STATUS_MISSING
    for item in predicted:
        if item["status"] == "unmatched":
            item["status"] = ENTRY_STATUS_EXTRA

    expected_payload = [
        {
            "index": item["index"],
            "status": item["status"],
            "posting": posting_to_dict(item["posting"]),
            "matched_predicted_index": item["matched_predicted_index"],
        }
        for item in expected
    ]
    predicted_payload = [
        {
            "index": item["index"],
            "status": item["status"],
            "posting": posting_to_dict(item["posting"]),
            "matched_expected_index": item["matched_expected_index"],
        }
        for item in predicted
    ]
    return expected_payload, predicted_payload


def _apply_matches(
    expected: list[dict[str, Any]],
    predicted: list[dict[str, Any]],
    key_fn: Callable[[Posting], Any],
    status: str,
) -> None:
    predicted_lookup: dict[Any, deque[dict[str, Any]]] = defaultdict(deque)
    for item in predicted:
        if item["status"] == "unmatched":
            predicted_lookup[key_fn(item["posting"])].append(item)

    for item in expected:
        if item["status"] != "unmatched":
            continue
        match_queue = predicted_lookup.get(key_fn(item["posting"]))
        if not match_queue:
            continue
        matched = match_queue.popleft()
        item["status"] = status
        item["matched_predicted_index"] = matched["index"]
        matched["status"] = status
        matched["matched_expected_index"] = item["index"]


def _entry_reasoning_type(posting: dict[str, Any], document_index: dict[str, dict[str, str]]) -> str:
    label = str(posting.get("label", "")).strip().lower()
    if any(token in label for token in DERIVED_LABEL_TOKENS):
        return ENTRY_REASONING_DERIVED_COMPUTATION
    doc_roles = [
        str(document_index.get(doc_ref, {}).get("role", "unknown"))
        for doc_ref in posting.get("doc_refs", [])
    ]
    if any(role in {"adjustment_doc", "support_doc"} for role in doc_roles) and not any(role == "posting_doc" for role in doc_roles):
        return ENTRY_REASONING_ADJUSTMENT_SUPPORT
    posting_doc_count = sum(1 for role in doc_roles if role == "posting_doc")
    if posting_doc_count <= 1 and len(posting.get("doc_refs", [])) <= 1:
        return ENTRY_REASONING_SINGLE_DOC_VISIBLE
    if posting_doc_count >= 1:
        return ENTRY_REASONING_MULTI_DOC_VISIBLE
    return ENTRY_REASONING_ADJUSTMENT_SUPPORT


def _entry_error_family(status: str, *, reasoning_type: str, parse_success: bool) -> str:
    if status == ENTRY_STATUS_EXACT:
        return ENTRY_ERROR_FAMILY_EXACT
    if status == ENTRY_STATUS_DOC_REFS_MISMATCH:
        return ENTRY_ERROR_FAMILY_DOC_REF_LINKING
    if not parse_success:
        return ENTRY_ERROR_FAMILY_PARSE_OUTPUT
    if reasoning_type in {ENTRY_REASONING_DERIVED_COMPUTATION, ENTRY_REASONING_ADJUSTMENT_SUPPORT}:
        return ENTRY_ERROR_FAMILY_DERIVED_REASONING
    return ENTRY_ERROR_FAMILY_DIRECT_REASONING
