# FinBalance — LLM Benchmark for Balance Sheet Generation

> A structured financial reasoning benchmark that tests language models on their ability to construct GAAP-compliant balance sheets from transaction sequences of increasing complexity.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Repository Structure](#2-repository-structure)
3. [Benchmark Design](#3-benchmark-design)
4. [Dataset](#4-dataset)
5. [Evaluation Pipeline](#5-evaluation-pipeline)
6. [Failure Analysis Module](#6-failure-analysis-module)
7. [Error Propagation Simulator](#7-error-propagation-simulator)
8. [Results Summary](#8-results-summary)
9. [Quickstart](#9-quickstart)
10. [Configuration Reference](#10-configuration-reference)

---

## 1. Project Overview

FinBalance evaluates whether large language models understand double-entry bookkeeping and GAAP financial reporting well enough to convert a sequence of journal entries into a correct balance sheet. Unlike existing NLP financial benchmarks (FinQA, ConvFinQA, TAT-QA) which focus on question answering over existing documents, FinBalance requires the model to **construct** a structured financial statement from raw transactional data.

### Research Questions

1. How does performance degrade as transaction complexity increases (L1 → L5)?
2. Which transaction types are the primary error triggers?
3. Are errors due to arithmetic mistakes, conceptual gaps, or hallucination?
4. Does error accumulate gradually or emerge suddenly at specific transaction types?

### Core Finding

Claude Haiku 3 exhibits systematic **closing-entry blindness**: it omits `Retained Earnings` in 100% of evaluated problems, never folding Revenue/Expense accounts into Equity as GAAP requires. This is a conceptual deficit — the balance equation fails because the model is unaware that closing entries exist, not because of arithmetic.

---

## 2. Repository Structure

```
finbalance/
├── data/
│   ├── full.jsonl                        # 2,500-problem benchmark dataset
│   ├── sample.jsonl                      # 100-problem stratified sample
│   └── sample2.jsonl                     # Auxiliary sample
│
├── finbalance/                           # Core Python package
│   ├── data/
│   │   ├── schemas.py                    # Dataclasses + ACCOUNT_TYPE taxonomy
│   │   └── generation/
│   │       ├── generator.py             # Synthetic problem generator (Ledger engine)
│   │       └── templates.py             # TX / ADJ templates per difficulty level
│   │
│   ├── evaluation/
│   │   ├── runner.py                    # Orchestrator: prompt → model → parse → metrics
│   │   ├── metrics/
│   │   │   └── core.py                  # BA, ALA, TPA, FBS metric implementations
│   │   ├── models/
│   │   │   ├── base.py                  # BaseModel + ModelConfig
│   │   │   ├── anthropic_model.py       # Anthropic Messages API backend
│   │   │   └── openrouter.py            # OpenRouter multi-model backend
│   │   └── prompts/
│   │       └── strategies.py            # zero_shot / few_shot / cot / self_refine
│   │
│   └── analysis/
│       ├── error_detection.py            # Per-problem error classification
│       ├── failure_analysis.py           # 5-dimension paper-ready failure analysis
│       └── error_propagation.py          # Transaction-level error propagation simulator
│
├── scripts/
│   ├── generate_dataset.py              # CLI: generate full.jsonl / sample.jsonl
│   ├── run_evaluation.py                # CLI: run model evaluation
│   ├── analyze_failures.py             # CLI: run failure analysis on results
│   ├── simulate_propagation.py         # CLI: run error propagation simulation
│   ├── _test_parser.py                  # Parser regression tests (8 cases)
│   └── _test_saved_responses.py         # Validates saved model responses parse correctly
│
├── results/
│   ├── claude-3-haiku-20240307_zero_shot.json        # 25-problem evaluation results
│   ├── failure_analysis_haiku_zero_shot.json         # 5-dimension failure analysis
│   ├── propagation_haiku.json                        # Error propagation traces (5 problems)
│   └── propagation_haiku_summary.json               # Aggregated propagation statistics
│
└── requirements.txt
```

---

## 3. Benchmark Design

### 3.1 Difficulty Levels

| Level | Description | Typical Accounts | Key Features |
|-------|-------------|-----------------|--------------|
| L1 | Simple cash transactions, single equity source | 3–6 | owner investment, cash sales, expenses |
| L2 | Credit transactions, basic assets, simple debt | 7–10 | AR, AP, loans, prepaid items, depreciation |
| L3 | COGS tracking, multi-asset, adjusting entries | 10–14 | Inventory, COGS, accruals, bad debt provision |
| L4 | Mixed-funding purchases, derived interest, chained adjustments | 13–16 | Notes Payable, interest accrual, write-downs |
| L5 | Full complexity—all features combined | 14–17 | All of the above + bad debt write-off chains |

### 3.2 Transaction Templates

**Standard transactions (all levels):**
`cash_sale`, `credit_sale`, `cash_purchase`, `credit_purchase`, `cash_expense`, `loan_receipt`, `owner_investment`, `prepaid_rent`, `prepaid_insurance`, `buy_equipment`, `buy_furniture`, `buy_vehicles`

**Advanced transactions (L3+):**
- `cash_sale_with_cogs` / `credit_sale_with_cogs` — 4-entry transaction that simultaneously records revenue and cost (Dr Cash/AR + Cr Revenue + Dr COGS + Cr Inventory)
- `derived_interest_expense` — interest computed as `loan_balance × rate / 12` at runtime

**Advanced transactions (L4+):**
- `mixed_purchase_equipment` / `mixed_purchase_vehicles` — 3-entry split (Dr Asset, Cr Cash partial, Cr Notes Payable partial)

**Adjusting entries templates:**
`depreciation`, `prepaid_expense_used`, `accrual`, `bad_debt_provision`, `accrued_interest`, `inventory_write_down`, `bad_debt_write_off` (chained: requires `bad_debt_provision` as prerequisite)

### 3.3 Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **BA** (Balance Accuracy) | 1 if `|assets − (liab + equity)| < $1`, else 0 | Binary balance equation satisfaction |
| **ALA** (Account-Level Accuracy) | `correct_accounts / total_expected_accounts` | Fraction of expected accounts with correct values |
| **TPA** (Transaction Path Accuracy) | Fraction of intermediate states correctly predicted | Requires model to output per-step ledger state |
| **FBS** (FinBalance Score) | `0.4 × BA + 0.4 × ALA + 0.2 × TPA` | Composite score combining all dimensions |

### 3.4 Error Categories

| Code | Name | Description |
|------|------|-------------|
| AE | Arithmetic Error | Account present but value is wrong |
| OE | Omission Error | Expected account entirely absent |
| CV | Classification Violation | Account placed in wrong section |
| CO | Count/Order Error | Duplicate or reordered accounts |
| HE | Hallucination Error | Account present in response but not expected |

---

## 4. Dataset

### 4.1 Generation

The dataset is generated by a deterministic Ledger engine that:

1. Selects a difficulty level and assigns compatible transaction templates
2. Seeds a double-entry `Ledger` object with a randomised opening balance
3. Replays each transaction through `_apply_entry()`, maintaining running totals
4. Serialises the full journal, intermediate states, and the closing balance sheet
5. Validates the closing balance sheet (`|assets − (liab + equity)| < $1`)

The generator ensures 0 unbalanced problems across all 2,500 problems.

### 4.2 Dataset Statistics

| Split | Problems | L1 | L2 | L3 | L4 | L5 | Seed |
|-------|----------|----|----|----|----|-----|------|
| `full.jsonl` | 2,500 | 500 | 750 | 750 | 400 | 100 | 42 |
| `sample.jsonl` | 100 | 15 | 15 | 15 | 25 | 30 | 123 |

### 4.3 Account Taxonomy

27 accounts across 6 types:

- **Assets (normal debit):** Cash, Accounts Receivable, Inventory, Equipment, Furniture, Vehicles, Prepaid Rent, Prepaid Insurance
- **Contra-Assets (normal credit):** Accumulated Depreciation, Allowance for Doubtful Accounts
- **Liabilities (normal credit):** Accounts Payable, Loans Payable, Notes Payable, Accrued Expenses, Accrued Interest Payable, Unearned Revenue
- **Equity (normal credit):** Owner's Equity, Share Capital, Retained Earnings
- **Revenue (normal credit):** Revenue, Sales Revenue
- **Expenses (normal debit):** Cost of Goods Sold, Operating Expenses, Salaries Expense, Rent Expense, Insurance Expense, Depreciation Expense, Bad Debt Expense, Interest Expense, Utilities Expense

---

## 5. Evaluation Pipeline

### 5.1 Prompting Strategies

| Strategy | Description |
|----------|-------------|
| `zero_shot` | Bare instruction + transaction list, asks for JSON balance sheet |
| `few_shot` | Same as zero_shot + one complete worked example |
| `cot` | Chain-of-thought: model reasons step-by-step, then outputs `FINAL ANSWER: {...}` |
| `self_refine` | Two-pass: first generate, then model critiques and corrects its own output |

### 5.2 JSON Parser

The parser uses a multi-strategy cascade with robust cleaning to handle common model output quirks:

1. **Code-fence blocks** — ```` ```json ... ``` ```` — tried largest-first
2. **FINAL ANSWER marker** — used in CoT responses
3. **Balanced `{...}` blocks** — all extracted, sorted by length, tried largest-first
4. **Whole string** — last resort

The `_clean_json()` helper handles:
- **Thousands-separator commas** — `"Cash": 123,900` → `123900` (primary root cause of early 100% parse failure)
- Trailing commas — `{"key": val,}` → valid JSON
- Python literals — `None/True/False` → `null/true/false`

### 5.3 Running an Evaluation

```powershell
# Set API key
$env:ANTHROPIC_API_KEY = "your-key-here"

# Run evaluation
python scripts/run_evaluation.py \
    --dataset data/sample.jsonl \
    --model claude-3-haiku-20240307 \
    --strategies zero_shot

# Multiple strategies
python scripts/run_evaluation.py \
    --dataset data/sample.jsonl \
    --model claude-3-haiku-20240307 \
    --strategies zero_shot,few_shot,cot,self_refine
```

Results are saved to `results/<model>_<strategy>.json`.

---

## 6. Failure Analysis Module

`finbalance/analysis/failure_analysis.py` provides five analysis dimensions:

### Dimension 1 — Complexity Drivers
Correlates problem features with FBS/ALA degradation. Computes `ΔFBS` = difference between mean FBS of problems with vs without each feature.

### Dimension 2 — Account Miss Rates
Per-account breakdown of omission rate, arithmetic error rate, hallucination rate, and average absolute dollar error.

### Dimension 3 — Balance Failure Causes
Root cause taxonomy for problems where BA = 0:
- `missing_section` — entire assets/liabilities/equity section absent
- `omitted_key_account` — a structurally critical account is missing
- `arithmetic_error` — all accounts present but values don't balance
- `misclassified_account` — account in wrong section
- `hallucinated_account` — extra account breaks the equation

### Dimension 4 — Hallucination Catalog
Lists all accounts the model generated that were not expected, with `in_schema` (known account type) vs out-of-schema (fabricated account name) classification.

### Dimension 5 — Difficulty Gradient
Per-level error composition (`AE/OE/CV/CO` ratios), feature presence rates, and accuracy metrics.

### Running Failure Analysis

```powershell
python scripts/analyze_failures.py \
    --results results/claude-3-haiku-20240307_zero_shot.json \
    --dataset data/sample.jsonl \
    --output results/failure_analysis_haiku_zero_shot.json
```

---

## 7. Error Propagation Simulator

`finbalance/analysis/error_propagation.py` — identifies **exactly where in a problem the model first makes an error** by sending K-transaction prefixes (K = 1, 2, ..., N) as separate API calls.

### How It Works

For a problem with N transactions:
1. At checkpoint K, replay the opening balance + first K journal entries to compute the exact **ground-truth** ledger state
2. Send a prompt asking the model to produce the balance sheet "after these K transactions"
3. Diff predicted vs true per-account → MAE, per-account errors
4. Track the first checkpoint K where MAE > $1 — that is the **error onset transaction**

### Key Outputs

| Field | Description |
|-------|-------------|
| `first_error_k` | Index of the transaction that first triggers an error |
| `first_error_tx_type` | Template type of that transaction |
| `mae_trajectory` | List of MAE values at each checkpoint |
| `error_propagation_shape` | `immediate` / `gradual` / `late` |
| `first_balance_fail_k` | When balance equation first fails in prediction |

### Running the Simulator

```powershell
# 1 problem per difficulty level (5 total)
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --model claude-3-haiku-20240307 \
    --n-per-level 1 \
    --checkpoint-every 1 \
    --output results/propagation_haiku.json

# Print summary from saved traces (no new API calls)
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --output results/propagation_haiku.json \
    --summary-only

# Every 2nd transaction (halves cost)
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --n-per-level 3 \
    --checkpoint-every 2 \
    --output results/propagation_haiku_2step.json
```

---

## 8. Results Summary

> Model: `claude-3-haiku-20240307` | Strategy: `zero_shot` | N = 25 problems

### Overall

| Metric | Value |
|--------|-------|
| Balance Accuracy (BA) | **20.0%** |
| Account-Level Accuracy (ALA) | **0.4231** |
| FinBalance Score (FBS) | **36.3 / 100** |
| Parse Error Rate | **0%** |

### By Difficulty Level

| Level | N | BA | ALA | FBS | Avg Errors |
|-------|---|----|-----|-----|------------|
| L1 | 5 | 40.0% | 0.533 | 45.9 | 2.8 |
| L2 | 5 | 60.0% | 0.513 | 51.5 | 4.6 |
| L3 | 5 | 0.0% | 0.482 | 32.0 | 7.6 |
| L4 | 5 | 0.0% | 0.364 | 29.2 | 10.4 |
| L5 | 5 | 0.0% | 0.224 | 23.2 | 12.6 |

### Most Harmful Complexity Features (ΔFBS)

| Feature | ΔFBS | BA Rate | Notes |
|---------|------|---------|-------|
| `prepaid` | −23.7 | 16.7% | Prepaid adjustments confuse balance totals |
| `cogs` | −20.6 | 0.0% | COGS tracking never gets balanced |
| `derived_interest` | −17.0 | 0.0% | Computed interest not applied correctly |
| `mixed_funding` | −17.0 | 0.0% | Splits between cash and Notes Payable fail |
| `debt` | −12.9 | 11.1% | Loan balances arithmetically wrong |
| `credit_transaction` | −12.0 | 15.0% | AR/AP tracking causes runaway errors |
| `depreciable_asset` | −10.3 | 17.4% | Missing contra-account (Accumulated Depreciation) |

### Critical Account Failures

| Account | Type | Omission Rate | Arithmetic Rate | Avg $ Error |
|---------|------|--------------|----------------|-------------|
| Retained Earnings | equity | **100%** | 0% | — |
| Accumulated Depreciation | contra_asset | **56%** | 0% | — |
| Allowance for Doubtful Accounts | contra_asset | **50%** | 25% | $400 |
| Cash | asset | 0% | **96%** | $47,958 |
| Notes Payable | liability | 0% | **90%** | $25,289 |
| Accounts Receivable | asset | 0% | **82%** | $10,657 |
| Inventory | asset | 0% | **71%** | $12,907 |

### Balance Failure Causes (20/25 problems)

| Cause | Count | Pct |
|-------|-------|-----|
| `omitted_key_account` | 17 | 85% |
| `missing_section` | 3 | 15% |

Retained Earnings absent in all 17 `omitted_key_account` cases. Accumulated Depreciation co-absent in 7 of those.

### Error Propagation (5 problems, 1 per level)

| Metric | Value |
|--------|-------|
| Error propagation shape | **Gradual** |
| Mean onset fraction | **0.295** (errors appear ~30% into problem) |
| Mean final MAE | **$17,099** |
| Most common onset tx type | `cash_sale_with_cogs` (2/5) |

MAE by progress quartile: Q0=$0 → Q25=$2,243 → Q50=$4,333 → Q75=$8,990 → Q100=$17,099

---

## 9. Quickstart

### Prerequisites

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Generate dataset

```powershell
# Full dataset (2,500 problems)
python scripts/generate_dataset.py --counts 1:500,2:750,3:750,4:400,5:100 --output data/full.jsonl --seed 42

# Sample dataset (100 problems)
python scripts/generate_dataset.py --counts 1:15,2:15,3:15,4:25,5:30 --output data/sample.jsonl --seed 123
```

### Run evaluation

```powershell
$env:ANTHROPIC_API_KEY = "your-key"
python scripts/run_evaluation.py --dataset data/sample.jsonl --model claude-3-haiku-20240307 --strategies zero_shot
```

### Analyse failures

```powershell
python scripts/analyze_failures.py \
    --results results/claude-3-haiku-20240307_zero_shot.json \
    --dataset data/sample.jsonl \
    --output results/failure_analysis.json
```

### Simulate error propagation

```powershell
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --n-per-level 1 \
    --output results/propagation.json
```

---

## 10. Configuration Reference

### ModelConfig

| Parameter | Default | Description |
|-----------|---------|-------------|
| `model_id` | — | Model identifier string (e.g. `claude-3-haiku-20240307`) |
| `temperature` | `0` | Sampling temperature (0 = near-deterministic) |
| `max_tokens` | `2048` | Maximum response tokens |
| `timeout` | `60` | API request timeout in seconds |

### PropagationSimulator

| Parameter | Default | Description |
|-----------|---------|-------------|
| `checkpoint_every` | `1` | Transactions between API calls (1 = every single transaction) |
| `max_checkpoints` | `0` | Cap checkpoints per problem (0 = unlimited) |
| `sleep_between` | `0.5` | Seconds between API calls for rate-limit safety |
| `verbose` | `True` | Print progress to stdout |

---

## Roadmap

- [ ] Run all 4 strategies (`zero_shot`, `few_shot`, `cot`, `self_refine`) on 100-problem sample
- [ ] Add 3 additional models (GPT-4o-mini, Claude Sonnet 3.5, Gemini Flash)
- [ ] Statistical significance: bootstrap CIs + paired t-tests per feature
- [ ] Rule-based and human baselines
- [ ] OpenRouter backend integration for multi-model runs
- [ ] Investigate whether CoT/self-refine fixes closing-entry blindness
