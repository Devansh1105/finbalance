# FinBalance Paper Figures

Generated figures are written as both PDF and PNG:

- `fig_model_accuracy`: multi-model headline metric comparison.
- `fig_aggregation_gap`: reported balance sheet versus replayed-entry balance sheet.
- `fig_ablation_deltas`: Gemini 3 Flash ablation deltas versus baseline.
- `fig_verifier_model_deltas`: forced ledger-verifier deltas for models where verifier runs exist.
- `fig_verifier_inconsistency_tradeoff`: verifier gains on BS exact versus its inconsistency-code downside.
- `fig_doc_refs_persistence`: citation-prompt negative result versus evidence-only oracle retrieval.
- `fig_gap_repair_comparison`: self-consistency selection versus forced verifier on the same targeted gap records.
- `fig_difficulty_trend`: baseline and verifier performance by difficulty level.
- `fig_context_stress`: evidence-only and distractor/context-ordering ablations.
- `fig_dataset_composition`: coverage-set composition.
- `fig_failure_slices`: multi-model industry, ledger-family, and error-taxonomy heatmaps.
- `fig_concept_heatmap`: multi-model accuracy by accounting concept flag.
- `fig_cost_pareto`: cost-per-record versus BS exact accuracy.
- `diag_dataset_packet`: conceptual record packet diagram.
- `diag_generation_inference`: deterministic generation versus inverse inference diagram.
- `flow_codebase_pipeline`: package-level pipeline flow.

Regenerate all figures from repo root:

```bash
python scripts/generate_paper_figures.py \
  --dataset data/coverage/records.jsonl \
  --results-dir results \
  --output-dir paper/figures
```

Use the PDF files in LaTeX when possible; the PNG files are previews.
