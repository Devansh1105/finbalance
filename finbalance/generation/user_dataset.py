"""Public helpers for generating FinBalance dataset bundles.

These functions keep the user-facing scripts small while reusing the
same deterministic generator and manifest code as the benchmark CLI.
"""

from __future__ import annotations

import json
import random
import shutil
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Iterable

from finbalance.benchmark.manifests import dataset_manifest, record_manifest_row, write_jsonl
from finbalance.generation.builder import DocumentBenchmarkBuilder
from finbalance.generation.helpers import PERIOD_TYPES
from finbalance.industry_schemas import INDUSTRIES
from finbalance.schemas import DocumentRecord


DIFFICULTY_LEVELS = (1, 2, 3, 4, 5)


@dataclass(frozen=True)
class UserDatasetConfig:
    """Configuration for a public custom dataset bundle."""

    output_dir: str | Path
    dataset_name: str = "custom"
    records: int | None = None
    records_per_combo: int | None = None
    industries: tuple[str, ...] = tuple(INDUSTRIES)
    period_types: tuple[str, ...] = tuple(PERIOD_TYPES)
    levels: tuple[int, ...] = DIFFICULTY_LEVELS
    seed: int = 42
    negative_control_rate: float = 0.05
    overwrite: bool = False


def build_counts(
    *,
    industries: Iterable[str],
    period_types: Iterable[str],
    levels: Iterable[int],
    records: int | None,
    records_per_combo: int | None,
    seed: int,
) -> dict[str, dict[str, dict[int, int]]]:
    """Build generator counts for selected cells.

    If ``records_per_combo`` is set, every selected cell receives that many
    records. Otherwise, exactly ``records`` records are distributed as evenly
    as possible across selected cells using a deterministic seed.
    """

    industries = _validate_choices("industry", industries, INDUSTRIES)
    period_types = _validate_choices("period type", period_types, PERIOD_TYPES)
    levels = tuple(int(level) for level in levels)
    invalid_levels = [level for level in levels if level not in DIFFICULTY_LEVELS]
    if invalid_levels:
        raise ValueError(f"Unknown difficulty level(s): {invalid_levels}. Valid levels: {list(DIFFICULTY_LEVELS)}")

    if records is not None and records_per_combo is not None:
        raise ValueError("Use either records or records_per_combo, not both")
    if records is None and records_per_combo is None:
        records = 24
    if records is not None and records <= 0:
        raise ValueError("records must be positive")
    if records_per_combo is not None and records_per_combo <= 0:
        raise ValueError("records_per_combo must be positive")

    combos = list(product(industries, period_types, levels))
    if not combos:
        raise ValueError("At least one industry, period type, and difficulty level must be selected")

    allocation = {combo: 0 for combo in combos}
    if records_per_combo is not None:
        for combo in combos:
            allocation[combo] = records_per_combo
    else:
        assert records is not None
        base = records // len(combos)
        remainder = records % len(combos)
        for combo in combos:
            allocation[combo] = base
        shuffled = list(combos)
        random.Random(seed).shuffle(shuffled)
        for combo in shuffled[:remainder]:
            allocation[combo] += 1

    counts: dict[str, dict[str, dict[int, int]]] = {}
    for industry, period_type, level in combos:
        count = allocation[(industry, period_type, level)]
        if count <= 0:
            continue
        counts.setdefault(industry, {}).setdefault(period_type, {})[level] = count
    return counts


def generate_user_dataset(config: UserDatasetConfig) -> dict[str, object]:
    """Generate a dataset bundle and return a compact summary."""

    _validate_negative_control_rate(config.negative_control_rate)
    output_dir = Path(config.output_dir)
    if output_dir.exists() and any(output_dir.iterdir()):
        if not config.overwrite:
            raise FileExistsError(f"{output_dir} is not empty. Re-run with --overwrite or choose another output directory.")
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    counts = build_counts(
        industries=config.industries,
        period_types=config.period_types,
        levels=config.levels,
        records=config.records,
        records_per_combo=config.records_per_combo,
        seed=config.seed,
    )
    records_path = output_dir / "records.jsonl"
    assets_dir = output_dir / "assets"
    builder = DocumentBenchmarkBuilder(seed=config.seed)
    records = builder.generate_dataset(
        counts,
        records_path,
        assets_dir,
        negative_control_rate=config.negative_control_rate,
    )
    config_dict = {
        "dataset_name": config.dataset_name,
        "seed": config.seed,
        "requested_records": config.records,
        "records_per_combo": config.records_per_combo,
        "industries": list(config.industries),
        "period_types": list(config.period_types),
        "levels": list(config.levels),
        "negative_control_rate": config.negative_control_rate,
        "counts": counts,
    }
    _write_sidecars(output_dir, config.dataset_name, records, config=config_dict)
    _write_dataset_readme(output_dir, config.dataset_name, records, config=config_dict)
    return {
        "dataset_name": config.dataset_name,
        "records": len(records),
        "inconsistency_records": sum(1 for record in records if record.expected_inconsistency),
        "output_dir": str(output_dir),
        "records_jsonl": str(records_path),
        "assets_dir": str(assets_dir),
        "manifest": str(output_dir / "manifest.json"),
        "record_manifest": str(output_dir / "record_manifest.jsonl"),
    }


def _write_sidecars(dataset_dir: Path, dataset_name: str, records: list[DocumentRecord], *, config: dict[str, object]) -> None:
    rows = [record_manifest_row(record) for record in records]
    write_jsonl(dataset_dir / "record_manifest.jsonl", rows)
    manifest = dataset_manifest(dataset_name, records, rows, config=config)
    (dataset_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def _write_dataset_readme(dataset_dir: Path, dataset_name: str, records: list[DocumentRecord], *, config: dict[str, object]) -> None:
    manifest = dataset_manifest(dataset_name, records, [record_manifest_row(record) for record in records], config=config)
    summary = manifest["summary"]
    text = f"""# FinBalance Dataset: {dataset_name}

This dataset bundle was generated with the public FinBalance synthetic
accounting-document generator.

## Files

- `records.jsonl`: benchmark records with OCR text and deterministic ground truth
- `assets/`: rendered PDF-style document assets grouped by record ID
- `record_manifest.jsonl`: one compact metadata row per record
- `manifest.json`: dataset-level counts and generation configuration

## Summary

- Records: {summary["records"]}
- Inconsistency records: {summary["inconsistency_records"]}
- Documents: {summary["total_documents"]}
- Expected journal entries: {summary["total_expected_entries"]}
- Average documents per record: {summary["average_documents_per_record"]}
- Average expected entries per record: {summary["average_expected_entries_per_record"]}

The generated documents are synthetic. The expected entries and balance sheets
are computed by the deterministic FinBalance ledger.
"""
    (dataset_dir / "README.md").write_text(text, encoding="utf-8")


def _validate_choices(label: str, values: Iterable[str], valid_values: Iterable[str]) -> tuple[str, ...]:
    valid = tuple(valid_values)
    selected = tuple(values)
    missing = [value for value in selected if value not in valid]
    if missing:
        raise ValueError(f"Unknown {label}(s): {missing}. Valid values: {list(valid)}")
    if not selected:
        raise ValueError(f"At least one {label} must be selected")
    return selected


def _validate_negative_control_rate(rate: float) -> None:
    if rate < 0.0 or rate > 1.0:
        raise ValueError("negative_control_rate must be between 0.0 and 1.0")
