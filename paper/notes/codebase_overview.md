# FinBalance Paper Notes

These notes summarize the repository evidence used for the paper.

- `finbalance/data/generation/generator.py` is the source of truth for the dataset methodology.
- `finbalance/data/generation/templates.py` defines the difficulty ladder and complexity-factor tags.
- `finbalance/evaluation/metrics/core.py` defines BA, ALA, ACR, BEM, CECR, and FBS.
- `finbalance/evaluation/runner.py` explains JSON parsing, parse-fail retry behavior, and saved per-problem outputs.
- `results/leaderboard.json` provides the model table used in the manuscript.
- `results/deep_analysis.json` provides account difficulty, CoT decomposition, factor attribution, and robustness curves.
- `results/significance_tests.json` contains only a subset of pairwise tests, so inferential claims must stay narrow.
