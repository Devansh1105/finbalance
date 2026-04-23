# Docs Benchmark

`docs_benchmark/` is the synthetic accounting-document dataset generator.

It creates packets of related PDF-style documents and the exact accounting truth behind them:

- the expected journal entries
- the final balance sheet

It also now includes a basic benchmark runner for OCR-text evaluation:

- prompt building from dataset records
- strict JSON parsing
- exact-match scoring
- OpenRouter model execution

## What Changed In V3

The current generator is the v3 version.

Main changes:

- 8 industries instead of 6
- month, quarter, and year records
- more document types
- more business situations
- richer opening balances
- more realistic document rendering
- neutralized distractor document families
- richer cross-document scenarios such as combined payments, reissued invoices, transfers, and reclassifications
- expanded negative-control inconsistency codes

The 8 industries are:

- `professional_services`
- `field_services`
- `retail`
- `wholesale_distribution`
- `healthcare_clinic`
- `property_management`
- `manufacturing`
- `subscription_saas`

## How It Works

For each record, the generator does this:

1. pick an industry, difficulty level, and period type
2. build a period range such as one month, one quarter, or one fiscal year
3. build internal master data like customers, vendors, products, tenants, patients, lenders, or subscription plans
4. create a richer opening balance
5. choose business scenarios from the industry schema
6. turn those scenarios into document seeds, journal entries, and bank-account cash rows
7. add realistic distractors and, when needed, negative-control inconsistencies
8. render the document seeds into PDF-style files and OCR text
9. validate the clean packet
10. run the ledger to build the final balance sheet

The visible documents are synthetic. The expected accounting answer is made only by code.

## Main Code Layout

- [types.py](/home/devanshagarwal/projects/finbalance/docs_benchmark/types.py)
  - shared types such as `DocSchema`, `IndustrySchema`, `BusinessScenario`, `BusinessState`, and `PeriodSpec`
- [doc_schemas/](/home/devanshagarwal/projects/finbalance/docs_benchmark/doc_schemas)
  - one file per document type
- [industry_schemas/](/home/devanshagarwal/projects/finbalance/docs_benchmark/industry_schemas)
  - one file per industry
- [generation/helpers.py](/home/devanshagarwal/projects/finbalance/docs_benchmark/generation/helpers.py)
  - period selection, dates, amount helpers, and common generation helpers
- [generation/scenario_factories.py](/home/devanshagarwal/projects/finbalance/docs_benchmark/generation/scenario_factories.py)
  - reusable business-scenario builders
- [generation/builder.py](/home/devanshagarwal/projects/finbalance/docs_benchmark/generation/builder.py)
  - top-level record generation
- [rendering/renderer.py](/home/devanshagarwal/projects/finbalance/docs_benchmark/rendering/renderer.py)
  - PDF-style rendering and OCR text
- [validation/](/home/devanshagarwal/projects/finbalance/docs_benchmark/validation)
  - document and record checks
- [ledger.py](/home/devanshagarwal/projects/finbalance/docs_benchmark/ledger.py)
  - deterministic ledger used to build the final balance sheet
- [FLOW.md](/home/devanshagarwal/projects/finbalance/docs_benchmark/FLOW.md)
  - step-by-step record walkthrough
- [benchmark/](/home/devanshagarwal/projects/finbalance/docs_benchmark/benchmark)
  - prompt builder, dataset loader, parser, scoring, and model runner

## Period Types

The generator supports:

- `month`
- `quarter`
- `year`

Year records are hybrid packets. They are not a raw dump of every document from 12 months.

Instead, a year packet includes:

- selected in-period operating documents
- year-end or long-period documents such as summaries, schedules, rollforwards, or closing documents

## Commands

Generate a mixed pilot dataset:

```bash
python -m docs_benchmark generate \
  --output /tmp/docs_benchmark_v3_pilot.jsonl \
  --assets-dir /tmp/docs_benchmark_v3_assets \
  --records-per-combo 1 \
  --period-types month quarter year \
  --seed 42
```

Inspect one sample record:

```bash
python -m docs_benchmark inspect \
  --industry manufacturing \
  --level 4 \
  --period-type year \
  --assets-dir /tmp/docs_benchmark_v3_inspect \
  --seed 42
```

Preview the exact OCR-text prompt that the benchmark will send to a model:

```bash
python -m docs_benchmark prompt-preview \
  --dataset docs_benchmark/data/v3_preview.jsonl \
  --record-id PREVIEW_PRO_M3
```

Run the basic benchmark against one OpenRouter model:

```bash
python -m docs_benchmark evaluate-openrouter \
  --dataset docs_benchmark/data/v3_preview.jsonl \
  --output docs_benchmark/results/openrouter_eval.json \
  --model openai/gpt-4.1-mini \
  --max-records 15
```

The benchmark currently uses:

- OCR text only, not direct PDF vision
- strict JSON output with `entries` and `balance_sheet`
- simple exact-match metrics with no combined score yet
- grouped summary reporting by difficulty, period type, and industry

Current standard-record metrics are:

- `Final balance sheet matches`
- `Final balance sheet and the journal entries match`
- `Final journal entries match`
- `Final journal entries match (not considering doc_refs, only account and amount)`

For negative-control records, the benchmark separately checks:

- inconsistency flag match
- inconsistency code match
- whether the model returned an empty accounting answer

## Tests

Run the dataset tests with:

```bash
python -m unittest discover -s docs_benchmark/tests -v
```
