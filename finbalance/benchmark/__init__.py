"""Minimal benchmark runner for the synthetic document dataset."""

from finbalance.benchmark.ablations import (
    AblationSpec,
    apply_visibility_variant,
    load_existing_ablation_results,
    run_ablation_evaluation,
    select_ablation_specs,
    summarize_ablation_results,
    write_ablation_outputs,
)
from finbalance.benchmark.bootstrap import analyze_ablation_bootstrap
from finbalance.benchmark.analysis import (
    analyze_submission,
    group_results_by_feature_flags,
    group_results_by_field,
    group_results_by_membership,
    ledger_family_for_label,
    summarize_result_subset,
    summarize_expected_entry_groups,
)
from finbalance.benchmark.dataset import filter_records, load_records, stratified_sample_records
from finbalance.benchmark.manifests import dataset_manifest, record_manifest_row, record_feature_flags, write_jsonl
from finbalance.benchmark.model import OpenRouterClient
from finbalance.benchmark.parser import SubmissionParseError, parse_submission
from finbalance.benchmark.prompt import PROMPT_VARIANTS, VISIBILITY_VARIANTS, build_prompt
from finbalance.benchmark.runner import run_openrouter_evaluation
from finbalance.benchmark.scoring import score_submission, summarize_results
from finbalance.benchmark.tools import TOOL_VARIANTS

__all__ = [
    "analyze_submission",
    "analyze_ablation_bootstrap",
    "AblationSpec",
    "apply_visibility_variant",
    "dataset_manifest",
    "group_results_by_feature_flags",
    "group_results_by_field",
    "group_results_by_membership",
    "ledger_family_for_label",
    "load_existing_ablation_results",
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
    "stratified_sample_records",
    "summarize_ablation_results",
    "summarize_result_subset",
    "summarize_expected_entry_groups",
    "summarize_results",
    "TOOL_VARIANTS",
    "VISIBILITY_VARIANTS",
    "write_ablation_outputs",
    "write_jsonl",
]
