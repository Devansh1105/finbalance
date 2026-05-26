"""Command-line helpers for the schema-driven synthetic document dataset."""

from __future__ import annotations

import argparse
import copy
import json
import os
import shutil
import tempfile
from pathlib import Path

from finbalance.benchmark import (
    analyze_ablation_bootstrap,
    build_prompt,
    filter_records,
    load_existing_ablation_results,
    load_records,
    run_openrouter_evaluation,
    select_ablation_specs,
    stratified_sample_records,
    run_ablation_evaluation,
    write_ablation_outputs,
)
from finbalance.benchmark.manifests import dataset_manifest, record_manifest_row, write_jsonl
from finbalance.benchmark.model import OpenRouterClient
from finbalance.generation.builder import DocumentBenchmarkBuilder
from finbalance.generation.helpers import DISPLAY_PROFILES, PERIOD_TYPES
from finbalance.industry_schemas import INDUSTRIES
from finbalance.inconsistencies import INCONSISTENCY_CODES
from finbalance.schemas import ensure_parent


FORCED_INCONSISTENCY_CANDIDATES = {
    "invoice_total_mismatch": (("professional_services", "month", 2, None),),
    "bank_closing_mismatch": (("professional_services", "month", 1, None),),
    "statement_balance_mismatch": (("professional_services", "year", 5, None), ("manufacturing", "year", 5, None)),
    "payment_allocation_mismatch": (("professional_services", "quarter", 3, None),),
    "duplicate_reference_conflict": (("professional_services", "year", 5, None), ("subscription_saas", "year", 5, None)),
    "schedule_rollforward_mismatch": (("professional_services", "quarter", 3, None), ("subscription_saas", "month", 4, None)),
    "inventory_rollforward_mismatch": (("wholesale_distribution", "year", 5, None), ("retail", "year", 5, None)),
    "transfer_mismatch": (("subscription_saas", "quarter", 4, None), ("professional_services", "month", 4, None)),
    "reclassification_support_mismatch": (("professional_services", "quarter", 3, None),),
    "tax_total_mismatch": (("professional_services", "month", 2, "sales_tax"),),
    "tax_rate_mismatch": (("professional_services", "month", 2, "sales_tax"),),
    "input_tax_mismatch": (("professional_services", "month", 2, "sales_tax"),),
    "jurisdiction_tax_mismatch": (("wholesale_distribution", "month", 4, "us_sales_tax"),),
    "tax_exemption_conflict": (("wholesale_distribution", "month", 4, "us_sales_tax"),),
    "ssp_allocation_mismatch": (("subscription_saas", "month", 4, None),),
    "performance_obligation_release_mismatch": (("subscription_saas", "month", 4, None),),
    "asset_disposal_mismatch": (("professional_services", "month", 4, None),),
    "deferred_tax_rollforward_mismatch": (("professional_services", "month", 5, None),),
    "lease_schedule_mismatch": (("professional_services", "month", 4, None),),
    "lease_remeasurement_mismatch": (("professional_services", "month", 5, None),),
    "exchange_rate_mismatch": (("professional_services", "year", 5, None), ("subscription_saas", "year", 5, None)),
    "fx_settlement_mismatch": (("professional_services", "quarter", 5, None), ("subscription_saas", "quarter", 5, None)),
    "remeasurement_mismatch": (("subscription_saas", "year", 5, None), ("professional_services", "year", 5, None)),
}

BACKEND_CHAT_COMPLETIONS_URLS = {
    "openrouter": "https://openrouter.ai/api/v1/chat/completions",
    "deepseek": "https://api.deepseek.com/chat/completions",
}


def _aggregation_gap_record_ids(path: Path) -> set[str]:
    if path.is_dir():
        path = path / "per_record_results.jsonl"
    if not path.exists():
        raise SystemExit(f"Aggregation-gap source not found: {path}")

    if path.suffix == ".jsonl":
        with path.open(encoding="utf-8") as handle:
            rows = [json.loads(line) for line in handle if line.strip()]
    else:
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = list(payload.get("results", []))

    record_ids = {str(row.get("record_id")) for row in rows if _is_aggregation_gap_row(row)}
    if not record_ids:
        raise SystemExit(f"No aggregation-gap records found in {path}")
    return record_ids


def _is_aggregation_gap_row(row: dict) -> bool:
    metrics = row.get("metrics", {})
    return bool(
        metrics.get("parse_success")
        and not metrics.get("expected_inconsistency")
        and metrics.get("predicted_entries_reconstruct_correct_final_balance_sheet")
        and not metrics.get("final_balance_sheet_matches")
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Schema-driven synthetic document dataset generator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate a dataset JSONL and PDF assets")
    generate.add_argument("--output", default="data/pilot.jsonl")
    generate.add_argument("--assets-dir", default="data/assets")
    generate.add_argument("--records-per-combo", type=int, default=1)
    generate.add_argument("--period-types", nargs="+", choices=PERIOD_TYPES, default=list(PERIOD_TYPES))
    generate.add_argument("--seed", type=int, default=42)
    generate.add_argument("--negative-control-rate", type=float, default=0.05)

    standard = subparsers.add_parser("generate-standard-datasets", help="Regenerate finbalance coverage and main datasets with manifests")
    standard.add_argument("--base-dir", default="data")
    standard.add_argument("--seed", type=int, default=42)
    standard.add_argument("--records-per-combo", type=int, default=4)
    standard.add_argument("--negative-controls-per-code", type=int, default=10)
    standard.add_argument(
        "--main-only",
        action="store_true",
        help="Regenerate only data/main as an extension of existing data/coverage",
    )

    inspect = subparsers.add_parser("inspect", help="Generate one sample record and print a summary")
    inspect.add_argument("--industry", choices=INDUSTRIES, default="professional_services")
    inspect.add_argument("--level", type=int, default=3)
    inspect.add_argument("--period-type", choices=PERIOD_TYPES, default="month")
    inspect.add_argument("--assets-dir", default="data/sample_assets")
    inspect.add_argument("--seed", type=int, default=42)
    inspect.add_argument("--negative-control", action="store_true")

    prompt_preview = subparsers.add_parser("prompt-preview", help="Build a model prompt from an existing dataset record")
    prompt_preview.add_argument("--dataset", default="data/v3_preview.jsonl")
    prompt_preview.add_argument("--record-id")
    prompt_preview.add_argument("--industry", choices=INDUSTRIES)
    prompt_preview.add_argument("--period-type", choices=PERIOD_TYPES)
    prompt_preview.add_argument("--level", type=int)
    prompt_preview.add_argument("--max-records", type=int, default=1)

    evaluate = subparsers.add_parser("evaluate-openrouter", help="Run the basic FinBalance benchmark against one OpenRouter model")
    evaluate.add_argument("--dataset", default="data/v3_preview.jsonl")
    evaluate.add_argument("--output", default="results/openrouter_eval.json")
    evaluate.add_argument("--model", required=True)
    evaluate.add_argument("--api-key")
    evaluate.add_argument("--industries", nargs="+", choices=INDUSTRIES)
    evaluate.add_argument("--period-types", nargs="+", choices=PERIOD_TYPES)
    evaluate.add_argument("--levels", nargs="+", type=int)
    evaluate.add_argument("--max-records", type=int, default=15)
    evaluate.add_argument("--temperature", type=float, default=0.0)
    evaluate.add_argument("--max-output-tokens", type=int, default=8192)
    evaluate.add_argument("--timeout", type=int, default=180)
    evaluate.add_argument("--max-retries", type=int, default=3)
    evaluate.add_argument("--reasoning-effort", choices=["none", "minimal", "low", "medium", "high", "xhigh"])

    ablations = subparsers.add_parser("evaluate-ablations", help="Run provider-neutral benchmark ablations")
    ablations.add_argument("--dataset", default="data/coverage/records.jsonl")
    ablations.add_argument("--output-dir", default="results/ablations")
    ablations.add_argument("--backend", choices=["openrouter", "deepseek"], default="openrouter")
    ablations.add_argument("--model", required=True)
    ablations.add_argument("--api-key")
    ablations.add_argument("--matrix", choices=["coverage", "targeted", "context_stress"], default="coverage")
    ablations.add_argument("--ablations", nargs="+")
    ablations.add_argument("--industries", nargs="+", choices=INDUSTRIES)
    ablations.add_argument("--period-types", nargs="+", choices=PERIOD_TYPES)
    ablations.add_argument("--levels", nargs="+", type=int)
    ablations.add_argument("--max-records", type=int, default=15)
    ablations.add_argument("--sample-strategy", choices=["ordered", "stratified"], default="ordered")
    ablations.add_argument(
        "--aggregation-gap-from-results",
        help=(
            "Filter to record IDs from a baseline ablation result where predicted entries "
            "reconstruct the expected balance sheet but the submitted balance sheet is wrong."
        ),
    )
    ablations.add_argument("--temperature", type=float, default=0.0)
    ablations.add_argument("--max-output-tokens", type=int, default=8192)
    ablations.add_argument("--timeout", type=int, default=180)
    ablations.add_argument("--max-retries", type=int, default=3)
    ablations.add_argument("--reasoning-effort", choices=["none", "minimal", "low", "medium", "high", "xhigh"])
    ablations.add_argument("--agent-max-steps", type=int, default=8)
    ablations.add_argument("--resume", action="store_true", help="Skip records already present in per_record_results.jsonl")
    ablations.add_argument(
        "--resume-valid-only",
        action="store_true",
        help="With --resume, skip only prior rows that parsed successfully",
    )
    ablations.add_argument(
        "--checkpoint-every",
        type=int,
        default=0,
        help="Write partial ablation outputs every N records; use with --resume for safe continuation",
    )
    ablations.add_argument(
        "--abort-on-max-token-parse-failure",
        action="store_true",
        help="Stop the run if a response hits max output tokens and cannot be parsed",
    )

    analyze_ablations = subparsers.add_parser("analyze-ablations", help="Bootstrap compare ablation result directories")
    analyze_ablations.add_argument("--results-dir", required=True)
    analyze_ablations.add_argument("--baseline", default="prompt_baseline")
    analyze_ablations.add_argument("--iterations", type=int, default=5000)
    analyze_ablations.add_argument("--confidence", type=float, default=0.95)
    analyze_ablations.add_argument("--seed", type=int, default=1)
    analyze_ablations.add_argument("--output-dir")

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

    if args.command == "generate-standard-datasets":
        if args.main_only:
            summary = regenerate_main_dataset_from_existing_coverage(
                base_dir=args.base_dir,
                seed=args.seed,
                records_per_combo=args.records_per_combo,
                negative_controls_per_code=args.negative_controls_per_code,
            )
        else:
            summary = regenerate_standard_datasets(
                base_dir=args.base_dir,
                seed=args.seed,
                records_per_combo=args.records_per_combo,
                negative_controls_per_code=args.negative_controls_per_code,
            )
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

        client = OpenRouterClient(
            api_key=api_key,
            model=args.model,
            base_url=BACKEND_CHAT_COMPLETIONS_URLS["openrouter"],
            app_name="finbalance-openrouter",
            max_retries=args.max_retries,
            reasoning_effort=args.reasoning_effort,
        )
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

    if args.command == "evaluate-ablations":
        env_var = "DEEPSEEK_API_KEY" if args.backend == "deepseek" else "OPENROUTER_API_KEY"
        api_key = args.api_key or os.environ.get(env_var)
        if not api_key:
            raise SystemExit(f"{args.backend} API key is required via --api-key or {env_var}")

        records = filter_records(
            load_records(args.dataset),
            industries=args.industries,
            period_types=args.period_types,
            levels=args.levels,
            max_records=None if args.sample_strategy == "stratified" else args.max_records,
        )
        if args.sample_strategy == "stratified":
            records = stratified_sample_records(records, args.max_records)
        if args.aggregation_gap_from_results:
            record_ids = _aggregation_gap_record_ids(Path(args.aggregation_gap_from_results))
            records = [record for record in records if record.record_id in record_ids]
        if not records:
            raise SystemExit("No matching records found in dataset")

        specs = select_ablation_specs(matrix=args.matrix, names=args.ablations)
        client = OpenRouterClient(
            api_key=api_key,
            model=args.model,
            base_url=BACKEND_CHAT_COMPLETIONS_URLS[args.backend],
            app_name=f"finbalance-{args.backend}",
            max_retries=args.max_retries,
            reasoning_effort=args.reasoning_effort,
        )
        output_dirs = []
        for spec in specs:
            existing_results = (
                load_existing_ablation_results(
                    args.output_dir,
                    spec.name,
                    parse_success_only=args.resume_valid_only,
                )
                if args.resume
                else []
            )
            if args.resume:
                print(
                    json.dumps(
                        {
                            "ablation_name": spec.name,
                            "resuming_records": len(existing_results),
                            "resume_valid_only": bool(args.resume_valid_only),
                        },
                        indent=2,
                    )
                )
            evaluation = run_ablation_evaluation(
                records,
                client=client,
                dataset_path=args.dataset,
                spec=spec,
                backend_name=args.backend,
                temperature=args.temperature,
                max_tokens=args.max_output_tokens,
                timeout=args.timeout,
                agent_max_steps=args.agent_max_steps,
                existing_results=existing_results,
                checkpoint_output_root=args.output_dir if args.checkpoint_every else None,
                checkpoint_every=args.checkpoint_every,
                abort_on_max_token_parse_failure=args.abort_on_max_token_parse_failure,
            )
            output_dir = write_ablation_outputs(evaluation, args.output_dir)
            output_dirs.append(str(output_dir))
            print(
                json.dumps(
                    {
                        "ablation_name": spec.name,
                        "records_evaluated": evaluation["summary"]["records_evaluated"],
                        "parse_success_rate": evaluation["summary"]["parse_success_rate"],
                        "final_balance_sheet_and_journal_entries_match_rate": evaluation["summary"][
                            "final_balance_sheet_and_journal_entries_match_rate"
                        ],
                        "output_dir": str(output_dir),
                    },
                    indent=2,
                )
            )
        print(json.dumps({"ablations_completed": len(output_dirs), "output_dirs": output_dirs}, indent=2))
        return

    if args.command == "analyze-ablations":
        summary = analyze_ablation_bootstrap(
            args.results_dir,
            baseline_name=args.baseline,
            iterations=args.iterations,
            confidence=args.confidence,
            seed=args.seed,
            output_dir=args.output_dir,
        )
        output_root = args.output_dir or args.results_dir
        print(
            json.dumps(
                {
                    "comparisons": len(summary["comparisons"]),
                    "baseline_ablation": summary["baseline_ablation"],
                    "output_dir": output_root,
                },
                indent=2,
            )
        )
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


def regenerate_standard_datasets(
    *,
    base_dir: str | Path = "data",
    seed: int = 42,
    records_per_combo: int = 4,
    negative_controls_per_code: int = 10,
) -> dict[str, object]:
    base_path = Path(base_dir)
    coverage_dir = base_path / "coverage"
    main_dir = base_path / "main"
    for dataset_dir in (coverage_dir, main_dir):
        if dataset_dir.exists():
            shutil.rmtree(dataset_dir)

    coverage_records = _build_coverage_dataset(coverage_dir, seed)
    _write_dataset_bundle(
        coverage_dir,
        "coverage",
        coverage_records,
        config={
            "base_seed": seed,
            "selection_strategy": "all_combos_plus_forced_inconsistency_and_display_tax_coverage",
            "forced_inconsistency_codes": list(INCONSISTENCY_CODES),
        },
    )

    main_records = _build_main_extension_dataset(
        coverage_records=coverage_records,
        coverage_dir=coverage_dir,
        main_dir=main_dir,
        seed=seed,
        records_per_combo=records_per_combo,
        negative_controls_per_code=negative_controls_per_code,
    )
    return {
        "coverage_records": len(coverage_records),
        "main_records": len(main_records),
        "main_negative_target": len(INCONSISTENCY_CODES) * negative_controls_per_code,
    }


def regenerate_main_dataset_from_existing_coverage(
    *,
    base_dir: str | Path = "data",
    seed: int = 42,
    records_per_combo: int = 4,
    negative_controls_per_code: int = 10,
) -> dict[str, object]:
    """Regenerate ``data/main`` as a strict extension of existing ``data/coverage``."""

    base_path = Path(base_dir)
    coverage_dir = base_path / "coverage"
    main_dir = base_path / "main"
    coverage_path = coverage_dir / "records.jsonl"
    if not coverage_path.exists():
        raise SystemExit(f"Coverage split not found: {coverage_path}")
    if main_dir.exists():
        shutil.rmtree(main_dir)

    coverage_records = load_records(coverage_path)
    main_records = _build_main_extension_dataset(
        coverage_records=coverage_records,
        coverage_dir=coverage_dir,
        main_dir=main_dir,
        seed=seed,
        records_per_combo=records_per_combo,
        negative_controls_per_code=negative_controls_per_code,
    )
    return {
        "coverage_records": len(coverage_records),
        "main_records": len(main_records),
        "main_standard_records": sum(1 for record in main_records if not record.expected_inconsistency),
        "main_inconsistency_records": sum(1 for record in main_records if record.expected_inconsistency),
        "main_records_per_combo": records_per_combo,
        "main_negative_controls_per_code": negative_controls_per_code,
    }


def _build_coverage_dataset(dataset_dir: Path, seed: int) -> list:
    records = []
    assets_dir = dataset_dir / "assets"
    tax_cycle = ("none", "sales_tax", "vat", "gst", "us_sales_tax", "india_gst")
    combo_index = 0
    for industry in INDUSTRIES:
        for period_type in PERIOD_TYPES:
            for level in range(1, 6):
                display_profile = dict(DISPLAY_PROFILES[combo_index % len(DISPLAY_PROFILES)])
                tax_override = "none" if level == 1 else tax_cycle[combo_index % len(tax_cycle)]
                builder = DocumentBenchmarkBuilder(seed=seed + combo_index)
                record_id = f"COV_{industry[:3].upper()}_{period_type[0].upper()}{level}_{combo_index:04d}"
                records.append(
                    builder.generate_record(
                        record_id,
                        industry,
                        level,
                        assets_dir,
                        period_type=period_type,
                        display_profile_override=display_profile,
                        tax_regime_override=tax_override,
                    )
                )
                combo_index += 1

    for code_index, code in enumerate(INCONSISTENCY_CODES):
        records.append(_forced_negative_record(code, code_index, 0, assets_dir, seed, prefix="COV_NEG"))
    return records


def _build_main_extension_dataset(
    *,
    coverage_records: list,
    coverage_dir: Path,
    main_dir: Path,
    seed: int,
    records_per_combo: int,
    negative_controls_per_code: int,
) -> list:
    """Build the main split as coverage plus additional generated records.

    The coverage split already contains one standard record per
    industry-period-difficulty cell and one forced-inconsistency record per
    code. The main split preserves those record IDs so previous coverage
    evaluations can be reused, then adds enough records to reach the requested
    per-cell and per-code totals.
    """

    if records_per_combo < 1:
        raise ValueError("records_per_combo must be at least 1")
    if negative_controls_per_code < 1:
        raise ValueError("negative_controls_per_code must be at least 1")

    assets_dir = main_dir / "assets"
    main_records = [_copy_record_into_dataset(record, coverage_dir, main_dir) for record in coverage_records]

    extra_per_combo = records_per_combo - 1
    if extra_per_combo:
        counts = {
            industry: {
                period_type: {level: extra_per_combo for level in range(1, 6)}
                for period_type in PERIOD_TYPES
            }
            for industry in INDUSTRIES
        }
        builder = DocumentBenchmarkBuilder(seed=seed + 10_000)
        extra_path = main_dir / "_extra_standard_records.jsonl"
        extra_standard = builder.generate_dataset(
            counts,
            extra_path,
            assets_dir,
            negative_control_rate=0.0,
        )
        if extra_path.exists():
            extra_path.unlink()
        for record in extra_standard:
            _rewrite_record_asset_paths(record, assets_dir)
        main_records.extend(extra_standard)

    extra_negatives_per_code = negative_controls_per_code - 1
    if extra_negatives_per_code:
        for code_index, code in enumerate(INCONSISTENCY_CODES):
            for ordinal in range(1, negative_controls_per_code):
                record = _forced_negative_record(
                    code,
                    code_index,
                    ordinal,
                    assets_dir,
                    seed,
                    prefix="MAIN_NEG",
                )
                _rewrite_record_asset_paths(record, assets_dir)
                main_records.append(record)

    _write_dataset_bundle(
        main_dir,
        "main",
        main_records,
        config={
            "base_seed": seed,
            "selection_strategy": "strict_extension_of_coverage",
            "coverage_records_reused": len(coverage_records),
            "records_per_industry_period_difficulty_cell": records_per_combo,
            "extra_records_per_industry_period_difficulty_cell": extra_per_combo,
            "negative_controls_per_code": negative_controls_per_code,
            "extra_negative_controls_per_code": extra_negatives_per_code,
            "base_combo_records": len(INDUSTRIES) * len(PERIOD_TYPES) * 5 * records_per_combo,
            "forced_inconsistency_codes": list(INCONSISTENCY_CODES),
            "nonstandard_display_target_rate": 0.05,
        },
    )
    return main_records


def _copy_record_into_dataset(record, source_dataset_dir: Path, target_dataset_dir: Path):
    copied = copy.deepcopy(record)
    source_assets_dir = source_dataset_dir / "assets" / copied.record_id
    target_assets_dir = target_dataset_dir / "assets" / copied.record_id
    if source_assets_dir.exists():
        if target_assets_dir.exists():
            shutil.rmtree(target_assets_dir)
        shutil.copytree(source_assets_dir, target_assets_dir)
    _rewrite_record_asset_paths(copied, target_dataset_dir / "assets")
    return copied


def _rewrite_record_asset_paths(record, assets_dir: Path) -> None:
    for document in record.documents:
        filename = Path(document.asset_path).name
        document.asset_path = str(assets_dir / record.record_id / filename)


def _forced_negative_record(code: str, code_index: int, ordinal: int, assets_dir: Path, seed: int, *, prefix: str):
    candidates = FORCED_INCONSISTENCY_CANDIDATES.get(code, ())
    for seed_offset in range(20):
        for industry, period_type, level, tax_override in candidates:
            record_seed = seed + 1000 + code_index * 97 + ordinal * 1009 + seed_offset
            probe_builder = DocumentBenchmarkBuilder(seed=record_seed)
            with tempfile.TemporaryDirectory() as tmp_dir:
                probe = probe_builder.generate_record(
                    f"PROBE_{code}",
                    industry,
                    level,
                    tmp_dir,
                    period_type=period_type,
                    tax_regime_override=tax_override,
                )
            if code not in probe.metadata.get("available_inconsistency_codes", []):
                continue
            builder = DocumentBenchmarkBuilder(seed=record_seed)
            return builder.generate_record(
                f"{prefix}_{ordinal:02d}_{code.upper()[:32]}",
                industry,
                level,
                assets_dir,
                period_type=period_type,
                negative_control=True,
                negative_control_code=code,
                tax_regime_override=tax_override,
            )
    raise RuntimeError(f"Could not generate forced negative-control record for {code}")


def _write_dataset_bundle(dataset_dir: Path, dataset_name: str, records: list, *, config: dict[str, object]) -> None:
    output_path = ensure_parent(dataset_dir / "records.jsonl")
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record.to_dict(), ensure_ascii=True) + "\n")
    _write_dataset_sidecars(dataset_dir, dataset_name, records, config=config)


def _write_dataset_sidecars(dataset_dir: Path, dataset_name: str, records: list, *, config: dict[str, object]) -> None:
    rows = [record_manifest_row(record) for record in records]
    write_jsonl(dataset_dir / "record_manifest.jsonl", rows)
    manifest = dataset_manifest(dataset_name, records, rows, config=config)
    ensure_parent(dataset_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
