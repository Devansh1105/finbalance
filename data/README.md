# FinBalance Dataset Splits

This directory contains generated FinBalance dataset bundles. A bundle contains:

- `records.jsonl`: full benchmark records with OCR text and deterministic labels
- `assets/`: rendered PDF-style source-document assets
- `record_manifest.jsonl`: compact per-record metadata
- `manifest.json`: dataset-level counts and generation config
- `README.md`: bundle-local summary for custom generated datasets

## Canonical Splits

The repository keeps the original folder names for backward compatibility with
existing scripts and result directories:

| Split | Records | Contents | Intended use |
|---|---:|---|---|
| `coverage/` | 143 | One record per industry x period x difficulty cell, plus one forced-inconsistency record per code | Core evaluation split for the paper |
| `main/` | 1,052 | Eight clean records per industry x period x difficulty cell, plus four forced-inconsistency records per code | Training, stress tests, and downstream studies |

Both splits are generated from human-authored business scenarios, document
schemas, accounting policies, tax/FX assumptions, distractor templates, and
inconsistency perturbations. Given those rules and a seed, expected entries and
balance sheets are computed by deterministic ledger replay.

## Generate More Data

FinBalance is designed to create new datasets on demand. Use the public
generation script when you want a custom split for a model run, training set,
concept probe, or held-out evaluation.

Commands below assume they are run from the repository root.

Exact number of records:

```bash
python scripts/generate_dataset.py \
  --output-dir data/custom_retail_saas \
  --dataset-name retail_saas_l2_l4 \
  --records 50 \
  --industries retail subscription_saas \
  --period-types month quarter \
  --levels 2 3 4 \
  --negative-control-rate 0.10 \
  --seed 42
```

Balanced records per selected cell:

```bash
python scripts/generate_dataset.py \
  --output-dir data/custom_balanced \
  --dataset-name balanced_small \
  --records-per-combo 2 \
  --industries professional_services manufacturing wholesale_distribution \
  --period-types month year \
  --levels 3 4 5 \
  --clean-only \
  --seed 7
```

Python API:

```python
from finbalance.generation.user_dataset import (
    UserDatasetConfig,
    generate_user_dataset,
)

summary = generate_user_dataset(
    UserDatasetConfig(
        output_dir="data/custom_api",
        dataset_name="custom_api",
        records=100,
        industries=("retail", "subscription_saas"),
        period_types=("month", "quarter"),
        levels=(2, 3, 4),
        negative_control_rate=0.10,
        seed=42,
        overwrite=True,
    )
)
```

Regenerate the canonical paper splits:

```bash
python scripts/generate_standard_datasets.py \
  --base-dir data \
  --seed 42 \
  --records-per-combo 8 \
  --negative-controls-per-code 4 \
  --overwrite
```

## License

Generated benchmark records, OCR text, generated document artifacts, labels, and
manifests are released under CC BY 4.0. See
[`../DATA_LICENSE.md`](../DATA_LICENSE.md) for scope and provider-artifact
exclusions.
