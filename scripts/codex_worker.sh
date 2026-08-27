#!/usr/bin/env bash
# Codex-as-worker: delegate a self-contained grunt task to Codex.
#
# Usage:
#   scripts/codex_worker.sh "task description" [outdir]
#
# Sandbox: workspace-write, but instructed to write ONLY under the given
# output directory (default .codex-out/). Claude reviews and integrates the
# output; Codex never edits tracked files directly.
# Usage telemetry: token/rate-limit events land in .codex-out/last_run.jsonl
# so limits can be checked after each run.
set -euo pipefail
cd "$(dirname "$0")/.."

TASK="${1:?usage: codex_worker.sh \"task\" [outdir]}"
OUTDIR="${2:-.codex-out}"
mkdir -p "$OUTDIR"

codex exec --sandbox workspace-write --json -m gpt-5.6-sol -c model_reasoning_effort=high \
  -o "$OUTDIR/last_message.md" \
  "You are a diligent worker agent on the FinBalance EMNLP rebuttal project.
Complete this task end to end. Write any produced files ONLY inside $OUTDIR/
(never modify tracked repo files). Read whatever repo files you need.
Finish your final message with a short list of files you wrote and any
caveats.

TASK: ${TASK}" > "$OUTDIR/last_run.jsonl"

echo "=== final message ==="
cat "$OUTDIR/last_message.md"
echo
echo "=== usage ==="
grep -o '"type":"turn.completed".*' "$OUTDIR/last_run.jsonl" | tail -1 | head -c 400 || true
