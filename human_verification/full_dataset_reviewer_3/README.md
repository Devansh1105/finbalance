# Full-Dataset Human Review Packets

This folder contains Markdown verification packets for an accounting expert to
review without touching JSON or code.

## Scope

- Dataset: `data/coverage/records.jsonl`
- Records: 143
- Standard records: 120
- Forced-inconsistency records: 23

Each file in `samples/` contains the record context, allowed accounts,
opening trial balance, document OCR text, ground-truth journal entries,
ground-truth balance sheet, and a verification form.

## Reviewer Workflow

1. Open files in `samples/` in order.
2. Read sections 1-6.
3. Fill in section 7 in each file, or use `verification_responses.md` as one
   consolidated response sheet.
4. Save completed files in this folder.

## What To Check

- Whether the documents are a reasonable analogue of real reconciliation
  paperwork for the industry and period.
- Whether the expected journal entries are correct and complete.
- Whether `doc_refs` cite the documents that actually support each entry.
- Whether the final balance sheet follows from the entries.
- For forced-inconsistency records, whether the contradiction is visible and
  would block a clean reconciliation.

See `sample_manifest.json` for record IDs, difficulty levels, industries,
document counts, and inconsistency codes.
