"""Generate the full FinBalance paper figure set."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from finbalance.figures.diagrams import (
    diagram_dataset_packet,
    diagram_generation_inference,
    flow_codebase_pipeline,
)
from finbalance.figures.plots import (
    plot_ablation_deltas,
    plot_aggregation_gap,
    plot_concept_heatmap,
    plot_context_stress,
    plot_cost_pareto,
    plot_dataset_composition,
    plot_difficulty_trend,
    plot_doc_refs_persistence,
    plot_failure_slices,
    plot_gap_repair_comparison,
    plot_model_accuracy,
    plot_results_heatmap,
    plot_verifier_inconsistency_tradeoff,
    plot_verifier_model_deltas,
)


def generate_all_figures(
    *,
    results_dir: str | Path = "results",
    dataset_path: str | Path = "data/coverage/records.jsonl",
    output_dir: str | Path = "paper/figures",
    min_model_records: int = 100,
) -> dict[str, list[str]]:
    results_root = Path(results_dir)
    dataset_file = Path(dataset_path)
    out_root = Path(output_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    generated: dict[str, list[str]] = {}
    tasks: list[tuple[str, Callable[[], list[Path]]]] = [
        ("model_accuracy", lambda: plot_model_accuracy(results_root, out_root, min_records=min_model_records)),
        ("results_heatmap", lambda: plot_results_heatmap(results_root, out_root, min_records=min_model_records)),
        ("aggregation_gap", lambda: plot_aggregation_gap(results_root, out_root, min_records=min_model_records)),
        ("ablation_deltas", lambda: plot_ablation_deltas(results_root, out_root)),
        ("verifier_model_deltas", lambda: plot_verifier_model_deltas(results_root, out_root, min_records=min_model_records)),
        ("verifier_inconsistency_tradeoff", lambda: plot_verifier_inconsistency_tradeoff(results_root, out_root, min_records=min_model_records)),
        ("doc_refs_persistence", lambda: plot_doc_refs_persistence(results_root, out_root)),
        ("gap_repair_comparison", lambda: plot_gap_repair_comparison(results_root, out_root)),
        ("difficulty_trend", lambda: plot_difficulty_trend(results_root, out_root)),
        ("context_stress", lambda: plot_context_stress(results_root, out_root)),
        ("dataset_composition", lambda: plot_dataset_composition(dataset_file, out_root)),
        ("failure_slices", lambda: plot_failure_slices(results_root, out_root)),
        ("concept_heatmap", lambda: plot_concept_heatmap(results_root, out_root, min_records=min_model_records)),
        ("cost_pareto", lambda: plot_cost_pareto(results_root, out_root, min_records=min_model_records)),
        ("dataset_packet_diagram", lambda: diagram_dataset_packet(out_root)),
        ("generation_inference_diagram", lambda: diagram_generation_inference(out_root)),
        ("codebase_pipeline_flow", lambda: flow_codebase_pipeline(out_root)),
    ]
    for name, task in tasks:
        paths = task()
        if paths:
            generated[name] = [str(path) for path in paths]

    index_path = out_root / "figure_index.json"
    index_path.write_text(json.dumps(generated, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    generated["index"] = [str(index_path)]
    return generated
