# FinBalance — LLM Benchmark for Balance Sheet Generation

> A structured financial reasoning benchmark that tests language models on their ability to construct GAAP-compliant balance sheets from transaction sequences of increasing complexity.

---

## Abstract

> *Prepared for submission to ACL 2025.*

We introduce **FinBalance**, a benchmark for evaluating large language models on the task of constructing GAAP-compliant balance sheets from sequences of double-entry journal transactions. Existing financial NLP benchmarks predominantly target question answering over pre-formed documents; FinBalance instead requires models to *generate* a structured financial statement by correctly accumulating, closing, and classifying every account across a full transaction sequence. The benchmark comprises 2,500 synthetically generated problems across five difficulty levels (L1–L5), with complexity scaled by transaction type, adjusting-entry depth, and inter-entry dependency. We evaluate six models — GPT-5.2, gpt-oss-120b, Qwen 3.5 Flash, DeepSeek-v3.2, Gemini 3 Flash, and Llama 3.3 70B — on a stratified 100-problem held-out test set under zero-shot and chain-of-thought prompting, reporting twelve metrics including a composite FinBalance Score (FBS) with bootstrap confidence intervals and pairwise permutation tests.

Our experiments reveal a five-tier capability hierarchy: GPT-5.2 achieves near-perfect balance equation satisfaction (BA = 98–100%, FBS = 90.2–90.9); gpt-oss-120b CoT, Qwen CoT, and DeepSeek-v3.2 CoT cluster in a mid-high tier (FBS = 85.6–86.7); Gemini 3 Flash and zero-shot variants occupy a mid tier (FBS = 78–84); DeepSeek-v3.2 zero-shot represents a partial-failure tier (BA = 15%, FBS = 53.0) notable for near-zero parse failures combined with catastrophic arithmetic collapse; and Llama 3.3 70B fails completely (BA = 2%, FBS = 33.4). All inter-tier gaps are statistically significant (p < 0.001, paired permutation test). The most striking single finding is **DeepSeek-v3.2's extreme CoT sensitivity**: zero-shot FBS = 53.0 (BA = 15%) versus CoT FBS = 85.6 (BA = 89%), a +32.6 point gain — the largest CoT lift of any model evaluated, suggesting that DeepSeek-v3.2 possesses latent accounting knowledge that zero-shot prompting fails to mobilise. Across all models, **Retained Earnings remains the single hardest account** (72.5% omission rate, difficulty score 0.481), with qualitatively distinct failure modes ranging from complete blindness (GPT-5.2: 93–100% omission) to over-compliance (gpt-oss-120b: CECR = 43–51%). Complexity Factor Attribution identifies `mixed_funding` as the universally most harmful transaction type (DFBS up to −26.7 for gpt-oss-120b), while GPT-5.2 is immune to all complexity factors (|DFBS| < 3.4). Difficulty curve analysis using coefficient of variation cleanly separates tiers: GPT-5.2 (CV < 3%, robust) vs. mid-tier (CV 6–10%) vs. cliff models (CV > 15%), with DeepSeek-v3.2 zero-shot exhibiting the highest CV (24.6%) and the earliest cliff (L1→L2, −23.8 points). FinBalance, its dataset, evaluation harness, and all model results are released publicly.

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

**Five-tier capability hierarchy.** GPT-5.2 achieves 98–100% Balance Accuracy (FBS ~90); a mid-high tier groups gpt-oss-120b CoT, Qwen CoT, and DeepSeek-v3.2 CoT (FBS 85.6–86.7); a mid tier covers Gemini, Qwen ZS, and gpt-oss ZS (FBS 78–84); a partial-failure tier (T4-p) contains DeepSeek-v3.2 ZS (FBS = 53.0, BA = 15%) and Llama 3.3 70B CoT (FBS = 51.7, BA = 29%) — both show reasonable structural coverage but arithmetic collapse; and Llama 3.3 70B zero-shot fails completely (BA = 2%, FBS = 33.4). GPT-5.2 is the only model with a robustness CV below 3%. The most striking single findings are **DeepSeek-v3.2's CoT sensitivity** (+32.6 FBS, largest CoT lift) and **Llama 3.3 70B's CoT sensitivity** (+18.3 FBS, second largest) — revealing that CoT gain scales inversely with zero-shot capability.

**Retained Earnings is THE diagnostic account.** Across all 6 models and 11 configurations, Retained Earnings has a 72.5% omission rate — the single hardest account in the benchmark (difficulty score 0.481, nearly 2x the next-hardest). Models either omit RE entirely (GPT-5.2: 93–100%, Qwen: 94%, DeepSeek ZS: ~0% CECR, Llama: 100%) or include it but compute it incorrectly (Gemini ZS: 76% arithmetic error). gpt-oss-120b is the only model that partially succeeds (38–53% omission, CECR = 43–51%). The CECR spectrum (1% → 51%) expands with DeepSeek: ZS = 2%, CoT = 23%.

**`mixed_funding` is the universally most harmful transaction type.** Complexity Factor Attribution analysis shows that transactions requiring split cash/credit allocation cause DFBS drops of −6.5 to −26.7 for every model except GPT-5.2 (which is immune to all complexity factors with |DFBS| < 3.4).

**CoT operates through different mechanisms per model.** CoT Benefit Decomposition reveals: DeepSeek gains +32.6 FBS (largest, latent knowledge mobilisation); Llama gains +18.3 FBS (second largest, combined parse recovery + arithmetic improvement, CV degrades to 35.6% — worst in benchmark); gpt-oss-120b gains +8.2 FBS via parse recovery; Gemini gains +4.4 FBS via arithmetic improvement; Qwen gains +3.2 FBS only at L4/L5; GPT-5.2 gains +0.7 FBS (not significant, p = 0.53). CoT gain scales inversely with zero-shot capability: the weakest models benefit most.

**Equity is the hardest section for closing-entry-aware models.** Section-level error asymmetry shows gpt-oss-120b (which attempts closing entries) has its largest errors in the equity section ($5,562 mean error), while all other models fail hardest on assets ($11,604 cross-model mean).

---

## 2. Repository Structure

```
finbalance/
├── data/
│   ├── full.jsonl                        # 2,500-problem benchmark dataset
│   ├── dev.jsonl                         # 50-problem dev split (10/level, seed 42)
│   ├── test.jsonl                        # 100-problem test split (20/level, seed 42)
│   ├── large500.jsonl                    # Fixed 500-problem subset (100/level) for shared OpenRouter runs
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
│   │   │   ├── base.py                  # BaseModel + ModelConfig (max_tokens=16384, timeout=120)
│   │   │   ├── anthropic_model.py       # Anthropic Messages API backend
│   │   │   └── openrouter.py            # Legacy OpenRouter requests backend
│   │   ├── pydantic_ai/
│   │   │   ├── config.py                # Pydantic config models for OpenRouter batch runs
│   │   │   ├── dataset.py               # JSONL loading + stratified subset sampling
│   │   │   └── openrouter_model.py      # PydanticAI OpenRouter backend
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
│   ├── create_custom_subset.py          # CLI: create a fixed stratified subset JSONL
│   ├── run_evaluation.py                # CLI: run model evaluation
│   ├── run_openrouter_pydanticai.py     # CLI: PydanticAI/OpenRouter evaluation on a stratified subset
│   ├── analyze_failures.py             # CLI: run failure analysis on results
│   ├── simulate_propagation.py         # CLI: run error propagation simulation
│   ├── run_baseline.py                  # CLI: rule-based baseline + bootstrap CIs
│   ├── compute_extended_metrics.py      # Post-process results: add ACR, BEM, SPA, PSR, HR, CECR
│   ├── generate_figures.py              # Generate all 8 publication figures (F1–F8)
│   ├── permutation_tests.py             # Bootstrap CIs + pairwise permutation tests
│   ├── deep_analysis.py                 # CFA, Account Difficulty, CoT Decomp, Section Errors, Curves
│   ├── _test_parser.py                  # Parser regression tests (8 cases)
│   └── _test_saved_responses.py         # Validates saved model responses parse correctly
│
├── results/
│   ├── openai_gpt-5.2_zero_shot.json                      # GPT-5.2 zero_shot (100 problems, test set)
│   ├── openai_gpt-5.2_cot.json                            # GPT-5.2 CoT (100 problems, test set)
│   ├── google_gemini-3-flash-preview_zero_shot.json       # Gemini 3 Flash zero_shot (100 problems)
│   ├── google_gemini-3-flash-preview_cot.json             # Gemini 3 Flash CoT (100 problems)
│   ├── meta-llama_llama-3.3-70b-instruct_zero_shot.json  # Llama 3.3 70B zero_shot (100 problems)
│   ├── meta-llama_llama-3.3-70b-instruct_cot.json        # Llama 3.3 70B CoT (100 problems)
│   ├── qwen_qwen3.5-flash-02-23_zero_shot.json           # Qwen 3.5 Flash zero_shot (100 problems)
│   ├── qwen_qwen3.5-flash-02-23_cot.json                 # Qwen 3.5 Flash CoT (100 problems)
│   ├── openai_gpt-oss-120b_zero_shot.json                 # gpt-oss-120b zero_shot (100 problems)
│   ├── openai_gpt-oss-120b_cot.json                       # gpt-oss-120b CoT (100 problems)
│   ├── deepseek_deepseek-v3.2_zero_shot.json              # DeepSeek-v3.2 zero_shot (100 problems)
│   ├── deepseek_deepseek-v3.2_cot.json                    # DeepSeek-v3.2 CoT (100 problems)
│   ├── failure_analysis_*.json                             # Per-model failure analyses
│   ├── deep_analysis.json                                  # CFA, Account Difficulty, CoT Decomp, Section Errors, Curves
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
├── pyproject.toml                     # uv-managed project metadata and dependencies
└── uv.lock                            # Locked dependency graph for reproducible runs
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
| PydanticAI OpenRouter | `PydanticAIOpenRouterModel` | `OPENROUTER_API_KEY` | Dedicated OpenRouter runner with Pydantic configs, the fixed `Large-500` dataset, and OpenRouter native reasoning enabled by default for `cot` |

The runner auto-detects backend: model IDs starting with `claude-` route to `AnthropicModel`; all others route to `OpenRouterModel`.

**Important:** Reasoning-heavy frontier models (e.g. GPT-5.2) generate extensive chain-of-thought before emitting the final JSON even in zero_shot mode. `ModelConfig` defaults have been updated to `max_tokens=16384` and `timeout=120s` to reduce truncation risk. `max_tokens` here is the response budget, not the full input+output context window.

### 5.4 Running an Evaluation

```bash
# Create stratified dev/test splits from full.jsonl
uv run python scripts/create_splits.py --input data/full.jsonl --seed 42

# Run evaluation on the held-out test set (OpenRouter)
export OPENROUTER_API_KEY="your-key"
uv run python scripts/run_evaluation.py \
    --dataset data/test.jsonl \
    --models openai/gpt-5.2 \
    --strategies zero_shot,cot

# Run the dedicated PydanticAI/OpenRouter path on the appendix Large-500 subset.
# Defaults:
#   models = qwen/qwen3.6-plus-preview:free,qwen/qwen3.5-flash-02-23,deepseek/deepseek-v3.2,openai/gpt-oss-120b,google/gemini-3-flash-preview
#   dataset = data/large500.jsonl
#   cot = prompt-level CoT + OpenRouter native reasoning by default
uv run python scripts/run_openrouter_pydanticai.py \
    --strategies zero_shot,cot \
    --write-subset-path data/large500.jsonl

# Keep the CoT prompt but disable OpenRouter native reasoning explicitly
uv run python scripts/run_openrouter_pydanticai.py \
    --strategies cot \
    --cot-reasoning-effort off

# Run with Anthropic key
export ANTHROPIC_API_KEY="your-key"
uv run python scripts/run_evaluation.py \
    --dataset data/test.jsonl \
    --models claude-3-5-sonnet-20241022 \
    --strategies zero_shot
```

Results are saved to `results/<model>_<strategy>.json` for the legacy runner and `results/pydantic_ai/<model>_<strategy>.json` for the PydanticAI/OpenRouter runner.

### 5.5 Bootstrap Statistical Analysis

```bash
uv run python scripts/run_baseline.py \
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
uv run python scripts/analyze_failures.py \
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
uv run python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --model claude-3-haiku-20240307 \
    --n-per-level 1 \
    --checkpoint-every 1 \
    --output results/propagation_haiku.json

# Print summary from saved traces (no new API calls)
uv run python scripts/simulate_propagation.py \
    --dataset data/sample.jsonl \
    --output results/propagation_haiku.json \
    --summary-only

# Every 2nd transaction checkpoint (halves API cost)
uv run python scripts/simulate_propagation.py \
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

| Model | Strategy | n | BA | ALA | ACR | BEM | FBS | CECR | CV% | Tier |
|-------|----------|---|-----|-----|-----|-----|-----|------|-----|------|
| **Rule-based Oracle** | — | 100 | **100%** | **1.000** | **100%** | **$0** | **99.97** | — | 0.0 | — |
| GPT-5.2 | `cot` | 100 | **100%** | 0.813 | 87.0% | **$0** | **90.9** | 1% | **1.5** | T1 |
| GPT-5.2 | `zero_shot` | 100 | 98% | **0.827** | 85.9% | **$0** | 90.2 | 8% | **2.2** | T1 |
| Qwen 3.5 Flash | `cot` | 100 | 91% | 0.782 | 89.1% | $1,317 | 86.7 | 7% | 6.4 | T2 |
| gpt-oss-120b | `cot` | 100 | 86% | 0.834 | 88.8% | $4,886 | 86.4 | **43%** | 9.5 | T2 |
| DeepSeek-v3.2 | `cot` | 100 | 89% | 0.774 | 87.4% | $3,531 | 85.6 | 23% | 7.3 | T2 |
| Qwen 3.5 Flash | `zero_shot` | 100 | 86% | 0.754 | 88.4% | $1,956 | 83.5 | 3% | 12.1 | T3 |
| Gemini 3 Flash | `cot` | 100 | 80% | 0.801 | 91.7% | $4,630 | 83.5 | 17% | 6.3 | T3 |
| Gemini 3 Flash | `zero_shot` | 100 | 73% | 0.719 | **98.2%** | $4,376 | 79.0 | 15% | 9.6 | T3 |
| gpt-oss-120b | `zero_shot` | 100 | 81% | 0.738 | 77.8% | $1,712 | 78.1 | **51%** | **18.4** | T3 |
| DeepSeek-v3.2 | `zero_shot` | 100 | 15% | 0.645 | **96.8%** | $56,722 | 53.0 | 2% | 24.6 | T4-p |
| Llama 3.3 70B | `cot` | 100 | 29% | 0.545 | 80.4% | $36,300 | 51.7 | 1% | **35.6** | T4-p |
| Llama 3.3 70B | `zero_shot` | 100 | 2% | 0.390 | 74.1% | $56,856 | 33.4 | 1% | 18.2 | T4 |

CV% = coefficient of variation of FBS across difficulty levels (lower = more robust). Tier assignment: T1 (FBS > 88), T2 (FBS 85–88), T3 (FBS 75–85), T4-p (partial failure: structural coverage with arithmetic collapse), T4 (FBS < 40, catastrophic). Llama CoT has the highest CV of any model (35.6%).

\* Preliminary results on legacy `sample.jsonl` (not shown): GPT-5.1 FBS=47.9, Claude Haiku 4.5 FBS=43.4, Claude Haiku 3 FBS=36.3.

**Statistical significance (pairwise permutation test, n=10,000, metric=FBS):**
All inter-tier gaps are statistically significant (p < 0.001). Within-strategy comparisons: GPT-5.2 CoT vs. ZS (p = 0.53, n.s.), Gemini CoT vs. ZS (p = 0.06, marginal).

### 8.2 Deep Analysis Findings

#### Account Difficulty Index (Top 5)

| Rank | Account | Omission% | Arithmetic% | Correct% | Difficulty Score |
|------|---------|-----------|-------------|----------|-----------------|
| 1 | **Retained Earnings** | **70.4%** | 15.6% | 14.0% | **0.485** |
| 2 | Accumulated Depreciation | **34.0%** | 3.5% | 62.4% | 0.218 |
| 3 | Owner's Equity | 2.2% | 50.7% | 47.0% | 0.216 |
| 4 | Allowance for Doubtful Accounts | 18.7% | 5.6% | 75.7% | 0.135 |
| 5 | Cash | 0.3% | 31.9% | 67.8% | 0.129 |

*Aggregated across all 12 model×strategy runs. With Llama CoT included, Accumulated Depreciation rises to #2 (Llama CoT has 76% omission rate on AccumDepr — it frequently misses this account entirely under CoT, unlike zero-shot where it was partially present).*

#### Complexity Factor Attribution (Most Harmful Factor per Model)

| Model | Most Harmful Factor | DFBS |
|-------|-------------------|------|
| GPT-5.2 | prepaid (controlled) | −2.5 |
| gpt-oss-120b ZS | mixed_funding | −26.7 |
| Gemini ZS | mixed_funding | −12.8 |
| Qwen ZS | mixed_funding | −14.7 |
| Llama ZS | prepaid (controlled) | −12.3 |

`mixed_funding` is the universal killer for all non-GPT-5.2 models.

#### CoT Benefit Decomposition

| Model | DFBS | Primary Mechanism | Parse Fixes | DArith | Improved | Degraded |
|-------|------|-------------------|-------------|--------|----------|---------|
| **DeepSeek-v3.2** | **+32.6** | **Latent knowledge mobilisation** | 0 | −3.47 | 87 | 11 |
| **Llama 3.3 70B** | **+18.3** | **Parse recovery + arithmetic** | 16 | −1.52 | 79 | 15 |
| gpt-oss-120b | +8.2 | Parse recovery only | 16 | +0.22 | 37 | 33 |
| Gemini | +4.4 | Arithmetic improvement | 0 | −2.09 | 53 | 41 |
| Qwen | +3.2 | L4/L5 only | 1 | −0.35 | 19 | 13 |
| GPT-5.2 | +0.7 | Neutral (p=0.53) | 2 | +0.19 | 21 | 44 |

**CoT gain scales inversely with zero-shot capability.** The two models with the highest CoT gains (DeepSeek +32.6, Llama +18.3) are also the two worst zero-shot performers. Both fix parse failures (Llama: 16, gpt-oss: 16) but Llama also fixes arithmetic (DArith = −1.52), while gpt-oss arithmetic *worsens* (+0.22). Llama CoT's gains are front-loaded at L1/L2 (+44.1, +29.7) and negligible at L3–L5, producing the worst CV in the benchmark (35.6%).

#### Difficulty Robustness (CV Classification)

| Classification | CV% | Models |
|---------------|-----|--------|
| ROBUST | < 3% | GPT-5.2 (both strategies) |
| MODERATE | 3–8% | Gemini CoT (6.3%), Qwen CoT (6.4%), DeepSeek CoT (7.3%) |
| STEEP | 8–15% | gpt-oss CoT (9.5%), Gemini ZS (9.6%), Qwen ZS (12.1%) |
| CLIFF | > 15% | Llama ZS (18.2%), gpt-oss ZS (18.4%), DeepSeek ZS (24.6%), **Llama CoT (35.6% — worst in benchmark)** |

### 8.3 GPT-5.2 — By Difficulty Level

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

### 8.4 GPT-5.2 — Failure Analysis

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

### 8.5 gpt-oss-120b — By Difficulty Level

#### Zero-shot (CV = 18.4%, CLIFF)

| Level | N | BA | ALA | ACR | BEM | FBS | CECR |
|-------|---|----|-----|-----|-----|-----|------|
| L1 | 20 | 90.0% | 0.667 | 77.8% | $0 | 80.6 | 25% |
| L2 | 20 | 90.0% | 0.855 | 89.7% | $920 | 88.8 | 50% |
| L3 | 20 | 100.0% | 0.945 | 96.3% | $0 | **97.0** | 85% |
| L4 | 20 | 65.0% | 0.667 | 68.6% | $7,640 | 66.6 | 50% |
| L5 | 20 | 60.0% | 0.556 | 56.7% | $0 | 57.6 | 45% |

#### Chain-of-Thought (CV = 9.5%, STEEP)

| Level | N | BA | ALA | ACR | BEM | FBS | CECR |
|-------|---|----|-----|-----|-----|-----|------|
| L1 | 20 | 100.0% | 0.760 | 86.5% | $0 | 90.1 | 30% |
| L2 | 20 | 95.0% | 0.859 | 90.7% | $780 | 91.3 | 25% |
| L3 | 20 | 95.0% | 0.936 | 96.1% | $3,250 | 95.0 | 70% |
| L4 | 20 | 70.0% | 0.910 | 94.0% | $19,175 | 83.6 | 55% |
| L5 | 20 | 70.0% | 0.704 | 76.5% | $1,225 | 71.7 | 35% |

**Interpretation:** gpt-oss-120b exhibits the most dramatic cliff in the benchmark: ZS L3 FBS = 97.0 (the single best level result of any model) drops to L4 = 66.6 (−30.4 points). This non-monotonic "sweet-spot then cliff" suggests the model's training data contains L3-complexity financial tasks heavily but lacks L4/L5 multi-entity patterns. CECR is anomalously high (43–51% overall) — the polar opposite of GPT-5.2's closing-entry blindness. gpt-oss-120b frequently includes closing entries but often computes them incorrectly, especially at L4/L5.

### 8.6 Qwen 3.5 Flash — By Difficulty Level

#### Zero-shot (CV = 12.1%, STEEP)

| Level | N | BA | ALA | ACR | BEM | FBS | CECR |
|-------|---|----|-----|-----|-----|-----|------|
| L1 | 20 | 100.0% | 0.660 | 82.0% | $0 | 86.2 | 5% |
| L2 | 20 | 100.0% | 0.768 | 88.4% | $0 | 89.7 | 0% |
| L3 | 20 | 100.0% | 0.837 | 91.9% | $0 | 92.2 | 5% |
| L4 | 20 | 85.0% | 0.812 | 92.7% | $3,420 | 85.4 | 0% |
| L5 | 20 | 45.0% | 0.692 | 87.0% | $6,360 | 64.0 | 5% |

#### Chain-of-Thought (CV = 6.4%, MODERATE)

| Level | N | BA | ALA | ACR | BEM | FBS | CECR |
|-------|---|----|-----|-----|-----|-----|------|
| L1 | 20 | 100.0% | 0.650 | 82.0% | $0 | 85.8 | 5% |
| L2 | 20 | 100.0% | 0.774 | 88.4% | $0 | 89.9 | 0% |
| L3 | 20 | 100.0% | 0.834 | 91.5% | $0 | 92.2 | 5% |
| L4 | 20 | 90.0% | 0.856 | 93.1% | $665 | 89.3 | 15% |
| L5 | 20 | 65.0% | 0.796 | 90.7% | $5,920 | 76.3 | 10% |

**Interpretation:** Qwen 3.5 Flash has the lowest BEM among mid-tier models ($1,317–$1,956) and very low hallucination rate (HR = 1.0–1.6%), indicating high section placement precision. However, it shares the closing-entry blindness pattern with GPT-5.2 (RE omission = 94%, CECR = 3–7%). CoT has minimal impact at L1–L3 (DFBS ~0) but provides meaningful gains at L4 (+3.9) and L5 (+12.4), consistent with CoT being most useful where complexity exceeds the model's zero-shot capacity.

### 8.7 Gemini 3 Flash — By Difficulty Level

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

### 8.8 Llama 3.3 70B — By Difficulty Level

#### Zero-shot

| Level | N | BA | ALA | ACR | BEM | FBS | Parse Fails |
|-------|---|----|-----|-----|-----|-----|-------------|
| L1 | 20 | 10.0% | 0.423 | 62.0% | $5,110 | 36.3 | 5 |
| L2 | 20 | 0.0% | 0.471 | 66.4% | $26,054 | 33.8 | 5 |
| L3 | 20 | 0.0% | 0.570 | 85.0% | $49,825 | 41.9 | 1 |
| L4 | 20 | 0.0% | 0.310 | 79.9% | $55,780 | 31.9 | 2 |
| L5 | 20 | 0.0% | 0.173 | 77.1% | $147,510 | 23.3 | 3 |

**Interpretation:** Llama 3.3 70B fails catastrophically across all levels (BA = 2%, FBS = 33.4). The dominant error type is arithmetic (AE = 70.7%), with the model identifying accounts in the right category (ACR 62–85%) but producing wildly incorrect values — BEM reaches $147,510 at L5. The 16 parse failures (16%) are concentrated at L1–L2. CECR = 1%: Retained Earnings is correctly handled in only 1 out of 100 problems.

#### Chain-of-Thought (CV = 35.6%, CLIFF — highest CV of any model)

| Level | N | BA | ALA | ACR | BEM | FBS | CECR |
|-------|---|----|-----|-----|-----|-----|------|
| L1 | 20 | 85.0% | 0.668 | 82.0% | $595 | **80.5** | 5% |
| L2 | 20 | 30.0% | 0.814 | 88.4% | $9,725 | 63.4 | 0% |
| L3 | 20 | 25.0% | 0.558 | 69.0% | $19,025 | 48.2 | 0% |
| L4 | 20 | 0.0% | 0.463 | 74.9% | $42,990 | 37.8 | 0% |
| L5 | 20 | 5.0% | 0.221 | 64.5% | $69,160 | 28.8 | 0% |

**Interpretation:** Llama CoT represents the largest absolute CoT gain in the benchmark after DeepSeek (+18.3 FBS vs. ZS). The gain is almost entirely front-loaded: L1 improves dramatically (FBS 36.3 → 80.5, BA 10% → 85%) as CoT eliminates parse failures and fixes simple arithmetic. However, from L2 onward the model still collapses, making Llama CoT the **worst CV in the entire benchmark (35.6%)** — worse than even DeepSeek ZS (24.6%). The cliff at L1→L2 (−17.1 FBS) is the steepest level-to-level drop of any CoT run. CECR remains 1%: CoT does not activate closing-entry awareness in Llama at any level. The error pattern shifts from arithmetic-dominant (ZS: AE=70.7%) to still arithmetic-dominant (CoT: AE=62.3%) but with fewer parse failures (6% vs 16%).

### 8.9 DeepSeek-v3.2 — By Difficulty Level

#### Zero-shot (CV = 24.6%, CLIFF — earliest cliff L1→L2)

| Level | N | BA | ALA | ACR | BEM | FBS | CECR |
|-------|---|----|-----|-----|-----|-----|------|
| L1 | 20 | 70.0% | 0.677 | 93.7% | $1,525 | 76.67 | 10% |
| L2 | 20 | 5.0% | 0.743 | 96.2% | $17,455 | 52.83 | 0% |
| L3 | 20 | 0.0% | 0.763 | 98.1% | $31,105 | 51.83 | 0% |
| L4 | 20 | 0.0% | 0.602 | 98.9% | $68,010 | 45.72 | 0% |
| L5 | 20 | 0.0% | 0.440 | 97.2% | $165,515 | 37.75 | 0% |

#### Chain-of-Thought (CV = 7.3%, MODERATE)

| Level | N | BA | ALA | ACR | BEM | FBS | CECR |
|-------|---|----|-----|-----|-----|-----|------|
| L1 | 20 | 100.0% | 0.723 | 85.7% | $0 | 88.76 | 25% |
| L2 | 20 | 100.0% | 0.856 | 92.8% | $0 | **93.49** | **40%** |
| L3 | 20 | 95.0% | 0.801 | 87.5% | $100 | 89.11 | 20% |
| L4 | 20 | 75.0% | 0.748 | 85.4% | $4,025 | 78.98 | 25% |
| L5 | 20 | 75.0% | 0.741 | 85.6% | $13,530 | 77.46 | 5% |

**Interpretation:** DeepSeek-v3.2 exhibits the most dramatic CoT sensitivity in the benchmark (+32.6 FBS). Under zero-shot prompting, the model identifies accounts with high structural accuracy (ACR = 96.8%) but fails arithmetic completely from L2 onward (BA collapses to 5% at L2, then 0% at L3–L5). The cliff is the earliest of any model — L1→L2 drop of −23.8 FBS — and the highest CV (24.6%). Under CoT, the model fully recovers: BA = 89%, peak FBS = 93.49 at L2 (the second-highest level result across all models), and consistent performance through L5. CECR = 23% CoT vs 2% ZS — DeepSeek ZS has essentially zero closing-entry compliance, while CoT partially activates it. The pattern suggests DeepSeek-v3.2 has internalized accounting knowledge but requires explicit step-by-step reasoning to activate correct arithmetic output.

### 8.10 Historical Baseline — Claude Haiku 3 (25-problem sample, preliminary)

Included for qualitative contrast. See commit `fd55235` for full analysis.

| Metric | Value |
|--------|-------|
| Balance Accuracy (BA) | **20.0%** |
| Account-Level Accuracy (ALA) | **0.423** |
| FinBalance Score (FBS) | **36.3 / 100** |
| Retained Earnings omission | **100%** |
| `depreciable_asset` ΔFBS | **−10.3** |

### 8.11 Error Propagation (Claude Haiku 3, 5 problems)

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
uv sync
printf 'OPENROUTER_API_KEY=your-key\n' > .env
```

### Generate dataset

```bash
# Full dataset (2,500 problems)
uv run python scripts/generate_dataset.py --counts 1:500,2:750,3:750,4:400,5:100 --output data/full.jsonl --seed 42

# Create stratified dev/test splits
uv run python scripts/create_splits.py --input data/full.jsonl --seed 42
# → data/dev.jsonl (50 problems, 10/level)
# → data/test.jsonl (100 problems, 20/level)

# Create the fixed Large-500 subset used for shared OpenRouter runs
uv run python scripts/create_custom_subset.py \
    --input data/full.jsonl \
    --output data/large500.jsonl \
    --size 500 \
    --seed 42
# → data/large500.jsonl (500 problems, 100/level)
```

### Run evaluation

```bash
# Anthropic model
export ANTHROPIC_API_KEY="your-key"
uv run python scripts/run_evaluation.py \
    --dataset data/test.jsonl \
    --models claude-3-5-sonnet-20241022 \
    --strategies zero_shot,cot

# OpenRouter model (GPT, Llama, Gemini, etc.)
export OPENROUTER_API_KEY="your-key"
uv run python scripts/run_evaluation.py \
    --dataset data/test.jsonl \
    --models openai/gpt-5.2 \
    --strategies zero_shot,cot

# PydanticAI/OpenRouter path using data/large500.jsonl by default
# (500 problems = 100 per difficulty level) and the five default
# OpenRouter models used in this repo.
uv run python scripts/run_openrouter_pydanticai.py \
    --strategies zero_shot,cot \
    --write-subset-path data/large500.jsonl

# Full batch fan-out across model×strategy jobs plus per-run request concurrency
uv run python scripts/run_openrouter_pydanticai.py \
    --strategies zero_shot,cot \
    --parallel-runs 10 \
    --workers 8 \
    --write-subset-path data/large500.jsonl
```

### Analyse failures

```bash
uv run python scripts/analyze_failures.py \
    --results results/openai_gpt-5.2_zero_shot.json \
    --dataset data/test.jsonl
```

### Bootstrap confidence intervals

```bash
uv run python scripts/run_baseline.py \
    --dataset data/test.jsonl \
    --model-results results/openai_gpt-5.2_cot.json \
    --stats-only \
    --n-boot 2000
```

### Simulate error propagation

```bash
uv run python scripts/simulate_propagation.py \
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
| `max_tokens` | `16384` | Maximum response tokens — increased from 2048 to accommodate extended reasoning in frontier models |
| `timeout` | `120` | API request timeout in seconds — increased from 60 for L4/L5 problems |

**Note on `max_tokens`:** Models such as GPT-5.2 generate extensive internal chain-of-thought reasoning before emitting the final JSON, even under zero_shot prompting. At `max_tokens=2048` or `max_tokens=4096`, these models hit the token cap and OpenRouter can return `null` content rather than usable text. The default is now `16384` to give a larger response budget. This still does not bypass a model's total context-window limit, which includes both prompt and completion tokens.

### OpenRouterBatchConfig

`scripts/run_openrouter_pydanticai.py` is the separate PydanticAI-backed harness for OpenRouter runs. Its defaults align with the paper appendix `Large-500` protocol and point at the fixed dataset file `data/large500.jsonl`: `500` problems total, `100` from each difficulty level.

The default model list is:
`qwen/qwen3.6-plus-preview:free`,
`qwen/qwen3.5-flash-02-23`,
`deepseek/deepseek-v3.2`,
`openai/gpt-oss-120b`,
`google/gemini-3-flash-preview`

Outputs go to `results/pydantic_ai/` by default, and `--write-subset-path` saves the exact sampled JSONL used for the run. The runner loads `OPENROUTER_API_KEY` from a repo-local `.env` file automatically. Use `--parallel-runs` to fan out model×strategy jobs and `--workers` to control concurrent requests inside each job.

Prompting semantics in the PydanticAI/OpenRouter runner:
- `zero_shot`: prompt-only direct JSON generation, with OpenRouter native reasoning explicitly disabled
- `cot`: prompt-level chain-of-thought plus OpenRouter native reasoning enabled by default with `--cot-reasoning-effort high`
- `--cot-reasoning-effort off`: keeps the CoT prompt but disables the OpenRouter native reasoning control

### PropagationSimulator

| Parameter | Default | Description |
|-----------|---------|-------------|
| `checkpoint_every` | `1` | Transactions between API calls (1 = every single transaction) |
| `max_checkpoints` | `0` | Cap checkpoints per problem (0 = unlimited) |
| `sleep_between` | `0.5` | Seconds between API calls for rate-limit safety |
| `verbose` | `True` | Print progress to stdout |

---

## Roadmap

### Completed
- [x] Generate full 2,500-problem benchmark dataset (`full.jsonl`)
- [x] Create standardised stratified dev/test splits (`dev.jsonl`, `test.jsonl`)
- [x] OpenRouter backend for multi-model evaluation (with `--workers` and `--max-tokens` flags)
- [x] Run GPT-5.2 evaluation (zero_shot + CoT) on 100-problem test set
- [x] Run Gemini 3 Flash Preview (zero_shot + CoT) on 100-problem test set
- [x] Run Llama 3.3 70B Instruct (zero_shot) on 100-problem test set
- [x] Run Qwen 3.5 Flash (zero_shot + CoT) on 100-problem test set
- [x] Run gpt-oss-120b (zero_shot + CoT) on 100-problem test set
- [x] Run DeepSeek-v3.2 (zero_shot + CoT) on 100-problem test set
- [x] Run Llama 3.3 70B CoT on 100-problem test set (FBS=51.7, CV=35.6%, +18.3 from ZS)
- [x] Extended metrics: ACR, BEM, SPA, PSR, HR, CECR
- [x] Bootstrap confidence intervals and pairwise permutation tests
- [x] 5-dimension failure analysis module
- [x] Error propagation simulator
- [x] Publication figures (F1–F8)
- [x] Rule-based oracle baseline (FBS = 99.97)
- [x] Deep analysis: CFA, Account Difficulty Index, CoT Decomposition, Section Error Asymmetry, Difficulty Curves

### Pending
- [x] Llama 3.3 70B CoT evaluation
- [ ] Human baseline (20 problems, 4 per level)
- [ ] Error propagation run for GPT-5.2 and Gemini (n=3/level, checkpoint-every=2)
- [ ] Few-shot and self-refine strategies on top-performing models
- [ ] Investigate whether targeted prompting fixes Retained Earnings omission

### Adding a new model
```bash
# 1. Run evaluation
uv run python scripts/run_evaluation.py --dataset data/test.jsonl \
    --models <model_id> --strategies zero_shot,cot --workers 8 \
    --max-tokens 32768 --api-key <key>

# 2. Compute extended metrics + update leaderboard.json
uv run python scripts/compute_extended_metrics.py

# 3. Failure analysis
uv run python scripts/analyze_failures.py --results results/<model>_zero_shot.json \
    --dataset data/test.jsonl --output results/failure_analysis_<model>_zero_shot.json
uv run python scripts/analyze_failures.py --results results/<model>_cot.json \
    --dataset data/test.jsonl --output results/failure_analysis_<model>_cot.json

# 4. Regenerate deep analysis, permutation tests, and figures
uv run python scripts/deep_analysis.py
uv run python scripts/permutation_tests.py
uv run python scripts/generate_figures.py
```
