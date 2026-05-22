#!/usr/bin/env python3
"""Build the two benchmark-first docs_benchmark datasets."""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from docs_benchmark.benchmark.manifests import dataset_manifest, record_manifest_row, write_jsonl
from docs_benchmark.generation.builder import DocumentBenchmarkBuilder
from docs_benchmark.generation.helpers import DISPLAY_PROFILES, INDUSTRY_TAX_REGIMES, PERIOD_TYPES
from docs_benchmark.industry_schemas import INDUSTRIES
from docs_benchmark.inconsistencies import INCONSISTENCY_CODES
from docs_benchmark.schemas import DocumentRecord


DATA_ROOT = PROJECT_ROOT / "docs_benchmark" / "data"
COVERAGE_DIR = DATA_ROOT / "coverage"
MAIN_DIR = DATA_ROOT / "main"

FORCE_REBUILD = True
BASE_SEED = 42
COVERAGE_POOL_SEEDS = (42, 43, 44, 45, 55, 58)
EXPECTED_COVERAGE_RECORDS = 121
MAIN_RECORDS_PER_COMBO = 8
MAIN_NEGATIVE_CONTROLS_PER_CODE = 6
MAIN_NONSTANDARD_DISPLAY_COUNT = 48

OLD_GENERATED_ARTIFACTS = (
    DATA_ROOT / "initial_eval_slice.jsonl",
    DATA_ROOT / "initial_eval_assets",
    DATA_ROOT / "v3_preview.jsonl",
    DATA_ROOT / "v3_preview_assets",
    DATA_ROOT / "gpt51_eval6.jsonl",
    COVERAGE_DIR,
    MAIN_DIR,
)

INDUSTRY_CODES = {
    "professional_services": "PRO",
    "field_services": "FLD",
    "retail": "RET",
    "wholesale_distribution": "WHD",
    "healthcare_clinic": "HLC",
    "property_management": "PRP",
    "manufacturing": "MAN",
    "subscription_saas": "SUB",
}
DISPLAY_PROFILE_BY_CODE = {profile["currency_code"]: dict(profile) for profile in DISPLAY_PROFILES}


@dataclass(frozen=True)
class RecordSpec:
    record_id: str
    seed: int
    industry: str
    period_type: str
    difficulty_level: int
    negative_control: bool = False
    negative_control_code: str | None = None
    display_profile: dict[str, str] | None = None
    tax_regime: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "record_id": self.record_id,
            "seed": self.seed,
            "industry": self.industry,
            "period_type": self.period_type,
            "difficulty_level": self.difficulty_level,
            "negative_control": self.negative_control,
            "negative_control_code": self.negative_control_code,
            "display_profile": dict(self.display_profile) if self.display_profile else None,
            "tax_regime": self.tax_regime,
        }


def _spec_seed(*parts: object) -> int:
    digest = hashlib.sha256("|".join(str(part) for part in parts).encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % (2**31)


def _period_code(period_type: str) -> str:
    return period_type[0].upper()


def _record_builder(spec: RecordSpec) -> DocumentBenchmarkBuilder:
    return DocumentBenchmarkBuilder(seed=spec.seed)


def _generate_record(spec: RecordSpec, assets_root: Path) -> DocumentRecord:
    builder = _record_builder(spec)
    return builder.generate_record(
        record_id=spec.record_id,
        industry=spec.industry,
        difficulty_level=spec.difficulty_level,
        assets_root=assets_root,
        period_type=spec.period_type,
        negative_control=spec.negative_control,
        negative_control_code=spec.negative_control_code,
        display_profile_override=dict(spec.display_profile) if spec.display_profile else None,
        tax_regime_override=spec.tax_regime,
    )


def _delete_path(path: Path) -> None:
    if not path.exists():
        return
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


def _clear_old_generated_artifacts() -> None:
    for path in OLD_GENERATED_ARTIFACTS:
        _delete_path(path)


def _tax_regime_override(industry: str, difficulty_level: int, variant_index: int) -> str:
    if difficulty_level < 2:
        return "none"
    options = INDUSTRY_TAX_REGIMES.get(industry, ())
    if not options:
        return "none"
    return options[variant_index % len(options)]


def _coverage_display_profile(variant_index: int) -> dict[str, str]:
    cycle = ("USD", "EUR", "GBP", "USD")
    return dict(DISPLAY_PROFILE_BY_CODE[cycle[variant_index % len(cycle)]])


def _main_nonstandard_indices(total_specs: int, target_count: int) -> set[int]:
    if target_count <= 0:
        return set()
    if total_specs % target_count == 0:
        step = total_specs // target_count
        return {index * step for index in range(target_count)}

    indices: list[int] = []
    used: set[int] = set()
    step = total_specs / target_count
    cursor = 0.0
    for _ in range(target_count):
        candidate = min(total_specs - 1, int(cursor))
        while candidate in used and candidate < total_specs - 1:
            candidate += 1
        used.add(candidate)
        indices.append(candidate)
        cursor += step
    return set(indices)


def _main_display_profile(spec_index: int, nonstandard_indices: set[int]) -> dict[str, str]:
    if spec_index not in nonstandard_indices:
        return dict(DISPLAY_PROFILE_BY_CODE["USD"])
    return dict(DISPLAY_PROFILE_BY_CODE["EUR" if len([index for index in nonstandard_indices if index < spec_index]) % 2 == 0 else "GBP"])


def _coverage_feature_keys(record: DocumentRecord) -> set[tuple[Any, ...]]:
    row = record_manifest_row(record)
    features: set[tuple[Any, ...]] = {
        ("combo", row["industry"], row["period_type"], row["difficulty_level"]),
        ("tax_regime", row["tax_regime"]),
        ("currency_code", row["currency_code"]),
        ("date_format", row["date_format"]),
    }
    for scenario in row["scenario_sequence"]:
        features.add(("scenario", scenario))
    for doc_type in row["doc_types_present"]:
        features.add(("doc_type", doc_type))
    for doc_type in row["doc_types_present"]:
        if any(document.role == "distractor_doc" and document.doc_type == doc_type for document in record.documents):
            features.add(("distractor_doc_type", doc_type))
    for code in row["expected_inconsistency_codes"]:
        features.add(("inconsistency_code", code))
    return features


def _coverage_targets(candidate_records: list[DocumentRecord]) -> set[tuple[Any, ...]]:
    targets: set[tuple[Any, ...]] = {
        ("combo", industry, period_type, level)
        for industry in INDUSTRIES
        for period_type in PERIOD_TYPES
        for level in range(1, 6)
    }
    targets.update(("scenario", scenario) for record in candidate_records for scenario in record.metadata.get("scenario_sequence", []))
    targets.update(("doc_type", document.doc_type) for record in candidate_records for document in record.documents)
    targets.update(("distractor_doc_type", document.doc_type) for record in candidate_records for document in record.documents if document.role == "distractor_doc")
    targets.update(("inconsistency_code", code) for code in INCONSISTENCY_CODES)
    targets.update(("tax_regime", regime) for regime in {"none", "sales_tax", "vat", "gst"})
    targets.update(("currency_code", code) for code in {"USD", "EUR", "GBP"})
    targets.update(("date_format", fmt) for fmt in {"YYYY-MM-DD", "DD/MM/YYYY"})
    return targets


def _select_coverage_specs(candidate_records: list[tuple[RecordSpec, DocumentRecord]]) -> list[RecordSpec]:
    targets = _coverage_targets([record for _, record in candidate_records])
    uncovered = set(targets)
    selected: list[RecordSpec] = []
    remaining = list(candidate_records)

    while uncovered:
        best_spec: RecordSpec | None = None
        best_coverage: set[tuple[Any, ...]] = set()
        best_index = -1
        for index, (spec, record) in enumerate(remaining):
            coverage = _coverage_feature_keys(record) & uncovered
            if len(coverage) > len(best_coverage):
                best_spec = spec
                best_coverage = coverage
                best_index = index
        if not best_coverage or best_spec is None:
            missing = sorted(uncovered)
            raise RuntimeError(f"Coverage candidate pool could not satisfy all targets. Missing: {missing[:20]}")
        selected.append(best_spec)
        uncovered -= best_coverage
        remaining.pop(best_index)

    return sorted(
        selected,
        key=lambda spec: (
            spec.industry,
            spec.period_type,
            spec.difficulty_level,
            spec.negative_control,
            spec.record_id,
        ),
    )


def _build_coverage_candidate_specs() -> list[RecordSpec]:
    specs: list[RecordSpec] = []
    for pool_index, pool_seed in enumerate(COVERAGE_POOL_SEEDS):
        for industry in INDUSTRIES:
            for period_type in PERIOD_TYPES:
                for difficulty_level in range(1, 6):
                    common = {
                        "seed": _spec_seed("coverage", BASE_SEED, pool_seed, industry, period_type, difficulty_level),
                        "industry": industry,
                        "period_type": period_type,
                        "difficulty_level": difficulty_level,
                        "display_profile": _coverage_display_profile(pool_index),
                        "tax_regime": _tax_regime_override(industry, difficulty_level, pool_index),
                    }
                    base_id = f"COV_{INDUSTRY_CODES[industry]}_{_period_code(period_type)}{difficulty_level}_S{pool_seed}"
                    specs.append(
                        RecordSpec(
                            record_id=f"{base_id}_CLN",
                            negative_control=False,
                            **common,
                        )
                    )
                    specs.append(
                        RecordSpec(
                            record_id=f"{base_id}_NEG",
                            negative_control=True,
                            **common,
                        )
                    )
    return specs


def _build_main_specs() -> list[RecordSpec]:
    specs: list[RecordSpec] = []
    total_specs = len(INDUSTRIES) * len(PERIOD_TYPES) * 5 * MAIN_RECORDS_PER_COMBO
    nonstandard_indices = _main_nonstandard_indices(total_specs, MAIN_NONSTANDARD_DISPLAY_COUNT)
    spec_index = 0
    for industry in INDUSTRIES:
        for period_type in PERIOD_TYPES:
            for difficulty_level in range(1, 6):
                for replica in range(1, MAIN_RECORDS_PER_COMBO + 1):
                    specs.append(
                        RecordSpec(
                            record_id=f"MAIN_{INDUSTRY_CODES[industry]}_{_period_code(period_type)}{difficulty_level}_R{replica:02d}",
                            seed=_spec_seed("main", BASE_SEED, industry, period_type, difficulty_level, replica),
                            industry=industry,
                            period_type=period_type,
                            difficulty_level=difficulty_level,
                            negative_control=False,
                            display_profile=_main_display_profile(spec_index, nonstandard_indices),
                            tax_regime=_tax_regime_override(industry, difficulty_level, replica - 1),
                        )
                    )
                    spec_index += 1
    return specs


def _assign_negative_control_codes(clean_records: dict[str, DocumentRecord], specs: list[RecordSpec]) -> dict[str, str]:
    available_by_spec = {
        spec.record_id: set(clean_records[spec.record_id].metadata.get("available_inconsistency_codes", []))
        for spec in specs
    }
    selected_by_code: dict[str, list[str]] = {code: [] for code in INCONSISTENCY_CODES}
    selected_specs: set[str] = set()
    combo_usage: dict[tuple[str, str, int], int] = {}

    for code in INCONSISTENCY_CODES:
        eligible = [
            spec
            for spec in specs
            if code in available_by_spec[spec.record_id]
        ]
        while len(selected_by_code[code]) < MAIN_NEGATIVE_CONTROLS_PER_CODE:
            eligible_unselected = [spec for spec in eligible if spec.record_id not in selected_specs]
            if len(eligible_unselected) < (MAIN_NEGATIVE_CONTROLS_PER_CODE - len(selected_by_code[code])):
                raise RuntimeError(f"Not enough distinct eligible specs to assign inconsistency code '{code}'")
            ranked = sorted(
                eligible_unselected,
                key=lambda spec: (
                    combo_usage.get((spec.industry, spec.period_type, spec.difficulty_level), 0),
                    spec.difficulty_level,
                    spec.record_id,
                ),
            )
            chosen = ranked[0]
            selected_by_code[code].append(chosen.record_id)
            selected_specs.add(chosen.record_id)
            combo_key = (chosen.industry, chosen.period_type, chosen.difficulty_level)
            combo_usage[combo_key] = combo_usage.get(combo_key, 0) + 1
            eligible.remove(chosen)

    return {
        record_id: code
        for code, record_ids in selected_by_code.items()
        for record_id in record_ids
    }


def _write_dataset(dataset_dir: Path, dataset_name: str, records: list[DocumentRecord], specs: list[RecordSpec], *, config: dict[str, Any]) -> None:
    dataset_dir.mkdir(parents=True, exist_ok=True)
    record_rows = [record_manifest_row(record) for record in records]
    records_path = dataset_dir / "records.jsonl"
    with records_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record.to_dict(), ensure_ascii=True) + "\n")
    write_jsonl(dataset_dir / "record_manifest.jsonl", record_rows)

    manifest = dataset_manifest(dataset_name, records, record_rows, config=config)
    manifest["record_specs"] = [spec.to_dict() for spec in specs]
    (dataset_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def _print_dataset_summary(name: str, records: list[DocumentRecord], manifest: dict[str, Any]) -> None:
    summary = manifest["summary"]
    print(f"\n{name}")
    print(f"  records: {summary['records']}")
    print(f"  inconsistency records: {summary['inconsistency_records']}")
    print(f"  total documents: {summary['total_documents']}")
    print(f"  total expected entries: {summary['total_expected_entries']}")
    print(f"  avg docs/record: {summary['average_documents_per_record']}")
    print(f"  avg entries/record: {summary['average_expected_entries_per_record']}")


def build_coverage_dataset() -> tuple[list[DocumentRecord], dict[str, Any]]:
    candidate_specs = _build_coverage_candidate_specs()
    candidate_records: list[tuple[RecordSpec, DocumentRecord]] = []
    with tempfile.TemporaryDirectory(prefix="docs_benchmark_coverage_pool_") as tmp_dir:
        pool_root = Path(tmp_dir)
        for spec in candidate_specs:
            candidate_records.append((spec, _generate_record(spec, pool_root)))

    selected_specs = _select_coverage_specs(candidate_records)
    if len(selected_specs) != EXPECTED_COVERAGE_RECORDS:
        raise RuntimeError(
            f"Coverage selection produced {len(selected_specs)} records; expected {EXPECTED_COVERAGE_RECORDS}. "
            "Update the plan or adjust the generator targets."
        )

    assets_root = COVERAGE_DIR / "assets"
    records = [_generate_record(spec, assets_root) for spec in selected_specs]
    config = {
        "base_seed": BASE_SEED,
        "coverage_pool_seeds": list(COVERAGE_POOL_SEEDS),
        "expected_record_count": EXPECTED_COVERAGE_RECORDS,
        "selection_strategy": "greedy_feature_cover",
    }
    _write_dataset(COVERAGE_DIR, "coverage", records, selected_specs, config=config)
    manifest = json.loads((COVERAGE_DIR / "manifest.json").read_text(encoding="utf-8"))
    return records, manifest


def build_main_dataset() -> tuple[list[DocumentRecord], dict[str, Any]]:
    specs = _build_main_specs()
    assets_root = MAIN_DIR / "assets"
    clean_records = {spec.record_id: _generate_record(spec, assets_root) for spec in specs}
    negative_assignments = _assign_negative_control_codes(clean_records, specs)

    final_records: list[DocumentRecord] = []
    final_specs: list[RecordSpec] = []
    for spec in specs:
        forced_code = negative_assignments.get(spec.record_id)
        final_spec = RecordSpec(
            record_id=spec.record_id,
            seed=spec.seed,
            industry=spec.industry,
            period_type=spec.period_type,
            difficulty_level=spec.difficulty_level,
            negative_control=forced_code is not None,
            negative_control_code=forced_code,
            display_profile=spec.display_profile,
            tax_regime=spec.tax_regime,
        )
        if forced_code is None:
            final_record = clean_records[spec.record_id]
        else:
            final_record = _generate_record(final_spec, assets_root)
        final_records.append(final_record)
        final_specs.append(final_spec)

    config = {
        "base_seed": BASE_SEED,
        "records_per_combo": MAIN_RECORDS_PER_COMBO,
        "negative_controls_per_code": MAIN_NEGATIVE_CONTROLS_PER_CODE,
        "nonstandard_display_count": MAIN_NONSTANDARD_DISPLAY_COUNT,
    }
    _write_dataset(MAIN_DIR, "main", final_records, final_specs, config=config)
    manifest = json.loads((MAIN_DIR / "manifest.json").read_text(encoding="utf-8"))
    return final_records, manifest


def main() -> None:
    if FORCE_REBUILD:
        _clear_old_generated_artifacts()

    print("Building coverage dataset...")
    coverage_records, coverage_manifest = build_coverage_dataset()
    _print_dataset_summary("coverage", coverage_records, coverage_manifest)

    print("\nBuilding main dataset...")
    main_records, main_manifest = build_main_dataset()
    _print_dataset_summary("main", main_records, main_manifest)

    print(f"\nSaved datasets under {DATA_ROOT}")
    print(f"  coverage: {COVERAGE_DIR}")
    print(f"  main:     {MAIN_DIR}")


if __name__ == "__main__":
    main()
