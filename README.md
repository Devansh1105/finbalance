# FinBalance — LLM Benchmark for Balance Sheet Generation

> A structured financial reasoning benchmark that tests language models on their ability to construct GAAP-compliant balance sheets from transaction sequences of increasing complexity.

---

## Abstract

> *Prepared for submission to ACL 2025.*

We introduce **FinBalance**, a benchmark for evaluating large language models on the task of constructing GAAP-compliant balance sheets from sequences of double-entry journal transactions. Existing financial NLP benchmarks predominantly target question answering over pre-formed documents; FinBalance instead requires models to *generate* a structured financial statement by correctly accumulating, closing, and classifying every account across a full transaction sequence. The benchmark comprises 2,500 synthetically generated problems across five difficulty levels (L1–L5), with complexity scaled by transaction type, adjusting-entry depth, and inter-entry dependency. We evaluate three frontier models — GPT-5.2, Gemini 3 Flash, and Llama 3.3 70B — on a stratified 100-problem held-out test set under zero-shot and chain-of-thought prompting, reporting nine metrics including Balance Accuracy (BA), Account Coverage Rate (ACR), Balance Error Magnitude (BEM), Section Placement Accuracy (SPA), Closing Entry Compliance Rate (CECR), and a composite FinBalance Score (FBS) with bootstrap confidence intervals and pairwise permutation tests.

Our experiments reveal a three-tier capability hierarchy: GPT-5.2 achieves near-perfect balance equation satisfaction (BA = 98–100%, FBS = 90.2–90.9), Gemini 3 Flash reaches moderate accuracy (BA = 73–80%, FBS = 79.0–83.5), and Llama 3.3 70B fails catastrophically (BA = 2%, FBS = 33.4). All pairwise gaps are statistically significant (p < 0.001, paired permutation test), except GPT-5.2 CoT vs. zero-shot (p = 0.53). Despite GPT-5.2's headline accuracy, a systematic conceptual gap persists across *all* models: **Retained Earnings is correctly produced in fewer than 8% of responses** (CECR: GPT-5.2 zero-shot 8%, GPT-5.2 CoT 1%, Gemini 15–17%), with Net Income hallucinated onto the balance sheet in its place — revealing that models conflate balance sheet preparation with income statement reporting. Structural analysis using ACR and BEM distinguishes two failure modes: GPT-5.2 achieves structural coverage (ACR = 86–87%) but near-zero balance equation error (BEM ≈ $0) by compensating for omitted accounts; Gemini achieves higher account coverage (ACR = 92–98%) but large residual balance errors (BEM ≈ $4,400). Chain-of-thought prompting achieves perfect BA (100%) for GPT-5.2 and eliminates parse failures, but degrades L1 account-level accuracy (ALA: 79.0% → 71.8%), raises CECR failures to 99%, and worsens equity arithmetic errors (38% → 57%). Error propagation analysis shows gradual error onset at approximately 30% through each problem, consistently triggered by COGS and depreciation transactions. FinBalance, its dataset, evaluation harness, and all model results are released publicly.

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
│   ├── compute_extended_metrics.py      # Post-process results: add ACR, BEM, SPA, PSR, HR, CECR
│   ├── generate_figures.py              # Generate all 8 publication figures (F1–F8)
│   ├── permutation_tests.py             # Bootstrap CIs + pairwise permutation tests
│   ├── _test_parser.py                  # Parser regression tests (8 cases)
│   └── _test_saved_responses.py         # Validates saved model responses parse correctly
│
├── results/
│   ├── openai_gpt-5.2_zero_shot.json                      # GPT-5.2 zero_shot (100 problems, test set)
│   ├── openai_gpt-5.2_cot.json                            # GPT-5.2 CoT (100 problems, test set)
│   ├── google_gemini-3-flash-preview_zero_shot.json       # Gemini 3 Flash zero_shot (100 problems)
│   ├── google_gemini-3-flash-preview_cot.json             # Gemini 3 Flash CoT (100 problems)
│   ├── meta-llama_llama-3.3-70b-instruct_zero_shot.json  # Llama 3.3 70B zero_shot (100 problems)
│   ├── openai_gpt-5.1_zero_shot.json                      # GPT-5.1 zero_shot (25 problems, preliminary)
│   ├── anthropic_claude-haiku-4-5_zero_shot.json          # Claude Haiku 4.5 zero_shot (25 problems)
│   ├── claude-3-haiku-20240307_zero_shot.json             # Claude Haiku 3 zero_shot (25 problems)
│   ├── failure_analysis_gpt52_zero_shot.json              # Failure analysis for GPT-5.2
│   ├── propagation_haiku.json                              # Error propagation traces (5 problems)
│   ├── propagation_haiku_summary.json                      # Aggregated propagation statistics
│   ├── leaderboard.json                                    # Full leaderboard with extended metrics
│   └── significance_tests.json                            # Bootstrap CIs + permutation test p-values
│
├── figures/
│   ├── F1_capability_curve.png        # FBS and BA vs difficulty level (all models)
│   ├── F2_error_composition.png       # AE/OE/CV/CO stacked bar chart
│   ├── F3_cot_effect.png              # CoT effect: delta FBS/BA/ALA per model
│   ├── F4_account_heatmap.png         # Account omission and arithmetic error rates by model
│   ├── F5_bem_distribution.png        # Balance Error Magnitude box plots per model
│   ├── F6_cot_by_difficulty.png       # CoT delta FBS per difficulty level per model
│   ├── F7_propagation.png             # Error propagation MAE trajectory (Haiku 3, 5 problems)
│   └── F8_dataset_complexity.png      # Transaction/account counts and feature presence by level
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

#### Primary metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **BA** (Balance Accuracy) | 1 if `\|assets − (liab + equity)\| < $1`, else 0 | Binary balance equation satisfaction |
| **ALA** (Account-Level Accuracy) | `correct_accounts / total_expected_accounts` | Correct = within max($10, 1% of expected value) — scale-invariant across difficulty levels |
| **ACR** (Account Coverage Rate) | `\|predicted ∩ expected\| / \|expected\|` | Structural recall: presence-only, ignores values. Separates structural from numerical errors. |
| **BEM** (Balance Error Magnitude) | `\|assets − (liabilities + equity)\|` | Continuous version of BA. Shows how wrong the sheet is in dollar terms. |
| **SPA** (Section Placement Accuracy) | `correctly_placed / total_predicted` | Fraction of predicted accounts in the correct section (assets/liabilities/equity). Catches income-statement contamination. |
| **PSR** (Perfect Score Rate) | 1 if FBS = 100, else 0 | Fraction of problems where the model gets everything exactly right. |
| **CECR** (Closing Entry Compliance Rate) | 1 if Retained Earnings present and within tolerance | Formalises the closing-entry blindness finding. RE not required → trivially 1. |
| **HR** (Hallucination Rate) | `hallucinated_accounts / predicted_accounts` | Fraction of predicted accounts not in the expected set. |
| **CSR** (Constraint Satisfaction Rate) | Fraction of accounting constraints satisfied | Non-negativity, contra-asset rule, completeness, balance equation |
| **FBS** (FinBalance Score) | Weighted aggregate on 0–100 scale | See below |

#### Secondary / analysis metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **MAE** | Mean absolute error across expected accounts | Raw dollar error magnitude |
| **TPA** (Transaction Path Accuracy) | Fraction of intermediate states correctly predicted | Requires per-step ledger output. Not elicited by current prompt strategies — reported as 0.0%; future work. |

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

All models below evaluated on `data/test.jsonl` (100 problems, 20/level, seed 42) unless noted with *.

| Model | Strategy | n | BA | ALA | ACR | BEM | FBS | PSR | CECR | 95% CI (FBS) |
|-------|----------|---|-----|-----|-----|-----|-----|-----|------|--------------|
| GPT-5.2 | `cot` | 100 | **100.0%** | 0.813 | 87.0% | **$0** | **90.9** | 1.0% | 1.0% | [90.2, 91.5] |
| GPT-5.2 | `zero_shot` | 100 | 98.0% | **0.827** | 85.9% | **$0** | 90.2 | 5.0% | 8.0% | [87.2, 92.4] |
| Gemini 3 Flash | `cot` | 100 | 80.0% | 0.801 | 91.7% | $4,630 | 83.5 | 9.0% | 17.0% | [79.9, 86.6] |
| Gemini 3 Flash | `zero_shot` | 100 | 73.0% | 0.719 | **98.2%** | $4,376 | 79.0 | 8.0% | 15.0% | [75.6, 82.5] |
| Llama 3.3 70B | `zero_shot` | 100 | 2.0% | 0.390 | 74.1% | $56,856 | 33.4 | 0.0% | 1.0% | [30.1, 36.5] |
| GPT-5.1 | `zero_shot` | 25* | 16.0% | 0.569 | — | — | 47.9 | — | — | — |
| Claude Haiku 4.5 | `zero_shot` | 25* | 0.0% | 0.592 | — | — | 43.4 | — | — | — |
| Claude Haiku 3 | `zero_shot` | 25* | 20.0% | 0.423 | — | — | 36.3 | — | — | — |
| **Rule-based Oracle** | — | 100 | **100.0%** | **1.000** | **100%** | **$0** | **99.97** | **97%** | — | [100.0, 100.0] |

\* Preliminary results on the legacy `sample.jsonl`. Not directly comparable.

The rule-based oracle confirms **FBS ≈ 100 is achievable** — the benchmark is solvable and has a well-anchored upper bound.

**Statistical significance (pairwise permutation test, n=10,000, metric=FBS):**
All pairwise gaps are statistically significant (p < 0.001) except GPT-5.2 CoT vs. GPT-5.2 zero-shot (Δ = +0.65, p = 0.53, n.s.) and Gemini CoT vs. Gemini zero-shot (Δ = +4.4, p = 0.06, marginal).

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

### 8.3 Gemini 3 Flash — By Difficulty Level

#### Zero-shot

| Level | N | BA | ALA | ACR | BEM | FBS |
|-------|---|----|-----|-----|-----|-----|
| L1 | 20 | 90.0% | 0.797 | 93.5% | $420 | 88.5 |
| L2 | 20 | 65.0% | 0.795 | 98.1% | $2,090 | 79.0 |
| L3 | 20 | 80.0% | 0.794 | 100.0% | $4,650 | 85.0 |
| L4 | 20 | 70.0% | 0.675 | 99.3% | $1,150 | 76.1 |
| L5 | 20 | 60.0% | 0.534 | 100.0% | $13,570 | 66.5 |

#### Chain-of-Thought

| Level | N | BA | ALA | ACR | BEM | FBS |
|-------|---|----|-----|-----|-----|-----|
| L1 | 20 | 100.0% | 0.727 | 85.8% | $0 | 89.1 |
| L2 | 20 | 85.0% | 0.774 | 89.5% | $460 | 84.3 |
| L3 | 20 | 85.0% | 0.864 | 93.7% | $485 | 87.8 |
| L4 | 20 | 75.0% | 0.812 | 93.8% | $2,760 | 81.8 |
| L5 | 20 | 55.0% | 0.827 | 95.7% | $19,445 | 74.4 |

**Interpretation:** Gemini's defining failure mode is arithmetic, not structural. ACR is 93–100% (it identifies nearly all expected accounts) but BA is only 60–90% because it cannot sum them correctly. BEM rises steeply at L5 ($13k zero-shot, $19k CoT), revealing that complexity overloads the arithmetic engine rather than account recall. Notably, Gemini is the only model where CoT *reduces* ACR (98% → 92% on average) while improving BA — suggesting the reasoning trace trades off coverage for arithmetic consistency. CECR = 15–17%: Gemini attempts Retained Earnings in most problems but computes it incorrectly (75.8% arithmetic error rate on RE vs. 10.1% omission rate — the opposite of GPT-5.2's 92.8% omission pattern).

### 8.4 Llama 3.3 70B — By Difficulty Level

#### Zero-shot

| Level | N | BA | ALA | ACR | BEM | FBS | Parse Fails |
|-------|---|----|-----|-----|-----|-----|-------------|
| L1 | 20 | 10.0% | 0.423 | 62.0% | $5,110 | 36.3 | 5 |
| L2 | 20 | 0.0% | 0.471 | 66.4% | $26,054 | 33.8 | 5 |
| L3 | 20 | 0.0% | 0.570 | 85.0% | $49,825 | 41.9 | 1 |
| L4 | 20 | 0.0% | 0.310 | 79.9% | $55,780 | 31.9 | 2 |
| L5 | 20 | 0.0% | 0.173 | 77.1% | $147,510 | 23.3 | 3 |

**Interpretation:** Llama 3.3 70B fails catastrophically across all levels (BA = 2%, FBS = 33.4). The dominant error type is arithmetic (AE = 70.7%), with the model identifying accounts in the right category (ACR 62–85%) but producing wildly incorrect values — BEM reaches $147,510 at L5. The 16 parse failures (16%) are concentrated at L1–L2, suggesting the model also struggles to produce valid JSON for structurally simple problems. CECR = 1%: Retained Earnings is correctly handled in only 1 out of 100 problems.

### 8.5 Historical Baseline — Claude Haiku 3 (25-problem sample, preliminary)

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
- [x] Run Gemini 3 Flash Preview (zero_shot + CoT) on 100-problem test set
- [x] Run Llama 3.3 70B Instruct (zero_shot) on 100-problem test set
- [x] Extended metrics: ACR, BEM, SPA, PSR, HR, CECR
- [x] Bootstrap confidence intervals and pairwise permutation tests
- [x] 5-dimension failure analysis module
- [x] Error propagation simulator
- [x] Publication figures: capability curve, error composition, CoT effect
- [ ] Llama 3.3 70B CoT evaluation
- [ ] Rule-based and human baselines
- [ ] Few-shot and self-refine strategies on top-performing models
- [ ] Error propagation run for GPT-5.2 (n=3/level, checkpoint-every=2)
- [x] Account omission heatmap (F4) — failure analysis for all 3 models
- [x] BEM distribution (F5), CoT-by-difficulty (F6), propagation trajectory (F7), dataset profile (F8)
- [x] Rule-based oracle baseline (FBS = 99.97, anchors upper bound)
- [x] EPR slope computed from Haiku 3 propagation data (mean EPR = $743/checkpoint)
- [ ] Llama 3.3 70B CoT evaluation
- [ ] Human baseline (20 problems, 4 per level)
- [ ] Few-shot and self-refine strategies on top-performing models
- [ ] Error propagation run for GPT-5.2 and Gemini (n=3/level, checkpoint-every=2)
- [ ] Investigate whether targeted prompting fixes Retained Earnings omission
