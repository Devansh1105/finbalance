#!/usr/bin/env python3
"""Run the FinBalance harness with PydanticAI's OpenRouter integration."""

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from finbalance.analysis.error_detection import aggregate_errors
from finbalance.evaluation.metrics.core import aggregate
from finbalance.evaluation.models.base import DEFAULT_MAX_TOKENS
from finbalance.evaluation.pydantic_ai import (
    DEFAULT_OPENROUTER_MODELS,
    OpenRouterAgentConfig,
    OpenRouterBatchConfig,
    PydanticAIOpenRouterModel,
    load_dataset,
    sample_stratified_subset,
)
from finbalance.evaluation.runner import EvaluationRunner


def build_model(config: OpenRouterBatchConfig, model_id: str, strategy: str) -> PydanticAIOpenRouterModel:
    """Create one PydanticAI/OpenRouter-backed model instance."""
    return PydanticAIOpenRouterModel(
        OpenRouterAgentConfig(
            model_id=model_id,
            temperature=config.temperature,
            seed=config.seed,
            max_tokens=config.max_tokens,
            timeout=config.timeout,
            api_key=config.api_key,
            app_url=config.app_url,
            app_title=config.app_title,
            openrouter_reasoning_effort=(
                config.cot_openrouter_reasoning_effort
                if strategy == "cot" and config.cot_openrouter_reasoning_effort.lower() != "off"
                else None
            ),
        )
    )


def print_summary(model_id: str, strategy: str, results, agg, err_stats) -> None:
    print(f"\n{'=' * 65}")
    print(f"  Model:    {model_id}")
    print(f"  Strategy: {strategy}")
    print(f"  Problems: {agg.n_problems}")
    print(f"{'=' * 65}")
    print(f"  {'Metric':<30} {'Value':>10}")
    print(f"  {'-' * 42}")
    print(f"  {'Balance Accuracy (BA)':<30} {agg.BA * 100:>9.1f}%")
    print(f"  {'Account-Level Accuracy (ALA)':<30} {agg.ALA * 100:>9.1f}%")
    print(f"  {'Transaction Processing (TPA)':<30} {agg.TPA * 100:>9.1f}%")
    print(f"  {'Constraint Satisfaction (CSR)':<30} {agg.CSR * 100:>9.1f}%")
    print(f"  {'MAE':<30} {agg.MAE:>10,.0f}")
    print(f"  {'FinBalance Score (FBS)':<30} {agg.FBS:>10.1f}")
    print(f"  {'FBS weighted':<30} {agg.FBS_weighted:>10.1f}")
    print(f"  {'Parse error rate':<30} {agg.parse_error_rate * 100:>9.1f}%")

    if agg.by_difficulty:
        print("\n  By difficulty:")
        print(f"  {'Level':<8} {'N':>5} {'BA':>7} {'ALA':>7} {'FBS':>7}")
        for level in sorted(agg.by_difficulty):
            bucket = agg.by_difficulty[level]
            print(
                f"  {level:<8} {bucket['n']:>5} {bucket['BA'] * 100:>6.1f}% "
                f"{bucket['ALA'] * 100:>6.1f}% {bucket['FBS']:>7.1f}"
            )

    if err_stats.by_category:
        print("\n  Error breakdown:")
        for category, info in err_stats.by_category.items():
            print(f"  {'  ' + category:<30} {info['count']:>5}  ({info['pct']:.1f}%)")


def parse_args() -> OpenRouterBatchConfig:
    parser = argparse.ArgumentParser(
        description="Run FinBalance via PydanticAI + OpenRouter on the Large-500 subset by default"
    )
    parser.add_argument("--dataset", default="data/large500.jsonl", help="Path to JSONL dataset file")
    parser.add_argument(
        "--models",
        default=",".join(DEFAULT_OPENROUTER_MODELS),
        help="Comma-separated OpenRouter model IDs",
    )
    parser.add_argument(
        "--strategies",
        default="zero_shot",
        help="Comma-separated strategies: zero_shot,few_shot,cot,self_refine",
    )
    parser.add_argument(
        "--subset-size",
        type=int,
        default=500,
        help="Number of problems to sample stratified by difficulty (Large-500 default: 500)",
    )
    parser.add_argument(
        "--subset-seed",
        type=int,
        default=42,
        help="Random seed used for the stratified subset draw",
    )
    parser.add_argument(
        "--write-subset-path",
        default=None,
        help="Optional path to save the sampled subset JSONL before evaluation",
    )
    parser.add_argument("--output", default="results/pydantic_ai", help="Output directory")
    parser.add_argument("--seed", type=int, default=42, help="Model seed")
    parser.add_argument("--temperature", type=float, default=0.0, help="Model temperature")
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_TOKENS,
        help=f"Max response tokens per call (default {DEFAULT_MAX_TOKENS}); not the combined input+output limit",
    )
    parser.add_argument("--timeout", type=int, default=120, help="Timeout per request in seconds")
    parser.add_argument("--api-key", default=None, help="Overrides OPENROUTER_API_KEY")
    parser.add_argument(
        "--cot-reasoning-effort",
        default="high",
        choices=["off", "low", "medium", "high"],
        help="OpenRouter native reasoning effort to apply when strategy=cot",
    )
    parser.add_argument(
        "--parallel-runs",
        type=int,
        default=1,
        help="How many model×strategy jobs to run concurrently",
    )
    parser.add_argument("--workers", type=int, default=1, help="Concurrent requests per run")
    parser.add_argument("--app-url", default=None, help="Optional OpenRouter attribution URL")
    parser.add_argument("--app-title", default="FinBalance", help="Optional OpenRouter attribution title")
    args = parser.parse_args()

    return OpenRouterBatchConfig(
        dataset_path=Path(args.dataset),
        output_dir=Path(args.output),
        subset_size=args.subset_size,
        subset_seed=args.subset_seed,
        write_subset_path=Path(args.write_subset_path) if args.write_subset_path else None,
        model_ids=tuple(model.strip() for model in args.models.split(",") if model.strip()),
        strategies=tuple(strategy.strip() for strategy in args.strategies.split(",") if strategy.strip()),
        parallel_runs=args.parallel_runs,
        workers=args.workers,
        seed=args.seed,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        timeout=args.timeout,
        api_key=args.api_key,
        app_url=args.app_url,
        app_title=args.app_title,
        cot_openrouter_reasoning_effort=args.cot_reasoning_effort,
    )


def main() -> None:
    config = parse_args()

    print(f"Loading dataset from {config.dataset_path}...")
    problems = load_dataset(config.dataset_path)
    if not problems:
        raise ValueError(f"No problems found in {config.dataset_path}")

    if config.subset_size > 0 and config.subset_size < len(problems):
        eval_problems = sample_stratified_subset(problems, config.subset_size, config.subset_seed)
        subset_label = "Large-500 " if len(eval_problems) == 500 else ""
        print(
            f"Using {subset_label}stratified subset of {len(eval_problems)} problems "
            f"(seed={config.subset_seed}) from {len(problems)} total."
        )
    else:
        eval_problems = problems
        print(f"Using full dataset with {len(eval_problems)} problems.")

    level_counts = Counter(problem.difficulty_level for problem in eval_problems)
    print("Subset breakdown:", ", ".join(f"L{level}={level_counts[level]}" for level in sorted(level_counts)))

    if config.write_subset_path is not None:
        config.write_subset_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config.write_subset_path, "w") as handle:
            for problem in eval_problems:
                handle.write(json.dumps(problem.to_dict()) + "\n")
        print(f"Saved sampled subset to {config.write_subset_path}")

    config.output_dir.mkdir(parents=True, exist_ok=True)

    jobs = [(model_id, strategy) for model_id in config.model_ids for strategy in config.strategies]
    if not jobs:
        print("No model jobs requested. Exiting after subset preparation.")
        return

    def run_job(model_id: str, strategy: str) -> tuple[str, str]:
        model = build_model(config, model_id, strategy)
        runner = EvaluationRunner(
            model,
            strategy=strategy,
            verbose=True,
            max_workers=config.workers,
        )
        safe_model = model_id.replace("/", "_")
        out_path = config.output_dir / f"{safe_model}_{strategy}.json"

        results = runner.run(eval_problems, autosave_path=str(out_path))
        agg = aggregate([result.metrics for result in results])
        err_stats = aggregate_errors(
            [result.errors for result in results],
            [result.difficulty for result in results],
        )

        print_summary(model_id, strategy, results, agg, err_stats)

        runner.save_results(results, str(out_path))
        return model_id, strategy

    if config.parallel_runs <= 1 or len(jobs) == 1:
        for model_id, strategy in jobs:
            run_job(model_id, strategy)
        return

    max_parallel_runs = min(config.parallel_runs, len(jobs))
    print(f"Running {len(jobs)} model×strategy jobs with parallel-runs={max_parallel_runs}.")
    with ThreadPoolExecutor(max_workers=max_parallel_runs) as executor:
        futures = {
            executor.submit(run_job, model_id, strategy): (model_id, strategy)
            for model_id, strategy in jobs
        }
        for future in as_completed(futures):
            model_id, strategy = futures[future]
            completed_model, completed_strategy = future.result()
            print(f"Completed job: {completed_model} | {completed_strategy}")


if __name__ == "__main__":
    main()
