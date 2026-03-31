"""
Evaluation runner: orchestrates model → prompt → parse → metrics → errors.
"""

import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from threading import Lock
from typing import Optional

from finbalance.analysis.error_detection import ErrorReport, detect_errors
from finbalance.data.schemas import Problem
from finbalance.evaluation.metrics.core import ProblemMetrics, evaluate_problem
from finbalance.evaluation.models.base import BaseModel
from finbalance.evaluation.prompts.strategies import (
    build_prompt,
    describe_strategy,
    self_refine_stage1,
    self_refine_stage2,
)


# ---------------------------------------------------------------------------
# JSON parsing
# ---------------------------------------------------------------------------

_JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*([\s\S]*?)```", re.IGNORECASE)
_FINAL_ANSWER_RE = re.compile(r"FINAL ANSWER:\s*(\{[\s\S]*\})", re.IGNORECASE)

# Patterns for light JSON cleaning
_TRAILING_COMMA_RE = re.compile(r",\s*([}\]])")


def _clean_json(s: str) -> str:
    """Fix common LLM JSON quirks: thousands-separator commas, trailing commas, Python literals."""
    # Remove thousands-separator commas inside numbers  e.g. 123,900 -> 123900
    # Match digit,digit{3} not followed by another digit (so 1,234,567 all collapse)
    s = re.sub(r'(-?\d{1,3}(?:,\d{3})+)', lambda m: m.group(0).replace(',', ''), s)
    s = _TRAILING_COMMA_RE.sub(r"\1", s)           # remove trailing commas
    s = re.sub(r"\bNone\b", "null", s)             # Python None → null
    s = re.sub(r"\bTrue\b", "true", s)             # Python True → true
    s = re.sub(r"\bFalse\b", "false", s)           # Python False → false
    return s


def _try_parse(candidate: str) -> Optional[dict]:
    """Attempt to parse a string as JSON, with cleaning fallback."""
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass
    try:
        return json.loads(_clean_json(candidate))
    except json.JSONDecodeError:
        return None


def parse_response(raw: str) -> Optional[dict]:
    """
    Try several strategies to extract a JSON balance sheet from raw text:
    1. Code-fence block(s)
    2. FINAL ANSWER: marker (CoT)
    3. All balanced { ... } blocks in the string (largest first)
    4. Entire string
    """
    # 1. Code-fence blocks (try all matches, largest first)
    fence_matches = list(_JSON_BLOCK_RE.finditer(raw))
    for m in sorted(fence_matches, key=lambda x: len(x.group(1)), reverse=True):
        result = _try_parse(m.group(1).strip())
        if result is not None and _looks_like_balance_sheet(result):
            return result
    # Fall through to any parseable fence block
    for m in fence_matches:
        result = _try_parse(m.group(1).strip())
        if result is not None:
            return result

    # 2. CoT final answer
    m = _FINAL_ANSWER_RE.search(raw)
    if m:
        result = _try_parse(m.group(1).strip())
        if result is not None:
            return result

    # 3. All balanced brace blocks — collect then try largest first
    candidates: list[str] = []
    start = 0
    while True:
        idx = raw.find("{", start)
        if idx == -1:
            break
        depth = 0
        end = -1
        for i, ch in enumerate(raw[idx:], idx):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = i
                    break
        if end == -1:
            break
        candidates.append(raw[idx:end + 1])
        start = end + 1

    # Try largest candidates first (most likely to be the full balance sheet)
    for candidate in sorted(candidates, key=len, reverse=True):
        result = _try_parse(candidate)
        if result is not None and _looks_like_balance_sheet(result):
            return result
    # Fall through to any parseable candidate
    for candidate in sorted(candidates, key=len, reverse=True):
        result = _try_parse(candidate)
        if result is not None:
            return result

    # 4. Whole string
    return _try_parse(raw.strip())


def _looks_like_balance_sheet(d: dict) -> bool:
    """Heuristic: a balance sheet dict has at least one of the expected keys."""
    return bool({"assets", "liabilities", "equity"} & set(d.keys()))


# ---------------------------------------------------------------------------
# Per-problem result
# ---------------------------------------------------------------------------

@dataclass
class EvalResult:
    problem_id:   str
    difficulty:   int
    model_id:     str
    strategy:     str
    raw_response: str
    parsed:       Optional[dict]
    metrics:      ProblemMetrics
    errors:       ErrorReport
    model_backend: str
    model_config: dict
    strategy_metadata: dict
    latency_s:    float = 0.0

    def to_dict(self) -> dict:
        d = asdict(self.metrics)
        d.update({
            "model_id":   self.model_id,
            "strategy":   self.strategy,
            "latency_s":  self.latency_s,
            "parse_failed": self.errors.parse_failed,
            "n_errors":   self.errors.total_errors,
            "error_categories": self.errors.by_category,
            "model_backend": self.model_backend,
            "model_config": self.model_config,
            "strategy_metadata": self.strategy_metadata,
            "raw_response": self.raw_response,
        })
        return d


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

class EvaluationRunner:

    def __init__(
        self,
        model: BaseModel,
        strategy: str = "zero_shot",
        retry_on_parse_fail: bool = True,
        verbose: bool = True,
        max_workers: int = 1,
    ):
        self.model      = model
        self.strategy   = strategy
        self.retry      = retry_on_parse_fail
        self.verbose    = verbose
        self.max_workers = max_workers
        self._print_lock = Lock()

    def _log(self, msg: str):
        if self.verbose:
            with self._print_lock:
                print(msg, flush=True)

    def run_one(self, problem: Problem) -> EvalResult:
        prompt = build_prompt(problem, self.strategy)

        t0 = time.perf_counter()
        try:
            raw = self.model.complete(prompt)
        except Exception as e:
            raw = ""
            self._log(f"  [API ERROR] {problem.problem_id}: {e}")

        # Self-refine second pass
        if self.strategy == "self_refine" and raw:
            try:
                raw = self.model.complete(self_refine_stage2(raw, problem))
            except Exception as e:
                self._log(f"  [API ERROR stage2] {problem.problem_id}: {e}")

        latency = time.perf_counter() - t0

        parsed = parse_response(raw)

        # Retry once with zero_shot if CoT parse failed
        if parsed is None and self.retry and self.strategy != "zero_shot":
            self._log(f"  [RETRY] {problem.problem_id}: parse failed, retrying zero_shot")
            try:
                raw2 = self.model.complete(build_prompt(problem, "zero_shot"))
                parsed = parse_response(raw2)
                if parsed is not None:
                    raw = raw2
            except Exception:
                pass

        metrics = evaluate_problem(problem, parsed or {})
        metrics.parse_error = parsed is None
        if metrics.parse_error:
            # Zero out all scores — a failed parse is a total failure, not a balanced empty sheet
            metrics.BA = metrics.ALA = metrics.TPA = metrics.CSR = metrics.FBS = 0.0
        errors  = detect_errors(problem, parsed)

        if self.verbose:
            status = "OK" if not metrics.parse_error else "PARSE_FAIL"
            self._log(
                f"  [{status}] {problem.problem_id} L{problem.difficulty_level} | "
                f"BA={metrics.BA:.0f} ALA={metrics.ALA:.2f} FBS={metrics.FBS:.1f} "
                f"errors={errors.total_errors}"
            )

        return EvalResult(
            problem_id=problem.problem_id,
            difficulty=problem.difficulty_level,
            model_id=self.model.config.model_id,
            strategy=self.strategy,
            raw_response=raw,
            parsed=parsed,
            metrics=metrics,
            errors=errors,
            model_backend=type(self.model).__name__,
            model_config=self.model.export_metadata(),
            strategy_metadata=describe_strategy(self.strategy),
            latency_s=round(latency, 2),
        )

    def _write_rows(self, results: list[EvalResult], path: str):
        rows = [r.to_dict() for r in results]
        with open(path, "w") as f:
            json.dump(rows, f, indent=2)

    def _autosave(self, results: list[Optional[EvalResult]], path: str):
        completed = [r for r in results if r is not None]
        self._write_rows(completed, path)

    def run(self, problems: list[Problem], autosave_path: str | None = None) -> list[EvalResult]:
        n = len(problems)
        self._log(f"\nRunning {n} problems | model={self.model} | strategy={self.strategy} | workers={self.max_workers}\n")

        if self.max_workers <= 1:
            results = []
            for i, problem in enumerate(problems, 1):
                self._log(f"[{i}/{n}]")
                results.append(self.run_one(problem))
                if autosave_path:
                    self._autosave(results, autosave_path)
            return results

        # Parallel execution — preserve original problem order in output
        results = [None] * n
        completed = [0]

        def _run_indexed(idx_problem):
            idx, problem = idx_problem
            result = self.run_one(problem)
            with self._print_lock:
                completed[0] += 1
                print(f"[{completed[0]}/{n}] (worker)", flush=True)
            return idx, result

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(_run_indexed, (i, p)): i
                       for i, p in enumerate(problems)}
            for future in as_completed(futures):
                idx, result = future.result()
                results[idx] = result
                if autosave_path:
                    self._autosave(results, autosave_path)

        return results

    def save_results(self, results: list[EvalResult], path: str):
        self._write_rows(results, path)
        self._log(f"\nSaved {len(results)} results to {path}")
