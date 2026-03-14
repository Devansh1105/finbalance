# FinBalance — LLM Benchmark for Balance Sheet Generation

> A structured financial reasoning benchmark that tests language models on their ability to construct GAAP-compliant balance sheets from transaction sequences of increasing complexity.

---

## Abstract

> *Prepared for submission to ACL 2025.*

We introduce **FinBalance**, a benchmark for evaluating large language models on the task of constructing GAAP-compliant balance sheets from sequences of double-entry journal transactions. Existing financial NLP benchmarks predominantly target question answering over pre-formed documents; FinBalance instead requires models to *generate* a structured financial statement by correctly accumulating, closing, and classifying every account across a full transaction sequence. The benchmark comprises 2,500 synthetically generated problems across five difficulty levels (L1–L5), with complexity scaled by transaction type, adjusting-entry depth, and inter-entry dependency. We evaluate on a stratified 100-problem held-out test set and report Balance Accuracy (BA), Account-Level Accuracy (ALA), and a composite FinBalance Score (FBS) with bootstrap confidence intervals.

Our experiments reveal a sharp generational divide: frontier models such as GPT-5.2 achieve near-perfect balance equation satisfaction (BA = 98–100%, FBS = 90.2–90.9), while earlier models fail catastrophically (GPT-5.1 BA = 16%, Claude Haiku 3 BA = 20%). Despite this headline improvement, a systematic conceptual gap persists across all models: **Retained Earnings is omitted in 92.8% of zero-shot and 100% of chain-of-thought responses**, with Net Income hallucinated onto the balance sheet in its place — revealing that models conflate balance sheet preparation with income statement reporting. Chain-of-thought prompting achieves perfect BA (100%) and eliminates parse failures, but degrades account-level accuracy on simple problems (L1 ALA: 79.0% → 71.8%) and worsens equity arithmetic error rates (38% → 57%), suggesting that extended reasoning traces disrupt rather than support structured financial generation. Error propagation analysis on earlier models shows gradual error onset at approximately 30% through each problem, consistently triggered by COGS and depreciation transactions. FinBalance, its dataset, evaluation harness, and all model results are released publicly.

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
5. Does chain-of-thought prompting help or hurt on structured financial generation tasks?

### Core Findings

**Generational leap in GAAP comprehension.** GPT-5.2 achieves 98–100% Balance Accuracy on the 100-problem test set — a result unmatched by any prior model evaluated (GPT-5.1: 16%, Claude Haiku 4.5: 0%, Claude Haiku 3: 20%). This confirms that balance sheet generation is now a solved task for frontier models at the equation-level, while account-level precision (ALA ≈ 81–83%) remains an open challenge.

**Systematic closing-entry blindness persists even in top models.** GPT-5.2 omits `Retained Earnings` in 92.8% of zero_shot responses and 100% of CoT responses. This is not an arithmetic failure — the balance equation is satisfied by inflating `Owner's Equity` instead. The model conflates the equity section of a balance sheet with the closing-entry step that produces it.

**CoT is a double-edged sword.** Chain-of-thought prompting eliminates parse failures (0 vs 2) and raises BA to a perfect 100%, but degrades L1 account-level accuracy (71.8% vs 79.0%) and worsens `Owner's Equity` arithmetic error rates (57% vs 38%). The extended reasoning trace introduces more equity calculation mistakes on simple problems than it solves.

---

## 2. Repository Structure

```
finbalance/
├── data/
│   ├── full.jsonl                        # 2,500-problem benchmark dataset
│   ├── dev.jsonl                         # 50-problem dev split (10/level, seed 42)
│   ├── test.jsonl                        # 100-problem test split (20/level, seed 42)
│   └── sample.jsonl                      # Legacy 100-problem stratified sample
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
│   │   │   ├── base.py                  # BaseModel + ModelConfig (max_tokens=8192, timeout=120)
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
│   ├── create_splits.py                 # CLI: create stratified dev/test splits from full.jsonl
│   ├── run_evaluation.py                # CLI: run model evaluation
│   ├── analyze_failures.py             # CLI: run failure analysis on results
│   ├── simulate_propagation.py         # CLI: run error propagation simulation
│   ├── run_baseline.py                  # CLI: rule-based baseline + bootstrap CIs
│   ├── _test_parser.py                  # Parser regression tests (8 cases)
│   └── _test_saved_responses.py         # Validates saved model responses parse correctly
│
├── results/
│   ├── openai_gpt-5.2_zero_shot.json             # GPT-5.2 zero_shot (100 problems, test set)
│   ├── openai_gpt-5.2_cot.json                   # GPT-5.2 CoT (100 problems, test set)
│   ├── openai_gpt-5.1_zero_shot.json             # GPT-5.1 zero_shot (25 problems, preliminary)
│   ├── anthropic_claude-haiku-4-5_zero_shot.json # Claude Haiku 4.5 zero_shot (25 problems)
│   ├── claude-sonnet-4-6_zero_shot.json          # Claude Sonnet 4.6 zero_shot (10 problems)
│   ├── claude-3-haiku-20240307_zero_shot.json    # Claude Haiku 3 zero_shot (25 problems)
│   ├── failure_analysis_haiku_zero_shot.json      # Failure analysis for Haiku 3
│   ├── propagation_haiku.json                     # Error propagation traces (5 problems)
│   ├── propagation_haiku_summary.json             # Aggregated propagation statistics
│   └── leaderboard.json                           # FBS-ranked leaderboard across all runs
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
| **BA** (Balance Accuracy) | 1 if `\|assets − (liab + equity)\| < $1`, else 0 | Binary balance equation satisfaction |
| **ALA** (Account-Level Accuracy) | `correct_accounts / total_expected_accounts` | Correct = within max($10, 1% of expected value) — scale-invariant across difficulty levels |
| **TPA** (Transaction Path Accuracy) | Fraction of intermediate states correctly predicted | Requires model to output per-step ledger state (CoT / self_refine only) |
| **CSR** (Constraint Satisfaction Rate) | Fraction of accounting constraints satisfied | Non-negativity, contra-asset rule, completeness, balance equation |
| **FBS** (FinBalance Score) | Weighted aggregate on 0–100 scale | See below |

**FBS formula** differs by strategy because TPA requires intermediate state output:

- **With TPA** (CoT, self_refine): `FBS = 0.30×BA + 0.25×ALA + 0.20×TPA + 0.15×CSR + 0.10×NE`
- **Without TPA** (zero_shot, few_shot): TPA weight redistributed proportionally → `FBS = 0.375×BA + 0.3125×ALA + 0.1875×CSR + 0.125×NE`

where NE = `1 − min(MAE / $50,000, 1)` (normalised mean absolute error, inverted so higher = better).

### 3.4 Error Categories

| Code | Name | Description |
|------|------|-------------|
| AE | Arithmetic Error | Account present but value is wrong |
| OE | Omission Error | Expected account entirely absent |
| CV | Classification Violation | Account placed in wrong section |
| CO | Commission Error | Duplicate or hallucinated account |
| FE | Format Error | Structural issues in the response |

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

| Split | Problems | L1 | L2 | L3 | L4 | L5 | Seed | Purpose |
|-------|----------|----|----|----|----|-----|------|---------|
| `full.jsonl` | 2,500 | 500 | 750 | 750 | 400 | 100 | 42 | Full benchmark release |
| `dev.jsonl` | 50 | 10 | 10 | 10 | 10 | 10 | 42 | Prompt tuning (public) |
| `test.jsonl` | 100 | 20 | 20 | 20 | 20 | 20 | 42 | Paper results (held-out) |
| `sample.jsonl` | 100 | 15 | 15 | 15 | 25 | 30 | 123 | Legacy exploratory sample |

The `dev` and `test` splits are stratified random samples drawn from `full.jsonl` using `scripts/create_splits.py`. They are non-overlapping by construction.

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

### 5.3 Model Backends

| Backend | Class | API Key Env Var | Notes |
|---------|-------|----------------|-------|
| Anthropic | `AnthropicModel` | `ANTHROPIC_API_KEY` | Direct Messages API |
| OpenRouter | `OpenRouterModel` | `OPENROUTER_API_KEY` | Multi-model gateway; auto-selected for non-`claude-*` model IDs |

The runner auto-detects backend: model IDs starting with `claude-` route to `AnthropicModel`; all others route to `OpenRouterModel`.

**Important:** Reasoning-heavy frontier models (e.g. GPT-5.2) generate extensive chain-of-thought before emitting the final JSON even in zero_shot mode. `ModelConfig` defaults have been updated to `max_tokens=8192` and `timeout=120s` to accommodate this.

### 5.4 Running an Evaluation

```bash
# Create stratified dev/test splits from full.jsonl
python scripts/create_splits.py --input data/full.jsonl --seed 42

# Run evaluation on the held-out test set (OpenRouter)
export OPENROUTER_API_KEY="your-key"
python scripts/run_evaluation.py \
    --dataset data/test.jsonl \
    --models openai/gpt-5.2 \
    --strategies zero_shot,cot

# Run with Anthropic key
export ANTHROPIC_API_KEY="your-key"
python scripts/run_evaluation.py \
    --dataset data/test.jsonl \
    --models claude-3-5-sonnet-20241022 \
    --strategies zero_shot
```

Results are saved to `results/<model>_<strategy>.json`.

### 5.5 Bootstrap Statistical Analysis

```bash
python scripts/run_baseline.py \
    --dataset data/test.jsonl \
    --model-results results/openai_gpt-5.2_zero_shot.json \
    --stats-only \
    --n-boot 2000
```

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

```bash
python scripts/analyze_failures.py \
    --results results/openai_gpt-5.2_zero_shot.json \
    --dataset data/test.jsonl \
    --output results/failure_analysis_gpt52_zero_shot.json
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

```bash
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

# Every 2nd transaction checkpoint (halves API cost)
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --n-per-level 3 \
    --checkpoint-every 2 \
    --max-checkpoints 15 \
    --output results/propagation_haiku_2step.json
```

---

## 8. Results Summary

All results in this section are on the **100-problem held-out test set** (`data/test.jsonl`, 20 problems per difficulty level, seed 42), except where noted as preliminary.

### 8.1 Leaderboard

| Model | Strategy | n | BA | ALA | FBS | FBS_w | 95% CI (FBS) |
|-------|----------|---|-----|-----|-----|-------|--------------|
| GPT-5.2 | `cot` | 100 | **100.0%** | 0.813 | **90.9** | **91.2** | [90.2, 91.5] |
| GPT-5.2 | `zero_shot` | 100 | 98.0% | **0.827** | 90.2 | 90.9 | [87.4, 92.4] |
| GPT-5.1 | `zero_shot` | 25* | 16.0% | 0.569 | 47.9 | — | — |
| Claude Haiku 4.5 | `zero_shot` | 25* | 0.0% | 0.592 | 43.4 | — | — |
| Claude Haiku 3 | `zero_shot` | 25* | 20.0% | 0.423 | 36.3 | — | — |

\* Preliminary results on the legacy `sample.jsonl`. Not directly comparable to the 100-problem test set.

### 8.2 GPT-5.2 — By Difficulty Level

#### Zero-shot

| Level | N | BA | ALA | FBS | Parse Fails |
|-------|---|----|-----|-----|-------------|
| L1 | 20 | 100.0% | 0.790 | 90.7 | 0 |
| L2 | 20 | 95.0% | 0.827 | 88.8 | 1 (timeout) |
| L3 | 20 | 100.0% | 0.848 | 92.2 | 0 |
| L4 | 20 | 100.0% | 0.858 | 92.3 | 0 |
| L5 | 20 | 95.0% | 0.811 | 87.0 | 1 (null content) |

#### Chain-of-Thought

| Level | N | BA | ALA | FBS | Parse Fails |
|-------|---|----|-----|-----|-------------|
| L1 | 20 | 100.0% | 0.718 | 88.2 | 0 |
| L2 | 20 | 100.0% | 0.829 | 91.8 | 0 |
| L3 | 20 | 100.0% | 0.822 | 91.2 | 0 |
| L4 | 20 | 100.0% | 0.843 | 91.7 | 0 |
| L5 | 20 | 100.0% | 0.852 | 91.4 | 0 |

**Interpretation:** CoT achieves perfect BA across all levels and eliminates parse failures. However, L1 ALA drops sharply (79.0% → 71.8%) — the extended reasoning trace introduces spurious sub-account splits (e.g. `Accumulated Depreciation - Vehicles` instead of `Accumulated Depreciation`) that inflate error counts on structurally simple problems. For harder levels (L4, L5), CoT ALA is equal or better.

### 8.3 GPT-5.2 — Failure Analysis

#### Error Composition

| Error Type | Zero-shot | CoT |
|------------|-----------|-----|
| OE (Omission) | 44.5% | 45.6% |
| CO (Commission/Hallucination) | 34.5% | 28.7% |
| AE (Arithmetic) | 13.5% | 19.3% |
| CV (Constraint Violation) | 6.8% | 6.4% |
| FE (Format) | 0.7% | 0.0% |

CoT shifts the error distribution: fewer hallucinations but significantly more arithmetic errors. The reasoning trace appears to introduce intermediate rounding and equity-calculation mistakes that zero_shot avoids by directly outputting the final number.

#### Critical Account Failures (GPT-5.2 zero_shot)

| Account | Omission Rate | Arithmetic Rate | Avg $ Error |
|---------|--------------|----------------|-------------|
| Retained Earnings | **92.8%** | 0% | — |
| Accumulated Depreciation | **75.6%** | 0% | — |
| Owner's Equity | 2.0% | **37.8%** | $23,995 |
| Cash | 0% | 1.0% | $4,100 |

**Retained Earnings omission is the dominant failure mode.** GPT-5.2 systematically excludes `Retained Earnings` from the equity section, instead rolling net income directly into `Owner's Equity`. This is structurally incorrect under GAAP (which requires a separate `Retained Earnings` line reflecting accumulated undistributed profit), but the balance equation remains satisfied because the model compensates by inflating `Owner's Equity`. This explains the apparent paradox of 98–100% BA alongside 81–83% ALA.

**CoT worsens this failure**: the omission rate for `Retained Earnings` rises to 100% under CoT, and `Owner's Equity` arithmetic errors jump from 37.8% to 57.0%. The reasoning trace leads the model to elaborate on equity components in ways that make the final number less accurate, not more.

#### Top Hallucinated Accounts (GPT-5.2 zero_shot)

| Account | Frequency | Note |
|---------|-----------|------|
| Net Income | 39 | Income statement item; does not belong on a balance sheet |
| Accumulated Depreciation - Vehicles | 14 | Sub-account split; schema expects unified `Accumulated Depreciation` |
| Accumulated Depreciation - Furniture | 10 | Same issue |
| Inventory | 5 | Present in schema but hallucinated when not expected |

`Net Income` is the most frequently hallucinated account. Models conflate the balance sheet with the income statement — `Net Income` is a temporary account that should be closed into `Retained Earnings` before the balance sheet is prepared.

#### Complexity Drivers (GPT-5.2 zero_shot, ΔFBS vs baseline without feature)

| Feature | ΔFBS | BA% | Notes |
|---------|------|-----|-------|
| `mixed_funding` | −0.9 | 97.5% | Marginal: only 40 problems, high variance |
| `credit_transaction` | −0.6 | 97.5% | Slight AR/AP tracking cost |
| `derived_interest` | −0.2 | 97.8% | Near-zero impact on GPT-5.2 |
| `depreciable_asset` | +6.7 | 98.9% | **GPT-5.2 is actually stronger on depreciation problems** |

Unlike older models where `depreciable_asset` was the largest negative driver (ΔFBS = −10.3 for Haiku 3), GPT-5.2 handles depreciation better than problems without it. This inversion suggests that GPT-5.2 has internalized the debit/credit mechanics of depreciation adjusting entries.

### 8.4 Historical Baseline — Claude Haiku 3 (25-problem sample, preliminary)

Included for qualitative contrast. See commit `fd55235` for full analysis.

| Metric | Value |
|--------|-------|
| Balance Accuracy (BA) | **20.0%** |
| Account-Level Accuracy (ALA) | **0.423** |
| FinBalance Score (FBS) | **36.3 / 100** |
| Retained Earnings omission | **100%** |
| `depreciable_asset` ΔFBS | **−10.3** |

### 8.5 Error Propagation (Claude Haiku 3, 5 problems)

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

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Generate dataset

```bash
# Full dataset (2,500 problems)
python scripts/generate_dataset.py --counts 1:500,2:750,3:750,4:400,5:100 --output data/full.jsonl --seed 42

# Create stratified dev/test splits
python scripts/create_splits.py --input data/full.jsonl --seed 42
# → data/dev.jsonl (50 problems, 10/level)
# → data/test.jsonl (100 problems, 20/level)
```

### Run evaluation

```bash
# Anthropic model
export ANTHROPIC_API_KEY="your-key"
python scripts/run_evaluation.py \
    --dataset data/test.jsonl \
    --models claude-3-5-sonnet-20241022 \
    --strategies zero_shot,cot

# OpenRouter model (GPT, Llama, Gemini, etc.)
export OPENROUTER_API_KEY="your-key"
python scripts/run_evaluation.py \
    --dataset data/test.jsonl \
    --models openai/gpt-5.2 \
    --strategies zero_shot,cot
```

### Analyse failures

```bash
python scripts/analyze_failures.py \
    --results results/openai_gpt-5.2_zero_shot.json \
    --dataset data/test.jsonl
```

### Bootstrap confidence intervals

```bash
python scripts/run_baseline.py \
    --dataset data/test.jsonl \
    --model-results results/openai_gpt-5.2_cot.json \
    --stats-only \
    --n-boot 2000
```

### Simulate error propagation

```bash
python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --model claude-3-haiku-20240307 \
    --n-per-level 1 \
    --checkpoint-every 1 \
    --output results/propagation.json
```

---

## 10. Configuration Reference

### ModelConfig

| Parameter | Default | Description |
|-----------|---------|-------------|
| `model_id` | — | Model identifier string (e.g. `openai/gpt-5.2`, `claude-3-5-sonnet-20241022`) |
| `temperature` | `0` | Sampling temperature (0 = near-deterministic) |
| `seed` | `42` | Random seed for reproducible sampling |
| `max_tokens` | `8192` | Maximum response tokens — increased from 2048 to accommodate extended reasoning in frontier models |
| `timeout` | `120` | API request timeout in seconds — increased from 60 for L4/L5 problems |

**Note on `max_tokens`:** Models such as GPT-5.2 generate extensive internal chain-of-thought reasoning before emitting the final JSON, even under zero_shot prompting. At `max_tokens=2048` or `max_tokens=4096`, these models hit the token cap and OpenRouter returns `null` content rather than truncated text. The default of `8192` is sufficient for all tested models across all difficulty levels.

### PropagationSimulator

| Parameter | Default | Description |
|-----------|---------|-------------|
| `checkpoint_every` | `1` | Transactions between API calls (1 = every single transaction) |
| `max_checkpoints` | `0` | Cap checkpoints per problem (0 = unlimited) |
| `sleep_between` | `0.5` | Seconds between API calls for rate-limit safety |
| `verbose` | `True` | Print progress to stdout |

---

## Roadmap

- [x] Generate full 2,500-problem benchmark dataset (`full.jsonl`)
- [x] Create standardised stratified dev/test splits (`dev.jsonl`, `test.jsonl`)
- [x] OpenRouter backend for multi-model evaluation
- [x] Run GPT-5.2 evaluation (zero_shot + CoT) on 100-problem test set
- [x] Bootstrap confidence intervals on all primary metrics
- [x] 5-dimension failure analysis module
- [x] Error propagation simulator
- [ ] Run GPT-5.1, Claude Sonnet, and Llama-3.3-70B on 100-problem test set
- [ ] Few-shot and self-refine strategies on top-performing models
- [ ] Rule-based and human baselines
- [ ] Error propagation run for GPT-5.2 (n=3/level, checkpoint-every=2)
- [ ] Investigate whether targeted prompting fixes Retained Earnings omission
