"""Shared visual style for FinBalance paper figures."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


BLUE = "#2F5F8F"
TEAL = "#2A9D8F"
ORANGE = "#D97732"
RED = "#B85656"
PURPLE = "#6F5AA7"
GREEN = "#5F8D4E"
GRAY = "#6B7280"
DARK = "#17212B"
LIGHT_GRAY = "#E5E7EB"
PANEL = "#F7F8FA"

PALETTE = [BLUE, ORANGE, TEAL, PURPLE, GREEN, RED, "#8F6B3B", "#577590"]

METRIC_LABELS = {
    "parse_success_rate": "Parse",
    "predicted_entries_reconstruct_correct_final_balance_sheet_rate": "BS recon",
    "final_balance_sheet_matches_rate": "BS exact",
    "final_journal_entries_match_no_doc_refs_rate": "JE acct.",
    "final_balance_sheet_and_journal_entries_match_rate": "Strict BS+JE",
    "inconsistency_code_match_rate": "Inc. code",
    "entries_accounting_correct_but_doc_refs_wrong_rate": "Acct. right, refs wrong",
}

MODEL_LABELS = {
    "google/gemini-3-flash-preview": "Gemini 3 Flash",
    "openai/gpt-5": "GPT-5",
    "deepseek/deepseek-v3.2-exp": "DeepSeek V3.2",
    "qwen/qwen3-235b-a22b-2507": "Qwen3 235B",
    "x-ai/grok-4.3": "Grok 4.3",
    "anthropic/claude-haiku-4.5": "Claude Haiku 4.5",
    "deepseek-chat": "DeepSeek Chat",
    "deepseek-reasoner": "DeepSeek Reasoner",
    "meta-llama/llama-3.3-70b-instruct": "Llama 3.3 70B",
    "anthropic/claude-sonnet-4.6": "Claude Sonnet 4.6",
    "google/gemini-3.1-pro-preview": "Gemini 3.1 Pro",
}

ABLATION_LABELS = {
    "prompt_guided_private_solve": "Guided solve",
    "prompt_self_check": "Guided + verify",
    "visibility_ocr_only": "OCR only",
    "visibility_no_distractors_oracle": "No distractors",
    "visibility_support_docs_removed": "No support docs",
    "visibility_no_allowed_accounts": "No account list",
    "tool_calculator": "Tool prompt: calc.",
    "tool_document_search": "Tool prompt: search",
    "tool_ledger_check": "Tool prompt: ledger",
    "tool_full_tool_agent": "Tool prompt: full",
    "forced_ledger_verifier": "Forced verifier",
    "forced_ledger_verifier_2pass": "Forced verifier x2",
    "prompt_doc_refs_strict": "Citation prompt",
    "self_consistency_k3": "Self-consistency k=3",
    "evidence_only": "Evidence only",
    "evidence_plus_5_distractors": "+5 distractors",
    "evidence_plus_15_distractors": "+15 distractors",
    "evidence_plus_30_distractors": "+30 distractors",
    "evidence_relevant_last": "Relevant last",
}


def apply_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.dpi": 180,
            "savefig.dpi": 300,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "grid.linestyle": "-",
            "axes.axisbelow": True,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def pct(value: float | int | None, digits: int = 0) -> str:
    if value is None:
        return "n/a"
    return f"{100 * float(value):.{digits}f}%"


def pp(value: float | int | None, digits: int = 1) -> str:
    if value is None:
        return "n/a"
    return f"{100 * float(value):+.{digits}f} pp"


def short_label(value: str) -> str:
    return value.replace("_", " ").replace(" and ", " & ").title()


def wrap_label(value: str, width: int = 16) -> str:
    words = short_label(value).split()
    return _wrap_words(words, width)


def wrap_display_label(value: str, width: int = 16) -> str:
    words = value.replace("_", " ").split()
    return _wrap_words(words, width)


def _wrap_words(words: list[str], width: int) -> str:
    lines: list[str] = []
    current: list[str] = []
    current_len = 0
    for word in words:
        next_len = current_len + len(word) + (1 if current else 0)
        if current and next_len > width:
            lines.append(" ".join(current))
            current = [word]
            current_len = len(word)
        else:
            current.append(word)
            current_len = next_len
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines)


def save_figure(fig, output_dir: Path, stem: str) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = [output_dir / f"{stem}.pdf", output_dir / f"{stem}.png"]
    for path in paths:
        fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return paths
