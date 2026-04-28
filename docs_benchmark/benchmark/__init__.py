"""Minimal benchmark runner for the synthetic document dataset."""

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
from docs_benchmark.benchmark.prompt import build_prompt
from docs_benchmark.benchmark.runner import run_openrouter_evaluation
from docs_benchmark.benchmark.scoring import score_submission, summarize_results

__all__ = [
    "analyze_submission",
    "dataset_manifest",
    "group_results_by_feature_flags",
    "group_results_by_field",
    "group_results_by_membership",
    "ledger_family_for_label",
    "OpenRouterClient",
    "record_feature_flags",
    "record_manifest_row",
    "SubmissionParseError",
    "build_prompt",
    "filter_records",
    "load_records",
    "parse_submission",
    "run_openrouter_evaluation",
    "score_submission",
    "summarize_result_subset",
    "summarize_expected_entry_groups",
    "summarize_results",
    "write_jsonl",
]
