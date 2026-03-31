# Large-500 Integration Plan

## Backup Status

Before analysis, the current results were backed up locally at:

- `backups/pre_paper_analysis_20260401_040024/`

Latest synced server snapshot used for this analysis:

- `backups/server_sync/20260401_035735/results_pydantic_ai/`
- `backups/server_sync/20260401_035735/results_pydantic_ai_analysis_20260401/`

These backups preserve the raw run outputs and the server-generated analysis artifacts before any paper-integration work.

## Current Paper Structure

The manuscript entrypoint is:

- `paper/final.tex`

Section order is defined in:

- `paper/preamble/body.tex`

Current structure:

1. `paper/sections/00_abstract.tex`
2. `paper/sections/01_introduction.tex`
3. `paper/sections/01a_related_work.tex`
4. `paper/sections/02_benchmark_design.tex`
5. `paper/sections/03_experimental_setup.tex`
6. `paper/sections/04_results.tex`
7. `paper/sections/05_analysis_discussion.tex`
8. `paper/sections/06_limitations_ethics.tex`
9. `paper/sections/07_conclusion.tex`
10. `paper/sections/appendix.tex`

Primary paper tables:

- `paper/tables/main_results.tex`
- `paper/tables/account_difficulty.tex`
- `paper/tables/complexity_factors.tex`

## Manuscript Mismatch With Latest Results

The current paper is still written around the older paired 100-problem study, not the Large-500 OpenRouter/PydanticAI runs.

Places that explicitly encode the old setting:

- `paper/sections/00_abstract.tex`
- `paper/sections/01_introduction.tex`
- `paper/sections/03_experimental_setup.tex`
- `paper/sections/04_results.tex`
- `paper/sections/06_limitations_ethics.tex`
- `paper/tables/main_results.tex`

Examples of hard-coded older claims:

- `paper/sections/04_results.tex` references:
  - GPT-5.2 as the clear winner
  - Qwen 3.5 CoT = `86.72`
  - gpt-oss-120b CoT = `86.35`
  - DeepSeek CoT = `85.56`
  - DeepSeek zero-shot = `52.96`
  - DeepSeek CoT gain = `+32.6`
- `paper/tables/main_results.tex` is the old paired-100 table.

That means the manuscript currently mixes an older benchmark narrative with newer repo infrastructure and newer Large-500 outputs.

## Valid Large-500 Runs

Complete and valid runs in the latest synced snapshot:

- `deepseek/deepseek-v3.2` `cot`
- `deepseek/deepseek-v3.2` `zero_shot`
- `google/gemini-3-flash-preview` `cot`
- `google/gemini-3-flash-preview` `zero_shot`
- `qwen/qwen3.5-flash-02-23` `cot`
- `qwen/qwen3.5-flash-02-23` `zero_shot`
- `qwen/qwen3.6-plus-preview:free` `cot`

Excluded:

- `openai/gpt-oss-120b` `cot`
  - incomplete in the synced snapshot
  - only `37` rows present
  - should not be used in cross-model claims

## Large-500 Topline Findings

Source:

- `backups/server_sync/20260401_035735/results_pydantic_ai_analysis_20260401/leaderboard.json`
- `backups/server_sync/20260401_035735/results_pydantic_ai_analysis_20260401/deep_analysis.json`
- `backups/server_sync/20260401_035735/results_pydantic_ai_analysis_20260401/significance_tests.json`

Completed-run ranking by FBS:

1. DeepSeek CoT: `FBS 92.25`, `BA 99.4%`
2. Gemini CoT: `FBS 88.84`, `BA 96.2%`
3. Qwen 3.6 CoT: `FBS 86.92`, `BA 90.2%`
4. Qwen 3.5 CoT: `FBS 82.91`, `BA 83.0%`
5. Gemini zero-shot: `FBS 80.20`, `BA 75.6%`
6. DeepSeek zero-shot: `FBS 50.82`, `BA 11.6%`
7. Qwen 3.5 zero-shot: `FBS 46.51`, `BA 18.0%`

Strongest significance results:

- DeepSeek CoT vs Gemini CoT: `+3.4164 FBS`, `p < 0.001`
- DeepSeek CoT vs Qwen 3.6 CoT: `+5.3266 FBS`, `p < 0.001`
- DeepSeek CoT vs Qwen 3.5 CoT: `+9.34 FBS`, `p < 0.001`
- DeepSeek CoT vs DeepSeek zero-shot: `+41.4316 FBS`, `p < 0.001`
- Qwen 3.5 CoT vs Qwen 3.5 zero-shot: `+36.4045 FBS`, `p < 0.001`
- Gemini CoT vs Gemini zero-shot: `+8.633 FBS`, `p < 0.001`

## Strongest New Paper-Worthy Claims

### 1. DeepSeek CoT is not just best overall; it is best specifically on hard cases.

DeepSeek CoT beats Gemini CoT more strongly at L5 than at L1.

- L1 FBS:
  - DeepSeek CoT `87.74`
  - Gemini CoT `85.45`
  - delta `+2.29`
- L5 FBS:
  - DeepSeek CoT `93.30`
  - Gemini CoT `85.13`
  - delta `+8.17`

This supports a stronger claim than "best aggregate score": DeepSeek CoT has the best hard-case robustness.

### 2. DeepSeek CoT shows a reverse difficulty curve.

DeepSeek CoT is the only run in the set where L5 performance is above L1.

- L1 FBS `87.74`
- L5 FBS `93.30`
- robustness CV `2.57`

This is a stronger and more distinctive result than generic robustness.

### 3. DeepSeek zero-shot is a canonical "structure without arithmetic" failure mode.

DeepSeek zero-shot has:

- `ACR 0.9656`
- `parse_fail_rate 0.0`
- but `BA 11.6%`
- and `BEM 61,339.2`

After L1, BA is nearly dead:

- L2 `3%`
- L3 `0%`
- L4 `1%`
- L5 `1%`

This is experimentally cleaner than saying it merely "performs poorly".

### 4. Gemini CoT is difficulty-conditional, not uniformly beneficial.

Per-level mean FBS improvement from zero-shot to CoT:

- L1 `-0.97`
- L2 `+7.47`
- L3 `+3.40`
- L4 `+14.35`
- L5 `+18.91`

Gemini CoT is slightly worse on easy cases and strongly better on hard ones. This is a useful contrast class against DeepSeek and Qwen 3.5.

### 5. Qwen 3.6 improves over Qwen 3.5 almost entirely through hard-case robustness.

Per-level CoT deltas (`Qwen 3.6 - Qwen 3.5`):

- L1 `+0.75`
- L2 `+0.57`
- L3 `-0.13`
- L4 `+8.84`
- L5 `+10.03`

This makes Qwen 3.6 a cleaner "hard-case upgrade" story than a general across-the-board improvement story.

### 6. DeepSeek CoT wins while retaining a different error profile from Gemini/Qwen.

DeepSeek CoT has much larger:

- `PSR 25.4`
- `CECR 29.4`

than:

- Gemini CoT: `PSR 4.4`, `CECR 5.0`
- Qwen 3.6 CoT: `PSR 8.0`, `CECR 9.4`

So the best overall run is not uniformly "cleaner"; it is stronger under the benchmark objective while still showing qualitatively different accounting-side behavior.

### 7. Retained Earnings is now an even clearer outlier bottleneck.

Global account difficulty:

- `Retained Earnings` difficulty score `0.4941`
- next hardest `Owner's Equity` `0.2637`

That gap is large enough to frame Retained Earnings as a true outlier, not merely one hard account among several.

## Real Inconsistencies Found

### 1. Summary sign error

In:

- `backups/server_sync/20260401_035735/results_pydantic_ai_analysis_20260401/summary.md`

the text says Gemini zero-shot outperforms Qwen 3.5 CoT by `2.71 FBS`.

That is incorrect. The actual leaderboard says:

- Gemini zero-shot `80.20`
- Qwen 3.5 CoT `82.91`

and the paired test delta is negative for Gemini zero-shot:

- `delta: -2.7094`

### 2. GPT OSS cannot be used in the main comparative paper story

In the latest synced snapshot:

- `openai_gpt-oss-120b_cot.json` has only `37` rows
- `463` problems are missing

So any paper version using the current Large-500 analysis must explicitly exclude GPT OSS or rerun it to completion later.

## Zero-Shot BA Collapse Audit

The zero-shot BA collapse for DeepSeek and Qwen is real, not a run artifact.

Checked locally against:

- `backups/server_sync/20260401_035735/results_pydantic_ai/`

Findings:

- both files have `500/500` rows
- no duplicate problem IDs
- no missing problem IDs
- zero parse failures
- non-empty raw outputs

The bad high-level rows are valid-looking structured predictions with wrong arithmetic, not parser failures.

## Section-Level Paper Update Plan

### Abstract

Replace the old paired-100 story with the new completed-run Large-500 story:

- DeepSeek CoT as best completed run
- DeepSeek zero-shot as structure-without-arithmetic collapse
- Qwen 3.6 as stronger hard-case CoT model than Qwen 3.5
- Gemini CoT as smaller but difficulty-conditional benefit

### Introduction

Keep the benchmark motivation, but update the empirical hook:

- the strongest story is no longer "GPT-5.2 dominates"
- the strongest current story is that among completed Large-500 runs, DeepSeek CoT is best and zero-shot prompt sensitivity is massive

### Experimental Setup

This section needs the largest rewrite.

It currently describes:

- a paired 100-problem split

It should either:

1. remain explicitly the old 100-problem paper, and treat Large-500 as new appendix/follow-up analysis

or

2. be rewritten around the Large-500 OpenRouter/PydanticAI protocol, including:
   - `data/large500.jsonl`
   - completed model set
   - exclusion of incomplete GPT OSS
   - OpenRouter/PydanticAI execution setup

Do not mix both evaluation protocols without clearly separating them.

### Results

`paper/sections/04_results.tex` and `paper/tables/main_results.tex` should be updated together.

If switching to Large-500:

- replace the old main table entirely
- remove GPT-5.2 and Llama claims from the main comparative narrative unless they are still intentionally part of the paper's primary study
- rewrite the CoT discussion around:
  - DeepSeek CoT best overall
  - Gemini zero-shot stronger than any zero-shot peer
  - Qwen 3.6 vs Qwen 3.5 hard-case separation

### Analysis and Discussion

This section can absorb the richest new material with minimal conceptual change:

- DeepSeek reverse difficulty curve
- DeepSeek zero-shot structural-but-arithmetic failure mode
- Gemini difficulty-conditional CoT benefit
- Qwen 3.6 hard-case robustness gain over Qwen 3.5
- Retained Earnings as an outlier account bottleneck
- section-error asymmetry by prompting regime

### Limitations

Add:

- GPT OSS Large-500 incomplete
- current Large-500 comparison excludes one intended model
- OpenRouter/provider-native reasoning behavior can interact with prompt labels, so experimental labeling must stay explicit

## Suggested Immediate Writing Strategy

Best path if we want to start writing now:

1. Treat the current paper as structurally sound but empirically outdated.
2. Decide whether the paper is:
   - still the original paired-100 study, with Large-500 as an extended evaluation
   - or fully migrating to Large-500 as the main empirical core
3. If migrating, update first:
   - `paper/sections/00_abstract.tex`
   - `paper/sections/03_experimental_setup.tex`
   - `paper/sections/04_results.tex`
   - `paper/tables/main_results.tex`
4. Then refresh:
   - `paper/sections/05_analysis_discussion.tex`
   - `paper/tables/account_difficulty.tex`
   - `paper/tables/complexity_factors.tex`

## Recommended Narrative Positioning

The strongest current narrative is:

- The benchmark distinguishes structural recall from exact accounting competence.
- Zero-shot can preserve structure while failing arithmetic catastrophically.
- CoT is not a uniform intervention:
  - DeepSeek: transformational
  - Qwen 3.5: strong and broad
  - Gemini: targeted to difficult cases
- Among completed Large-500 runs, DeepSeek CoT is the only model that is both near-ceiling and difficulty-robust.
