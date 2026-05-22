"""Re-parse saved raw responses with the fixed parser."""
import json, sys
sys.path.insert(0, ".")
from finbalance.evaluation.runner import parse_response

with open("results/claude-3-haiku-20240307_zero_shot.json") as f:
    results = json.load(f)

all_ok = True
for r in results:
    raw = r.get("raw_response", "")
    parsed = parse_response(raw)
    ok = parsed is not None
    all_ok = all_ok and ok
    status = "OK  " if ok else "FAIL"
    keys = list(parsed.keys()) if parsed else None
    print(f"[{status}] {r['problem_id']}: parsed_keys={keys}")

print()
print("All parse OK!" if all_ok else "Some FAILED — check raw responses above")
