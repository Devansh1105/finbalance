# Human Verification — finbalance Synthetic Dataset

This folder contains 75 expert-reviewed records sampled from the benchmark dataset, rendered as plain Markdown so an accounting expert can read and verify the ground truth **without touching any JSON or code**.

> **Note on framing:** the benchmark's ground truth is computed by deterministic ledger replay once the chart of accounts, accounting policies, tax/FX assumptions, scenario schemas, and document templates are fixed. Your validation is therefore **about whether the documents are a reasonable analogue of what an accountant would normally receive, plus account-choice conventions, difficulty calibration, and inconsistency validity** — not about whether the paperwork is pixel-perfect, and not about catching arithmetic errors in the ledger.
>
> We are **not** aiming for documents that look exactly like real-world invoices, bank statements, or schedules. We are aiming for analogues — paperwork that carries roughly the same information content (parties, dates, amounts, line items, references) that an accountant would extract from the real equivalent. Please judge from that angle.

## What we need from you

For each record in `samples/`, decide whether:

1. **The documents are a reasonable analogue** of what an accountant would receive for that industry and reporting period — i.e. they carry the right kind of information, not that they look pixel-perfect.
2. **The "expected journal entries"** are the entries you would actually book given only those documents.
3. **The "expected balance sheet"** is what those entries should produce.
4. **The labeled inconsistency** (for inconsistency packets) is a real contradiction.

Each Markdown file contains a verification form at the bottom — just check the boxes and add notes. **No coding, no JSON, no command line required.**

## How to use this folder

1. Open `samples/01_STD_L1_..._.md` in any Markdown viewer (VS Code, Obsidian, GitHub web, or just a text editor).
2. Read sections 1–6 (record context, opening trial balance, documents, expected entries, expected balance sheet).
3. Fill in the form in section 7 by checking boxes and writing free-text notes.
4. Save the file back when done. You can also copy your responses into `verification_responses.md` if you prefer one consolidated file (template provided).

## How the sample was selected

- **60 standard packets** — spanning all five difficulty levels and all eight industries.
- **15 inconsistency packets** — covering 15 inconsistency codes and spanning difficulty levels.
- The original candidate pool was generated deterministically (seed = 42); this release folder keeps the records with completed expert review. To regenerate a fresh candidate pool, edit the constants at the top of `generate_samples.py` and re-run:
  ```bash
  python human_verification/generate_samples.py
  ```
- See `sample_manifest.json` for the exact list of record IDs, difficulty levels, industries, and inconsistency codes covered.

## Completed review artifacts

- The paper analysis uses this intended assignment: Reviewer 1 records 1–50;
  Reviewer 2 records 1–25 and 51–75.
- The independent overlap used for agreement is records 1–25. The remaining
  records give single-expert coverage over records 26–75.
- Collection folders may contain duplicate files outside this assignment; those
  are retained for auditability but are not used in the reported agreement table.

## What each record's file contains

Every Markdown file has 7 sections:

| Section | Contents |
|---|---|
| 1. Record context | Industry, period, currency, tax regime, difficulty level, doc count, inconsistency flag |
| 2. Allowed account names | The closed set of account names the benchmark's model is restricted to |
| 3. Opening trial balance | Starting position before the period |
| 4. Documents in this packet | Every document with its OCR text, type, and role (posting / support / adjustment / distractor) |
| 5. Expected journal entries | Ground truth entries the model should produce |
| 6. Expected final balance sheet | Ground truth ending balance sheet |
| 7. Verification form | Your checkboxes + notes |

## Key concepts (one-screen primer)

- **Document role:**
  - `posting_doc` — directly generates one or more journal entries (e.g. an invoice).
  - `support_doc` — provides inputs (rate cards, schedules, tax certificates) for postings derived from other documents. May appear in `doc_refs` of an entry.
  - `adjustment_doc` — period-end corrections (depreciation schedules, accruals).
  - `distractor_doc` — should NOT generate any entries; included to test whether the model is robust to irrelevant paperwork.
  - `opening_trial_balance` — starting balances only; never generates entries.
- **`doc_refs` field on each expected entry:** lists the document IDs that support that posting. A "Cash receipt applied to invoice INV-001" might list both the payment notice and the original invoice.
- **Inconsistency packets:** these have `Labeled as inconsistent: True` and have empty `expected_entries` / `expected_balance_sheet`. They contain a deliberate contradiction (e.g. bank closing balance doesn't tie to the listed transactions). The labeled `inconsistency_codes` say which contradiction the generator placed.
- **Difficulty levels:** L1 trivial single-thread postings; L5 contains multi-document dependencies, jurisdictional tax rules, ASC 606, leases, deferred tax, or asset disposals.

## What to flag

We're specifically looking for the following failure modes — please call them out in the form's notes:

1. **Wrong account.** The generator picked an account that an accountant would not use here.
2. **Wrong amount.** The math doesn't tie to the source document's numbers.
3. **Wrong direction.** Debit and credit are reversed for the transaction type.
4. **Missing entry.** A document clearly implies an entry that isn't in the ground truth.
5. **Extra entry.** An entry is booked that shouldn't be (e.g. from a distractor doc).
6. **Wrong doc_refs.** The supporting documents listed for an entry aren't the right ones.
7. **Inconsistency packet is actually reconcilable.** The labeled contradiction isn't visible / isn't a real contradiction.
8. **Difficulty mis-calibrated.** L5 packet feels like L2, or vice versa.

If you find a systematic issue (e.g. "every property_management record uses `Revenue` instead of `Rental Revenue`"), please note it once in `verification_responses.md` rather than repeating it on every record.
