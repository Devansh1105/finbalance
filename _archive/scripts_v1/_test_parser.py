"""Quick parser regression test — run via: python scripts/_test_parser.py"""
import sys
sys.path.insert(0, ".")
from finbalance.evaluation.runner import parse_response

test_cases = [
    (
        "trailing comma",
        '{"assets": {"Cash": 1000,}, "liabilities": {}, "equity": {"Owners Equity": 1000}}',
    ),
    (
        "intro text with inner brace",
        'Here is the result {step 1} and the balance sheet:\n'
        '{"assets": {"Cash": 1000}, "liabilities": {}, "equity": {"Owners Equity": 1000}}',
    ),
    (
        "code fence json",
        '```json\n{"assets": {"Cash": 5000}, "liabilities": {}, "equity": {"Owners Equity": 5000}}\n```',
    ),
    (
        "python None/True/False",
        '{"assets": {"Cash": None}, "liabilities": {}, "equity": {}}',
    ),
    (
        "trailing comma nested",
        '{"assets": {"Cash": 100, "Equipment": 200,}, "liabilities": {"Loans Payable": 50,}, "equity": {"Owners Equity": 250}}',
    ),
    (
        "explanation then plain JSON",
        'Based on the transactions provided, here is the balance sheet:\n\n'
        '{\n  "assets": {"Cash": 9000, "Equipment": 5000},\n'
        '  "liabilities": {"Loans Payable": 4000},\n'
        '  "equity": {"Owners Equity": 10000}\n}',
    ),
    (
        "thousands separator commas",
        '{\n  "assets": {\n    "Cash": 123,900,\n    "Equipment": 36,300\n  },'
        '\n  "liabilities": {"Accounts Payable": 7,200},\n  "equity": {"Owners Equity": 153,000}\n}',
    ),
    (
        "thousands separator with negative",
        '{"assets": {"Cash": 1,234,567}, "liabilities": {}, "equity": {"Owners Equity": 1,234,567}}',
    ),
]

all_pass = True
for name, raw in test_cases:
    result = parse_response(raw)
    ok = result is not None
    all_pass = all_pass and ok
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}: {result}")

print()
print("All tests passed!" if all_pass else "Some tests FAILED!")
