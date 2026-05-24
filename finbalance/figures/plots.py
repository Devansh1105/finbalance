"""Quantitative plots for the FinBalance paper."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from finbalance.figures.data import (
    ResultRun,
    doc_ref_mismatch_rate,
    load_ablation_group,
    load_default_baselines,
    load_default_gemini_ablation_rows,
    load_result_run,
    load_records,
    load_verifier_pairs,
    record_ids_for_run,
    subset_run_for_record_ids,
)
from finbalance.figures.style import (
    ABLATION_LABELS,
    BLUE,
    DARK,
    GRAY,
    GREEN,
    LIGHT_GRAY,
    METRIC_LABELS,
    ORANGE,
    PALETTE,
    PURPLE,
    RED,
    TEAL,
    PANEL,
    apply_style,
    pct,
    save_figure,
    short_label,
    wrap_display_label,
    wrap_label,
)


MODEL_METRICS = (
    "predicted_entries_reconstruct_correct_final_balance_sheet_rate",
    "final_balance_sheet_matches_rate",
    "final_journal_entries_match_no_doc_refs_rate",
    "final_balance_sheet_and_journal_entries_match_rate",
)

ABLATION_METRICS = (
    "predicted_entries_reconstruct_correct_final_balance_sheet_rate",
    "final_balance_sheet_matches_rate",
    "final_journal_entries_match_no_doc_refs_rate",
    "final_balance_sheet_and_journal_entries_match_rate",
)


def plot_model_accuracy(results_dir: Path, output_dir: Path, *, min_records: int = 100) -> list[Path]:
    apply_style()
    runs = load_default_baselines(results_dir, min_records=min_records)
    if not runs:
        return []
    runs = sorted(runs, key=lambda run: run.metric("final_balance_sheet_matches_rate"), reverse=True)

    labels = [run.label for run in runs]
    x = np.arange(len(runs))
    width = 0.18
    fig, ax = plt.subplots(figsize=(7.2, 3.7))

    for idx, metric in enumerate(MODEL_METRICS):
        values = [100 * run.metric(metric) for run in runs]
        offsets = x + (idx - 1.5) * width
        bars = ax.bar(
            offsets,
            values,
            width=width,
            color=PALETTE[idx],
            label=METRIC_LABELS[metric],
            edgecolor="white",
            linewidth=0.6,
        )
        for bar, value in zip(bars, values, strict=False):
            if value >= 7:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    value + 1.2,
                    f"{value:.0f}",
                    ha="center",
                    va="bottom",
                    fontsize=6.5,
                    color=DARK,
                )

    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(0, 105)
    ax.set_xticks(x)
    ax.set_xticklabels([wrap_display_label(label, 13) for label in labels])
    record_counts = sorted({run.records for run in runs})
    suffix = f" (n={record_counts[0]} records)" if len(record_counts) == 1 else ""
    ax.set_title(f"Model Accuracy on FinBalance Coverage Set{suffix}")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.19), ncol=4, frameon=False)
    return save_figure(fig, output_dir, "fig_model_accuracy")


def plot_aggregation_gap(results_dir: Path, output_dir: Path, *, min_records: int = 100) -> list[Path]:
    apply_style()
    runs = load_default_baselines(results_dir, min_records=min_records)
    if not runs:
        return []

    runs = sorted(
        runs,
        key=lambda run: run.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate")
        - run.metric("final_balance_sheet_matches_rate"),
        reverse=True,
    )
    y = np.arange(len(runs))
    recon = np.array([100 * run.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate") for run in runs])
    exact = np.array([100 * run.metric("final_balance_sheet_matches_rate") for run in runs])
    gaps = recon - exact

    fig, ax = plt.subplots(figsize=(7.0, 3.9))
    for idx, (left, right, gap) in enumerate(zip(exact, recon, gaps, strict=True)):
        ax.plot([left, right], [idx, idx], color=LIGHT_GRAY, linewidth=4, solid_capstyle="round", zorder=1)
        ax.text(max(left, right) + 2, idx, f"{gap:+.1f} pp", va="center", fontsize=8, color=GRAY)
    ax.scatter(exact, y, s=46, color=ORANGE, label="BS_exact", zorder=3)
    ax.scatter(recon, y, s=46, color=BLUE, label="BS recon", zorder=4)
    ax.set_yticks(y)
    ax.set_yticklabels([run.label for run in runs])
    ax.invert_yaxis()
    ax.set_xlim(0, max(75, float(max(recon.max(), exact.max()) + 15)))
    ax.set_xlabel("Record-level accuracy (%)")
    ax.set_title("Aggregation Gap Across Baseline Models")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False)
    ax.grid(axis="y", visible=False)
    fig.subplots_adjust(bottom=0.24)
    return save_figure(fig, output_dir, "fig_aggregation_gap")


def plot_ablation_deltas(results_dir: Path, output_dir: Path) -> list[Path]:
    apply_style()
    rows = load_default_gemini_ablation_rows(results_dir)
    if not rows:
        return []

    preferred_order = [
        "forced_ledger_verifier",
        "forced_ledger_verifier_2pass",
        "self_consistency_k3",
        "prompt_doc_refs_strict",
        "evidence_only",
        "evidence_plus_15_distractors",
        "visibility_support_docs_removed",
        "visibility_no_allowed_accounts",
    ]
    by_name = {row["ablation"]: row for row in rows}
    ordered = [by_name[name] for name in preferred_order if name in by_name]
    if not ordered:
        return []

    labels = [ABLATION_LABELS.get(row["ablation"], short_label(row["ablation"])) for row in ordered]
    labels = [label.replace("Forced verifier x2", "Verifier 2-pass").replace("Self-consistency k=3", "Best-of-3 selection") for label in labels]
    y = np.arange(len(ordered))
    metrics = [
        ("final_balance_sheet_matches_rate", "BS exact", ORANGE),
        ("predicted_entries_reconstruct_correct_final_balance_sheet_rate", "BS recon", BLUE),
    ]

    fig, ax = plt.subplots(figsize=(3.55, 3.15))
    ax.axvline(0, color=GRAY, linewidth=0.8)
    for metric_idx, (metric, label, color) in enumerate(metrics):
        yy = y + (metric_idx - 0.5) * 0.18
        deltas = [100 * (row["run"].metric(metric) - row["baseline"].metric(metric)) for row in ordered]
        ax.scatter(deltas, yy, s=30, color=color, label=label, zorder=3)
        for delta, yyy in zip(deltas, yy, strict=True):
            if abs(delta) >= 8:
                ax.text(
                    delta + (1.2 if delta >= 0 else -1.2),
                    yyy,
                    f"{delta:+.0f}",
                    va="center",
                    ha="left" if delta >= 0 else "right",
                    fontsize=6.2,
                    color=color,
                    weight="bold",
                )
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Effect vs. baseline (pp)")
    ax.set_xlim(-55, 42)
    ax.grid(axis="y", visible=False)
    ax.legend(loc="lower right", frameon=False, fontsize=7)
    fig.subplots_adjust(left=0.44, right=0.98, bottom=0.16, top=0.98)
    return save_figure(fig, output_dir, "fig_ablation_deltas")


def plot_verifier_model_deltas(results_dir: Path, output_dir: Path, *, min_records: int = 100) -> list[Path]:
    apply_style()
    model_dirs = [
        ("Gemini 3 Flash", "gemini3flash_promoted_coverage_full_clean"),
        ("DeepSeek V3.2", "deepseek_v32_sweep"),
        ("Qwen3 235B", "qwen3_235b_sweep_baseline"),
        ("Claude Haiku 4.5", "claude_haiku45_sweep_baseline"),
    ]
    metrics = [
        ("final_balance_sheet_matches_rate", "Delta BS exact (pp)"),
        ("predicted_entries_reconstruct_correct_final_balance_sheet_rate", "Delta BS recon (pp)"),
    ]
    model_colors = {
        "Gemini 3 Flash": BLUE,
        "DeepSeek V3.2": ORANGE,
        "Qwen3 235B": TEAL,
        "Claude Haiku 4.5": PURPLE,
    }

    observations: list[dict[str, Any]] = []
    for label, relative in model_dirs:
        runs = load_ablation_group(results_dir, relative)
        baseline = runs.get("prompt_baseline")
        verifier = runs.get("forced_ledger_verifier")
        if not baseline or not verifier:
            continue
        if baseline.records < min_records or verifier.records < min_records:
            continue
        observations.append(
            {
                "model": label,
                "final_balance_sheet_matches_rate": 100
                * (verifier.metric("final_balance_sheet_matches_rate") - baseline.metric("final_balance_sheet_matches_rate")),
                "predicted_entries_reconstruct_correct_final_balance_sheet_rate": 100
                * (
                    verifier.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate")
                    - baseline.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate")
                ),
            }
        )
    if not observations:
        return []

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.7), sharey=True)
    y = np.arange(len(observations))
    model_labels = [wrap_display_label(str(row["model"]), 14) for row in observations]
    for ax, (metric, title) in zip(axes, metrics, strict=True):
        values = [float(row[metric]) for row in observations]
        colors = [model_colors.get(str(row["model"]), GRAY) for row in observations]
        ax.axvline(0, color=GRAY, linewidth=0.8)
        bars = ax.barh(y, values, color=colors, edgecolor="white", linewidth=0.6)
        for bar, value in zip(bars, values, strict=False):
            ax.text(
                value + (1.1 if value >= 0 else -1.1),
                bar.get_y() + bar.get_height() / 2,
                f"{value:+.0f}",
                ha="left" if value >= 0 else "right",
                va="center",
                fontsize=7,
                color=DARK,
            )
        ax.set_yticks(y)
        ax.set_yticklabels(model_labels)
        ax.set_title(title)
        ax.set_xlim(-8, 36)
        ax.set_xlabel("Delta from baseline")
        ax.grid(axis="y", visible=False)
    axes[0].set_ylabel("Model")
    axes[0].invert_yaxis()
    fig.suptitle("Forced Ledger Verifier Deltas Across Models", y=1.03, fontsize=10.5, fontweight="bold")
    fig.subplots_adjust(wspace=0.16)
    return save_figure(fig, output_dir, "fig_verifier_model_deltas")


def plot_verifier_inconsistency_tradeoff(
    results_dir: Path,
    output_dir: Path,
    *,
    min_records: int = 100,
) -> list[Path]:
    apply_style()
    pairs = load_verifier_pairs(results_dir, min_records=min_records)
    if not pairs:
        return []

    labels = [label for label, _, _ in pairs]
    baseline = [100 * base.metric("inconsistency_code_match_rate") for _, base, _ in pairs]
    verifier = [100 * ver.metric("inconsistency_code_match_rate") for _, _, ver in pairs]
    x = np.arange(len(pairs))
    width = 0.32
    fig, ax = plt.subplots(figsize=(6.7, 3.5))
    ax.bar(x - width / 2, baseline, width=width, color=BLUE, label="Baseline", edgecolor="white", linewidth=0.6)
    ax.bar(x + width / 2, verifier, width=width, color=RED, label="Forced verifier", edgecolor="white", linewidth=0.6)
    for idx, (base_value, ver_value) in enumerate(zip(baseline, verifier, strict=True)):
        delta = ver_value - base_value
        ax.text(
            idx,
            max(base_value, ver_value) + 3.0,
            f"{delta:+.0f} pp",
            ha="center",
            va="bottom",
            fontsize=7,
            color=RED if delta < 0 else GREEN,
        )
    ax.set_ylabel("Inconsistency code match (%)")
    ax.set_ylim(0, 108)
    ax.set_xticks(x)
    ax.set_xticklabels([wrap_display_label(label, 13) for label in labels])
    ax.set_title("Ledger Verifier Trade-off on Inconsistency Detection")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False)
    return save_figure(fig, output_dir, "fig_verifier_inconsistency_tradeoff")


def plot_doc_refs_persistence(results_dir: Path, output_dir: Path) -> list[Path]:
    apply_style()
    runs = load_ablation_group(results_dir, "gemini3flash_promoted_coverage_full_clean")
    selected = [
        ("Baseline", runs.get("prompt_baseline"), BLUE),
        ("Citation prompt", runs.get("prompt_doc_refs_strict"), ORANGE),
        ("Evidence only", runs.get("evidence_only"), TEAL),
    ]
    selected = [(label, run, color) for label, run, color in selected if run]
    if len(selected) < 2:
        return []

    labels = [label for label, _, _ in selected]
    values = [100 * doc_ref_mismatch_rate(run) for _, run, _ in selected]
    colors = [color for _, _, color in selected]
    baseline = values[0]
    fig, ax = plt.subplots(figsize=(3.35, 2.45))
    bars = ax.bar(np.arange(len(values)), values, color=colors, edgecolor="white", linewidth=0.6)
    for idx, (bar, value) in enumerate(zip(bars, values, strict=True)):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 1.5,
            f"{value:.1f}%",
            ha="center",
            va="bottom",
            fontsize=7,
            color=DARK,
        )
        if idx > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                max(2.0, value - 5.0),
                f"{value - baseline:+.1f} pp",
                ha="center",
                va="center",
                fontsize=7,
                color="white" if value > 24 else DARK,
                weight="bold",
            )
    ax.set_ylabel("Entry-level doc-ref mismatch (%)")
    ax.set_ylim(0, max(62, max(values) + 12))
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels([wrap_display_label(label, 13) for label in labels])
    ax.grid(axis="x", visible=False)
    return save_figure(fig, output_dir, "fig_doc_refs_persistence")


def plot_gap_repair_comparison(results_dir: Path, output_dir: Path) -> list[Path]:
    apply_style()
    self_consistency = load_result_run(
        results_dir / "gemini3flash_self_consistency_gap" / "self_consistency_k3",
        label="Best-of-3",
    )
    promoted = load_ablation_group(results_dir, "gemini3flash_promoted_coverage_full_clean")
    baseline = promoted.get("prompt_baseline")
    verifier = promoted.get("forced_ledger_verifier")
    if not self_consistency or not baseline or not verifier:
        return []

    target_ids = record_ids_for_run(self_consistency)
    baseline_subset = subset_run_for_record_ids(baseline, target_ids, label="One-shot baseline")
    verifier_subset = subset_run_for_record_ids(verifier, target_ids, label="Forced verifier")
    if not baseline_subset or not verifier_subset:
        return []

    runs = [
        ("One-shot baseline", baseline_subset, GRAY),
        ("Best-of-3 selection", self_consistency, TEAL),
        ("Forced verifier", verifier_subset, RED),
    ]
    values = [100 * run.metric("final_balance_sheet_matches_rate") for _, run, _ in runs]
    recon_values = [100 * run.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate") for _, run, _ in runs]
    x = np.arange(len(runs))
    fig, ax = plt.subplots(figsize=(3.35, 2.45))
    bars = ax.bar(x, values, color=[color for _, _, color in runs], edgecolor="white", linewidth=0.6)
    ax.plot(x, recon_values, color=BLUE, marker="o", linewidth=1.8, label="BS recon")
    for idx, (bar, value) in enumerate(zip(bars, values, strict=True)):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 2.0,
            f"{value:.0f}%",
            ha="center",
            va="bottom",
            fontsize=7,
            color=DARK,
        )
        if idx > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                max(5.0, value / 2),
                f"{value - values[0]:+.0f} pp",
                ha="center",
                va="center",
                fontsize=7,
                color="white",
                weight="bold",
            )
    ax.set_ylabel("BS exact (%)")
    ax.set_ylim(0, 105)
    ax.set_xticks(x)
    ax.set_xticklabels([wrap_display_label(label, 13) for label, _, _ in runs])
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=1, frameon=False)
    ax.grid(axis="x", visible=False)
    return save_figure(fig, output_dir, "fig_gap_repair_comparison")


def plot_difficulty_trend(results_dir: Path, output_dir: Path) -> list[Path]:
    apply_style()
    runs = load_ablation_group(results_dir, "gemini3flash_promoted_coverage_full_clean")
    baseline = runs.get("prompt_baseline")
    verifier = runs.get("forced_ledger_verifier")
    if not baseline or not verifier:
        return []

    difficulties = [str(level) for level in range(1, 6)]
    series = [
        (
            "Baseline BS exact",
            baseline,
            "final_balance_sheet_matches_rate",
            ORANGE,
            "o",
        ),
        (
            "Baseline BS recon",
            baseline,
            "predicted_entries_reconstruct_correct_final_balance_sheet_rate",
            BLUE,
            "o",
        ),
        (
            "Verifier BS exact",
            verifier,
            "final_balance_sheet_matches_rate",
            RED,
            "s",
        ),
    ]
    fig, ax = plt.subplots(figsize=(4.0, 2.65))
    x = np.arange(1, 6)
    for label, run, metric, color, marker in series:
        rows = run.summary.get("by_difficulty_level", {})
        values = [100 * float(rows.get(level, {}).get(metric) or 0.0) for level in difficulties]
        ax.plot(x, values, marker=marker, linewidth=2, markersize=5, color=color, label=label)
        for xx, value in zip(x, values, strict=True):
            ax.text(xx, value + 2.0, f"{value:.0f}", ha="center", va="bottom", fontsize=6.5, color=color)
    ax.set_xticks(x)
    ax.set_xlabel("Difficulty level")
    ax.set_ylabel("Record-level accuracy (%)")
    ax.set_ylim(0, 105)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=1, frameon=False)
    return save_figure(fig, output_dir, "fig_difficulty_trend")


def plot_concept_heatmap(results_dir: Path, output_dir: Path, *, min_records: int = 100) -> list[Path]:
    apply_style()
    runs = sorted(
        load_default_baselines(results_dir, min_records=min_records),
        key=lambda run: run.metric("final_balance_sheet_matches_rate"),
        reverse=True,
    )
    if not runs:
        return []

    features = [
        ("has_asc606", "ASC 606"),
        ("has_lease", "Lease"),
        ("has_deferred_tax", "Deferred tax"),
        ("has_asset_disposal", "Asset disposal"),
        ("has_tax_exemption", "Tax exemption"),
    ]
    matrix = np.full((len(runs), len(features)), np.nan)
    for row_idx, run in enumerate(runs):
        by_feature = run.summary.get("by_feature_flags", {})
        for col_idx, (feature, _) in enumerate(features):
            row = by_feature.get(feature, {})
            if int(row.get("standard_records") or 0) >= 3:
                matrix[row_idx, col_idx] = 100 * float(
                    row.get("predicted_entries_reconstruct_correct_final_balance_sheet_rate") or 0.0
                )

    fig, ax = plt.subplots(figsize=(6.9, 3.8))
    _annotated_heatmap(
        ax,
        matrix,
        [wrap_display_label(run.label, 12) for run in runs],
        [label for _, label in features],
        "BS Recon Accuracy by Accounting Concept",
        cmap="YlGnBu",
        vmin=0,
        vmax=100,
        cbar_label="Accuracy (%)",
    )
    fig.subplots_adjust(bottom=0.18)
    return save_figure(fig, output_dir, "fig_concept_heatmap")


def plot_cost_pareto(results_dir: Path, output_dir: Path, *, min_records: int = 100) -> list[Path]:
    apply_style()
    runs = load_default_baselines(results_dir, min_records=min_records)
    if not runs:
        return []

    x = np.array([1000 * float(run.summary.get("cost_average_per_record") or 0.0) for run in runs])
    y = np.array([100 * run.metric("final_balance_sheet_matches_rate") for run in runs])
    recon = np.array([100 * run.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate") for run in runs])
    sizes = 42 + 1.8 * recon
    fig, ax = plt.subplots(figsize=(6.0, 3.55))
    ax.scatter(x, y, s=sizes, color=BLUE, alpha=0.88, edgecolor="white", linewidth=0.7)
    for idx, run in enumerate(runs):
        offsets = {
            "GPT-5": (5, -10),
            "Gemini 3 Flash": (5, 5),
            "Grok 4.3": (-8, 10),
            "DeepSeek V3.2": (5, 8),
            "Qwen3 235B": (8, 10),
            "Claude Haiku 4.5": (5, 8),
        }
        dx, dy = offsets.get(run.label, (5, 5))
        ax.annotate(
            run.label,
            (x[idx], y[idx]),
            textcoords="offset points",
            xytext=(dx, dy),
            ha="left" if dx >= 0 else "right",
            va="center",
            fontsize=7,
            color=DARK,
        )
    ax.set_xlabel("Cost per record (USD x 1,000)")
    ax.set_ylabel("BS_exact accuracy (%)")
    ax.set_title("Cost and Accuracy Trade-off")
    ax.set_ylim(0, max(60, float(y.max() + 10)))
    ax.set_xlim(0, max(12, float(x.max() * 1.15)))
    return save_figure(fig, output_dir, "fig_cost_pareto")


def plot_two_model_context_deltas(results_dir: Path, output_dir: Path, *, min_records: int = 100) -> list[Path]:
    apply_style()
    model_dirs = [
        ("Gemini 3 Flash", "gemini3flash_promoted_coverage_full_clean"),
        ("DeepSeek V3.2", "deepseek_v32_sweep"),
    ]
    ablations = [
        ("evidence_only", "Evidence only"),
        ("evidence_plus_15_distractors", "+15 distractors"),
    ]
    metrics = [
        ("final_balance_sheet_matches_rate", "Delta BS exact (pp)"),
        ("predicted_entries_reconstruct_correct_final_balance_sheet_rate", "Delta BS recon (pp)"),
    ]
    model_colors = {
        "Gemini 3 Flash": BLUE,
        "DeepSeek V3.2": ORANGE,
    }

    observations: dict[str, list[dict[str, Any]]] = {name: [] for name, _ in ablations}
    for label, relative in model_dirs:
        runs = load_ablation_group(results_dir, relative)
        baseline = runs.get("prompt_baseline")
        if not baseline or baseline.records < min_records:
            continue
        for ablation, _ in ablations:
            run = runs.get(ablation)
            if not run or run.records < min_records:
                continue
            observations[ablation].append(
                {
                    "model": label,
                    "final_balance_sheet_matches_rate": 100
                    * (run.metric("final_balance_sheet_matches_rate") - baseline.metric("final_balance_sheet_matches_rate")),
                    "predicted_entries_reconstruct_correct_final_balance_sheet_rate": 100
                    * (
                        run.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate")
                        - baseline.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate")
                    ),
                }
            )
    if not any(observations.values()):
        return []

    fig, axes = plt.subplots(1, 2, figsize=(6.8, 3.6), sharey=True)
    group_centers = np.arange(len(ablations))
    handles: dict[str, Any] = {}
    for ax, (metric, title) in zip(axes, metrics, strict=True):
        ax.axhline(0, color=GRAY, linewidth=0.8)
        for group_idx, (ablation, _) in enumerate(ablations):
            rows = observations[ablation]
            offsets = (np.arange(len(rows)) - (len(rows) - 1) / 2) * 0.18
            for offset, row in zip(offsets, rows, strict=False):
                value = float(row[metric])
                model = str(row["model"])
                bar = ax.bar(
                    group_idx + offset,
                    value,
                    width=0.16,
                    color=model_colors.get(model, GRAY),
                    edgecolor="white",
                    linewidth=0.6,
                    label=model,
                )
                handles.setdefault(model, bar[0])
                ax.text(
                    group_idx + offset,
                    value + (1.4 if value >= 0 else -1.7),
                    f"{value:+.0f}",
                    ha="center",
                    va="bottom" if value >= 0 else "top",
                    fontsize=6.5,
                    color=DARK,
                )
        ax.set_xticks(group_centers)
        ax.set_xticklabels([label for _, label in ablations])
        ax.set_title(title)
        ax.set_ylim(-20, 6)
        ax.grid(axis="x", visible=False)
        ax.set_xlabel("Ablation")
    axes[0].set_ylabel("Delta from each model baseline")
    fig.suptitle("Two-Model Context Ablation Deltas", y=1.03, fontsize=10.5, fontweight="bold")
    fig.legend(
        handles.values(),
        handles.keys(),
        loc="lower center",
        bbox_to_anchor=(0.5, -0.04),
        ncol=4,
        frameon=False,
    )
    fig.subplots_adjust(bottom=0.24, wspace=0.14)
    return save_figure(fig, output_dir, "fig_two_model_context_deltas")


def plot_context_stress(results_dir: Path, output_dir: Path) -> list[Path]:
    apply_style()
    runs = load_ablation_group(results_dir, "gemini3flash_promoted_coverage_full_clean")
    baseline = runs.get("prompt_baseline")
    distractor_order = [
        "evidence_only",
        "evidence_plus_5_distractors",
        "evidence_plus_15_distractors",
        "evidence_plus_30_distractors",
    ]
    distractor_runs = [runs[name] for name in distractor_order if name in runs]
    relevant_last = runs.get("evidence_relevant_last")
    if not baseline or len(distractor_runs) < 2:
        return []

    metrics = (
        "predicted_entries_reconstruct_correct_final_balance_sheet_rate",
        "final_journal_entries_match_no_doc_refs_rate",
        "final_balance_sheet_matches_rate",
    )
    colors = [BLUE, TEAL, ORANGE]
    fig, axes = plt.subplots(1, 2, figsize=(7.3, 3.65), sharey=True)
    x = np.arange(len(distractor_runs))
    labels = ["Evidence\nonly", "+5\ndistractors", "+15\ndistractors", "+30\ndistractors"][: len(distractor_runs)]
    for metric, color in zip(metrics, colors, strict=True):
        values = [100 * (run.metric(metric) - baseline.metric(metric)) for run in distractor_runs]
        axes[0].plot(x, values, marker="o", linewidth=2, markersize=5, color=color, label=METRIC_LABELS[metric])
        for xx, value in zip(x, values, strict=True):
            if abs(value) >= 4:
                axes[0].text(xx, value + (1.2 if value >= 0 else -1.4), f"{value:+.0f}", ha="center", va="bottom" if value >= 0 else "top", fontsize=6.3, color=color)
        axes[0].axhline(0, color=LIGHT_GRAY, linewidth=1.0)
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(labels)
    axes[0].set_title("Distractor count")
    axes[0].set_ylabel("Delta from full packet (pp)")
    axes[0].set_ylim(-24, 10)

    if relevant_last:
        width = 0.22
        positions = np.arange(len(metrics))
        values = [100 * (relevant_last.metric(metric) - baseline.metric(metric)) for metric in metrics]
        bars = axes[1].bar(positions, values, width=width, color=colors[: len(metrics)], edgecolor="white", linewidth=0.6)
        axes[1].axhline(0, color=LIGHT_GRAY, linewidth=1.0)
        for bar, value in zip(bars, values, strict=True):
            axes[1].text(bar.get_x() + bar.get_width() / 2, value + (1.2 if value >= 0 else -1.4), f"{value:+.0f}", ha="center", va="bottom" if value >= 0 else "top", fontsize=6.4, color=DARK)
        axes[1].set_xticks(positions)
        axes[1].set_xticklabels([wrap_display_label(METRIC_LABELS[metric], 10) for metric in metrics])
        axes[1].set_title("Relevant docs last")
    fig.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=3, frameon=False)
    fig.subplots_adjust(bottom=0.24, top=0.90, wspace=0.12)
    return save_figure(fig, output_dir, "fig_context_stress")


def plot_verifier_transfer(results_dir: Path, output_dir: Path, *, min_records: int = 100) -> list[Path]:
    apply_style()
    pairs = load_verifier_pairs(results_dir, min_records=min_records)
    if not pairs:
        return []

    labels = [label for label, _, _ in pairs]
    x = np.arange(len(pairs))
    width = 0.2
    fig, ax = plt.subplots(figsize=(7.2, 3.7))
    series = [
        ("Baseline BS exact", [100 * base.metric("final_balance_sheet_matches_rate") for _, base, _ in pairs], ORANGE, -1.5),
        ("Verifier BS exact", [100 * ver.metric("final_balance_sheet_matches_rate") for _, _, ver in pairs], RED, -0.5),
        ("Baseline BS recon", [100 * base.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate") for _, base, _ in pairs], BLUE, 0.5),
        ("Verifier BS recon", [100 * ver.metric("predicted_entries_reconstruct_correct_final_balance_sheet_rate") for _, _, ver in pairs], TEAL, 1.5),
    ]
    for label, values, color, offset in series:
        ax.bar(x + offset * width, values, width=width, color=color, label=label, edgecolor="white", linewidth=0.6)
    for idx, (_, base, ver) in enumerate(pairs):
        delta = 100 * (ver.metric("final_balance_sheet_matches_rate") - base.metric("final_balance_sheet_matches_rate"))
        ax.text(idx - 0.2, max(100 * base.metric("final_balance_sheet_matches_rate"), 100 * ver.metric("final_balance_sheet_matches_rate")) + 2.2, f"{delta:+.0f} pp", ha="center", fontsize=7, color=RED)
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(0, 72)
    ax.set_xticks(x)
    ax.set_xticklabels([wrap_display_label(label, 13) for label in labels])
    ax.set_title("Forced Ledger Verifier Transfers Across Models")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, frameon=False)
    return save_figure(fig, output_dir, "fig_verifier_transfer")


def plot_dataset_composition(dataset_path: Path, output_dir: Path) -> list[Path]:
    apply_style()
    records = load_records(dataset_path)
    if not records:
        return []

    industry = Counter(record["industry"] for record in records)
    difficulty = Counter(str(record["difficulty_level"]) for record in records)
    periods = Counter(record.get("metadata", {}).get("period_type", "unknown") for record in records)
    doc_roles = Counter()
    doc_counts = []
    feature_counts = Counter()
    doc_type_records = Counter()
    for record in records:
        docs = record.get("documents", [])
        doc_counts.append(len(docs))
        for doc in docs:
            doc_roles[doc.get("role", "unknown")] += 1
        for flag in ("has_asc606", "has_asset_disposal", "has_deferred_tax", "has_lease", "has_tax_exemption"):
            if record.get("metadata", {}).get(flag):
                feature_counts[flag] += 1
        for doc_type in {doc.get("doc_type", "unknown") for doc in docs}:
            doc_type_records[doc_type] += 1

    fig, axes = plt.subplots(2, 3, figsize=(9.4, 6.2))
    axes = axes.ravel()

    _barh_counter(axes[0], industry, "Records by Industry", color=BLUE)
    _bar_counter(axes[1], difficulty, "Records by Difficulty", color=ORANGE, sort_key=lambda item: int(item[0]), rotate=0)
    _bar_counter(axes[2], periods, "Records by Period", color=TEAL, rotate=0)
    _barh_counter(axes[3], doc_roles, "Documents by Role", color=PURPLE)
    axes[4].hist(doc_counts, bins=range(min(doc_counts), max(doc_counts) + 2), color=GREEN, edgecolor="white")
    axes[4].set_title("Documents per Record")
    axes[4].set_xlabel("Document count")
    axes[4].set_ylabel("Records")
    top_doc_types = Counter(dict(doc_type_records.most_common(8)))
    _barh_counter(axes[5], top_doc_types, "Most Common Doc Types", color=GRAY)

    fig.subplots_adjust(hspace=0.50, wspace=0.58, top=0.96)
    return save_figure(fig, output_dir, "fig_dataset_composition")


def plot_failure_slices(results_dir: Path, output_dir: Path) -> list[Path]:
    apply_style()
    runs = sorted(
        load_default_baselines(results_dir, min_records=100),
        key=lambda run: run.metric("final_balance_sheet_matches_rate"),
        reverse=True,
    )
    if not runs:
        return []

    metric = "predicted_entries_reconstruct_correct_final_balance_sheet_rate"
    industries = sorted(
        {
            industry
            for run in runs
            for industry, row in run.summary.get("by_industry", {}).items()
            if int(row.get("records_evaluated") or 0) >= 10
        }
    )
    industries = _sort_categories_by_mean(runs, "by_industry", industries, metric)
    ledger_candidates = sorted(
        {
            family
            for run in runs
            for family, row in run.summary.get("by_ledger_family", {}).items()
            if int(row.get("records_evaluated") or 0) >= 20
        }
    )
    ledgers = _sort_categories_by_mean(runs, "by_ledger_family", ledger_candidates, metric)[:8]
    error_candidates = sorted(
        {
            str(row.get("error_type"))
            for run in runs
            for row in run.summary.get("error_taxonomy", [])
            if row.get("error_type")
        }
    )
    errors = _sort_errors_by_mean(runs, error_candidates)[:7]

    model_labels = [wrap_display_label(run.label, 12) for run in runs]
    fig, axes = plt.subplots(3, 1, figsize=(8.9, 7.6))
    _annotated_heatmap(
        axes[0],
        _slice_matrix(runs, "by_industry", industries, metric),
        model_labels,
        [wrap_label(label, 13) for label in industries],
        "BS Recon Accuracy by Industry",
        cmap="YlGnBu",
        vmin=0,
        vmax=100,
        cbar_label="Accuracy (%)",
    )
    _annotated_heatmap(
        axes[1],
        _slice_matrix(runs, "by_ledger_family", ledgers, metric),
        model_labels,
        [wrap_label(label, 14) for label in ledgers],
        "BS Recon Accuracy by Ledger Family",
        cmap="YlGnBu",
        vmin=0,
        vmax=100,
        cbar_label="Accuracy (%)",
    )
    _annotated_heatmap(
        axes[2],
        _error_matrix(runs, errors),
        model_labels,
        [wrap_label(label, 14) for label in errors],
        "Affected Standard Records by Error Type",
        cmap="OrRd",
        vmin=0,
        vmax=100,
        cbar_label="Failure rate (%)",
    )
    fig.subplots_adjust(hspace=0.56, top=0.96)
    return save_figure(fig, output_dir, "fig_failure_slices")


def _bar_counter(ax, counts: Counter, title: str, *, color: str, sort_key=None, rotate: int = 25) -> None:
    items = list(counts.items())
    if sort_key:
        items = sorted(items, key=sort_key)
    else:
        items = sorted(items)
    labels = [short_label(key) for key, _ in items]
    values = [value for _, value in items]
    ax.bar(labels, values, color=color, edgecolor="white", linewidth=0.6)
    ax.set_title(title)
    ax.tick_params(axis="x", labelrotation=rotate)
    ax.set_ylabel("Count")


def _barh_counter(ax, counts: Counter, title: str, *, color: str) -> None:
    items = sorted(counts.items(), key=lambda item: item[1])
    labels = [short_label(key) for key, _ in items]
    values = [value for _, value in items]
    y = np.arange(len(items))
    ax.barh(y, values, color=color, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_title(title)
    ax.set_xlabel("Count")


def _slice_accuracy_panel(
    ax,
    rows: dict[str, dict[str, Any]],
    title: str,
    metric: str,
    *,
    min_records: int,
    color: str,
    limit: int | None = None,
) -> None:
    items = [
        (name, values)
        for name, values in rows.items()
        if int(values.get("records_evaluated") or 0) >= min_records
    ]
    items = sorted(items, key=lambda item: float(item[1].get(metric) or 0.0))
    if limit:
        items = items[:limit]
    labels = [wrap_label(name, 16) for name, _ in items]
    values = [100 * float(row.get(metric) or 0.0) for _, row in items]
    y = np.arange(len(items))
    ax.barh(y, values, color=color, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlim(0, 105)
    ax.set_xlabel("BS recon accuracy (%)")
    ax.set_title(title)
    ax.grid(axis="y", visible=False)


def _error_taxonomy_panel(ax, rows: list[dict[str, Any]]) -> None:
    selected = sorted(rows, key=lambda row: float(row.get("affected_record_rate") or 0.0), reverse=True)[:7]
    selected = list(reversed(selected))
    labels = [wrap_label(str(row.get("error_type", "")), 17) for row in selected]
    values = [100 * float(row.get("affected_record_rate") or 0.0) for row in selected]
    y = np.arange(len(selected))
    ax.barh(y, values, color=RED, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlim(0, 105)
    ax.set_xlabel("Affected standard records (%)")
    ax.set_title("Error Taxonomy")
    ax.grid(axis="y", visible=False)


def _sort_categories_by_mean(
    runs: list[ResultRun],
    slice_name: str,
    categories: list[str],
    metric: str,
) -> list[str]:
    return sorted(
        categories,
        key=lambda category: np.nanmean(
            [
                100 * float(run.summary.get(slice_name, {}).get(category, {}).get(metric, np.nan))
                for run in runs
            ]
        ),
    )


def _sort_errors_by_mean(runs: list[ResultRun], errors: list[str]) -> list[str]:
    def mean_rate(error: str) -> float:
        rates: list[float] = []
        for run in runs:
            for row in run.summary.get("error_taxonomy", []):
                if row.get("error_type") == error:
                    rates.append(100 * float(row.get("affected_record_rate") or 0.0))
                    break
        return float(np.nanmean(rates)) if rates else 0.0

    return sorted(errors, key=mean_rate, reverse=True)


def _slice_matrix(
    runs: list[ResultRun],
    slice_name: str,
    categories: list[str],
    metric: str,
) -> np.ndarray:
    matrix = np.full((len(runs), len(categories)), np.nan)
    for row_idx, run in enumerate(runs):
        rows = run.summary.get(slice_name, {})
        for col_idx, category in enumerate(categories):
            value = rows.get(category, {}).get(metric)
            if value is not None:
                matrix[row_idx, col_idx] = 100 * float(value)
    return matrix


def _error_matrix(runs: list[ResultRun], errors: list[str]) -> np.ndarray:
    matrix = np.full((len(runs), len(errors)), np.nan)
    for row_idx, run in enumerate(runs):
        by_error = {str(row.get("error_type")): row for row in run.summary.get("error_taxonomy", [])}
        for col_idx, error in enumerate(errors):
            row = by_error.get(error)
            if row:
                matrix[row_idx, col_idx] = 100 * float(row.get("affected_record_rate") or 0.0)
    return matrix


def _annotated_heatmap(
    ax,
    matrix: np.ndarray,
    row_labels: list[str],
    col_labels: list[str],
    title: str,
    *,
    cmap: str,
    vmin: float,
    vmax: float,
    suffix: str = "%",
    fmt: str = "{:.0f}",
    na_text: str = "n/a",
    cbar_label: str | None = None,
) -> None:
    masked = np.ma.masked_invalid(matrix)
    cmap_obj = plt.get_cmap(cmap).copy()
    cmap_obj.set_bad("#F2F3F5")
    im = ax.imshow(masked, aspect="auto", cmap=cmap_obj, vmin=vmin, vmax=vmax)
    ax.set_title(title)
    ax.set_xticks(np.arange(len(col_labels)))
    ax.set_xticklabels(col_labels)
    ax.set_yticks(np.arange(len(row_labels)))
    ax.set_yticklabels(row_labels)
    ax.tick_params(axis="x", labelrotation=25, length=0)
    ax.tick_params(axis="y", length=0)
    ax.grid(False)
    threshold = vmin + 0.62 * (vmax - vmin)
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            value = matrix[row, col]
            if np.isnan(value):
                text = na_text
                color = GRAY
            else:
                text = f"{fmt.format(value)}{suffix}"
                color = "white" if value >= threshold else DARK
            if text:
                ax.text(col, row, text, ha="center", va="center", fontsize=6.3, color=color)
    cbar = plt.colorbar(im, ax=ax, fraction=0.025, pad=0.015)
    if cbar_label:
        cbar.set_label(cbar_label, fontsize=7)
    cbar.ax.tick_params(labelsize=7, length=0)
