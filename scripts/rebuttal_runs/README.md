# Rebuttal experiment runs

All scripts are resumable (`--resume --checkpoint-every N`): re-running a script
skips completed records, so an interrupted run loses at most one checkpoint.

## No-OpenRouter path (run these first)

| Script | Key needed | What it covers | Cost |
|---|---|---|---|
| `06_deepseek_now.sh` | `DEEPSEEK_API_KEY` | DeepSeek 3x repeats + deepseek-reasoner reasoning data point | ~$2-3 |
| `07_gemini_free.sh` | `GEMINI_API_KEY` (free, aistudio.google.com) | Anchor model: OCR-noise sweep, native tool agent, 3x repeats | ~$0 |

These two fill the highest-value pending slots (OCR-noise for R1, native-tools
anchor + within-family reasoning for R2) with no OpenRouter access. The
remaining scripts below cover GPT-5 / Haiku / Grok / Qwen conditions and need
either `OPENROUTER_API_KEY` or direct provider keys.

## OpenRouter path

Prerequisite: `export OPENROUTER_API_KEY=...`

Run in this order (impact per dollar, cheapest risk first):

| # | Script | Answers | Est. cost |
|---|--------|---------|-----------|
| 1 | `03_ocr_noise.sh` | R1 W2, R2 Q3: graded OCR-noise robustness sweep | ~$4 |
| 2 | `01_reasoning_parity.sh` | R2 W2: reasoning/budget confound control | ~$16-25 |
| 3 | `02_repeats.sh` | R2 W2: run-to-run error bars (3x per model) | ~$33 |
| 4 | `04_native_tools.sh` | R2 W1/Q1: native function-calling vs text-protocol tool agent | ~$25-35 |
| 5 | `05_fresh_seed_panel.sh` | R2 Q2: ranking stability on a fresh-seed 710 split | ~$55 |

Total ≈ $130-150 (fits a $200 top-up with buffer). GPT-5 conditions sit last
inside each script where possible; kill a script early if credit runs low and
the cheaper conditions are already banked.

Existing free results referenced by the rebuttal (no new spend needed):

- Text-protocol tool agent: `results/gemini3flash_ablation_coverage/tool_*`
  (full agent BS_exact 20.0% vs 24.2% no-tools; **zero tool invocations in all
  572 record-runs across the four tool variants**)
- Structural-invariant audit: `results/structural_audit/AUDIT_SUMMARY.md`
  (6,710 records across three samples, 9 invariants, 100% pass)
