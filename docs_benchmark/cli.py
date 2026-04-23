"""Command-line helpers for the schema-driven synthetic document dataset."""

from __future__ import annotations

import argparse
import json
import os

from docs_benchmark.benchmark import build_prompt, filter_records, load_records, run_openrouter_evaluation
from docs_benchmark.benchmark.model import OpenRouterClient
from docs_benchmark.generation.builder import DocumentBenchmarkBuilder
from docs_benchmark.generation.helpers import PERIOD_TYPES
from docs_benchmark.industry_schemas import INDUSTRIES
from docs_benchmark.schemas import ensure_parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Schema-driven synthetic document dataset generator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate a dataset JSONL and PDF assets")
    generate.add_argument("--output", default="docs_benchmark/data/pilot.jsonl")
    generate.add_argument("--assets-dir", default="docs_benchmark/data/assets")
    generate.add_argument("--records-per-combo", type=int, default=1)
    generate.add_argument("--period-types", nargs="+", choices=PERIOD_TYPES, default=list(PERIOD_TYPES))
    generate.add_argument("--seed", type=int, default=42)
    generate.add_argument("--negative-control-rate", type=float, default=0.05)

    inspect = subparsers.add_parser("inspect", help="Generate one sample record and print a summary")
    inspect.add_argument("--industry", choices=INDUSTRIES, default="professional_services")
    inspect.add_argument("--level", type=int, default=3)
    inspect.add_argument("--period-type", choices=PERIOD_TYPES, default="month")
    inspect.add_argument("--assets-dir", default="docs_benchmark/data/sample_assets")
    inspect.add_argument("--seed", type=int, default=42)
    inspect.add_argument("--negative-control", action="store_true")

    prompt_preview = subparsers.add_parser("prompt-preview", help="Build a model prompt from an existing dataset record")
    prompt_preview.add_argument("--dataset", default="docs_benchmark/data/v3_preview.jsonl")
    prompt_preview.add_argument("--record-id")
    prompt_preview.add_argument("--industry", choices=INDUSTRIES)
    prompt_preview.add_argument("--period-type", choices=PERIOD_TYPES)
    prompt_preview.add_argument("--level", type=int)
    prompt_preview.add_argument("--max-records", type=int, default=1)

    evaluate = subparsers.add_parser("evaluate-openrouter", help="Run the basic docs benchmark against one OpenRouter model")
    evaluate.add_argument("--dataset", default="docs_benchmark/data/v3_preview.jsonl")
    evaluate.add_argument("--output", default="docs_benchmark/results/openrouter_eval.json")
    evaluate.add_argument("--model", required=True)
    evaluate.add_argument("--api-key")
    evaluate.add_argument("--industries", nargs="+", choices=INDUSTRIES)
    evaluate.add_argument("--period-types", nargs="+", choices=PERIOD_TYPES)
    evaluate.add_argument("--levels", nargs="+", type=int)
    evaluate.add_argument("--max-records", type=int, default=15)
    evaluate.add_argument("--temperature", type=float, default=0.0)
    evaluate.add_argument("--max-output-tokens", type=int, default=8192)
    evaluate.add_argument("--timeout", type=int, default=180)

    args = parser.parse_args()
    if args.command == "generate":
        builder = DocumentBenchmarkBuilder(seed=args.seed)
        counts = {
            industry: {
                period_type: {level: args.records_per_combo for level in range(1, 6)}
                for period_type in args.period_types
            }
            for industry in INDUSTRIES
        }
        records = builder.generate_dataset(counts, args.output, args.assets_dir, negative_control_rate=args.negative_control_rate)
        summary = {
            "records": len(records),
            "industries": sorted({record.industry for record in records}),
            "period_types": sorted({record.metadata.get("period_type", "month") for record in records}),
            "avg_docs": round(sum(len(record.documents) for record in records) / len(records), 2) if records else 0.0,
        }
        print(json.dumps(summary, indent=2))
        return

    if args.command == "prompt-preview":
        records = load_records(args.dataset)
        selected = records
        if args.record_id:
            selected = [record for record in selected if record.record_id == args.record_id]
        else:
            selected = filter_records(
                selected,
                industries=[args.industry] if args.industry else None,
                period_types=[args.period_type] if args.period_type else None,
                levels=[args.level] if args.level is not None else None,
                max_records=args.max_records,
            )
        if not selected:
            raise SystemExit("No matching records found in dataset")
        print(build_prompt(selected[0]))
        return

    if args.command == "evaluate-openrouter":
        api_key = args.api_key or os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise SystemExit("OpenRouter API key is required via --api-key or OPENROUTER_API_KEY")

        records = filter_records(
            load_records(args.dataset),
            industries=args.industries,
            period_types=args.period_types,
            levels=args.levels,
            max_records=args.max_records,
        )
        if not records:
            raise SystemExit("No matching records found in dataset")

        client = OpenRouterClient(api_key=api_key, model=args.model)
        evaluation = run_openrouter_evaluation(
            records,
            client=client,
            dataset_path=args.dataset,
            temperature=args.temperature,
            max_tokens=args.max_output_tokens,
            timeout=args.timeout,
        )
        output_path = ensure_parent(args.output)
        output_path.write_text(json.dumps(evaluation, indent=2), encoding="utf-8")
        print(json.dumps(evaluation["summary"], indent=2))
        print(f"Saved detailed results to {output_path}")
        return

    builder = DocumentBenchmarkBuilder(seed=args.seed)
    record = builder.generate_record("SAMPLE", args.industry, args.level, args.assets_dir, period_type=args.period_type, negative_control=args.negative_control)
    summary = {
        "record_id": record.record_id,
        "industry": record.industry,
        "difficulty_level": record.difficulty_level,
        "period_type": record.metadata.get("period_type"),
        "period_label": record.metadata.get("period_label"),
        "documents": len(record.documents),
        "entries": len(record.expected_entries),
        "balanced": record.expected_balance_sheet.balanced,
        "expected_inconsistency": record.expected_inconsistency,
        "scenario_sequence": record.metadata.get("scenario_sequence", []),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
