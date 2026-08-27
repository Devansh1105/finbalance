#!/usr/bin/env bash
# DeepSeek runs via the DeepSeek platform key (no OpenRouter needed).
#   - 3x repeats of the headline deepseek-chat baseline (error bars, R2 point 3)
#   - deepseek-reasoner on the same split: same family with reasoning at 32k,
#     a clean within-family data point for the reasoning-parity answer (R2 point 2)
#
# Est. cost: ~$2-3. Requires DEEPSEEK_API_KEY.
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${DEEPSEEK_API_KEY:?set DEEPSEEK_API_KEY first}"

COMMON=(--backend deepseek --dataset data/coverage/records.jsonl --matrix coverage
        --ablations prompt_baseline --max-records 143 --temperature 0.0 --timeout 1800
        --resume --resume-valid-only --checkpoint-every 10)

for run in 1 2 3; do
  uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
    --model deepseek-chat --max-output-tokens 8192 \
    --output-dir "results/rebuttal/repeats/deepseek_chat_run${run}"
done

uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --model deepseek-reasoner --max-output-tokens 32768 \
  --output-dir results/rebuttal/reasoning_parity/deepseek_reasoner_32k

echo "deepseek runs complete"
