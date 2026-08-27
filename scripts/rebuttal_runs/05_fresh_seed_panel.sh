#!/usr/bin/env bash
# Fresh-seed second 710-record split + full six-model panel (R2 point 6).
# Demonstrates ranking stability on records no model has seen and shows the
# generator regenerates coverage-preserving splits from a new seed.
#
# Est. cost: ~$55. Requires OPENROUTER_API_KEY.
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY first}"
: "${DEEPSEEK_API_KEY:?set DEEPSEEK_API_KEY too -- the panel is six models incl. DeepSeek on its original provider}"

FRESH_DIR=data/fresh_seed_20260712
if [[ ! -f "$FRESH_DIR/main/records.jsonl" ]]; then
  uv run python -m finbalance generate-standard-datasets \
    --base-dir "$FRESH_DIR" --seed 20260712 \
    --records-per-combo 4 --negative-controls-per-code 10
fi

COMMON=(--dataset "$FRESH_DIR/main/records.jsonl" --matrix coverage --ablations prompt_baseline
        --max-records 710 --temperature 0.0 --timeout 1800 --resume --resume-valid-only --checkpoint-every 25)

declare -A MODELS=(
  [gemini3flash]="google/gemini-3-flash-preview 12000"
  [qwen3_235b]="qwen/qwen3-235b-a22b-2507 12000"
  [haiku45]="anthropic/claude-haiku-4.5 16000"
  [grok43]="x-ai/grok-4.3 16000"
  [gpt5]="openai/gpt-5 32768"
)
declare -A EFFORT=([gpt5]="low")

# DeepSeek keeps its original provider (DeepSeek platform) so the panel
# matches the headline configuration model-for-model.
if true; then
  uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
    --backend deepseek --model deepseek-chat --max-output-tokens 8192 \
    --output-dir results/rebuttal/fresh_seed_panel/deepseek_chat
fi

# Cheap models first so a budget stop still yields usable panel coverage.
for name in gemini3flash qwen3_235b haiku45 grok43 gpt5; do
  read -r slug budget <<<"${MODELS[$name]}"
  extra=()
  if [[ -n "${EFFORT[$name]:-}" ]]; then extra+=(--reasoning-effort "${EFFORT[$name]}"); fi
  uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
    --model "$slug" --max-output-tokens "$budget" "${extra[@]}" \
    --output-dir "results/rebuttal/fresh_seed_panel/${name}"
done

echo "fresh-seed panel complete"
