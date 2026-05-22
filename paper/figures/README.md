# FinBalance Paper Figures

Generated figures are written as both PDF and PNG:

- `fig_model_accuracy`: multi-model headline metric comparison.
- `fig_aggregation_gap`: reported balance sheet versus replayed-entry balance sheet.
- `fig_ablation_deltas`: Gemini 3 Flash ablation deltas versus baseline.
- `fig_context_stress`: evidence-only and distractor/context-ordering ablations.
- `fig_verifier_transfer`: forced ledger-verifier replication across available models.
- `fig_dataset_composition`: coverage-set composition.
- `fig_failure_slices`: industry, ledger-family, and error-taxonomy slices.
- `diag_dataset_packet`: conceptual record packet diagram.
- `diag_generation_inference`: deterministic generation versus inverse inference diagram.
- `flow_codebase_pipeline`: package-level pipeline flow.
- `flow_record_generation_detail`: appendix record-generation flow.

Regenerate all figures from repo root:

```bash
python scripts/generate_paper_figures.py \
  --dataset data/coverage/records.jsonl \
  --results-dir results \
  --output-dir paper/figures
```

Use the PDF files in LaTeX when possible; the PNG files are previews.

