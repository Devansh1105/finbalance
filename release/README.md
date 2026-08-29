# FinBalance release archives

Run `bash scripts/build_release_artifacts.sh` from the repository root to build
the two camera-ready release archives in `output/release/`:

- `finbalance-main-dataset-v1.tar.zst`: the frozen 710-record core split,
  including OCR text, labels, manifests, and rendered documents.
- `finbalance-paper-results-v1.tar.zst`: completed model runs used in the paper,
  response-period diagnostics reported in the appendix, and structural-audit
  outputs.

`PAPER_RUNS.txt` is the allowlist for the results archive. Intermediate shards,
scratch directories, incomplete runs, and duplicate `evaluation.json` files are
excluded. Each retained `per_record_results.jsonl` contains the raw model response,
parsed answer, metrics, timing, usage, cost, and diagnostic fields. The opaque
`raw_provider_payload` object is removed because it is redundant for scoring and
can contain provider-internal reasoning blobs. No model call is rerun.

The script writes SHA-256 checksums and a file manifest alongside the archives.
The code, tests, compact coverage split, human-verification materials, paper
source, and licenses remain versioned directly in the repository.
