#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
paper_dir="$repo_root/paper"
output_dir="$repo_root/output/arxiv"
source_archive="$output_dir/finbalance-arxiv-v2-source.tar.gz"
pdf_copy="$output_dir/finbalance-arxiv-v2.pdf"

[[ -f "$paper_dir/main.pdf" && -f "$paper_dir/main.bbl" ]] || {
  echo "Build paper/main.pdf and paper/main.bbl before packaging" >&2
  exit 1
}

mkdir -p "$output_dir"
staging_dir="$(mktemp -d)"
trap 'rm -rf -- "$staging_dir"' EXIT
package_root="$staging_dir/finbalance-arxiv-v2"
mkdir -p "$package_root"

cp "$paper_dir/main.tex" "$package_root/main.tex"
cp "$paper_dir/main.bbl" "$package_root/main.bbl"
cp "$paper_dir/references.bib" "$package_root/references.bib"
cp "$paper_dir/acl.sty" "$package_root/acl.sty"
cp "$paper_dir/acl_natbib.bst" "$package_root/acl_natbib.bst"
cp "$paper_dir/macros.tex" "$package_root/macros.tex"
cp -R "$paper_dir/preamble" "$package_root/preamble"
cp -R "$paper_dir/sections" "$package_root/sections"
cp -R "$paper_dir/tables" "$package_root/tables"
mkdir -p "$package_root/figures"
for figure_name in \
  diag_dataset_packet.pdf \
  diag_generation_inference.pdf \
  fig_dataset_composition.pdf \
  fig_failure_slices.pdf \
  fig_cost_pareto.pdf \
  fig_ablation_deltas.pdf \
  fig_gap_repair_comparison.pdf \
  fig_model_accuracy.pdf \
  fig_results_heatmap.pdf \
  fig_doc_refs_persistence.pdf \
  fig_difficulty_trend.pdf \
  fig_context_stress.pdf; do
  cp "$paper_dir/figures/$figure_name" "$package_root/figures/$figure_name"
done

rm -f -- "$source_archive" "$pdf_copy"
tar --sort=name --mtime='UTC 2026-08-29' --owner=0 --group=0 --numeric-owner \
  -czf "$source_archive" -C "$staging_dir" finbalance-arxiv-v2
cp "$paper_dir/main.pdf" "$pdf_copy"
sha256sum "$source_archive" "$pdf_copy" > "$output_dir/SHA256SUMS"

echo "Built arXiv replacement package in $output_dir"
