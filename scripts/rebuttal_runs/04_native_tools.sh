#!/usr/bin/env bash
# Native function-calling tool agent vs text-protocol tool agent (R2 point 1),
# compact split. The text-protocol full agent already has anchor-model numbers
# (results/gemini3flash_ablation_coverage); this adds the native-API condition
# on the anchor plus both conditions on GPT-5 and Haiku 4.5.
#
# Est. cost: ~$25-35 (agent loops multiply calls). Requires OPENROUTER_API_KEY.
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY first}"

COMMON=(--dataset data/coverage/records.jsonl --matrix coverage
        --max-records 143 --temperature 0.0 --timeout 1800 --resume --resume-valid-only --checkpoint-every 10
        --agent-max-steps 8)

uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --ablations tool_native_full_tool_agent \
  --model google/gemini-3-flash-preview --max-output-tokens 12000 \
  --output-dir results/rebuttal/native_tools/gemini3flash

uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --ablations tool_full_tool_agent tool_native_full_tool_agent \
  --model anthropic/claude-haiku-4.5 --max-output-tokens 16000 \
  --output-dir results/rebuttal/native_tools/haiku45

# GPT-5 last: most expensive; skip if budget is tight.
uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --ablations tool_full_tool_agent tool_native_full_tool_agent \
  --model openai/gpt-5 --reasoning-effort low --max-output-tokens 32768 \
  --output-dir results/rebuttal/native_tools/gpt5

echo "native-tools runs complete"
