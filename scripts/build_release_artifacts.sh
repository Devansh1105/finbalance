#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_dir="$repo_root/output/release"
run_list="$repo_root/release/PAPER_RUNS.txt"
results_archive="$output_dir/finbalance-paper-results-v1.tar.zst"
dataset_archive="$output_dir/finbalance-main-dataset-v1.tar.zst"
checksum_file="$output_dir/SHA256SUMS"
manifest_file="$output_dir/RELEASE_MANIFEST.txt"

for command_name in jq tar zstd sha256sum; do
  command -v "$command_name" >/dev/null || {
    echo "Missing required command: $command_name" >&2
    exit 1
  }
done

[[ -f "$run_list" ]] || {
  echo "Missing run allowlist: $run_list" >&2
  exit 1
}

[[ -f "$repo_root/data/main/records.jsonl" ]] || {
  echo "Missing frozen core split: data/main/records.jsonl" >&2
  exit 1
}

mkdir -p "$output_dir"
staging_dir="$(mktemp -d)"
trap 'rm -rf -- "$staging_dir"' EXIT

results_root="$staging_dir/finbalance-paper-results-v1"
dataset_root="$staging_dir/finbalance-main-dataset-v1"
mkdir -p "$results_root" "$dataset_root/data"

cp "$repo_root/release/README.md" "$results_root/README.md"
cp "$run_list" "$results_root/PAPER_RUNS.txt"
cp "$repo_root/DATA_LICENSE.md" "$results_root/DATA_LICENSE.md"

while IFS= read -r run_dir; do
  [[ -z "$run_dir" || "$run_dir" == \#* ]] && continue
  source_dir="$repo_root/$run_dir"
  destination_dir="$results_root/$run_dir"

  [[ -f "$source_dir/summary.json" && -f "$source_dir/per_record_results.jsonl" ]] || {
    echo "Incomplete allowlisted run: $run_dir" >&2
    exit 1
  }

  mkdir -p "$destination_dir"
  cp "$source_dir/summary.json" "$destination_dir/summary.json"
  jq -c 'del(.raw_provider_payload)' \
    "$source_dir/per_record_results.jsonl" \
    > "$destination_dir/per_record_results.jsonl"

  if [[ -d "$source_dir/slice_tables" ]]; then
    cp -R "$source_dir/slice_tables" "$destination_dir/slice_tables"
  fi
done < "$run_list"

if [[ -d "$repo_root/results/structural_audit" ]]; then
  mkdir -p "$results_root/results"
  cp -R "$repo_root/results/structural_audit" "$results_root/results/structural_audit"
fi

cp -R "$repo_root/data/main" "$dataset_root/data/main"
cp "$repo_root/data/README.md" "$dataset_root/data/README.md"
cp "$repo_root/DATA_LICENSE.md" "$dataset_root/DATA_LICENSE.md"

(
  cd "$results_root"
  find . -type f -print0 | sort -z | xargs -0 sha256sum > FILES_SHA256SUMS
)
(
  cd "$dataset_root"
  find . -type f -print0 | sort -z | xargs -0 sha256sum > FILES_SHA256SUMS
)

rm -f -- "$results_archive" "$dataset_archive" "$checksum_file" "$manifest_file"
tar --sort=name --mtime='UTC 2026-08-29' --owner=0 --group=0 --numeric-owner \
  -I 'zstd -19 -T0' -cf "$results_archive" -C "$staging_dir" \
  finbalance-paper-results-v1
tar --sort=name --mtime='UTC 2026-08-29' --owner=0 --group=0 --numeric-owner \
  -I 'zstd -19 -T0' -cf "$dataset_archive" -C "$staging_dir" \
  finbalance-main-dataset-v1

(
  cd "$output_dir"
  sha256sum "$(basename "$dataset_archive")" "$(basename "$results_archive")" \
    > "$(basename "$checksum_file")"
  {
    echo "FinBalance EMNLP 2026 camera-ready release"
    echo "Built: 2026-08-29"
    echo
    du -h "$(basename "$dataset_archive")" "$(basename "$results_archive")"
    echo
    cat "$(basename "$checksum_file")"
  } > "$(basename "$manifest_file")"
)

echo "Built release archives in $output_dir"
