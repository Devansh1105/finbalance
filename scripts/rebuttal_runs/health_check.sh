#!/usr/bin/env bash
# Health check for in-flight rebuttal runs. Scans every ablation result dir
# under results/rebuttal/. Exit codes:
#   0 = all discovered runs healthy (some still in progress)
#   1 = PROBLEM: a run looks unhealthy (low parse rate / stalled)
#   2 = all discovered runs complete
set -uo pipefail
cd "$(dirname "$0")/../.."

problem=0
all_done=1
found=0
now=$(date +%s)

while IFS= read -r f; do
  found=1
  dir="${f%/per_record_results.jsonl}"
  target=143
  [[ "$dir" == *main710* ]] && target=710
  n=$(wc -l < "$f")
  ok=$(grep -c '"parse_success": true' "$f" 2>/dev/null || true)
  age=$(( now - $(stat -c %Y "$f") ))
  status="RUNNING"
  if (( n >= target )); then status="DONE"; else all_done=0; fi
  rate="n/a"
  (( n > 0 )) && rate=$(( 100 * ok / n ))
  echo "$status  ${dir#results/rebuttal/}: $n/$target, parse ${rate}%, checkpoint ${age}s old"
  if (( n >= 10 && 100 * ok / n < 80 )); then
    if [[ "$dir" == *native_tools* || "$dir" == *gpt5_minimal* ]]; then
      # Known, measured phenomenon: heavy native tool use can exhaust the
      # output budget and truncate the final JSON. Informational only.
      echo "  (info) low parse rate is expected under native tool use"
    else
      echo "  !! parse rate below 80% -- investigate before burning more credits"
      problem=1
    fi
  fi
  if [[ "$status" == "RUNNING" && "$dir" != *qwen3_thinking* ]] && (( age > 4500 )); then
    echo "  !! checkpoint stale >40min -- run may be stalled"
    problem=1
  fi
done < <(find results/rebuttal -name per_record_results.jsonl 2>/dev/null \
  | grep -v "reasoning_parity/deepseek_reasoner_main710/" \
  | grep -v "reasoning_parity/qwen3_thinking_32k/" \
  | sort)  # monolithic dirs superseded by shards; their partial rows merge later

(( found )) || { echo "no runs found yet"; exit 0; }
(( problem )) && exit 1
(( all_done )) && exit 2
exit 0
