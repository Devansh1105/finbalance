#!/usr/bin/env bash
# Codex-as-critic: send a work product for adversarial review, read-only.
#
# Usage:
#   scripts/critic.sh <file> [extra context/instructions...]
#   echo "text" | scripts/critic.sh - [instructions...]
#
# Runs `codex exec` in a read-only sandbox from the repo root so the critic
# can open referenced files but cannot modify anything.
set -euo pipefail
cd "$(dirname "$0")/.."

TARGET="${1:?usage: critic.sh <file|-> [instructions]}"
shift || true
EXTRA="${*:-}"

if [[ "$TARGET" == "-" ]]; then
  CONTENT="$(cat)"
  WHAT="the following text"
else
  CONTENT="$(cat "$TARGET")"
  WHAT="the file $TARGET (content inlined below; you may also read related repo files)"
fi

codex exec --sandbox read-only -m gpt-5.6-sol -c model_reasoning_effort=high "You are an adversarial but fair critic reviewing ${WHAT}.
Context: this repo holds FinBalance, an EMNLP ARR submission (multi-document accounting
reconciliation benchmark) currently in the author-response phase. Reviewer scores: 2.0 /
3.5 / 3.5. The goal is maximum credibility with expert reviewers.

Your job: find real problems, not style nits. Specifically:
1. Factual or internal inconsistencies (numbers, claims that contradict each other).
2. Claims a skeptical reviewer could attack or that overreach the evidence.
3. Missing counterarguments we should preempt.
4. Anything that weakens credibility (tone, evasion, unsupported promises).
5. For code/experiment designs: bugs, confounds, or methodological holes.

Rank findings by severity (CRITICAL / MAJOR / MINOR). For each: quote the exact passage,
explain the problem in one or two sentences, and propose a concrete fix. If something is
genuinely strong, say so in one line at the end. Do not rewrite the whole document.

${EXTRA}

=== CONTENT UNDER REVIEW ===
${CONTENT}"
