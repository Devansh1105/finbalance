#!/usr/bin/env bash
# Anchor-model runs via Vertex AI (bills against the GCP $300 trial credit).
# Same experiments as 07_gemini_free.sh; Vertex's OpenAI-compatible endpoint,
# auth via gcloud access tokens (auto-refreshed by the harness).
#
# Prereqs:
#   ~/google-cloud-sdk/bin/gcloud auth login          (interactive, once)
#   gcloud config set project <PROJECT_ID>
#   gcloud services enable aiplatform.googleapis.com
#   export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
# Optional: export GOOGLE_CLOUD_LOCATION=global  (default)
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${GOOGLE_CLOUD_PROJECT:?set GOOGLE_CLOUD_PROJECT to the trial project id}"
export PATH="$HOME/google-cloud-sdk/bin:$PATH"

MODEL=google/gemini-3-flash-preview   # Vertex openapi endpoint uses the google/ prefix
COMMON=(--backend vertex --model "$MODEL" --max-output-tokens 12000 --reasoning-effort minimal
        --dataset data/coverage/records.jsonl --max-records 143
        --temperature 0.0 --timeout 1800 --resume --resume-valid-only --checkpoint-every 10)

uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --matrix ocr_noise \
  --output-dir results/rebuttal/ocr_noise/gemini3flash_vertex

uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
  --matrix coverage --ablations tool_native_full_tool_agent --agent-max-steps 8 \
  --output-dir results/rebuttal/native_tools/gemini3flash_vertex

for run in 1 2 3; do
  uv run python -m finbalance evaluate-ablations "${COMMON[@]}" \
    --matrix coverage --ablations prompt_baseline \
    --output-dir "results/rebuttal/repeats/gemini3flash_vertex_run${run}"
done

uv run python -m finbalance analyze-ablations \
  --results-dir results/rebuttal/ocr_noise/gemini3flash_vertex --baseline prompt_baseline

echo "vertex anchor runs complete"
