"""Generate the full FinBalance paper figure set."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from finbalance.figures.diagrams import (
    diagram_dataset_packet,
    diagram_generation_inference,
    flow_codebase_pipeline,
    flow_record_generation_detail,
)
from finbalance.figures.plots import (
    plot_ablation_deltas,
    plot_aggregation_gap,
    plot_context_stress,
    plot_dataset_composition,
    plot_failure_slices,
    plot_model_accuracy,
    plot_two_model_context_deltas,
    plot_verifier_model_deltas,
    plot_verifier_transfer,
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
        ("aggregation_gap", lambda: plot_aggregation_gap(results_root, out_root, min_records=min_model_records)),
        ("ablation_deltas", lambda: plot_ablation_deltas(results_root, out_root)),
        ("verifier_model_deltas", lambda: plot_verifier_model_deltas(results_root, out_root, min_records=min_model_records)),
        ("two_model_context_deltas", lambda: plot_two_model_context_deltas(results_root, out_root, min_records=min_model_records)),
        ("context_stress", lambda: plot_context_stress(results_root, out_root)),
        ("verifier_transfer", lambda: plot_verifier_transfer(results_root, out_root, min_records=min_model_records)),
        ("dataset_composition", lambda: plot_dataset_composition(dataset_file, out_root)),
        ("failure_slices", lambda: plot_failure_slices(results_root, out_root)),
        ("dataset_packet_diagram", lambda: diagram_dataset_packet(out_root)),
        ("generation_inference_diagram", lambda: diagram_generation_inference(out_root)),
        ("codebase_pipeline_flow", lambda: flow_codebase_pipeline(out_root)),
        ("record_generation_flow", lambda: flow_record_generation_detail(out_root)),
    ]
    for name, task in tasks:
        paths = task()
        if paths:
            generated[name] = [str(path) for path in paths]

    index_path = out_root / "figure_index.json"
    index_path.write_text(json.dumps(generated, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    generated["index"] = [str(index_path)]
    return generated
