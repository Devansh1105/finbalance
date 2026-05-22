# `_archive/` — FinBalance v1 Legacy

This folder contains the **FinBalance v1** submission to **COLM 2026** plus all
supporting code, data, results, figures, and scripts. It is preserved here for
reference only.

The current repo root is **FinBalance v2** — a different and strictly broader
benchmark for multi-document accounting reconciliation, targeting EMNLP. v2
supersedes v1; the only assets carried forward are the bibliography, the LaTeX
preamble and macros, and the prior-work comparison table template (now living
in the new `paper/` directory).

## Contents

| Path | What it is |
|---|---|
| `finbalance_v1/` | v1 Python package (ledger generator, evaluation harness, baselines, analysis) |
| `data_v1/` | v1 synthetic datasets — `dev.jsonl`, `test.jsonl`, `full.jsonl`, `large500.jsonl`, `sample*.jsonl` |
| `figures_v1/` | v1 publication figures F1–F8 (capability curve, error composition, CoT effect, etc.) |
| `paper_v1/` | v1 COLM 2026 TEX source, compiled PDFs (`final.pdf`, `review.pdf`), references, notes |
| `results_v1/` | v1 model outputs (~45 JSONs) — zero-shot + CoT runs across 7 model families |
| `scripts_v1/` | v1 scripts (dataset generation, baseline runs, deep analysis, figure generation) |
| `results_report_v1.txt` | v1 executive summary of headline findings |
| `README_v1.md` | v1 repo README (the original 53KB documentation) |

## Status

- v1 received mixed COLM 2026 reviews and is being withdrawn / not pursued
  further. Authors pivoted to v2 (multi-document reconciliation) for EMNLP.
- Nothing in this folder is on the Python path. v2 code does **not** import
  from here.
- Treat as read-only. If anything in here needs to be revived, copy it out;
  do not modify in place.

## Why keep it?

- The v1 work informed v2's design (concept flags, deterministic ledger, etc.).
- Cross-paper analysis in the v2 Discussion section may reference v1 results
  (e.g., "models achieve X on clean-input BS construction but only Y on
  document-grounded reconciliation").
- COLM rebuttal / withdrawal correspondence may still need the artifacts.
