#!/usr/bin/env bash
# Run-to-run variance: 3 independent baseline runs per model (R2 point 3),
# compact 143-record split, identical settings to the headline configuration.
# Reports mean and range of BS_exact / BS_recon per model.
#
# Est. cost: ~$30 for 3x5 runs. Requires OPENROUTER_API_KEY.
# DeepSeek is NOT repeated here: its headline baseline used the DeepSeek
# platform, so routing it through OpenRouter would confound provider changes
# with run-to-run nondeterminism. 06_deepseek_now.sh repeats it on the
# original provider instead.
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY first}"

COMMON=(--dataset data/coverage/records.jsonl --matrix coverage --ablations prompt_baseline
        --max-records 143 --temperature 0.0 --timeout 1800 --resume --resume-valid-only --checkpoint-every 10)

declare -A MODELS=(
  [gemini3flash]="google/gemini-3-flash-preview 12000"
  [gpt5]="openai/gpt-5 32768"
  [haiku45]="anthropic/claude-haiku-4.5 16000"
  [grok43]="x-ai/grok-4.3 16000"
  [qwen3_235b]="qwen/qwen3-235b-a22b-2507 12000"
)
# GPT-5 keeps its headline reasoning effort so repeats measure the same config.
declare -A EFFORT=([gpt5]="low")

for run in 1 2 3; do
  for name in "${!MODELS[@]}"; do
    read -r slug budget <<<"${MODELS[$name]}"
    extra=()
    if [[ -n "${EFFORT[$name]:-}" ]]; then extra+=(--reasoning-effort "${EFFORT[$name]}"); fi
    uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
      --model "$slug" --max-output-tokens "$budget" "${extra[@]}" \
      --output-dir "results/rebuttal/repeats/${name}_run${run}"
  done
done

echo "repeat runs complete"
