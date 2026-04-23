"""Minimal benchmark runner for the synthetic document dataset."""

from docs_benchmark.benchmark.dataset import filter_records, load_records
from docs_benchmark.benchmark.model import OpenRouterClient
from docs_benchmark.benchmark.parser import SubmissionParseError, parse_submission
from docs_benchmark.benchmark.prompt import build_prompt
from docs_benchmark.benchmark.runner import run_openrouter_evaluation
from docs_benchmark.benchmark.scoring import score_submission, summarize_results

__all__ = [
    "OpenRouterClient",
    "SubmissionParseError",
    "build_prompt",
    "filter_records",
    "load_records",
    "parse_submission",
    "run_openrouter_evaluation",
    "score_submission",
    "summarize_results",
]
