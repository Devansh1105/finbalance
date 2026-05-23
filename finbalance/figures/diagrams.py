"""Conceptual diagrams and flowcharts for the FinBalance paper."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

from finbalance.figures.style import (
    BLUE,
    DARK,
    GRAY,
    GREEN,
    LIGHT_GRAY,
    ORANGE,
    PANEL,
    PURPLE,
    RED,
    TEAL,
    apply_style,
    save_figure,
)


def diagram_dataset_packet(output_dir: Path) -> list[Path]:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.0, 4.7))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    _title(ax, 0.5, 0.96, "One FinBalance Record")
    _box(ax, 0.04, 0.76, 0.24, 0.125, "Posting documents", "Invoice, receipt,\npayment advice,\nopening trial balance", BLUE, body_size=6.9)
    _box(ax, 0.04, 0.58, 0.24, 0.125, "Support documents", "Bank statement,\nrate card, rollforward,\ntax profile", TEAL, body_size=6.9)
    _box(ax, 0.04, 0.40, 0.24, 0.125, "Distractor documents", "Duplicate copies,\nmemos, void/cancel\nnotices", ORANGE, body_size=6.9)
    _box(ax, 0.04, 0.18, 0.24, 0.125, "Allowed accounts", "Benchmark account\ntaxonomy visible\nin prompt", PURPLE, body_size=6.9)

    _box(ax, 0.38, 0.60, 0.24, 0.16, "Visible packet", "Doc IDs + OCR text\n+ titles/types/roles depending\non visibility ablation", GREEN)
    _box(ax, 0.38, 0.27, 0.24, 0.16, "Hidden accounting truth", "Journal entries\nReplayed ledger\nFinal balance sheet", GRAY)

    _box(ax, 0.72, 0.66, 0.23, 0.13, "Model answer", "Strict JSON:\nentries + doc_refs + BS", BLUE)
    _box(ax, 0.72, 0.43, 0.23, 0.13, "Scoring", "Parse, account match,\ndoc refs, BS exact,\nBS replay", RED)
    _box(ax, 0.72, 0.18, 0.23, 0.13, "Inconsistency mode", "Mutated visible doc ->\nclaim code, no entries", ORANGE)

    for y in (0.82, 0.64, 0.46, 0.24):
        _arrow(ax, (0.29, y), (0.38, 0.68 if y > 0.35 else 0.35))
    _arrow(ax, (0.62, 0.68), (0.72, 0.72))
    _arrow(ax, (0.84, 0.66), (0.84, 0.56))
    _arrow(ax, (0.62, 0.35), (0.72, 0.49))
    _arrow(ax, (0.62, 0.35), (0.72, 0.24))

    _caption(
        ax,
        0.5,
        0.06,
        "The model sees the document packet and account list; entries, final balances, and injected contradictions remain hidden.",
    )
    return save_figure(fig, output_dir, "diag_dataset_packet")


def diagram_generation_inference(output_dir: Path) -> list[Path]:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.1, 4.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    _title(ax, 0.5, 0.96, "Deterministic Forward Generation, Hard Backward Inference")
    _box(ax, 0.03, 0.74, 0.18, 0.13, "Design axes", "Industry\nPeriod\nDifficulty", BLUE, body_size=7.1)
    _box(ax, 0.03, 0.54, 0.18, 0.13, "Accounting axes", "Tax regime\nFX/currency\nSubledgers", TEAL, body_size=7.1)
    _box(ax, 0.03, 0.34, 0.18, 0.13, "Scenario axes", "Billing, collections\naccruals, leases/assets", ORANGE, body_size=7.1)
    _box(ax, 0.03, 0.14, 0.18, 0.13, "Noise axes", "Distractors\nOrdering\nInconsistency", PURPLE, body_size=7.1)

    _box(ax, 0.31, 0.58, 0.20, 0.14, "Scenario builders", "Create document seeds,\npostings, bank rows,\nsubledger updates", GREEN)
    _box(ax, 0.31, 0.30, 0.20, 0.14, "Ledger replay", "Apply all postings to\nopening balance", GRAY)

    _box(ax, 0.60, 0.58, 0.17, 0.14, "Rendered packet", "PDF-style assets\n+ OCR text", BLUE)
    _box(ax, 0.60, 0.30, 0.17, 0.14, "Answer key", "Entries\nDoc refs\nBalance sheet", TEAL)

    _box(ax, 0.84, 0.58, 0.13, 0.14, "Model view", "Mixed visible\ndocuments", ORANGE)
    _box(ax, 0.84, 0.30, 0.13, 0.14, "Inverse task", "Recover hidden\nledger state", RED, body_size=7.2)

    for y in (0.80, 0.60, 0.40, 0.20):
        _arrow(ax, (0.22, y), (0.31, 0.65 if y >= 0.5 else 0.37))
    _arrow(ax, (0.51, 0.65), (0.60, 0.65))
    _arrow(ax, (0.51, 0.37), (0.60, 0.37))
    _arrow(ax, (0.68, 0.58), (0.68, 0.44))
    _arrow(ax, (0.77, 0.65), (0.84, 0.65))
    _arrow(ax, (0.90, 0.58), (0.90, 0.44))
    _arrow(ax, (0.84, 0.37), (0.77, 0.37))

    _caption(
        ax,
        0.5,
        0.055,
        "Generation composes many simple deterministic choices; evaluation asks the model to invert the composition from noisy evidence.",
    )
    return save_figure(fig, output_dir, "diag_generation_inference")


def flow_codebase_pipeline(output_dir: Path) -> list[Path]:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.0, 4.3))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    _title(ax, 0.5, 0.95, "FinBalance Codebase Flow")
    nodes = [
        (0.04, 0.68, 0.16, 0.13, "Schemas", "Document and\nindustry schemas", BLUE),
        (0.27, 0.68, 0.16, 0.13, "Generator", "Scenarios,\nmaster data,\nledger state", TEAL),
        (0.50, 0.68, 0.16, 0.13, "Dataset", "records.jsonl\nassets/\nmanifest", GREEN),
        (0.73, 0.68, 0.16, 0.13, "Prompting", "Visibility +\nprompt variant", ORANGE),
        (0.73, 0.36, 0.16, 0.13, "Model run", "OpenRouter or\nother backend", RED),
        (0.50, 0.36, 0.16, 0.13, "Parser", "Strict JSON\nsubmission", PURPLE),
        (0.27, 0.36, 0.16, 0.13, "Scorer", "Entries, doc refs,\nBS replay", BLUE),
        (0.04, 0.36, 0.16, 0.13, "Analysis", "Summaries,\nslices,\nfigures", GRAY),
    ]
    for x, y, w, h, title, body, color in nodes:
        _box(ax, x, y, w, h, title, body, color)
    for start, end in [
        ((0.20, 0.745), (0.27, 0.745)),
        ((0.43, 0.745), (0.50, 0.745)),
        ((0.66, 0.745), (0.73, 0.745)),
        ((0.81, 0.68), (0.81, 0.49)),
        ((0.73, 0.425), (0.66, 0.425)),
        ((0.50, 0.425), (0.43, 0.425)),
        ((0.27, 0.425), (0.20, 0.425)),
    ]:
        _arrow(ax, start, end)
    _caption(ax, 0.5, 0.15, "The same artifacts drive benchmark release, model evaluation, ablations, and final paper figures.")
    return save_figure(fig, output_dir, "flow_codebase_pipeline")


def flow_record_generation_detail(output_dir: Path) -> list[Path]:
    apply_style()
    fig, ax = plt.subplots(figsize=(7.4, 7.1))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    _title(ax, 0.5, 0.96, "Record Generation Detail")
    steps = [
        ("1. Select task cell", "industry, period type, difficulty"),
        ("2. Choose display/accounting profile", "currency, date format, tax regime"),
        ("3. Build business state", "opening balance, entity, master data"),
        ("4. Run scenario builders", "documents, postings, bank rows, subledgers"),
        ("5. Add benchmark surface", "distractors, trial balance, bank statement"),
        ("6. Render and validate", "PDF-style assets, OCR text, schema checks"),
        ("7. Create labels", "ledger replay, balance sheet, entry refs"),
        ("8. Optional negative control", "mutate visible evidence and store inconsistency code"),
    ]
    x = 0.18
    y = 0.84
    box_h = 0.061
    step_gap = 0.112
    for idx, (title, body) in enumerate(steps):
        color = PALETTE_FOR_STEPS[idx % len(PALETTE_FOR_STEPS)]
        _box(ax, x, y, 0.64, box_h, title, body, color, body_size=6.7, header_h=0.025)
        if idx < len(steps) - 1:
            _arrow(ax, (0.50, y - 0.004), (0.50, y - (step_gap - box_h) + 0.004))
        y -= step_gap
    _caption(ax, 0.5, 0.025, "This figure is intended for the appendix; it mirrors finbalance/FLOW.md.")
    return save_figure(fig, output_dir, "flow_record_generation_detail")


PALETTE_FOR_STEPS = [BLUE, TEAL, ORANGE, GREEN, PURPLE, GRAY, RED, "#8F6B3B"]


def _box(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    body: str,
    color: str,
    *,
    body_size: float = 7.8,
    header_h: float = 0.032,
) -> None:
    shadow = FancyBboxPatch(
        (x + 0.006, y - 0.006),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=0,
        facecolor="#000000",
        alpha=0.08,
        zorder=1,
    )
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=1,
        edgecolor=color,
        facecolor=_tint(color),
        zorder=2,
    )
    ax.add_patch(shadow)
    ax.add_patch(patch)
    ax.add_patch(Rectangle((x, y + h - header_h), w, header_h, linewidth=0, facecolor=color, zorder=3))
    ax.text(x + w / 2, y + h - header_h / 2, title, ha="center", va="center", fontsize=7.8, color="white", weight="bold", zorder=4)
    body_y = y + (h - header_h) * 0.43
    ax.text(x + w / 2, body_y, body, ha="center", va="center", fontsize=body_size, color=DARK, linespacing=1.16, zorder=4)


def _arrow(ax, start: tuple[float, float], end: tuple[float, float]) -> None:
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=10,
        linewidth=1.1,
        color=GRAY,
        shrinkA=2,
        shrinkB=2,
        zorder=0,
    )
    ax.add_patch(arrow)


def _title(ax, x: float, y: float, text: str) -> None:
    ax.text(x, y, text, ha="center", va="center", fontsize=11, weight="bold", color=DARK)


def _caption(ax, x: float, y: float, text: str) -> None:
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=7.5,
        color=GRAY,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": PANEL, "edgecolor": LIGHT_GRAY, "linewidth": 0.6},
    )


def _tint(color: str) -> str:
    # Hand-picked light tints avoid depending on color conversion helpers.
    return {
        BLUE: "#EAF1F8",
        TEAL: "#E8F5F3",
        ORANGE: "#FAEFE6",
        RED: "#F8EDED",
        PURPLE: "#F0EDF7",
        GREEN: "#EEF5EC",
        GRAY: "#F1F3F5",
        "#8F6B3B": "#F5F0EA",
    }.get(color, "#F6F7F8")
