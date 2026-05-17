import json
import tempfile
import unittest
from pathlib import Path

from docs_benchmark.benchmark.analysis import analyze_submission, ledger_family_for_label, summarize_expected_entry_groups
from docs_benchmark.benchmark.dataset import load_records
from docs_benchmark.benchmark.parser import parse_submission
from docs_benchmark.benchmark.prompt import build_prompt
from docs_benchmark.benchmark.runner import run_openrouter_evaluation
from docs_benchmark.generation.builder import DocumentBenchmarkBuilder


class _FakeClient:
    def __init__(self, response_text: str):
        self.model = "fake/model"
        self._response_text = response_text

    def complete(self, prompt: str, *, temperature: float, max_tokens: int, timeout: int):
        return self._response_text, {"choices": [{"message": {"content": self._response_text}}]}


class BenchmarkTests(unittest.TestCase):
    def test_parse_submission_accepts_fenced_json(self):
        submission = parse_submission(
            """```json
            {
              "entries": [
                {
                  "doc_refs": ["D001"],
                  "debit_account": "Cash",
                  "credit_account": "Revenue",
                  "amount": 125.50
                }
              ],
              "has_inconsistency": false,
              "inconsistency_codes": [],
              "inconsistency_notes": [],
              "balance_sheet": {
                "assets": {"Cash": 125.50},
                "liabilities": {},
                "equity": {"Retained Earnings": 125.50}
              }
            }
            ```"""
        )
        self.assertEqual(len(submission.entries), 1)
        self.assertEqual(submission.entries[0].doc_refs, ["D001"])
        self.assertEqual(submission.balance_sheet["assets"]["Cash"], 125.50)
        self.assertFalse(submission.has_inconsistency)

    def test_prompt_contains_context_and_documents(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="PROMPT_TEST",
                industry="professional_services",
                difficulty_level=2,
                assets_root=tmp_dir,
                period_type="month",
            )
            prompt = build_prompt(record)
            self.assertIn("Allowed account names", prompt)
            self.assertIn("has_inconsistency", prompt)
            self.assertIn('inconsistency_codes": ["bank_closing_mismatch"]', prompt)
            self.assertIn("ISO currency prefixes such as GBP or EUR", prompt)
            self.assertIn("ASC 606 bundled contracts", prompt)
            self.assertIn("US sales tax on purchases is embedded", prompt)
            self.assertIn("India GST uses CGST plus SGST", prompt)
            self.assertIn("fixed asset disposals", prompt)
            self.assertIn("lease modifications", prompt)
            self.assertIn("do not invent missing exchange rates, tax rates, SSPs, lease rates, or assumptions", prompt)
            self.assertIn(record.record_id, prompt)
            self.assertIn(record.documents[0].doc_id, prompt)
            self.assertIn(record.documents[0].ocr_text.splitlines()[0], prompt)
            self.assertNotIn("Document Role:", prompt)

    def test_load_and_score_records_end_to_end(self):
        builder = DocumentBenchmarkBuilder(seed=7)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="RUNNER_TEST",
                industry="subscription_saas",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
            )
            dataset_path = Path(tmp_dir) / "dataset.jsonl"
            dataset_path.write_text(json.dumps(record.to_dict()) + "\n", encoding="utf-8")
            records = load_records(dataset_path)
            self.assertEqual(len(records), 1)

            response_text = json.dumps(
                {
                    "entries": [
                        {
                            "doc_refs": posting.doc_refs,
                            "debit_account": posting.debit_account,
                            "credit_account": posting.credit_account,
                            "amount": posting.amount,
                        }
                        for posting in record.expected_entries
                    ],
                    "has_inconsistency": False,
                    "inconsistency_codes": [],
                    "inconsistency_notes": [],
                    "balance_sheet": {
                        "assets": record.expected_balance_sheet.assets,
                        "liabilities": record.expected_balance_sheet.liabilities,
                        "equity": record.expected_balance_sheet.equity,
                    },
                }
            )
            evaluation = run_openrouter_evaluation(
                records,
                client=_FakeClient(response_text),
                dataset_path=str(dataset_path),
                temperature=0.0,
                max_tokens=4096,
                timeout=30,
            )
            self.assertEqual(evaluation["summary"]["records_evaluated"], 1)
            self.assertEqual(evaluation["summary"]["parse_success_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["journal_entries_matched_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["journal_entries_exact_record_match_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["journal_entries_accounting_record_match_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["final_balance_sheet_matches_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["final_journal_entries_match_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["final_journal_entries_match_no_doc_refs_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["final_balance_sheet_and_journal_entries_match_rate"], 1.0)
            self.assertIn("record_features", evaluation["results"][0])
            self.assertIn("parsed_submission", evaluation["results"][0])
            self.assertIn("reconstructed_balance_sheet", evaluation["results"][0])
            self.assertIn("entry_diagnostics", evaluation["results"][0])
            self.assertIn("3", evaluation["summary"]["by_difficulty"])
            self.assertIn("quarter", evaluation["summary"]["by_period_type"])
            self.assertIn("subscription_saas", evaluation["summary"]["by_industry"])

    def test_negative_control_scores_on_inconsistency_flag(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="NEGATIVE_RUNNER_TEST",
                industry="subscription_saas",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
                negative_control=True,
            )
            dataset_path = Path(tmp_dir) / "dataset.jsonl"
            dataset_path.write_text(json.dumps(record.to_dict()) + "\n", encoding="utf-8")
            records = load_records(dataset_path)
            response_text = json.dumps(
                {
                    "has_inconsistency": True,
                    "inconsistency_codes": record.expected_inconsistency_codes,
                    "inconsistency_notes": ["Invoice total does not tie to visible support."],
                    "entries": [],
                    "balance_sheet": {"assets": {}, "liabilities": {}, "equity": {}},
                }
            )
            evaluation = run_openrouter_evaluation(
                records,
                client=_FakeClient(response_text),
                dataset_path=str(dataset_path),
                temperature=0.0,
                max_tokens=4096,
                timeout=30,
            )
            self.assertEqual(evaluation["summary"]["inconsistency_records"], 1)
            self.assertEqual(evaluation["summary"]["inconsistency_flag_match_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["inconsistency_code_match_rate"], 1.0)
            self.assertEqual(evaluation["summary"]["missed_inconsistency_rate"], 0.0)

    def test_doc_ref_only_mismatch_counts_as_accounting_match(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="ACCOUNTING_MATCH_TEST",
                industry="professional_services",
                difficulty_level=1,
                assets_root=tmp_dir,
                period_type="month",
            )
            posting = record.expected_entries[0]
            parsed = parse_submission(
                json.dumps(
                    {
                        "has_inconsistency": False,
                        "inconsistency_codes": [],
                        "inconsistency_notes": [],
                        "entries": [
                            {
                                "doc_refs": posting.doc_refs + ["D999"],
                                "debit_account": posting.debit_account,
                                "credit_account": posting.credit_account,
                                "amount": posting.amount,
                            }
                        ]
                        + [
                            {
                                "doc_refs": entry.doc_refs,
                                "debit_account": entry.debit_account,
                                "credit_account": entry.credit_account,
                                "amount": entry.amount,
                            }
                            for entry in record.expected_entries[1:]
                        ],
                        "balance_sheet": {
                            "assets": record.expected_balance_sheet.assets,
                            "liabilities": record.expected_balance_sheet.liabilities,
                            "equity": record.expected_balance_sheet.equity,
                        },
                    }
                )
            )
            analysis = analyze_submission(record, parsed, parse_success=True)
            self.assertFalse(analysis["metrics"]["journal_entries_matched"])
            self.assertTrue(analysis["metrics"]["journal_entries_accounting_matched"])
            self.assertEqual(analysis["metrics"]["doc_refs_mismatch_count"], 1)
            self.assertTrue(analysis["metrics"]["entries_accounting_correct_but_doc_refs_wrong"])

    def test_entries_can_be_correct_while_reported_balance_sheet_is_wrong(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="BALANCE_SHEET_WRONG_TEST",
                industry="subscription_saas",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
            )
            wrong_assets = dict(record.expected_balance_sheet.assets)
            wrong_assets["Cash"] = round(wrong_assets.get("Cash", 0.0) + 100.0, 2)
            parsed = parse_submission(
                json.dumps(
                    {
                        "has_inconsistency": False,
                        "inconsistency_codes": [],
                        "inconsistency_notes": [],
                        "entries": [
                            {
                                "doc_refs": entry.doc_refs,
                                "debit_account": entry.debit_account,
                                "credit_account": entry.credit_account,
                                "amount": entry.amount,
                            }
                            for entry in record.expected_entries
                        ],
                        "balance_sheet": {
                            "assets": wrong_assets,
                            "liabilities": record.expected_balance_sheet.liabilities,
                            "equity": record.expected_balance_sheet.equity,
                        },
                    }
                )
            )
            analysis = analyze_submission(record, parsed, parse_success=True)
            self.assertTrue(analysis["metrics"]["journal_entries_matched"])
            self.assertFalse(analysis["metrics"]["final_balance_sheet_matches"])
            self.assertTrue(analysis["metrics"]["entries_correct_but_final_balance_sheet_wrong"])
            self.assertTrue(analysis["metrics"]["predicted_entries_reconstruct_correct_final_balance_sheet"])
            self.assertFalse(analysis["metrics"]["predicted_balance_sheet_matches_reconstructed_balance_sheet"])

    def test_unknown_predicted_account_does_not_crash_analysis(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="UNKNOWN_ACCOUNT_TEST",
                industry="retail",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="month",
            )
            posting = record.expected_entries[0]
            parsed = parse_submission(
                json.dumps(
                    {
                        "has_inconsistency": False,
                        "inconsistency_codes": [],
                        "inconsistency_notes": [],
                        "entries": [
                            {
                                "doc_refs": posting.doc_refs,
                                "debit_account": "InventoryShrinkage Expense",
                                "credit_account": posting.credit_account,
                                "amount": posting.amount,
                            }
                        ],
                        "balance_sheet": {
                            "assets": record.expected_balance_sheet.assets,
                            "liabilities": record.expected_balance_sheet.liabilities,
                            "equity": record.expected_balance_sheet.equity,
                        },
                    }
                )
            )
            analysis = analyze_submission(record, parsed, parse_success=True)
            self.assertTrue(analysis["metrics"]["parse_success"])
            self.assertEqual(analysis["metrics"]["invalid_account_entry_count"], 1)
            self.assertEqual(analysis["metrics"]["invalid_accounts"], ["InventoryShrinkage Expense"])
            self.assertEqual(analysis["entry_diagnostics"]["invalid_account_entries"][0]["index"], 0)
            self.assertGreaterEqual(analysis["metrics"]["wrong_account_count"], 1)

    def test_unknown_predicted_balance_sheet_account_does_not_crash_analysis(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="UNKNOWN_BALANCE_ACCOUNT_TEST",
                industry="professional_services",
                difficulty_level=1,
                assets_root=tmp_dir,
                period_type="month",
            )
            parsed = parse_submission(
                json.dumps(
                    {
                        "has_inconsistency": False,
                        "inconsistency_codes": [],
                        "inconsistency_notes": [],
                        "entries": [],
                        "balance_sheet": {
                            "assets": {"Imaginary Asset": 10.0},
                            "liabilities": {},
                            "equity": {},
                        },
                    }
                )
            )
            analysis = analyze_submission(record, parsed, parse_success=True)
            self.assertFalse(analysis["metrics"]["final_balance_sheet_matches"])
            self.assertFalse(analysis["metrics"]["predicted_balance_sheet_matches_reconstructed_balance_sheet"])

    def test_ledger_family_mapper_covers_observed_labels(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            labels: set[str] = set()
            for industry in ("professional_services", "manufacturing", "subscription_saas"):
                for period_type in ("month", "quarter", "year"):
                    record = builder.generate_record(
                        record_id=f"LABELS_{industry}_{period_type}",
                        industry=industry,
                        difficulty_level=5,
                        assets_root=tmp_dir,
                        period_type=period_type,
                    )
                    labels.update(record.metadata.get("underlying_posting_labels", []))
            uncovered = sorted(label for label in labels if ledger_family_for_label(label) == "other")
            self.assertEqual(uncovered, [])

    def test_expected_entry_group_summary_reports_derived_reasoning_failures(self):
        grouped = summarize_expected_entry_groups(
            [
                {
                    "metrics": {"parse_success": True},
                    "document_index": {"D001": {"doc_type": "customer_invoice", "role": "posting_doc"}},
                    "entry_diagnostics": {
                        "expected_entries": [
                            {
                                "status": "missing",
                                "posting": {
                                    "doc_refs": ["D001"],
                                    "debit_account": "Cost of Goods Sold",
                                    "credit_account": "Inventory",
                                    "amount": 100.0,
                                    "posting_date": "2024-01-31",
                                    "label": "delivery_sale_cogs",
                                },
                            }
                        ]
                    },
                }
            ],
            "posting_label",
        )
        self.assertEqual(grouped["delivery_sale_cogs"]["dominant_failure_mode"], "derived_reasoning")
        self.assertEqual(grouped["delivery_sale_cogs"]["derived_reasoning_failure_rate"], 1.0)
        self.assertEqual(grouped["delivery_sale_cogs"]["doc_ref_linking_failure_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
