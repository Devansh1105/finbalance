"""Generate human-readable verification packets from the dataset.

Run from the repo root:
    python human_verification/generate_samples.py

This picks a stratified sample across difficulty, industry, period type, and
standard/inconsistency status, then writes one Markdown file per record so an
accounting expert can read and verify without touching JSON.

The script regenerates `samples/`, `sample_manifest.json`, and
`verification_responses.md` from scratch — so changing the targets below
keeps every artifact in sync.
"""

from __future__ import annotations

import json
import random
import shutil
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = REPO_ROOT / "data" / "coverage" / "records.jsonl"
OUTPUT_DIR = Path(__file__).resolve().parent / "samples"
MANIFEST_PATH = Path(__file__).resolve().parent / "sample_manifest.json"
RESPONSES_PATH = Path(__file__).resolve().parent / "verification_responses.md"

TARGET_STANDARD_PER_LEVEL = 12
TARGET_INCONSISTENCY = 15
RANDOM_SEED = 42


def load_records() -> list[dict]:
    with DATASET_PATH.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def stratified_sample(records: list[dict]) -> list[dict]:
    rng = random.Random(RANDOM_SEED)
    standard_by_level: dict[int, list[dict]] = defaultdict(list)
    inconsistency: list[dict] = []
    for record in records:
        if record.get("expected_inconsistency"):
            inconsistency.append(record)
        else:
            standard_by_level[int(record["difficulty_level"])].append(record)

    selected: list[dict] = []
    for level in sorted(standard_by_level):
        bucket = list(standard_by_level[level])
        rng.shuffle(bucket)
        by_industry: dict[str, list[dict]] = defaultdict(list)
        for record in bucket:
            by_industry[record["industry"]].append(record)
        industries = sorted(by_industry)
        cursors = {industry: 0 for industry in industries}
        picks: list[dict] = []
        while len(picks) < TARGET_STANDARD_PER_LEVEL:
            progressed = False
            for industry in industries:
                if len(picks) >= TARGET_STANDARD_PER_LEVEL:
                    break
                cursor = cursors[industry]
                if cursor < len(by_industry[industry]):
                    picks.append(by_industry[industry][cursor])
                    cursors[industry] = cursor + 1
                    progressed = True
            if not progressed:
                break
        selected.extend(picks)

    rng.shuffle(inconsistency)
    seen_codes: set[str] = set()
    inconsistency_picks: list[dict] = []
    remaining: list[dict] = []
    for record in inconsistency:
        codes = tuple(record.get("expected_inconsistency_codes", []))
        if codes and codes not in seen_codes and len(inconsistency_picks) < TARGET_INCONSISTENCY:
            inconsistency_picks.append(record)
            seen_codes.add(codes)
        else:
            remaining.append(record)
    if len(inconsistency_picks) < TARGET_INCONSISTENCY:
        inconsistency_picks.extend(remaining[: TARGET_INCONSISTENCY - len(inconsistency_picks)])
    selected.extend(inconsistency_picks)
    return selected


def format_money(value: float) -> str:
    return f"{value:,.2f}"


def render_balance_sheet(bs: dict) -> str:
    lines = []
    for section in ("assets", "liabilities", "equity"):
        entries = bs.get(section, {})
        if not entries:
            continue
        lines.append(f"**{section.title()}**")
        for account, amount in entries.items():
            lines.append(f"- {account}: {format_money(float(amount))}")
        lines.append("")
    total_assets = float(bs.get("total_assets", 0.0))
    total_liab = float(bs.get("total_liabilities", 0.0))
    total_eq = float(bs.get("total_equity", 0.0))
    lines.append(f"**Totals:** Assets = {format_money(total_assets)}; Liabilities = {format_money(total_liab)}; Equity = {format_money(total_eq)}")
    lines.append(f"**Balanced (A = L + E):** {bs.get('balanced', False)}")
    return "\n".join(lines)


def render_opening_balance(ob: dict) -> str:
    lines = [f"_As of {ob.get('date', '?')}_", ""]
    for section in ("assets", "liabilities", "equity"):
        entries = ob.get(section, {})
        if not entries:
            continue
        lines.append(f"**{section.title()}**")
        for account, amount in entries.items():
            lines.append(f"- {account}: {format_money(float(amount))}")
        lines.append("")
    return "\n".join(lines)


def render_document(document: dict) -> str:
    title = document.get("title", "")
    doc_type = document.get("doc_type", "")
    role = document.get("role", "")
    doc_id = document.get("doc_id", "")
    date = document.get("date", "")
    ocr = document.get("ocr_text", "").strip() or "(empty OCR text)"
    return (
        f"### Document {doc_id} — {title}\n\n"
        f"- **Type:** `{doc_type}`\n"
        f"- **Role:** `{role}`\n"
        f"- **Date:** {date}\n\n"
        f"```\n{ocr}\n```\n"
    )


def render_entries(entries: list[dict]) -> str:
    if not entries:
        return "_(no expected entries — packet is labeled inconsistent)_"
    lines = ["| # | Debit | Credit | Amount | Doc refs | Posting date | Label |", "|---|---|---|---:|---|---|---|"]
    for index, entry in enumerate(entries, start=1):
        doc_refs = ", ".join(entry.get("doc_refs", []))
        lines.append(
            f"| {index} | {entry['debit_account']} | {entry['credit_account']} | "
            f"{format_money(float(entry['amount']))} | {doc_refs} | "
            f"{entry.get('posting_date','')} | {entry.get('label','')} |"
        )
    return "\n".join(lines)


def render_record(record: dict) -> str:
    md = []
    rid = record["record_id"]
    md.append(f"# Verification Packet — {rid}\n")
    md.append(
        "_Read the documents in section 4. Then check whether the "
        "expected journal entries in section 5 and the expected balance sheet in section 6 are "
        "what you would book given those documents. Use the form at the bottom._\n"
    )

    md.append("## 1. Record Context\n")
    metadata = record.get("metadata", {})
    md.append(f"- **Industry:** `{record['industry']}`")
    md.append(f"- **Difficulty level (1–5):** {record['difficulty_level']}")
    md.append(f"- **Period type:** {metadata.get('period_type', '?')}")
    md.append(f"- **Period label:** {metadata.get('period_label', '?')}")
    md.append(f"- **Period start → end:** {record['period_start']} → {record['period_end']}")
    md.append(f"- **Entity:** {metadata.get('entity_name', 'Unknown Entity')}")
    md.append(f"- **Currency (display / functional):** {metadata.get('currency_code', 'USD')} / {metadata.get('functional_currency_code', metadata.get('currency_code', 'USD'))}")
    md.append(f"- **Tax regime:** `{metadata.get('tax_regime', 'none')}`")
    md.append(f"- **Document count:** {len(record['documents'])}")
    md.append(f"- **Labeled as inconsistent:** {record.get('expected_inconsistency', False)}")
    if record.get("expected_inconsistency"):
        md.append(f"- **Inconsistency codes:** {', '.join(record.get('expected_inconsistency_codes', []))}")
        if record.get("inconsistency_reasons"):
            md.append(f"- **Inconsistency reasons:** {'; '.join(record['inconsistency_reasons'])}")
    md.append("")

    md.append("## 2. Allowed Account Names\n")
    md.append("_These are the only account names the model is allowed to use._\n")
    md.append(", ".join(f"`{name}`" for name in record.get("allowed_accounts", [])))
    md.append("")

    md.append("## 3. Opening Trial Balance\n")
    md.append(render_opening_balance(record["opening_balance"]))
    md.append("")

    md.append("## 4. Documents in this packet\n")
    md.append(
        "_Each document has a role. `posting_doc` directly creates one or more journal entries. "
        "`support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is "
        "for period-end adjustments. `distractor_doc` should NOT generate any entries. "
        "`opening_trial_balance` is starting state only._\n"
    )
    for document in record["documents"]:
        md.append(render_document(document))

    md.append("## 5. Expected Journal Entries (ground truth)\n")
    md.append(render_entries(record.get("expected_entries", [])))
    md.append("")

    md.append("## 6. Expected Final Balance Sheet (ground truth)\n")
    if record.get("expected_inconsistency"):
        md.append("_Packet is labeled inconsistent — the expected balance sheet should be empty._\n")
    md.append(render_balance_sheet(record["expected_balance_sheet"]))
    md.append("")

    md.append("---\n")
    md.append("## 7. Verification Form\n")
    md.append(
        "_Fill in your judgement below. For each question, mark one box and add notes where applicable._\n"
    )
    md.append(
        "### Q1 — Document analogy to real paperwork\n"
        "We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. "
        "Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?\n"
        "- [ ] Yes — analogous to what an accountant would receive\n"
        "- [ ] Mostly — captures the right information, with rough edges\n"
        "- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent\n"
        "- Notes:\n"
    )
    md.append(
        "### Q2 — Are the expected journal entries correct?\n"
        "Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?\n"
        "- [ ] Yes — entries match what I would book\n"
        "- [ ] Mostly — minor account / amount issues (please describe)\n"
        "- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)\n"
        "- Notes:\n"
    )
    md.append(
        "### Q3 — Are entries complete?\n"
        "Are there any entries you would book that are MISSING from section 5? Or any entries in section 5 that should NOT be there?\n"
        "- [ ] Complete and exact\n"
        "- [ ] Missing entries (list them in notes)\n"
        "- [ ] Extra entries that should not be booked (list them)\n"
        "- Notes:\n"
    )
    md.append(
        "### Q4 — Are document references correct?\n"
        "For each expected entry, is `doc_refs` the set of documents that actually support that posting?\n"
        "- [ ] Yes, doc_refs are correct\n"
        "- [ ] Mostly correct with minor mismatches\n"
        "- [ ] Doc_refs are systematically wrong\n"
        "- Notes:\n"
    )
    md.append(
        "### Q5 — Difficulty calibration\n"
        "Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.\n"
        "- [ ] Calibration feels right\n"
        "- [ ] Too easy for this level\n"
        "- [ ] Too hard for this level\n"
        "- Notes:\n"
    )
    if record.get("expected_inconsistency"):
        md.append(
            "### Q6 — Inconsistency validity (inconsistency packets only)\n"
            f"Is the labeled contradiction (codes: `{', '.join(record.get('expected_inconsistency_codes', []))}`) actually present in the documents and would prevent a clean reconciliation?\n"
            "- [ ] Yes, the contradiction is real and would block reconciliation\n"
            "- [ ] Contradiction is real but the code(s) don't quite fit\n"
            "- [ ] No clear contradiction visible — this packet looks reconcilable\n"
            "- Notes:\n"
        )
    md.append(
        "### Q7 — Overall verdict\n"
        "- [ ] Acceptable as ground truth for benchmark evaluation\n"
        "- [ ] Acceptable with minor fixes (notes below)\n"
        "- [ ] Not acceptable as ground truth\n"
        "- Notes:\n"
    )

    return "\n".join(md)


def write_samples(records: list[dict]) -> list[dict]:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    width = max(2, len(str(len(records))))
    manifest_rows: list[dict] = []
    for index, record in enumerate(records, start=1):
        label = "INC" if record.get("expected_inconsistency") else "STD"
        filename = (
            f"{index:0{width}d}_{label}_L{record['difficulty_level']}_"
            f"{record['industry']}_{record['record_id']}.md"
        )
        path = OUTPUT_DIR / filename
        path.write_text(render_record(record), encoding="utf-8")
        manifest_rows.append(
            {
                "verification_index": index,
                "filename": filename,
                "record_id": record["record_id"],
                "industry": record["industry"],
                "difficulty_level": record["difficulty_level"],
                "period_type": record.get("metadata", {}).get("period_type"),
                "expected_inconsistency": bool(record.get("expected_inconsistency")),
                "inconsistency_codes": list(record.get("expected_inconsistency_codes", [])),
                "document_count": len(record["documents"]),
                "expected_entry_count": len(record.get("expected_entries", [])),
            }
        )
    return manifest_rows


def render_responses_template(rows: list[dict]) -> str:
    lines: list[str] = [
        "# Verification Responses — Consolidated Form\n",
        "_Use this file if you'd rather record all responses in one place instead of editing each `samples/*.md`. Either format is fine._\n",
        "---\n",
        "## Reviewer info\n",
        "- **Name / role:**",
        "- **Date completed:**",
        "- **Total records reviewed:**",
        "- **Time spent (hours):**\n",
        "---\n",
        "## Systematic issues (call out once, not per record)\n",
        "_If you notice a pattern across multiple records (e.g. \"all SaaS records use a deferred-revenue account that should really be deferred income\"), note it here._\n",
        "-\n",
        "---\n",
        "## Per-record responses\n",
        "_For each record below, fill in the verdict. The full record content is in `samples/<filename>.md`._\n",
    ]
    for row in rows:
        label = "INC" if row["expected_inconsistency"] else "STD"
        header = (
            f"### {row['verification_index']:02d} — {label} L{row['difficulty_level']} "
            f"{row['industry']} — `{row['record_id']}`"
        )
        lines.append(header)
        lines.append(f"_File:_ `samples/{row['filename']}`")
        lines.append("")
        lines.append("- Q1 Document analogy: [ ] Analogous   [ ] Mostly   [ ] Not analogous — notes:")
        lines.append("- Q2 Entries correct: [ ] Yes   [ ] Mostly   [ ] No — notes:")
        lines.append("- Q3 Entries complete: [ ] Complete   [ ] Missing   [ ] Extra — notes:")
        lines.append("- Q4 Doc_refs correct: [ ] Yes   [ ] Mostly   [ ] No — notes:")
        lines.append("- Q5 Difficulty calibration: [ ] Right   [ ] Too easy   [ ] Too hard — notes:")
        if row["expected_inconsistency"]:
            lines.append(
                "- Q6 Inconsistency validity: [ ] Real contradiction   [ ] Real but wrong code   [ ] No visible contradiction — notes:"
            )
        lines.append("- Q7 Overall: [ ] Accept   [ ] Accept w/ fixes   [ ] Reject — notes:\n")

    lines.extend(
        [
            "---\n",
            "## Aggregate verdict\n",
            "_Optional — your overall sense after reviewing all records._\n",
            "- Overall, the synthetic dataset is acceptable as a benchmark ground truth: [ ] Yes   [ ] With fixes   [ ] No",
            "- The single biggest concern you'd want addressed before publication:",
            "- Anything else we should know:",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    records = load_records()
    selected = stratified_sample(records)
    rows = write_samples(selected)
    MANIFEST_PATH.write_text(
        json.dumps(
            {
                "dataset": str(DATASET_PATH.relative_to(REPO_ROOT)),
                "seed": RANDOM_SEED,
                "standard_per_level_target": TARGET_STANDARD_PER_LEVEL,
                "inconsistency_target": TARGET_INCONSISTENCY,
                "sample_size": len(rows),
                "samples": rows,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    RESPONSES_PATH.write_text(render_responses_template(rows), encoding="utf-8")
    print(f"Wrote {len(rows)} verification packets to {OUTPUT_DIR}")
    print(f"Wrote manifest to {MANIFEST_PATH}")
    print(f"Wrote consolidated responses template to {RESPONSES_PATH}")


if __name__ == "__main__":
    main()
