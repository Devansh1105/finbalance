"""Minimal benchmark runner for the synthetic document dataset."""

from docs_benchmark.benchmark.ablations import (
    AblationSpec,
    apply_visibility_variant,
    run_ablation_evaluation,
    select_ablation_specs,
    summarize_ablation_results,
    write_ablation_outputs,
)
from docs_benchmark.benchmark.analysis import (
    analyze_submission,
    group_results_by_feature_flags,
    group_results_by_field,
    group_results_by_membership,
    ledger_family_for_label,
    summarize_result_subset,
    summarize_expected_entry_groups,
)
from docs_benchmark.benchmark.dataset import filter_records, load_records
from docs_benchmark.benchmark.manifests import dataset_manifest, record_manifest_row, record_feature_flags, write_jsonl
from docs_benchmark.benchmark.model import OpenRouterClient
from docs_benchmark.benchmark.parser import SubmissionParseError, parse_submission
from docs_benchmark.benchmark.prompt import PROMPT_VARIANTS, VISIBILITY_VARIANTS, build_prompt
from docs_benchmark.benchmark.runner import run_openrouter_evaluation
from docs_benchmark.benchmark.scoring import score_submission, summarize_results
from docs_benchmark.benchmark.tools import TOOL_VARIANTS

__all__ = [
    "analyze_submission",
    "AblationSpec",
    "apply_visibility_variant",
    "dataset_manifest",
    "group_results_by_feature_flags",
    "group_results_by_field",
    "group_results_by_membership",
    "ledger_family_for_label",
    "OpenRouterClient",
    "PROMPT_VARIANTS",
    "record_feature_flags",
    "record_manifest_row",
    "run_ablation_evaluation",
    "SubmissionParseError",
    "build_prompt",
    "filter_records",
    "load_records",
    "parse_submission",
    "run_openrouter_evaluation",
    "select_ablation_specs",
    "score_submission",
    "summarize_ablation_results",
    "summarize_result_subset",
    "summarize_expected_entry_groups",
    "summarize_results",
    "TOOL_VARIANTS",
    "VISIBILITY_VARIANTS",
    "write_ablation_outputs",
    "write_jsonl",
]
