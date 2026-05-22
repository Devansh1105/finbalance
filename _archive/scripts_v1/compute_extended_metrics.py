"""
Post-process existing result files to add extended metrics.

Computes ACR, BEM, SPA, PSR, HR, CECR for every problem in every primary
result file (those whose problem IDs are all in data/test.jsonl).

Updates result files in-place (adds new fields, does not change existing ones).
Also writes results/leaderboard.json with a full summary table.

Usage:
    python scripts/compute_extended_metrics.py
    python scripts/compute_extended_metrics.py --results-dir results --dataset data/test.jsonl
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
TOLERANCE_ABS = 10.0
TOLERANCE_PCT = 0.01
RE_KEYS = {"retained earnings", "retained earning"}


def _norm(s: str) -> str:
    return s.lower().strip()


# ---------------------------------------------------------------------------
# JSON parsing (mirrors runner.py logic)
# ---------------------------------------------------------------------------
_JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*([\s\S]*?)```", re.IGNORECASE)
_FINAL_ANSWER_RE = re.compile(r"FINAL ANSWER:\s*(\{[\s\S]*\})", re.IGNORECASE)
_TRAILING_COMMA_RE = re.compile(r",\s*([}\]])")


def _clean_json(s: str) -> str:
    s = re.sub(r'(-?\d{1,3}(?:,\d{3})+)', lambda m: m.group(0).replace(',', ''), s)
    s = _TRAILING_COMMA_RE.sub(r"\1", s)
    s = re.sub(r"\bNone\b", "null", s)
    s = re.sub(r"\bTrue\b", "true", s)
    s = re.sub(r"\bFalse\b", "false", s)
    return s


def _try_parse(s: str):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        pass
    try:
        return json.loads(_clean_json(s))
    except json.JSONDecodeError:
        return None


def _looks_like_bs(d: dict) -> bool:
    return bool({"assets", "liabilities", "equity"} & set(d.keys()))


def parse_response(raw: str):
    if not raw:
        return None
    for m in sorted(_JSON_BLOCK_RE.finditer(raw), key=lambda x: len(x.group(1)), reverse=True):
        r = _try_parse(m.group(1).strip())
        if r is not None and _looks_like_bs(r):
            return r
    for m in _JSON_BLOCK_RE.finditer(raw):
        r = _try_parse(m.group(1).strip())
        if r is not None:
            return r
    m = _FINAL_ANSWER_RE.search(raw)
    if m:
        r = _try_parse(m.group(1).strip())
        if r is not None:
            return r
    candidates, start = [], 0
    while True:
        idx = raw.find("{", start)
        if idx == -1:
            break
        depth, end = 0, -1
        for i, ch in enumerate(raw[idx:], idx):
            depth += (ch == "{") - (ch == "}")
            if depth == 0:
                end = i
                break
        if end == -1:
            break
        candidates.append(raw[idx:end + 1])
        start = end + 1
    for cand in sorted(candidates, key=len, reverse=True):
        r = _try_parse(cand)
        if r is not None and _looks_like_bs(r):
            return r
    for cand in sorted(candidates, key=len, reverse=True):
        r = _try_parse(cand)
        if r is not None:
            return r
    return _try_parse(raw.strip())


# ---------------------------------------------------------------------------
# Extended metric helpers
# ---------------------------------------------------------------------------

def _flat_expected(expected: dict) -> dict:
    flat = {}
    for section in ("assets", "liabilities", "equity"):
        for acc, val in expected.get(section, {}).items():
            if abs(float(val)) > 0.01:
                flat[acc] = float(val)
    return flat


def _section_map(expected: dict) -> dict[str, str]:
    sm = {}
    for section in ("assets", "liabilities", "equity"):
        for acc in expected.get(section, {}):
            sm[_norm(acc)] = section
    return sm


def compute_acr(predicted, expected: dict) -> float:
    if not predicted:
        return 0.0
    expected_flat = _flat_expected(expected)
    if not expected_flat:
        return 1.0
    expected_lower = {_norm(k) for k in expected_flat}
    pred_lower = set()
    for section in ("assets", "liabilities", "equity"):
        for acc in predicted.get(section, {}):
            pred_lower.add(_norm(acc))
    return round(len(pred_lower & expected_lower) / len(expected_lower), 4)


def compute_bem(result: dict) -> float:
    a = float(result.get("assets_predicted") or 0)
    l_ = float(result.get("liabilities_predicted") or 0)
    e = float(result.get("equity_predicted") or 0)
    return round(abs(a - (l_ + e)), 2)


def compute_spa(predicted, expected: dict):
    if not predicted:
        return None
    sm = _section_map(expected)
    total, correct = 0, 0
    for section in ("assets", "liabilities", "equity"):
        for acc in predicted.get(section, {}):
            total += 1
            if sm.get(_norm(acc)) == section:
                correct += 1
    return round(correct / total, 4) if total > 0 else None


def compute_psr(result: dict) -> int:
    return 1 if float(result.get("FBS") or 0) >= 100.0 else 0


def compute_hr(predicted, expected: dict):
    if not predicted:
        return None
    expected_lower = {_norm(k) for k in _flat_expected(expected)}
    pred = [_norm(acc)
            for section in ("assets", "liabilities", "equity")
            for acc in predicted.get(section, {})]
    if not pred:
        return 0.0
    return round(sum(1 for a in pred if a not in expected_lower) / len(pred), 4)


def compute_cecr(predicted, expected: dict) -> int:
    if not predicted:
        return 0
    re_expected = None
    for acc, val in expected.get("equity", {}).items():
        if _norm(acc) in RE_KEYS:
            re_expected = float(val)
            break
    if re_expected is None:
        return 1  # RE not required
    re_predicted = None
    for acc, val in predicted.get("equity", {}).items():
        if _norm(acc) in RE_KEYS and isinstance(val, (int, float)):
            re_predicted = float(val)
            break
    if re_predicted is None:
        return 0
    tol = max(TOLERANCE_ABS, abs(re_expected) * TOLERANCE_PCT)
    return 1 if abs(re_predicted - re_expected) <= tol else 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_ground_truth(path: Path) -> dict:
    gt = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                d = json.loads(line)
                gt[d["problem_id"]] = d
    return gt


def is_primary_file(data: list, test_ids: set) -> bool:
    if not data or not isinstance(data, list):
        return False
    ids = {r.get("problem_id") for r in data if isinstance(r, dict)}
    return len(ids & test_ids) == len(ids) and len(ids) > 0


def process_file(path: Path, gt: dict) -> tuple[list, dict]:
    """Returns (updated_results, summary_stats)."""
    with open(path) as f:
        results = json.load(f)

    extended = []
    for r in results:
        pid = r.get("problem_id")
        problem_gt = gt.get(pid)
        if not problem_gt:
            extended.append(r)
            continue

        raw = r.get("raw_response", "")
        predicted = parse_response(raw) if raw else None

        if predicted is None or r.get("parse_failed") or r.get("parse_error"):
            r.update(ACR=0.0, BEM=compute_bem(r), SPA=None, PSR=0, HR=None, CECR=0)
        else:
            expected = problem_gt["expected"]
            r.update(
                ACR=compute_acr(predicted, expected),
                BEM=compute_bem(r),
                SPA=compute_spa(predicted, expected),
                PSR=compute_psr(r),
                HR=compute_hr(predicted, expected),
                CECR=compute_cecr(predicted, expected),
            )
        extended.append(r)

    # Compute summary stats
    n = len(extended)
    valid = [r for r in extended if not r.get("parse_failed") and not r.get("parse_error")]
    nv = len(valid) or 1

    def mean(key, lst=extended):
        vals = [v for r in lst if (v := r.get(key)) is not None]
        return round(sum(vals) / len(vals), 4) if vals else None

    summary = {
        "file": path.name,
        "model_id": extended[0].get("model_id", "unknown") if extended else "unknown",
        "strategy": extended[0].get("strategy", "unknown") if extended else "unknown",
        "n": n,
        "BA":   round(sum(r.get("BA", 0) for r in extended) / n * 100, 1),
        "ALA":  round(sum(r.get("ALA", 0) for r in extended) / n, 3),
        "FBS":  round(sum(r.get("FBS", 0) for r in extended) / n, 2),
        "ACR":  mean("ACR"),
        "BEM":  round(sum(r.get("BEM", 0) for r in extended) / n, 1),
        "SPA":  mean("SPA"),
        "PSR":  round(sum(r.get("PSR", 0) for r in extended) / n * 100, 1),
        "HR":   mean("HR"),
        "CECR": round(sum(r.get("CECR", 0) for r in extended) / n * 100, 1),
        "parse_fail_rate": round(sum(1 for r in extended if r.get("parse_failed") or r.get("parse_error")) / n * 100, 1),
        "by_level": {},
    }

    by_level = defaultdict(list)
    for r in extended:
        by_level[r.get("difficulty", r.get("difficulty_level"))].append(r)
    for lvl in sorted(by_level):
        lvl_r = by_level[lvl]
        nl = len(lvl_r)
        summary["by_level"][str(lvl)] = {
            "n":   nl,
            "BA":  round(sum(r.get("BA", 0) for r in lvl_r) / nl * 100, 1),
            "ALA": round(sum(r.get("ALA", 0) for r in lvl_r) / nl, 3),
            "FBS": round(sum(r.get("FBS", 0) for r in lvl_r) / nl, 2),
            "ACR": mean("ACR", lvl_r),
            "BEM": round(sum(r.get("BEM", 0) for r in lvl_r) / nl, 1),
            "PSR": round(sum(r.get("PSR", 0) for r in lvl_r) / nl * 100, 1),
            "CECR": round(sum(r.get("CECR", 0) for r in lvl_r) / nl * 100, 1),
        }

    return extended, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results-dir", default="results")
    ap.add_argument("--dataset", default="data/test.jsonl")
    ap.add_argument("--dry-run", action="store_true", help="Print stats but don't write files")
    args = ap.parse_args()

    results_dir = Path(args.results_dir)
    gt = load_ground_truth(Path(args.dataset))
    test_ids = set(gt.keys())

    skip_patterns = {"failure_analysis", "propagation", "leaderboard"}
    all_summaries = []

    for path in sorted(results_dir.glob("*.json")):
        if any(p in path.name for p in skip_patterns):
            continue
        try:
            with open(path) as f:
                data = json.load(f)
        except Exception:
            continue

        if not is_primary_file(data, test_ids):
            continue

        print(f"Processing {path.name} ...", end=" ", flush=True)
        updated, summary = process_file(path, gt)
        all_summaries.append(summary)

        if not args.dry_run:
            with open(path, "w") as f:
                json.dump(updated, f, indent=2)
        print(f"BA={summary['BA']}%  ACR={summary['ACR']}  BEM={summary['BEM']}  PSR={summary['PSR']}%  CECR={summary['CECR']}%")

    # Sort leaderboard by FBS descending
    all_summaries.sort(key=lambda x: x["FBS"], reverse=True)

    leaderboard_path = results_dir / "leaderboard.json"
    if not args.dry_run:
        with open(leaderboard_path, "w") as f:
            json.dump(all_summaries, f, indent=2)
        print(f"\nLeaderboard written to {leaderboard_path}")

    # Print table
    print("\n=== LEADERBOARD ===")
    print(f"{'Model':<45} {'Strat':<10} {'BA':>6} {'ALA':>6} {'ACR':>6} {'BEM':>8} {'FBS':>6} {'PSR':>6} {'CECR':>6} {'HR':>6}")
    print("-" * 115)
    for s in all_summaries:
        model = s["model_id"].replace("openai/", "").replace("google/", "").replace("meta-llama/", "")
        hr = f"{s['HR']*100:.1f}%" if s.get("HR") is not None else "  N/A"
        acr = f"{s['ACR']*100:.1f}%" if s.get("ACR") is not None else "  N/A"
        spa = f"{s['SPA']*100:.1f}%" if s.get("SPA") is not None else "  N/A"
        print(f"{model:<45} {s['strategy']:<10} {s['BA']:>5}% {s['ALA']:>6.3f} {acr:>6} {s['BEM']:>8.0f} {s['FBS']:>6.1f} {s['PSR']:>5}% {s['CECR']:>5}% {hr:>6}")


if __name__ == "__main__":
    main()
