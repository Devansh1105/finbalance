#!/usr/bin/env bash
# OCR-noise robustness sweep (R1 weakness 2, R2 question 3), compact split,
# anchor model. Baseline + 2%/5%/10% seeded character noise.
#
# Est. cost: ~$4. Requires OPENROUTER_API_KEY.
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY first}"

uv run python -m finbalance evaluate-ablations \
  --dataset data/coverage/records.jsonl --matrix ocr_noise \
  --max-records 143 --temperature 0.0 --timeout 1800 --resume --resume-valid-only --checkpoint-every 10 \
  --model google/gemini-3-flash-preview --max-output-tokens 12000 \
  --output-dir results/rebuttal/ocr_noise/gemini3flash

uv run python -m finbalance analyze-ablations \
  --results-dir results/rebuttal/ocr_noise/gemini3flash --baseline prompt_baseline

echo "ocr-noise sweep complete"
