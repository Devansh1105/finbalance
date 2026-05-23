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
    load_ablation_group,
    load_bootstrap_comparisons,
    load_default_baselines,
    load_default_gemini_ablation_rows,
    load_records,
    load_verifier_pairs,
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
    ax.set_xticklabels([wrap_label(f"{label}\n(n={run.records})", 13) for label, run in zip(labels, runs, strict=True)])
    ax.set_title("Model Accuracy on FinBalance Coverage Set")
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
    ax.scatter(exact, y, s=46, color=ORANGE, label="Reported BS exact", zorder=3)
    ax.scatter(recon, y, s=46, color=BLUE, label="BS from replayed entries", zorder=4)
    ax.set_yticks(y)
    ax.set_yticklabels([run.label for run in runs])
    ax.set_xlim(0, max(75, float(max(recon.max(), exact.max()) + 15)))
    ax.set_xlabel("Record-level accuracy (%)")
    ax.set_title("Aggregation Gap: Correct Entries Do Not Imply Correct Balance Sheets")
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
        "prompt_guided_private_solve",
        "prompt_self_check",
        "prompt_doc_refs_strict",
        "visibility_ocr_only",
        "visibility_no_distractors_oracle",
        "visibility_support_docs_removed",
        "visibility_no_allowed_accounts",
        "tool_calculator",
        "tool_document_search",
        "tool_ledger_check",
        "tool_full_tool_agent",
        "forced_ledger_verifier",
        "forced_ledger_verifier_2pass",
        "self_consistency_k3",
    ]
    by_name = {row["ablation"]: row for row in rows}
    ordered = [by_name[name] for name in preferred_order if name in by_name]
    if not ordered:
        return []

    labels = [ABLATION_LABELS.get(row["ablation"], short_label(row["ablation"])) for row in ordered]
    y = np.arange(len(ordered))
    fig, axes = plt.subplots(1, 2, figsize=(7.3, 5.9), sharey=True)
    panels = [
        (
            axes[0],
            (
                "predicted_entries_reconstruct_correct_final_balance_sheet_rate",
                "final_balance_sheet_matches_rate",
            ),
            "Balance-sheet metrics",
        ),
        (
            axes[1],
            (
                "final_journal_entries_match_no_doc_refs_rate",
                "final_balance_sheet_and_journal_entries_match_rate",
            ),
            "Entry and strict metrics",
        ),
    ]
    metric_colors = {
        "predicted_entries_reconstruct_correct_final_balance_sheet_rate": BLUE,
        "final_balance_sheet_matches_rate": ORANGE,
        "final_journal_entries_match_no_doc_refs_rate": TEAL,
        "final_balance_sheet_and_journal_entries_match_rate": PURPLE,
    }

    for ax, metrics, title in panels:
        ax.axvline(0, color=GRAY, linewidth=0.8)
        for metric_idx, metric in enumerate(metrics):
            deltas = [
                100 * (row["run"].metric(metric) - row["baseline"].metric(metric))
                for row in ordered
            ]
            ax.scatter(
                deltas,
                y + (metric_idx - 0.5) * 0.22,
                s=34,
                color=metric_colors[metric],
                label=METRIC_LABELS[metric],
                zorder=3,
            )
            for delta, yy in zip(deltas, y + (metric_idx - 0.5) * 0.22, strict=True):
                if abs(delta) >= 8:
                    ax.text(
                        delta + (1.3 if delta >= 0 else -1.3),
                        yy,
                        f"{delta:+.0f}",
                        va="center",
                        ha="left" if delta >= 0 else "right",
                        fontsize=6.5,
                        color=GRAY,
                    )
        ax.set_title(title)
        ax.set_xlabel("Delta from baseline (pp)")
        ax.set_xlim(-55, 42)
        ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.17), ncol=1, frameon=False)

    axes[0].set_yticks(y)
    axes[0].set_yticklabels(labels)
    axes[0].invert_yaxis()
    fig.suptitle("Gemini 3 Flash Ablation Effects", y=1.01, fontsize=10.5, fontweight="bold")
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
    model_labels = [wrap_label(str(row["model"]), 14) for row in observations]
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
    order = [
        "prompt_baseline",
        "evidence_only",
        "evidence_plus_5_distractors",
        "evidence_plus_15_distractors",
        "evidence_plus_30_distractors",
        "evidence_relevant_last",
    ]
    selected = [runs[name] for name in order if name in runs]
    if len(selected) < 2:
        return []

    x = np.arange(len(selected))
    labels = ["Full packet", "Evidence\nonly", "+5\ndistractors", "+15\ndistractors", "+30\ndistractors", "Relevant\nlast"]
    labels = labels[: len(selected)]
    metrics = (
        "predicted_entries_reconstruct_correct_final_balance_sheet_rate",
        "final_journal_entries_match_no_doc_refs_rate",
        "final_balance_sheet_matches_rate",
        "final_balance_sheet_and_journal_entries_match_rate",
    )
    colors = [BLUE, TEAL, ORANGE, PURPLE]
    fig, ax = plt.subplots(figsize=(7.1, 3.8))
    for metric, color in zip(metrics, colors, strict=True):
        values = [100 * run.metric(metric) for run in selected]
        ax.plot(x, values, marker="o", linewidth=2, markersize=5, color=color, label=METRIC_LABELS[metric])
        for xx, value in zip(x, values, strict=True):
            ax.text(xx, value + 1.5, f"{value:.0f}", ha="center", va="bottom", fontsize=6.5, color=color)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(0, 75)
    ax.set_title("Context Stress: Evidence Ordering and Added Distractors")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=4, frameon=False)
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
    ax.set_xticklabels([wrap_label(label, 13) for label in labels])
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

    total_docs = sum(doc_counts)
    fig.suptitle(
        f"Coverage Dataset Composition: {len(records)} records, {total_docs} documents",
        y=1.02,
        fontsize=10.5,
        fontweight="bold",
    )
    fig.subplots_adjust(hspace=0.56, wspace=0.62)
    return save_figure(fig, output_dir, "fig_dataset_composition")


def plot_failure_slices(results_dir: Path, output_dir: Path) -> list[Path]:
    apply_style()
    runs = load_default_baselines(results_dir, min_records=100)
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

    model_labels = [wrap_label(run.label, 12) for run in runs]
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
    )
    fig.suptitle("Failure Slices Across Baseline Models", y=1.02, fontsize=10.5, fontweight="bold")
    fig.subplots_adjust(hspace=0.58)
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
    cbar.ax.tick_params(labelsize=7, length=0)
