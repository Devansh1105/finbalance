"""Post-hoc structural-invariant audit over generated FinBalance records.

Independently re-checks every record in a dataset JSONL against the invariants
the paper claims hold by construction, without calling the generator's own
validation gate:

  1.  unique visible document ids
  2.  document dates inside the record period
  3.  every posting doc_ref resolves to a visible document
  4.  posting accounts inside the allowed-account list and global taxonomy
  5.  positive posting amounts, distinct debit/credit accounts
  6.  balance-sheet section totals equal the sum of their line items
  7.  reported balanced flag consistent with assets = liabilities + equity
  8.  ledger replay (standard records): applying the expected entries to the
      opening balance with an independent double-entry implementation
      reproduces the expected balance sheet account-by-account
  9.  label convention: standard records carry no inconsistency codes;
      forced-inconsistency records carry at least one code from the released
      23-code taxonomy together with the empty gold entries and empty gold
      balance sheet that signal "flag, do not reconcile"

Pass rates are reported overall and per industry x period x difficulty cell.

Usage:
    uv run python scripts/audit_structural_invariants.py <records.jsonl> [--csv out.csv]
"""

from __future__ import annotations

import argparse
import collections
import json
import sys

from finbalance.accounts import ACCOUNT_TYPES, DEBIT_NORMAL_TYPES
from finbalance.inconsistencies import INCONSISTENCY_CODES

TOLERANCE = 0.02

CHECKS = [
    "unique_doc_ids",
    "doc_dates_in_period",
    "doc_refs_resolve",
    "accounts_allowed",
    "postings_well_formed",
    "section_totals_consistent",
    "balanced_flag_consistent",
    "ledger_replay_matches",
    "inconsistency_labels_valid",
]


def _replay(record: dict) -> dict[str, float]:
    """Independent double-entry replay of expected entries over the opening balance."""
    balances: dict[str, float] = {}
    opening = record["opening_balance"]
    for section in ("assets", "liabilities", "equity"):
        for account, value in opening.get(section, {}).items():
            balances[account] = round(float(value), 2)
    for entry in record["expected_entries"]:
        amount = round(float(entry["amount"]), 2)
        for account, sign in ((entry["debit_account"], 1), (entry["credit_account"], -1)):
            effect = amount if ACCOUNT_TYPES.get(account) in DEBIT_NORMAL_TYPES else -amount
            balances[account] = round(balances.get(account, 0.0) + sign * effect, 2)
    return balances


def _replayed_balance_sheet(balances: dict[str, float]) -> dict[str, dict[str, float]]:
    sections: dict[str, dict[str, float]] = {"assets": {}, "liabilities": {}, "equity": {}}
    revenue_total = 0.0
    expense_total = 0.0
    for account, balance in balances.items():
        account_type = ACCOUNT_TYPES.get(account)
        if account_type == "revenue":
            revenue_total += balance
            continue
        if account_type == "expense":
            expense_total += balance
            continue
        rendered = -balance if account_type == "contra_asset" else balance
        if abs(rendered) <= 0.004:
            continue
        section = {"asset": "assets", "contra_asset": "assets", "liability": "liabilities", "equity": "equity"}[
            account_type
        ]
        sections[section][account] = round(rendered, 2)
    retained = round(revenue_total - expense_total, 2)
    if abs(retained) > 0.004:
        sections["equity"]["Retained Earnings"] = round(
            sections["equity"].get("Retained Earnings", 0.0) + retained, 2
        )
    return sections


def audit_record(record: dict) -> dict[str, bool]:
    results: dict[str, bool] = {}
    documents = record["documents"]
    doc_ids = [doc["doc_id"] for doc in documents]
    results["unique_doc_ids"] = len(doc_ids) == len(set(doc_ids))
    results["doc_dates_in_period"] = all(
        record["period_start"] <= doc["date"] <= record["period_end"] for doc in documents
    )

    doc_id_set = set(doc_ids)
    entries = record["expected_entries"]
    results["doc_refs_resolve"] = all(ref in doc_id_set for entry in entries for ref in entry["doc_refs"])

    allowed = set(record["allowed_accounts"])
    results["accounts_allowed"] = all(
        entry[side] in allowed and entry[side] in ACCOUNT_TYPES
        for entry in entries
        for side in ("debit_account", "credit_account")
    )
    results["postings_well_formed"] = all(
        entry["amount"] > 0 and entry["debit_account"] != entry["credit_account"] for entry in entries
    )

    bs = record["expected_balance_sheet"]
    section_ok = all(
        abs(sum(bs[section].values()) - bs[f"total_{section}"]) <= TOLERANCE
        for section in ("assets", "liabilities", "equity")
    )
    results["section_totals_consistent"] = section_ok
    identity_gap = abs(bs["total_assets"] - (bs["total_liabilities"] + bs["total_equity"]))
    results["balanced_flag_consistent"] = bs["balanced"] == (identity_gap <= TOLERANCE)

    codes = record.get("expected_inconsistency_codes", [])
    if record.get("expected_inconsistency"):
        # Gold convention for forced-inconsistency records: flag, do not reconcile.
        results["ledger_replay_matches"] = not entries and not any(
            bs[section] for section in ("assets", "liabilities", "equity")
        )
        results["inconsistency_labels_valid"] = len(codes) > 0 and all(c in INCONSISTENCY_CODES for c in codes)
    else:
        replayed = _replayed_balance_sheet(_replay(record))
        replay_ok = True
        for section in ("assets", "liabilities", "equity"):
            expected_section = bs[section]
            replayed_section = replayed[section]
            accounts = set(expected_section) | set(replayed_section)
            for account in accounts:
                if abs(expected_section.get(account, 0.0) - replayed_section.get(account, 0.0)) > TOLERANCE:
                    replay_ok = False
        results["ledger_replay_matches"] = replay_ok
        results["inconsistency_labels_valid"] = len(codes) == 0
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", help="Path to dataset JSONL")
    parser.add_argument("--csv", help="Optional per-cell CSV output path")
    args = parser.parse_args()

    per_check = collections.Counter()
    per_cell: dict[tuple, list[int]] = collections.defaultdict(lambda: [0, 0])
    failures: list[tuple[str, str]] = []
    n = 0

    with open(args.records) as fh:
        for line in fh:
            record = json.loads(line)
            n += 1
            results = audit_record(record)
            all_ok = all(results.values())
            for check, ok in results.items():
                per_check[check] += ok
            kind = "INC" if record.get("expected_inconsistency") else "STD"
            cell = (
                record["industry"],
                record["metadata"]["period_type"],
                record["difficulty_level"],
                kind,
            )
            per_cell[cell][0] += all_ok
            per_cell[cell][1] += 1
            if not all_ok:
                failed = [check for check, ok in results.items() if not ok]
                failures.append((record["record_id"], ",".join(failed)))

    print(f"records audited: {n}")
    for check in CHECKS:
        print(f"  {check}: {per_check[check]}/{n} ({per_check[check] / n:.2%})")
    total_pass = sum(passed for passed, _ in per_cell.values())
    print(f"all-invariant pass rate: {total_pass}/{n} ({total_pass / n:.2%})")
    print(f"cells covered: {len(per_cell)}")
    imperfect = {cell: (p, t) for cell, (p, t) in per_cell.items() if p != t}
    print(f"cells with any failure: {len(imperfect)}")
    for cell, (passed, total) in sorted(imperfect.items()):
        print(f"  {cell}: {passed}/{total}")
    for record_id, failed in failures[:20]:
        print(f"  FAIL {record_id}: {failed}")

    if args.csv:
        with open(args.csv, "w") as out:
            out.write("industry,period_type,difficulty,kind,passed,total\n")
            for (industry, period, level, kind), (passed, total) in sorted(per_cell.items()):
                out.write(f"{industry},{period},{level},{kind},{passed},{total}\n")
        print(f"per-cell CSV written to {args.csv}")


if __name__ == "__main__":
    main()
