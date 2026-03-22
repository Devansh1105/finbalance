# Paper Workspace

This directory mirrors the ACL-style paper scaffold used in `llm-audit-bench/paper/`, but is specialized for the `finbalance` benchmark and its saved experiment artifacts.

## Compile

From this directory:

```bash
latexmk -pdf review.tex
```

For the camera-ready style:

```bash
latexmk -pdf final.tex
```

## Layout

- `review.tex` / `final.tex`: ACL entrypoints
- `macros.tex`: paper-wide benchmark and formatting macros
- `preamble/`: packages, metadata, and body includes
- `sections/`: one file per paper section
- `tables/`: standalone LaTeX tables for dataset and result summaries
- `figures/`: TikZ or LaTeX-native figure sources
- `notes/`: repository-grounded writing notes

Repository figures from `../figures/` are included directly in the manuscript so the paper stays synchronized with the saved analysis outputs.
