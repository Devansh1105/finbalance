# v1 Assets Worth Considering for v2 Paper

Items in `_archive/` that *might* be useful during paper writing. Reviewed during
the refactor; deliberately NOT auto-copied, but flagged here so they don't get
forgotten if reviewers ask or a new section idea emerges.

## v1 metrics implementation
- `_archive/finbalance_v1/evaluation/metrics/core.py` — v1 BA / ALA / FBS scoring.
- **Use only if** we want a calibration row like: "On the simpler clean-input
  task (v1), top model achieves FBS 90.9; on the document-grounded task (v2),
  top model achieves \bsexact{} only 0.575."

## v1 rule-based oracle baseline
- `_archive/finbalance_v1/baselines/rule_based.py` — deterministic solver for v1.
- **Use only if** we add a "perfect-extraction baseline" experiment to v2: skip
  the OCR / document-understanding stage entirely, hand the model the ground-truth
  entries, then measure the BS aggregation. Would isolate the aggregation gap
  cleanly from document-understanding noise.

## v1 deep analysis JSON
- `_archive/results_v1/deep_analysis.json` — aggregated v1 results across 6 models.
- **Use only if** we add a 1-sentence cross-paper observation in Section 7
  (Discussion).

## v1 figures
- `_archive/figures_v1/F8_dataset_complexity.pdf` — the only v1 figure with a
  conceptually transferable axis (difficulty stratification). Don't reuse the
  figure itself; reuse the concept.
- F1–F7 are all v1-specific findings (capability curve, CoT effect, retained-
  earnings heatmap, etc.) — leave behind.

## v1 LaTeX content
- `_archive/paper_v1/sections/01a_related_work.tex` — has clean framing of
  "comprehension vs construction" that may inform our intro paragraph. Don't
  copy verbatim; the v2 framing should emphasize document-grounding and
  inconsistency detection on top.
- `_archive/paper_v1/figures/benchmark_overview.tex` — v1 pipeline diagram.
  v2 pipeline is structurally different (OCR → extraction → reconciliation),
  so build a new figure.

## What's NOT useful

- v1 generation code, transaction templates, scripts, model outputs — all tied
  to the clean-entry task. Different scope.
- v1 dataset (`_archive/data_v1/*.jsonl`) — different schema, no carry-over.
