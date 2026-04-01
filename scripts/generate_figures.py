"""
Generate publication-quality figures for the FinBalance ACL paper.

Figures produced:
  F1 — Capability Curve: FBS vs difficulty level (line chart per model×strategy)
  F2 — Error Composition: AE/OE/CV/CO stacked bar chart per model×strategy
  F3 — CoT Effect: ΔFBS / ΔBA / ΔALA diverging bar chart per model

Auto-discovers all primary result files in --results-dir (those with at least
min-overlap scored problems).
Adding new model result files will automatically appear in all figures.

Usage:
    python scripts/generate_figures.py
    python scripts/generate_figures.py --results-dir results --out-dir figures --format pdf
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
plt.rcParams.update({
    "font.family":       "serif",
    "font.size":         15,
    "axes.titlesize":    16,
    "axes.labelsize":    15,
    "xtick.labelsize":   13,
    "ytick.labelsize":   13,
    "legend.fontsize":   12,
    "figure.dpi":        150,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.grid":         True,
    "grid.alpha":        0.3,
    "grid.linestyle":    "--",
})

# Colorblind-friendly palette (Wong 2011)
PALETTE = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9", "#F0E442"]

MODEL_DISPLAY = {
    "deepseek/deepseek-v3.2":               "DeepSeek v3.2",
    "google/gemini-3-flash-preview":        "Gemini 3 Flash",
    "meta-llama/llama-3.3-70b-instruct":    "Llama 3.3 70B",
    "openai/gpt-5.2":                       "GPT-5.2",
    "qwen/qwen3.5-flash-02-23":             "Qwen 3.5 Flash",
    "qwen/qwen3.6-plus-preview:free":       "Qwen 3.6 Plus",
}

STRATEGY_LABEL = {"zero_shot": "Zero-shot", "cot": "CoT"}
STRATEGY_LINESTYLE = {"zero_shot": "-", "cot": "--"}
STRATEGY_MARKER = {"zero_shot": "o", "cot": "s"}

ERROR_COLORS = {
    "OE": "#D55E00",   # Omission
    "AE": "#0072B2",   # Arithmetic
    "CO": "#CC79A7",   # Commission/Hallucination
    "CV": "#009E73",   # Constraint Violation
    "FE": "#E69F00",   # Format
    "CE": "#56B4E9",   # Other
}
ERROR_LABELS = {
    "OE": "Omission (OE)",
    "AE": "Arithmetic (AE)",
    "CO": "Commission (CO)",
    "CV": "Constraint Viol. (CV)",
    "FE": "Format (FE)",
    "CE": "Other (CE)",
}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_primary_results(results_dir: Path, min_overlap: int = 90) -> list[dict]:
    """Load all primary result files (those with ≥min_overlap test problems)."""
    records = []
    skip = {"failure_analysis", "propagation", "leaderboard", "baseline", "significance"}
    for path in sorted(results_dir.glob("*.json")):
        if any(s in path.name for s in skip):
            continue
        try:
            with open(path) as f:
                data = json.load(f)
        except Exception:
            continue
        if not isinstance(data, list) or len(data) < min_overlap:
            continue
        # Check it has the fields we need and a real model_id
        if not data or "FBS" not in data[0]:
            continue
        if not data[0].get("model_id"):
            continue
        for r in data:
            r["_source"] = path.name
        records.extend(data)
    return records


def group_by_model_strategy(records: list[dict]) -> dict:
    """Returns {(model_id, strategy): [results]}."""
    groups = defaultdict(list)
    for r in records:
        key = (r.get("model_id", "unknown"), r.get("strategy", "unknown"))
        groups[key].append(r)
    return dict(groups)


def bootstrap_ci(values: list[float], n_boot: int = 1000, alpha: float = 0.05) -> tuple[float, float]:
    arr = np.array(values)
    means = [np.mean(np.random.choice(arr, size=len(arr), replace=True)) for _ in range(n_boot)]
    return np.percentile(means, 100 * alpha / 2), np.percentile(means, 100 * (1 - alpha / 2))


def display_name(model_id: str, strategy: str) -> str:
    m = MODEL_DISPLAY.get(model_id, model_id.split("/")[-1])
    s = STRATEGY_LABEL.get(strategy, strategy)
    return f"{m} ({s})"


# ---------------------------------------------------------------------------
# F1 — Capability Curve
# ---------------------------------------------------------------------------

def fig_capability_curve(groups: dict, out_path: Path, fmt: str):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), sharey=False)
    metrics = [("FBS", "FinBalance Score (FBS)", (0, 100)), ("BA", "Balance Accuracy (%)", (0, 105))]
    levels = [1, 2, 3, 4, 5]

    # Assign colors per model
    models_seen = {}
    color_idx = 0

    for ax_idx, (metric, ylabel, ylim) in enumerate(metrics):
        ax = axes[ax_idx]
        for (model_id, strategy), results in sorted(groups.items()):
            if model_id not in models_seen:
                models_seen[model_id] = PALETTE[color_idx % len(PALETTE)]
                color_idx += 1
            color = models_seen[model_id]
            ls = STRATEGY_LINESTYLE.get(strategy, "-")
            marker = STRATEGY_MARKER.get(strategy, "o")

            by_level = defaultdict(list)
            for r in results:
                lvl = r.get("difficulty", r.get("difficulty_level"))
                val = r.get(metric, 0)
                if metric == "BA":
                    val = val * 100
                by_level[lvl].append(val)

            xs, ys, yerr_lo, yerr_hi = [], [], [], []
            for lvl in levels:
                if lvl not in by_level:
                    continue
                vals = by_level[lvl]
                mean = np.mean(vals)
                lo, hi = bootstrap_ci(vals, n_boot=500)
                xs.append(lvl)
                ys.append(mean)
                yerr_lo.append(mean - lo)
                yerr_hi.append(hi - mean)

            label = display_name(model_id, strategy)
            ax.plot(xs, ys, color=color, linestyle=ls, marker=marker,
                    linewidth=2, markersize=6, label=label, zorder=3)
            ax.fill_between(xs,
                            [y - e for y, e in zip(ys, yerr_lo)],
                            [y + e for y, e in zip(ys, yerr_hi)],
                            color=color, alpha=0.12, zorder=2)

        ax.set_xlabel("Difficulty Level")
        ax.set_ylabel(ylabel)
        ax.set_xticks(levels)
        ax.set_xticklabels([f"L{l}" for l in levels])
        ax.set_ylim(*ylim)
        ax.set_title(f"({'ab'[ax_idx]}) {ylabel}")

    # Shared legend below — push well below x-axis labels
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=min(len(handles), 4),
               bbox_to_anchor=(0.5, -0.18), frameon=True, framealpha=0.9,
               fontsize=13, handlelength=2.5)
    fig.suptitle("Performance vs. Difficulty Level (Capability Curve)",
                 fontsize=16, fontweight="bold", y=1.01)
    plt.tight_layout()
    fig.savefig(out_path, format=fmt, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved F1 -> {out_path}")


# ---------------------------------------------------------------------------
# F2 — Error Composition
# ---------------------------------------------------------------------------

def fig_error_composition(groups: dict, out_path: Path, fmt: str):
    error_keys = ["OE", "AE", "CO", "CV", "FE", "CE"]

    rows = []
    for (model_id, strategy), results in sorted(groups.items()):
        totals = defaultdict(int)
        for r in results:
            for cat, cnt in (r.get("error_categories") or {}).items():
                totals[cat] += cnt
        grand = sum(totals.values()) or 1
        rows.append({
            "label": display_name(model_id, strategy),
            "fracs": {k: totals.get(k, 0) / grand for k in error_keys},
        })

    if not rows:
        print("  F2: no error data found, skipping.")
        return

    n = len(rows)
    fig, ax = plt.subplots(figsize=(10, max(4, n * 0.8 + 2)))
    y_pos = np.arange(n)

    lefts = np.zeros(n)
    patches = []
    for key in error_keys:
        vals = np.array([r["fracs"].get(key, 0) * 100 for r in rows])
        color = ERROR_COLORS.get(key, "#999999")
        bar = ax.barh(y_pos, vals, left=lefts, color=color,
                      label=ERROR_LABELS.get(key, key), height=0.55, zorder=3)
        lefts += vals
        patches.append(mpatches.Patch(color=color, label=ERROR_LABELS.get(key, key)))

    ax.set_yticks(y_pos)
    ax.set_yticklabels([r["label"] for r in rows])
    ax.set_xlabel("Proportion of Total Errors (%)")
    ax.set_xlim(0, 100)
    ax.axvline(50, color="gray", linewidth=0.8, linestyle=":")
    ax.legend(handles=patches, loc="lower right", ncol=2, framealpha=0.9, fontsize=9)
    ax.set_title("Figure 2: Error Composition by Model and Strategy", fontweight="bold")
    plt.tight_layout()
    fig.savefig(out_path, format=fmt, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved F2 -> {out_path}")


# ---------------------------------------------------------------------------
# F3 — CoT Effect (diverging bar)
# ---------------------------------------------------------------------------

def fig_cot_effect(groups: dict, out_path: Path, fmt: str):
    # Find models that have both zero_shot and cot
    models_with_cot = {}
    for (model_id, strategy), results in groups.items():
        models_with_cot.setdefault(model_id, {})[strategy] = results

    deltas = []
    for model_id, strats in sorted(models_with_cot.items()):
        if "zero_shot" not in strats or "cot" not in strats:
            continue
        zs = strats["zero_shot"]
        cot = strats["cot"]
        n = min(len(zs), len(cot))
        if n == 0:
            continue

        def mean(lst, key):
            vals = [r.get(key, 0) for r in lst]
            return np.mean(vals)

        d_fbs  = mean(cot, "FBS")  - mean(zs, "FBS")
        d_ba   = (mean(cot, "BA")  - mean(zs, "BA"))  * 100
        d_ala  = (mean(cot, "ALA") - mean(zs, "ALA")) * 100
        d_acr  = (mean(cot, "ACR") - mean(zs, "ACR")) * 100 if all("ACR" in r for r in zs + cot) else None

        name = MODEL_DISPLAY.get(model_id, model_id.split("/")[-1])
        deltas.append({"model": name, "ΔFBS": d_fbs, "ΔBA (pp)": d_ba, "ΔALA (pp)": d_ala})

    if not deltas:
        print("  F3: no paired zero_shot/CoT data found, skipping.")
        return

    metrics_to_plot = ["ΔFBS", "ΔBA (pp)", "ΔALA (pp)"]
    n_models = len(deltas)
    n_metrics = len(metrics_to_plot)
    x = np.arange(n_models)
    width = 0.25

    fig, ax = plt.subplots(figsize=(max(10, n_models * 3.2), 6.5))

    for i, metric in enumerate(metrics_to_plot):
        vals = [d[metric] for d in deltas]
        colors = [PALETTE[i] if v >= 0 else "#cccccc" for v in vals]
        offset = (i - (n_metrics - 1) / 2) * width
        bars = ax.bar(x + offset, vals, width=width * 0.9,
                      color=colors, label=metric, zorder=3)
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    v + (0.4 if v >= 0 else -1.0),
                    f"{v:+.1f}", ha="center", va="bottom" if v >= 0 else "top",
                    fontsize=17, fontweight="bold")

    ax.axhline(0, color="black", linewidth=1.0)
    ax.set_xticks(x)
    ax.set_xticklabels([d["model"] for d in deltas], fontsize=20)
    ax.set_ylabel("CoT − Zero-shot (pp / FBS pts)", fontsize=20)
    ax.set_title("Effect of Chain-of-Thought Prompting", fontweight="bold", fontsize=20)
    ax.tick_params(axis="y", labelsize=19)

    # Custom legend: positive = improvement (blue), negative = degradation (gray)
    handles = [mpatches.Patch(color=PALETTE[i], label=m) for i, m in enumerate(metrics_to_plot)]
    handles += [mpatches.Patch(color="#cccccc", label="Degradation")]
    ax.legend(handles=handles, loc="upper right", ncol=2, framealpha=0.9, fontsize=20)

    plt.tight_layout()
    fig.savefig(out_path, format=fmt, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved F3 -> {out_path}")


# ---------------------------------------------------------------------------
# F4 — Account Omission Heatmap
# ---------------------------------------------------------------------------

def load_failure_analyses(results_dir: Path) -> dict:
    """Returns {(model_id, strategy): failure_analysis_dict}."""
    analyses = {}
    skip = {"leaderboard", "propagation", "significance", "baseline"}
    for path in sorted(results_dir.glob("failure_analysis_*.json")):
        if any(s in path.name for s in skip):
            continue
        try:
            with open(path) as f:
                d = json.load(f)
            key = (d.get("model_id", "unknown"), d.get("strategy", "unknown"))
            analyses[key] = d
        except Exception:
            continue
    return analyses


def fig_account_heatmap(analyses: dict, out_path: Path, fmt: str):
    if not analyses:
        print("  F4: no failure analysis files found, skipping.")
        return

    # Collect all accounts seen across models
    all_accounts: dict[str, str] = {}  # account -> type
    for fa in analyses.values():
        for entry in fa.get("account_miss_rates", {}).get("accounts", []):
            if entry["n_expected"] > 0:
                all_accounts[entry["account"]] = entry.get("account_type", "unknown")

    # Filter to accounts that appear in ≥10% of problems in at least one model
    threshold = 10
    common_accounts = []
    for acc in all_accounts:
        for fa in analyses.values():
            for entry in fa.get("account_miss_rates", {}).get("accounts", []):
                if entry["account"] == acc and entry["n_expected"] >= threshold:
                    common_accounts.append(acc)
                    break

    common_accounts = sorted(set(common_accounts))
    if not common_accounts:
        print("  F4: not enough common accounts, skipping.")
        return

    # Build model labels and two matrices: omission_rate and arithmetic_rate
    model_labels = [display_name(*k) for k in sorted(analyses.keys())]
    n_acc = len(common_accounts)
    n_mod = len(model_labels)

    omit_matrix  = np.zeros((n_acc, n_mod))
    arith_matrix = np.zeros((n_acc, n_mod))

    for col_idx, key in enumerate(sorted(analyses.keys())):
        fa = analyses[key]
        acc_data = {e["account"]: e for e in fa.get("account_miss_rates", {}).get("accounts", [])}
        for row_idx, acc in enumerate(common_accounts):
            entry = acc_data.get(acc, {})
            omit_matrix[row_idx, col_idx]  = entry.get("omission_rate", 0) * 100
            arith_matrix[row_idx, col_idx] = entry.get("arithmetic_rate", 0) * 100

    # 2×1 vertical layout, width capped at 12 to limit LaTeX down-scaling
    fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    plt.subplots_adjust(hspace=0.35)

    for ax, matrix, title, cmap in [
        (axes[0], omit_matrix,  "(a) Omission Rate (%)",   "Reds"),
        (axes[1], arith_matrix, "(b) Arithmetic Error Rate (%)", "Blues"),
    ]:
        im = ax.imshow(matrix, aspect="auto", cmap=cmap, vmin=0, vmax=100)
        ax.set_xticks(range(n_mod))
        ax.set_xticklabels(model_labels, rotation=40, ha="right", fontsize=11)
        ax.set_yticks(range(n_acc))
        ax.set_yticklabels(common_accounts, fontsize=13)
        ax.set_title(title, fontsize=15)
        cbar = plt.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
        cbar.ax.tick_params(labelsize=11)
        # Annotate cells
        for r in range(n_acc):
            for c in range(n_mod):
                val = matrix[r, c]
                if val > 1:
                    ax.text(c, r, f"{val:.0f}", ha="center", va="center",
                            fontsize=9,
                            color="white" if val > 60 else "black")

    fig.suptitle("Account-Level Error Rates by Model", fontweight="bold", fontsize=16, y=1.0)
    plt.tight_layout()
    fig.savefig(out_path, format=fmt, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved F4 -> {out_path}")


# ---------------------------------------------------------------------------
# F5 — BEM Distribution (box plots)
# ---------------------------------------------------------------------------

def fig_bem_distribution(groups: dict, out_path: Path, fmt: str):
    # Collect BEM values per model×strategy
    rows = []
    for (model_id, strategy), results in sorted(groups.items()):
        bems = [r.get("BEM", 0) for r in results if r.get("BEM") is not None]
        if not bems:
            continue
        rows.append({
            "label": display_name(model_id, strategy),
            "bems": bems,
            "color": PALETTE[list(sorted({m for m, _ in groups})).index(model_id) % len(PALETTE)],
        })

    if not rows:
        print("  F5: no BEM data found, skipping.")
        return

    # BEM is an absolute magnitude — clip to ≥0 and use log1p scale
    for row in rows:
        row["bems"] = [max(0, b) for b in row["bems"]]

    # Cap width at 10 so LaTeX scaling preserves readable font sizes
    fig, ax = plt.subplots(figsize=(min(10, max(7, len(rows) * 1.4)), 6))
    positions = range(len(rows))

    bps = ax.boxplot(
        [r["bems"] for r in rows],
        positions=list(positions),
        patch_artist=True,
        widths=0.5,
        medianprops=dict(color="black", linewidth=2),
        flierprops=dict(marker="o", markersize=3, alpha=0.5),
    )
    for patch, row in zip(bps["boxes"], rows):
        patch.set_facecolor(row["color"])
        patch.set_alpha(0.7)

    ax.set_xticks(list(positions))
    ax.set_xticklabels([r["label"] for r in rows], rotation=35, ha="right")
    ax.set_ylabel("Balance Error Magnitude ($)")
    ax.set_yscale("symlog", linthresh=1)
    ax.set_ylim(bottom=-0.5)
    ax.axhline(0, color="green", linewidth=1, linestyle="--", label="Perfect balance (BEM=0)")
    ax.legend(loc="upper left")
    ax.set_title("BEM Distribution by Model", fontweight="bold")
    plt.tight_layout()
    fig.savefig(out_path, format=fmt, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved F5 -> {out_path}")


# ---------------------------------------------------------------------------
# F6 — CoT Effect by Difficulty Level
# ---------------------------------------------------------------------------

def fig_cot_by_difficulty(groups: dict, out_path: Path, fmt: str):
    models_with_cot = {}
    for (model_id, strategy), results in groups.items():
        models_with_cot.setdefault(model_id, {})[strategy] = results

    plot_models = {m: s for m, s in models_with_cot.items()
                   if "zero_shot" in s and "cot" in s}

    if not plot_models:
        print("  F6: no paired zero_shot/CoT data, skipping.")
        return

    levels = [1, 2, 3, 4, 5]
    n_models = len(plot_models)
    fig, ax = plt.subplots(figsize=(9, 5))

    width = 0.8 / n_models
    x = np.arange(len(levels))

    for i, (model_id, strats) in enumerate(sorted(plot_models.items())):
        color = PALETTE[i % len(PALETTE)]
        name  = MODEL_DISPLAY.get(model_id, model_id.split("/")[-1])

        by_level_zs  = defaultdict(list)
        by_level_cot = defaultdict(list)
        for r in strats["zero_shot"]:
            by_level_zs[r.get("difficulty", r.get("difficulty_level"))].append(r.get("FBS", 0))
        for r in strats["cot"]:
            by_level_cot[r.get("difficulty", r.get("difficulty_level"))].append(r.get("FBS", 0))

        deltas = []
        for lvl in levels:
            zs  = np.mean(by_level_zs.get(lvl, [0]))
            cot = np.mean(by_level_cot.get(lvl, [0]))
            deltas.append(cot - zs)

        offset = (i - (n_models - 1) / 2) * width
        bar_colors = [color if d >= 0 else "#cccccc" for d in deltas]
        bars = ax.bar(x + offset, deltas, width=width * 0.9, color=bar_colors,
                      label=name, zorder=3, alpha=0.85)
        for bar, d in zip(bars, deltas):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    d + (0.2 if d >= 0 else -0.5),
                    f"{d:+.1f}", ha="center", va="bottom" if d >= 0 else "top",
                    fontsize=10)

    ax.axhline(0, color="black", linewidth=1)
    ax.set_xticks(x)
    ax.set_xticklabels([f"L{l}" for l in levels])
    ax.set_xlabel("Difficulty Level")
    ax.set_ylabel("CoT - Zero-shot FBS (points)")
    ax.legend(loc="upper right")
    ax.set_title("Figure 6: CoT Effect on FBS by Difficulty Level", fontweight="bold")
    plt.tight_layout()
    fig.savefig(out_path, format=fmt, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved F6 -> {out_path}")


# ---------------------------------------------------------------------------
# F7 — Error Propagation Trajectory
# ---------------------------------------------------------------------------

def fig_error_propagation(results_dir: Path, out_path: Path, fmt: str):
    prop_path = results_dir / "propagation_haiku.json"
    if not prop_path.exists():
        print("  F7: propagation_haiku.json not found, skipping.")
        return
    with open(prop_path) as f:
        traces = json.load(f)
    if not traces:
        print("  F7: no propagation traces, skipping.")
        return

    fig, ax = plt.subplots(figsize=(11, 6))
    level_colors = {1: PALETTE[0], 2: PALETTE[1], 3: PALETTE[2], 4: PALETTE[3], 5: PALETTE[4]}

    for t in traces:
        traj = t.get("mae_trajectory", [])
        if not traj:
            continue
        lvl = t.get("difficulty", t.get("difficulty_level", 0))
        pid = t.get("problem_id", "")
        n_tx = t.get("n_transactions", len(traj))
        onset = t.get("first_error_k")
        color = level_colors.get(lvl, "#999999")

        # Normalize x-axis to fraction of problem completed
        xs = [i / max(len(traj) - 1, 1) for i in range(len(traj))]
        ax.plot(xs, traj, color=color, linewidth=2.5, alpha=0.8,
                label=f"L{lvl} ({pid})")
        if onset is not None:
            onset_frac = onset / max(n_tx, 1)
            ax.axvline(onset_frac, color=color, linewidth=1, linestyle=":", alpha=0.5)

    # Mark 30% onset line
    ax.axvline(0.30, color="gray", linewidth=1.5, linestyle="--", label="Mean onset (~30%)")
    ax.set_xlabel("Fraction of Problem Completed (transactions processed)", fontsize=15)
    ax.set_ylabel("Mean Absolute Error ($)", fontsize=15)
    ax.set_xlim(0, 1)
    ax.tick_params(axis="both", labelsize=13)
    ax.legend(loc="upper left", fontsize=13)
    ax.set_title("Figure 7: Error Propagation Trajectory (Claude Haiku 3, 5 problems)",
                 fontweight="bold", fontsize=16)
    plt.tight_layout()
    fig.savefig(out_path, format=fmt, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved F7 -> {out_path}")


# ---------------------------------------------------------------------------
# F8 — Dataset Complexity Profile
# ---------------------------------------------------------------------------

def fig_dataset_complexity(dataset_path: Path, out_path: Path, fmt: str):
    if not dataset_path.exists():
        print(f"  F8: {dataset_path} not found, skipping.")
        return

    by_level: dict[int, list] = defaultdict(list)
    with open(dataset_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            by_level[d["difficulty_level"]].append(d)

    levels = sorted(by_level.keys())
    features = ["depreciable_asset", "cogs", "credit_transaction", "debt",
                "prepaid", "derived_interest", "mixed_funding"]
    feature_labels = {
        "depreciable_asset": "Depreciation",
        "cogs": "COGS",
        "credit_transaction": "Credit Txns",
        "debt": "Debt",
        "prepaid": "Prepaid Items",
        "derived_interest": "Derived Interest",
        "mixed_funding": "Mixed Funding",
    }

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # Left: avg transaction count + avg account count by level
    ax = axes[0]
    tx_means = [np.mean([len(p.get("transactions", [])) for p in by_level[l]]) for l in levels]
    acc_means = [np.mean([
        len({**p["expected"].get("assets", {}),
             **p["expected"].get("liabilities", {}),
             **p["expected"].get("equity", {})})
        for p in by_level[l]]) for l in levels]

    x = np.arange(len(levels))
    b1 = ax.bar(x - 0.2, tx_means, 0.35, label="Avg Transactions", color=PALETTE[0], alpha=0.85)
    b2 = ax.bar(x + 0.2, acc_means, 0.35, label="Avg Accounts", color=PALETTE[1], alpha=0.85)
    ax.set_xticks(x)
    ax.set_xticklabels([f"L{l}" for l in levels])
    ax.set_ylabel("Count")
    ax.set_title("(a) Problem Complexity by Level", fontweight="bold")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.95))
    for bar in list(b1) + list(b2):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                f"{bar.get_height():.0f}", ha="center", va="bottom", fontsize=13, fontweight="bold")

    # Right: feature presence rate heatmap by level
    ax = axes[1]
    feat_matrix = np.zeros((len(features), len(levels)))
    for col, lvl in enumerate(levels):
        problems = by_level[lvl]
        for row, feat in enumerate(features):
            rate = sum(1 for p in problems
                       if p.get("metadata", {}).get(feat) or
                       any(feat in str(t) for t in p.get("transactions", [])))
            feat_matrix[row, col] = rate / len(problems) * 100

    im = ax.imshow(feat_matrix, aspect="auto", cmap="YlOrRd", vmin=0, vmax=100)
    ax.set_xticks(range(len(levels)))
    ax.set_xticklabels([f"L{l}" for l in levels])
    ax.set_yticks(range(len(features)))
    ax.set_yticklabels([feature_labels.get(f, f) for f in features], fontsize=13)
    ax.set_title("(b) Feature Presence Rate (%) by Level", fontweight="bold")
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    for r in range(len(features)):
        for c in range(len(levels)):
            val = feat_matrix[r, c]
            if val > 1:
                ax.text(c, r, f"{val:.0f}", ha="center", va="center",
                        fontsize=13, fontweight="bold",
                        color="white" if val > 60 else "black")

    fig.suptitle("Figure 8: Dataset Complexity Profile", fontweight="bold", fontsize=15)
    plt.tight_layout()
    fig.savefig(out_path, format=fmt, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved F8 -> {out_path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results-dir", default="results")
    ap.add_argument("--dataset",     default="data/test.jsonl")
    ap.add_argument("--out-dir",     default="figures")
    ap.add_argument("--format",      default="pdf", choices=["pdf", "png", "svg"])
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Loading result files...")
    records = load_primary_results(Path(args.results_dir))
    if not records:
        print("No primary result files found.")
        return
    groups = group_by_model_strategy(records)
    print(f"Found {len(groups)} model×strategy combinations:")
    for (m, s) in sorted(groups.keys()):
        print(f"  {m} / {s}  (n={len(groups[(m,s)])})")
    print()

    analyses = load_failure_analyses(Path(args.results_dir))
    print(f"Found {len(analyses)} failure analysis files.")
    print()

    np.random.seed(42)

    print("Generating figures...")
    fig_capability_curve(groups, out_dir / f"F1_capability_curve.{args.format}", args.format)
    fig_error_composition(groups, out_dir / f"F2_error_composition.{args.format}", args.format)
    fig_cot_effect(groups, out_dir / f"F3_cot_effect.{args.format}", args.format)
    fig_account_heatmap(analyses, out_dir / f"F4_account_heatmap.{args.format}", args.format)
    fig_bem_distribution(groups, out_dir / f"F5_bem_distribution.{args.format}", args.format)
    fig_cot_by_difficulty(groups, out_dir / f"F6_cot_by_difficulty.{args.format}", args.format)
    fig_error_propagation(Path(args.results_dir), out_dir / f"F7_propagation.{args.format}", args.format)
    fig_dataset_complexity(Path(args.dataset), out_dir / f"F8_dataset_complexity.{args.format}", args.format)

    print(f"\nAll figures saved to {out_dir}/")


if __name__ == "__main__":
    main()
