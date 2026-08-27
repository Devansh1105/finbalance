#!/usr/bin/env bash
# Reasoning-and-budget parity runs (R2 point 2), compact 143-record split.
#
# The paper's headline runs give GPT-5 reasoning effort "low" with a 32k budget
# while the other reasoning-capable models run with no reasoning at 8k-16k.
# This controls the confound in both directions:
#   - Haiku 4.5 / Grok-4.3 / Qwen3-235B(thinking) WITH reasoning at 32k
#   - GPT-5 at the "minimal" effort floor with a 16k budget
#
# Est. cost: ~$16-25. Requires OPENROUTER_API_KEY.
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY first}"

COMMON=(--dataset data/coverage/records.jsonl --matrix coverage --ablations prompt_baseline
        --max-records 143 --temperature 0.0 --timeout 1800 --resume --resume-valid-only --checkpoint-every 10)

uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --model anthropic/claude-haiku-4.5 --reasoning-effort low --max-output-tokens 32768 \
  --output-dir results/rebuttal/reasoning_parity/haiku45_reasoning_low_32k

uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --model x-ai/grok-4.3 --reasoning-effort low --max-output-tokens 32768 \
  --output-dir results/rebuttal/reasoning_parity/grok43_reasoning_low_32k

# NOTE: reasoning requires the thinking variant slug for Qwen.
uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --model qwen/qwen3-235b-a22b-thinking-2507 --max-output-tokens 32768 \
  --output-dir results/rebuttal/reasoning_parity/qwen3_235b_thinking_32k

uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --model openai/gpt-5 --reasoning-effort minimal --max-output-tokens 16000 \
  --output-dir results/rebuttal/reasoning_parity/gpt5_minimal_16k

echo "reasoning-parity runs complete"
