#!/usr/bin/env python3
"""
Deep analysis for ACL paper -- FinBalance benchmark.

Five analyses computed entirely from existing result files (no re-evaluation):
  1. Complexity Factor Attribution (CFA) -- which accounting operations cause failures
  2. Account Difficulty Index -- which accounts are hardest to predict
  3. CoT Benefit Decomposition -- parse recovery vs reasoning vs structure
  4. Section-Level Error Asymmetry -- which balance sheet section fails first
  5. Difficulty Scaling Curves -- degradation rate + cliff detection

Usage:
    python scripts/deep_analysis.py
    python scripts/deep_analysis.py --results-dir results --dataset data/test.jsonl
"""

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ============================================================================
# JSON parsing (mirrors runner.py / compute_extended_metrics.py)
# ============================================================================
_JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*([\s\S]*?)```", re.IGNORECASE)
_FINAL_ANSWER_RE = re.compile(r"FINAL ANSWER:\s*(\{[\s\S]*\})", re.IGNORECASE)
_TRAILING_COMMA_RE = re.compile(r",\s*([}\]])")


def _clean_json(s):
    s = re.sub(r'(-?\d{1,3}(?:,\d{3})+)', lambda m: m.group(0).replace(',', ''), s)
    s = _TRAILING_COMMA_RE.sub(r"\1", s)
    s = re.sub(r"\bNone\b", "null", s)
    s = re.sub(r"\bTrue\b", "true", s)
    s = re.sub(r"\bFalse\b", "false", s)
    return s


def _try_parse(s):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        pass
    try:
        return json.loads(_clean_json(s))
    except json.JSONDecodeError:
        return None


def _looks_like_bs(d):
    return isinstance(d, dict) and bool({"assets", "liabilities", "equity"} & set(d.keys()))


def parse_response(raw):
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


# ============================================================================
# Helpers
# ============================================================================
def _norm(s):
    return s.lower().strip()


def _flat_expected(expected):
    flat = {}
    for sec in ("assets", "liabilities", "equity"):
        for acc, val in expected.get(sec, {}).items():
            if abs(float(val)) > 0.01:
                flat[acc] = float(val)
    return flat


def _flat_predicted(predicted):
    if not predicted:
        return {}
    flat = {}
    for sec in ("assets", "liabilities", "equity"):
        for acc, val in predicted.get(sec, {}).items():
            if isinstance(val, (int, float)):
                flat[acc] = float(val)
    return flat


EPSILON = 1.0
TOL_ABS = 10.0
TOL_PCT = 0.01


def _within_tolerance(pred_val, exp_val):
    tol = max(TOL_ABS, abs(exp_val) * TOL_PCT)
    return abs(pred_val - exp_val) <= tol


def _mean(lst):
    return sum(lst) / len(lst) if lst else 0.0


def _std(lst):
    if len(lst) < 2:
        return 0.0
    m = _mean(lst)
    return (sum((x - m) ** 2 for x in lst) / len(lst)) ** 0.5


def _median(lst):
    if not lst:
        return 0.0
    s = sorted(lst)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def _short_name(key):
    """Shorten 'openai/gpt-5.2 (cot)' -> 'gpt-5.2 (cot)'."""
    for prefix in ("openai/", "google/", "meta-llama/", "qwen/"):
        key = key.replace(prefix, "")
    return key


# ============================================================================
# Data loading
# ============================================================================
def load_ground_truth(path):
    gt = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                d = json.loads(line)
                gt[d["problem_id"]] = d
    return gt


def load_result_files(results_dir, test_ids):
    skip = {"failure_analysis", "propagation", "leaderboard", "baseline",
            "significance", "deep_analysis"}
    all_results = []
    for path in sorted(Path(results_dir).glob("*.json")):
        if any(p in path.name for p in skip):
            continue
        try:
            with open(path) as f:
                data = json.load(f)
        except Exception:
            continue
        if not isinstance(data, list) or not data:
            continue
        ids = {r.get("problem_id") for r in data if isinstance(r, dict)}
        if not (ids <= test_ids and len(ids) > 0):
            continue
        model_id = data[0].get("model_id", "unknown")
        strategy = data[0].get("strategy", "unknown")
        all_results.append((model_id, strategy, data))
        print(f"  Loaded {path.name}: {model_id} / {strategy} ({len(data)} problems)")
    return all_results


# ============================================================================
# Analysis 1: Complexity Factor Attribution (CFA)
# ============================================================================
def analyze_cfa(all_results, gt):
    """
    For each complexity factor x model x strategy, compute:
      - Raw DFBS:  mean_FBS(with factor) - mean_FBS(without factor)
      - Controlled DFBS: same but stratified by difficulty level to remove confounding
    """
    # Extract factors per problem and difficulty
    problem_factors = {}
    problem_difficulty = {}
    all_factors = set()
    for pid, prob in gt.items():
        factors = set()
        for tx in prob.get("transactions", []):
            factors.update(tx.get("complexity_factors", []))
        problem_factors[pid] = factors
        problem_difficulty[pid] = prob.get("difficulty_level", 0)
        all_factors.update(factors)

    results = {}
    for model_id, strategy, result_list in all_results:
        key = f"{model_id} ({strategy})"
        factor_data = {}

        pid_to_fbs = {r["problem_id"]: r.get("FBS", 0) for r in result_list}
        pid_to_ala = {r["problem_id"]: r.get("ALA", 0) for r in result_list}
        pid_to_ba = {r["problem_id"]: r.get("BA", 0) for r in result_list}

        for factor in sorted(all_factors):
            with_fbs, without_fbs = [], []
            with_ala, without_ala = [], []

            for pid in pid_to_fbs:
                if pid not in problem_factors:
                    continue
                if factor in problem_factors[pid]:
                    with_fbs.append(pid_to_fbs[pid])
                    with_ala.append(pid_to_ala[pid])
                else:
                    without_fbs.append(pid_to_fbs[pid])
                    without_ala.append(pid_to_ala[pid])

            if len(with_fbs) < 3 or len(without_fbs) < 3:
                continue

            raw_delta_fbs = _mean(with_fbs) - _mean(without_fbs)
            raw_delta_ala = _mean(with_ala) - _mean(without_ala)

            # Difficulty-controlled DFBS: stratify by level, average within-level deltas
            level_deltas = []
            for lvl in range(1, 6):
                w = [pid_to_fbs[pid] for pid in pid_to_fbs
                     if pid in problem_factors and factor in problem_factors[pid]
                     and problem_difficulty.get(pid) == lvl]
                wo = [pid_to_fbs[pid] for pid in pid_to_fbs
                      if pid in problem_factors and factor not in problem_factors[pid]
                      and problem_difficulty.get(pid) == lvl]
                if len(w) >= 2 and len(wo) >= 2:
                    level_deltas.append(_mean(w) - _mean(wo))

            controlled_delta = _mean(level_deltas) if level_deltas else None

            factor_data[factor] = {
                "n_with": len(with_fbs),
                "n_without": len(without_fbs),
                "fbs_with": round(_mean(with_fbs), 2),
                "fbs_without": round(_mean(without_fbs), 2),
                "delta_fbs_raw": round(raw_delta_fbs, 2),
                "delta_ala_raw": round(raw_delta_ala, 4),
                "delta_fbs_controlled": round(controlled_delta, 2) if controlled_delta is not None else None,
            }

        results[key] = factor_data

    return {"factors": sorted(all_factors), "by_model": results}


# ============================================================================
# Analysis 2: Account Difficulty Index
# ============================================================================
def analyze_account_difficulty(all_results, gt):
    """Per-account omission / arithmetic / hallucination rates across all models."""

    account_stats = defaultdict(lambda: {
        "n_expected": 0, "n_omitted": 0, "n_arithmetic": 0,
        "n_correct": 0, "n_hallucinated": 0, "abs_errors": [],
        "account_type": "unknown",
    })

    per_model_stats = defaultdict(lambda: defaultdict(lambda: {
        "n_expected": 0, "n_omitted": 0, "n_arithmetic": 0, "n_correct": 0,
    }))

    # Track n_not_expected for hallucination rate denominator
    n_models_evaluated = 0

    for model_id, strategy, result_list in all_results:
        model_key = f"{model_id} ({strategy})"
        n_models_evaluated += 1

        for r in result_list:
            pid = r.get("problem_id")
            if pid not in gt:
                continue

            raw = r.get("raw_response", "")
            predicted = parse_response(raw) if raw else None
            if predicted is None:
                continue

            expected = gt[pid]["expected"]
            exp_flat = _flat_expected(expected)
            pred_flat = _flat_predicted(predicted)
            pred_norms = {_norm(k): k for k in pred_flat}
            exp_norms = {_norm(k) for k in exp_flat}

            # Check expected accounts
            for acc, exp_val in exp_flat.items():
                s = account_stats[acc]
                s["n_expected"] += 1
                # Infer account type from ground truth section
                for sec_name, sec_key in [("assets", "asset"), ("liabilities", "liability"), ("equity", "equity")]:
                    if acc in expected.get(sec_name, {}):
                        s["account_type"] = sec_key
                        break

                per_model_stats[model_key][acc]["n_expected"] += 1

                pred_val = pred_flat.get(acc)
                if pred_val is None:
                    norm_match = pred_norms.get(_norm(acc))
                    if norm_match:
                        pred_val = pred_flat[norm_match]

                if pred_val is None:
                    s["n_omitted"] += 1
                    per_model_stats[model_key][acc]["n_omitted"] += 1
                elif _within_tolerance(pred_val, exp_val):
                    s["n_correct"] += 1
                    per_model_stats[model_key][acc]["n_correct"] += 1
                else:
                    s["n_arithmetic"] += 1
                    s["abs_errors"].append(abs(pred_val - exp_val))
                    per_model_stats[model_key][acc]["n_arithmetic"] += 1

            # Hallucinations
            for pred_acc in pred_flat:
                if _norm(pred_acc) not in exp_norms:
                    account_stats[pred_acc]["n_hallucinated"] += 1

    # Compute rates and difficulty score
    account_index = []
    for acc, stats in account_stats.items():
        if stats["n_expected"] < 10:  # need sufficient sample
            # Still include if frequently hallucinated
            if stats["n_hallucinated"] >= 5:
                account_index.append({
                    "account": acc,
                    "account_type": stats["account_type"],
                    "n_expected": stats["n_expected"],
                    "omission_rate": 0,
                    "arithmetic_rate": 0,
                    "correct_rate": 0,
                    "n_hallucinated": stats["n_hallucinated"],
                    "avg_abs_error": 0,
                    "difficulty_score": 0,
                })
            continue

        om = stats["n_omitted"] / stats["n_expected"]
        ar = stats["n_arithmetic"] / stats["n_expected"]
        co = stats["n_correct"] / stats["n_expected"]
        avg_err = _mean(stats["abs_errors"]) if stats["abs_errors"] else 0
        # Difficulty = weighted combo: omission is worst, arithmetic next
        difficulty = om * 0.6 + ar * 0.4

        account_index.append({
            "account": acc,
            "account_type": stats["account_type"],
            "n_expected": stats["n_expected"],
            "omission_rate": round(om, 4),
            "arithmetic_rate": round(ar, 4),
            "correct_rate": round(co, 4),
            "n_hallucinated": stats["n_hallucinated"],
            "avg_abs_error": round(avg_err, 2),
            "difficulty_score": round(difficulty, 4),
        })

    account_index.sort(key=lambda x: -x["difficulty_score"])

    # Per-model top hardest accounts
    per_model_hardest = {}
    for model_key, model_stats in per_model_stats.items():
        model_accs = []
        for acc, s in model_stats.items():
            if s["n_expected"] >= 3:
                om = s["n_omitted"] / s["n_expected"]
                ar = s["n_arithmetic"] / s["n_expected"]
                model_accs.append({
                    "account": acc,
                    "omission_rate": round(om, 4),
                    "arithmetic_rate": round(ar, 4),
                    "error_rate": round(om + ar, 4),
                })
        model_accs.sort(key=lambda x: -x["error_rate"])
        per_model_hardest[model_key] = model_accs[:10]

    return {"global_index": account_index, "per_model_hardest": per_model_hardest}


# ============================================================================
# Analysis 3: CoT Benefit Decomposition
# ============================================================================
def analyze_cot_decomposition(all_results, gt):
    """Decompose CoT FBS gain into: parse recovery, omission reduction,
    arithmetic improvement, hallucination change, CECR change."""

    # Group: model_id -> strategy -> {pid: result}
    model_results = defaultdict(lambda: defaultdict(dict))
    for model_id, strategy, result_list in all_results:
        for r in result_list:
            model_results[model_id][strategy][r["problem_id"]] = r

    decompositions = {}

    for model_id in model_results:
        strats = model_results[model_id]
        if "zero_shot" not in strats or "cot" not in strats:
            continue

        zs_map = strats["zero_shot"]
        cot_map = strats["cot"]
        common = set(zs_map) & set(cot_map) & set(gt)

        parse_fix = 0      # ZS parse fail -> CoT success
        parse_break = 0    # ZS success -> CoT parse fail
        fbs_d, ala_d, ba_d = [], [], []
        omit_d, arith_d, halluc_d, cecr_d = [], [], [], []

        for pid in common:
            zs, cot = zs_map[pid], cot_map[pid]

            zs_fail = zs.get("parse_failed") or zs.get("parse_error")
            cot_fail = cot.get("parse_failed") or cot.get("parse_error")
            if zs_fail and not cot_fail:
                parse_fix += 1
            elif not zs_fail and cot_fail:
                parse_break += 1

            fbs_d.append(cot.get("FBS", 0) - zs.get("FBS", 0))
            ala_d.append(cot.get("ALA", 0) - zs.get("ALA", 0))
            ba_d.append(cot.get("BA", 0) - zs.get("BA", 0))

            zs_e = zs.get("error_categories", {})
            cot_e = cot.get("error_categories", {})
            omit_d.append(cot_e.get("OE", 0) - zs_e.get("OE", 0))
            arith_d.append(cot_e.get("AE", 0) - zs_e.get("AE", 0))
            halluc_d.append(cot_e.get("CO", 0) - zs_e.get("CO", 0))
            cecr_d.append((cot.get("CECR", 0) or 0) - (zs.get("CECR", 0) or 0))

        n = len(common)
        improved = sum(1 for d in fbs_d if d > 0.5)
        degraded = sum(1 for d in fbs_d if d < -0.5)

        # Per-difficulty breakdown
        by_diff = defaultdict(list)
        for pid in common:
            d = zs_map[pid].get("difficulty", 0)
            by_diff[d].append(cot_map[pid].get("FBS", 0) - zs_map[pid].get("FBS", 0))

        decompositions[model_id] = {
            "n_problems": n,
            "mean_delta_fbs": round(_mean(fbs_d), 2),
            "std_delta_fbs": round(_std(fbs_d), 2),
            "mean_delta_ala": round(_mean(ala_d), 4),
            "mean_delta_ba": round(_mean(ba_d), 4),
            "parse_improvements": parse_fix,
            "parse_regressions": parse_break,
            "mean_delta_omissions": round(_mean(omit_d), 3),
            "mean_delta_arithmetic": round(_mean(arith_d), 3),
            "mean_delta_hallucinations": round(_mean(halluc_d), 3),
            "mean_delta_cecr": round(_mean(cecr_d), 3),
            "problems_improved": improved,
            "problems_degraded": degraded,
            "problems_unchanged": n - improved - degraded,
            "by_difficulty": {
                str(lvl): {
                    "n": len(deltas),
                    "mean_delta_fbs": round(_mean(deltas), 2),
                    "std": round(_std(deltas), 2),
                    "improved": sum(1 for d in deltas if d > 0.5),
                    "degraded": sum(1 for d in deltas if d < -0.5),
                }
                for lvl, deltas in sorted(by_diff.items())
            },
        }

    return decompositions


# ============================================================================
# Analysis 4: Section-Level Error Asymmetry
# ============================================================================
def analyze_section_errors(all_results, gt):
    """Per-section |predicted_total - expected_total| and relative error."""

    results = {}

    for model_id, strategy, result_list in all_results:
        key = f"{model_id} ({strategy})"
        sec_abs = {"assets": [], "liabilities": [], "equity": []}
        sec_rel = {"assets": [], "liabilities": [], "equity": []}
        by_level = defaultdict(lambda: {"assets": [], "liabilities": [], "equity": []})

        for r in result_list:
            pid = r.get("problem_id")
            if pid not in gt:
                continue

            raw = r.get("raw_response", "")
            predicted = parse_response(raw) if raw else None
            if predicted is None:
                continue

            expected = gt[pid]["expected"]
            difficulty = r.get("difficulty", gt[pid].get("difficulty_level", 0))

            for sec in ("assets", "liabilities", "equity"):
                pred_vals = predicted.get(sec, {})
                pred_total = sum(float(v) for v in pred_vals.values()
                                 if isinstance(v, (int, float)))
                exp_total = sum(float(v) for v in expected.get(sec, {}).values())

                abs_err = abs(pred_total - exp_total)
                rel_err = abs_err / abs(exp_total) if abs(exp_total) > 0.01 else 0

                sec_abs[sec].append(abs_err)
                sec_rel[sec].append(rel_err)
                by_level[difficulty][sec].append(abs_err)

        results[key] = {
            "overall": {
                sec: {
                    "mean_abs_error": round(_mean(errs), 2),
                    "median_abs_error": round(_median(errs), 2),
                    "mean_relative_error": round(_mean(sec_rel[sec]) * 100, 2),
                    "n": len(errs),
                }
                for sec, errs in sec_abs.items()
            },
            "by_difficulty": {
                str(lvl): {
                    sec: round(_mean(errs), 2)
                    for sec, errs in level_data.items()
                }
                for lvl, level_data in sorted(by_level.items())
            },
        }

    # Compute cross-model "which section is hardest" ranking
    section_ranking = {"assets": [], "liabilities": [], "equity": []}
    for key, data in results.items():
        for sec in ("assets", "liabilities", "equity"):
            section_ranking[sec].append(data["overall"][sec]["mean_abs_error"])

    results["_cross_model_mean"] = {
        sec: round(_mean(vals), 2) for sec, vals in section_ranking.items()
    }

    return results


# ============================================================================
# Analysis 5: Difficulty Scaling Curves
# ============================================================================
def analyze_difficulty_curves(all_results, gt):
    """Per-model FBS/BA/ALA across levels with degradation rate + cliff detection."""

    curves = {}

    for model_id, strategy, result_list in all_results:
        key = f"{model_id} ({strategy})"
        by_level = defaultdict(lambda: {"fbs": [], "ba": [], "ala": [], "mae": []})

        for r in result_list:
            d = r.get("difficulty", 0)
            by_level[d]["fbs"].append(r.get("FBS", 0))
            by_level[d]["ba"].append(r.get("BA", 0))
            by_level[d]["ala"].append(r.get("ALA", 0))
            by_level[d]["mae"].append(r.get("MAE", 0))

        levels = {}
        for lvl in sorted(by_level):
            d = by_level[lvl]
            levels[str(lvl)] = {
                "n": len(d["fbs"]),
                "fbs_mean": round(_mean(d["fbs"]), 2),
                "fbs_std": round(_std(d["fbs"]), 2),
                "ba_pct": round(_mean(d["ba"]) * 100, 1),
                "ala_mean": round(_mean(d["ala"]), 4),
                "mae_mean": round(_mean(d["mae"]), 2),
            }

        # Degradation rate: (L1 - L5) / 4
        l1 = levels.get("1", {}).get("fbs_mean", 0)
        l5 = levels.get("5", {}).get("fbs_mean", 0)
        deg_rate = round((l1 - l5) / 4, 2) if l1 > 0 else 0

        # Cliff detection: largest single-level FBS drop
        lvl_keys = sorted(levels.keys(), key=int)
        max_drop, cliff = 0, None
        for i in range(1, len(lvl_keys)):
            prev = levels[lvl_keys[i - 1]]["fbs_mean"]
            curr = levels[lvl_keys[i]]["fbs_mean"]
            drop = prev - curr
            if drop > max_drop:
                max_drop = drop
                cliff = f"L{lvl_keys[i-1]}->L{lvl_keys[i]}"

        # Robustness score: coefficient of variation across levels
        fbs_vals = [levels[str(l)]["fbs_mean"] for l in range(1, 6) if str(l) in levels]
        cv = round(_std(fbs_vals) / _mean(fbs_vals) * 100, 2) if _mean(fbs_vals) > 0 else 0

        curves[key] = {
            "levels": levels,
            "degradation_rate_per_level": deg_rate,
            "cliff_point": cliff,
            "cliff_magnitude": round(max_drop, 2),
            "l1_fbs": l1,
            "l5_fbs": l5,
            "robustness_cv": cv,
        }

    return curves


# ============================================================================
# Printing
# ============================================================================
def _print_cfa(cfa):
    factors = cfa["factors"]
    models = cfa["by_model"]

    # Build header
    model_keys = list(models.keys())
    shorts = [_short_name(k)[:18] for k in model_keys]

    print(f"\n  Raw DFBS (negative = factor makes it harder):\n")
    print(f"  {'Factor':<22}", end="")
    for s in shorts:
        print(f" {s:>18}", end="")
    print()
    print("  " + "-" * (22 + 19 * len(shorts)))

    for factor in factors:
        print(f"  {factor:<22}", end="")
        for key in model_keys:
            data = models[key].get(factor)
            if data:
                d = data["delta_fbs_raw"]
                print(f" {d:>+17.1f}", end="")
            else:
                print(f" {'N/A':>18}", end="")
        print()

    # Controlled DFBS
    print(f"\n  Difficulty-controlled DFBS:\n")
    print(f"  {'Factor':<22}", end="")
    for s in shorts:
        print(f" {s:>18}", end="")
    print()
    print("  " + "-" * (22 + 19 * len(shorts)))

    for factor in factors:
        print(f"  {factor:<22}", end="")
        for key in model_keys:
            data = models[key].get(factor)
            if data and data.get("delta_fbs_controlled") is not None:
                d = data["delta_fbs_controlled"]
                print(f" {d:>+17.1f}", end="")
            else:
                print(f" {'N/A':>18}", end="")
        print()

    # Most harmful per model
    print(f"\n  Most harmful factor per model:")
    for key in model_keys:
        data = models[key]
        if not data:
            continue
        worst = min(data.items(), key=lambda x: x[1].get("delta_fbs_controlled") or x[1]["delta_fbs_raw"])
        d = worst[1].get("delta_fbs_controlled") or worst[1]["delta_fbs_raw"]
        print(f"    {_short_name(key)}: {worst[0]} (DFBS={d:+.1f})")


def _print_adi(adi):
    print(f"\n  Top 15 hardest accounts (aggregated across all models):\n")
    print(f"  {'#':<4} {'Account':<30} {'Type':<10} {'N':>5} "
          f"{'Omit%':>7} {'Arith%':>8} {'Correct%':>9} {'Halluc':>7} {'DiffScore':>10}")
    print("  " + "-" * 95)
    for i, acc in enumerate(adi["global_index"][:15], 1):
        print(f"  {i:<4} {acc['account']:<30} {acc['account_type']:<10} "
              f"{acc['n_expected']:>5} "
              f"{acc['omission_rate']*100:>6.1f}% {acc['arithmetic_rate']*100:>7.1f}% "
              f"{acc['correct_rate']*100:>8.1f}% {acc['n_hallucinated']:>7} "
              f"{acc['difficulty_score']:>10.3f}")

    # Show which accounts differentiate tiers
    print(f"\n  Per-model hardest accounts (top 5 by error rate):")
    for model_key, accs in adi["per_model_hardest"].items():
        print(f"\n    {_short_name(model_key)}:")
        for acc in accs[:5]:
            print(f"      {acc['account']:<28} omit={acc['omission_rate']*100:>5.1f}%  "
                  f"arith={acc['arithmetic_rate']*100:>5.1f}%  total={acc['error_rate']*100:>5.1f}%")


def _print_cot(cot):
    if not cot:
        print("  No models with both ZS and CoT runs found.")
        return

    print(f"\n  CoT vs Zero-Shot decomposition:\n")
    print(f"  {'Model':<28} {'DFBS':>7} {'DBA':>6} {'DALA':>7} "
          f"{'Parse+':>7} {'DOmit':>7} {'DArith':>7} {'DHalluc':>8} {'DCECR':>7} "
          f"{'Impr':>5} {'Degr':>5}")
    print("  " + "-" * 110)
    for model_id, d in cot.items():
        short = _short_name(model_id)[:25]
        print(f"  {short:<28} {d['mean_delta_fbs']:>+6.1f} {d['mean_delta_ba']:>+5.2f} "
              f"{d['mean_delta_ala']:>+6.3f} {d['parse_improvements']:>7} "
              f"{d['mean_delta_omissions']:>+6.2f} {d['mean_delta_arithmetic']:>+6.2f} "
              f"{d['mean_delta_hallucinations']:>+7.2f} {d['mean_delta_cecr']:>+6.2f} "
              f"{d['problems_improved']:>5} {d['problems_degraded']:>5}")

    print(f"\n  CoT DFBS by difficulty level:")
    for model_id, d in cot.items():
        short = _short_name(model_id)[:25]
        print(f"\n    {short}:")
        for lvl, ld in sorted(d.get("by_difficulty", {}).items()):
            bar_plus = "+" * ld["improved"]
            bar_minus = "-" * ld["degraded"]
            print(f"      L{lvl}: DFBS={ld['mean_delta_fbs']:>+6.1f} (std={ld['std']:>5.1f})  "
                  f"{ld['improved']:>2}+ {ld['degraded']:>2}-  {bar_plus}{bar_minus}")


def _print_section(sec):
    print(f"\n  Mean absolute section error ($):\n")
    print(f"  {'Model':<40} {'Assets':>12} {'Liabilities':>12} {'Equity':>12} {'Hardest':>12}")
    print("  " + "-" * 92)
    for key, data in sec.items():
        if key.startswith("_"):
            continue
        short = _short_name(key)[:37]
        o = data["overall"]
        worst = max(o.items(), key=lambda x: x[1]["mean_abs_error"])
        print(f"  {short:<40} "
              f"${o['assets']['mean_abs_error']:>10,.0f} "
              f"${o['liabilities']['mean_abs_error']:>10,.0f} "
              f"${o['equity']['mean_abs_error']:>10,.0f} "
              f"{worst[0]:>12}")

    xm = sec.get("_cross_model_mean", {})
    if xm:
        print(f"\n  Cross-model mean:")
        print(f"    Assets:      ${xm.get('assets', 0):>10,.0f}")
        print(f"    Liabilities: ${xm.get('liabilities', 0):>10,.0f}")
        print(f"    Equity:      ${xm.get('equity', 0):>10,.0f}")
        worst = max(xm.items(), key=lambda x: x[1])
        print(f"    -> {worst[0].upper()} is the hardest section across all models")


def _print_curves(curves):
    print(f"\n  Difficulty degradation (FBS by level):\n")
    print(f"  {'Model':<40} {'L1':>7} {'L2':>7} {'L3':>7} {'L4':>7} {'L5':>7} "
          f"{'Deg/Lvl':>8} {'Cliff':>12} {'Drop':>6} {'CV%':>6}")
    print("  " + "-" * 120)
    for key, data in sorted(curves.items(), key=lambda x: -x[1]["degradation_rate_per_level"]):
        short = _short_name(key)[:37]
        levels = data["levels"]
        vals = [levels.get(str(i), {}).get("fbs_mean", 0) for i in range(1, 6)]
        print(f"  {short:<40} ", end="")
        for v in vals:
            print(f"{v:>7.1f}", end="")
        print(f" {data['degradation_rate_per_level']:>7.1f}  "
              f"{data.get('cliff_point', 'N/A'):>11} "
              f"{data['cliff_magnitude']:>5.1f} "
              f"{data['robustness_cv']:>5.1f}")

    # Classify models by robustness
    print(f"\n  Robustness classification:")
    for key, data in sorted(curves.items(), key=lambda x: x[1]["robustness_cv"]):
        cv = data["robustness_cv"]
        if cv < 3:
            label = "ROBUST (flat curve)"
        elif cv < 8:
            label = "MODERATE degradation"
        elif cv < 15:
            label = "STEEP degradation"
        else:
            label = "CLIFF (catastrophic at high levels)"
        print(f"    {_short_name(key):<40} CV={cv:>5.1f}%  {label}")


# ============================================================================
# Main
# ============================================================================
def main():
    ap = argparse.ArgumentParser(description="Deep analysis for ACL paper")
    ap.add_argument("--results-dir", default="results")
    ap.add_argument("--dataset", default="data/test.jsonl")
    ap.add_argument("--output", default="results/deep_analysis.json")
    args = ap.parse_args()

    print("Loading ground truth...")
    gt = load_ground_truth(Path(args.dataset))
    print(f"  {len(gt)} problems loaded\n")

    print("Loading result files...")
    all_results = load_result_files(args.results_dir, set(gt.keys()))
    print(f"  {len(all_results)} model x strategy runs loaded")

    # --- Run all analyses ---
    print("\n" + "=" * 70)
    print("  ANALYSIS 1: Complexity Factor Attribution (CFA)")
    print("=" * 70)
    cfa = analyze_cfa(all_results, gt)
    _print_cfa(cfa)

    print("\n" + "=" * 70)
    print("  ANALYSIS 2: Account Difficulty Index")
    print("=" * 70)
    adi = analyze_account_difficulty(all_results, gt)
    _print_adi(adi)

    print("\n" + "=" * 70)
    print("  ANALYSIS 3: CoT Benefit Decomposition")
    print("=" * 70)
    cot_decomp = analyze_cot_decomposition(all_results, gt)
    _print_cot(cot_decomp)

    print("\n" + "=" * 70)
    print("  ANALYSIS 4: Section-Level Error Asymmetry")
    print("=" * 70)
    sec = analyze_section_errors(all_results, gt)
    _print_section(sec)

    print("\n" + "=" * 70)
    print("  ANALYSIS 5: Difficulty Scaling Curves")
    print("=" * 70)
    curves = analyze_difficulty_curves(all_results, gt)
    _print_curves(curves)

    # --- Save ---
    output = {
        "complexity_factor_attribution": cfa,
        "account_difficulty_index": adi,
        "cot_decomposition": cot_decomp,
        "section_error_asymmetry": sec,
        "difficulty_curves": curves,
    }

    out_path = Path(args.output)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n\nFull analysis saved to {out_path}")


if __name__ == "__main__":
    main()
