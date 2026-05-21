import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from docs_benchmark.accounts import ALLOWED_ACCOUNT_NAMES
from docs_benchmark.benchmark.ablations import (
    AblationSpec,
    apply_visibility_variant,
    run_ablation_evaluation,
    select_ablation_specs,
    write_ablation_outputs,
)
from docs_benchmark.benchmark.bootstrap import analyze_ablation_bootstrap
from docs_benchmark.benchmark.dataset import stratified_sample_records
from docs_benchmark.benchmark.prompt import (
    PROMPT_VARIANT_BALANCE_RECONSTRUCTION,
    PROMPT_VARIANTS,
    VISIBILITY_VARIANT_EVIDENCE_ONLY,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_5_DISTRACTORS,
    VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST,
    VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS,
    VISIBILITY_VARIANT_NO_DISTRACTORS_ORACLE,
    VISIBILITY_VARIANT_NORMAL,
    VISIBILITY_VARIANT_OCR_ONLY,
    VISIBILITY_VARIANT_SUPPORT_DOCS_REMOVED,
    build_prompt,
)
from docs_benchmark.benchmark.tools import (
    TOOL_CALCULATOR,
    TOOL_VARIANT_FORCED_LEDGER_VERIFIER,
    calculator_tool,
    ledger_check_tool,
    run_forced_ledger_verifier_completion,
    run_tool_agent_completion,
)
from docs_benchmark.ledger import Ledger
from docs_benchmark.schemas import BalanceSheet, DocumentAsset, DocumentRecord, OpeningBalance, Posting


class _SequenceClient:
    def __init__(self, responses: list[str]):
        self.model = "fake/model"
        self.responses = list(responses)
        self.prompts: list[str] = []
        self.messages: list[list[dict[str, str]]] = []

    def complete(self, prompt: str, *, temperature: float, max_tokens: int, timeout: int):
        self.prompts.append(prompt)
        return self._next_response()

    def complete_messages(self, messages: list[dict[str, str]], *, temperature: float, max_tokens: int, timeout: int):
        self.messages.append(messages)
        return self._next_response()

    def _next_response(self):
        if not self.responses:
            raise AssertionError("fake client ran out of responses")
        text = self.responses.pop(0)
        return text, {"usage": {"prompt_tokens": 1, "completion_tokens": 2, "total_tokens": 3, "cost": 0.01}}


def _record(record_id: str = "ABLATION_TEST") -> DocumentRecord:
    opening = OpeningBalance(
        date="2024-01-01",
        assets={"Cash": 1000.0},
        liabilities={},
        equity={"Owner's Equity": 1000.0},
    )
    posting = Posting(
        doc_refs=["D001", "D002"],
        debit_account="Accounts Receivable",
        credit_account="Service Revenue",
        amount=100.0,
        posting_date="2024-01-31",
        label="service_invoice",
    )
    ledger = Ledger(opening)
    ledger.apply_all([posting])
    expected_balance_sheet: BalanceSheet = ledger.build_balance_sheet("2024-01-31")
    return DocumentRecord(
        record_id=record_id,
        industry="professional_services",
        difficulty_level=2,
        period_start="2024-01-01",
        period_end="2024-01-31",
        opening_balance=opening,
        allowed_accounts=list(ALLOWED_ACCOUNT_NAMES),
        documents=[
            DocumentAsset(
                doc_id="D001",
                doc_type="customer_invoice",
                role="posting_doc",
                title="Customer Invoice",
                date="2024-01-15",
                asset_path="assets/D001.pdf",
                ocr_text="Invoice INV-001 for professional services. Amount due 100.00.",
            ),
            DocumentAsset(
                doc_id="D002",
                doc_type="work_order",
                role="support_doc",
                title="Work Order",
                date="2024-01-10",
                asset_path="assets/D002.pdf",
                ocr_text="Work order WO-001 approves professional services for INV-001.",
            ),
            DocumentAsset(
                doc_id="D003",
                doc_type="depreciation_schedule",
                role="adjustment_doc",
                title="Depreciation Schedule",
                date="2024-01-31",
                asset_path="assets/D003.pdf",
                ocr_text="No current depreciation adjustment.",
            ),
            DocumentAsset(
                doc_id="D004",
                doc_type="memo",
                role="distractor_doc",
                title="Unrelated Memo",
                date="2024-01-20",
                asset_path="assets/D004.pdf",
                ocr_text="Unrelated planning memo.",
            ),
        ],
        expected_entries=[posting],
        expected_balance_sheet=expected_balance_sheet,
        metadata={
            "period_type": "month",
            "period_label": "Jan 2024",
            "entity_name": "Ablation Co",
            "tax_regime": "none",
            "scenario_sequence": ["service_invoice"],
            "underlying_posting_labels": ["service_invoice"],
            "doc_dependency_depth": 2,
            "subledger_count": 0,
            "jurisdictional_depth": 0,
            "temporal_lookback_depth": 1,
        },
    )


def _submission(record: DocumentRecord) -> str:
    return json.dumps(
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
                "assets": record.expected_balance_sheet.assets,
                "liabilities": record.expected_balance_sheet.liabilities,
                "equity": record.expected_balance_sheet.equity,
            },
        }
    )


def _wrong_balance_submission(record: DocumentRecord) -> str:
    payload = json.loads(_submission(record))
    payload["balance_sheet"]["assets"] = {"Cash": 1.0}
    return json.dumps(payload)


def _inconsistency_submission() -> str:
    return json.dumps(
        {
            "has_inconsistency": True,
            "inconsistency_codes": ["bank_closing_mismatch"],
            "inconsistency_notes": ["Bank closing balance does not tie."],
            "entries": [],
            "balance_sheet": {"assets": {}, "liabilities": {}, "equity": {}},
        }
    )


def _record_with_extra_distractors(record_id: str = "DISTRACTOR_SOURCE", count: int = 6) -> DocumentRecord:
    record = _record(record_id)
    documents = []
    for index in range(count):
        documents.append(
            DocumentAsset(
                doc_id=f"X{index + 1:03d}",
                doc_type="memo",
                role="distractor_doc",
                title=f"Injected Distractor {index + 1}",
                date="2024-01-20",
                asset_path=f"assets/X{index + 1:03d}.pdf",
                ocr_text=f"External distractor memo {index + 1}.",
            )
        )
    return replace(record, documents=documents)


class AblationTests(unittest.TestCase):
    def test_prompt_registry_builds_all_variants(self):
        record = _record()
        for prompt_variant in PROMPT_VARIANTS:
            prompt = build_prompt(record, prompt_variant=prompt_variant, visibility_variant=VISIBILITY_VARIANT_NORMAL)
            self.assertIn("has_inconsistency", prompt)
            self.assertIn(record.record_id, prompt)
        self.assertIn("Private workflow before the final JSON", build_prompt(record, prompt_variant="self_check"))
        reconstruction_prompt = build_prompt(record, prompt_variant=PROMPT_VARIANT_BALANCE_RECONSTRUCTION)
        self.assertIn("Private balance reconstruction workflow", reconstruction_prompt)

    def test_visibility_transforms_preserve_ground_truth_and_doc_ids(self):
        record = _record()
        transformed, metadata = apply_visibility_variant(record, VISIBILITY_VARIANT_NO_DISTRACTORS_ORACLE)
        self.assertEqual([doc.doc_id for doc in transformed.documents], ["D001", "D002", "D003"])
        self.assertEqual(metadata["removed_document_ids"], ["D004"])
        self.assertEqual([entry.doc_refs for entry in record.expected_entries], [["D001", "D002"]])

        transformed, _ = apply_visibility_variant(record, VISIBILITY_VARIANT_SUPPORT_DOCS_REMOVED)
        self.assertEqual([doc.doc_id for doc in transformed.documents], ["D001", "D003", "D004"])

        transformed, _ = apply_visibility_variant(record, VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS)
        self.assertEqual(transformed.allowed_accounts, [])
        self.assertGreater(len(record.allowed_accounts), 0)

    def test_context_visibility_variants_keep_evidence_and_pad_deterministically(self):
        record = _record()
        source = _record_with_extra_distractors()
        evidence_only, metadata = apply_visibility_variant(record, VISIBILITY_VARIANT_EVIDENCE_ONLY)
        self.assertEqual([doc.doc_id for doc in evidence_only.documents], ["D001", "D002"])
        self.assertEqual(metadata["kept_evidence_doc_ids"], ["D001", "D002"])
        self.assertEqual(metadata["removed_document_ids"], ["D003", "D004"])
        self.assertEqual(record.expected_entries[0].doc_refs, ["D001", "D002"])

        padded, metadata = apply_visibility_variant(
            record,
            VISIBILITY_VARIANT_EVIDENCE_PLUS_5_DISTRACTORS,
            corpus_records=[record, source],
        )
        self.assertEqual([doc.doc_id for doc in padded.documents[:3]], ["D001", "D002", "D004"])
        self.assertEqual(metadata["padding_doc_ids"], ["D004", "PX001", "PX002", "PX003", "PX004"])
        self.assertEqual(len(metadata["injected_documents"]), 4)

        relevant_last, metadata = apply_visibility_variant(
            record,
            VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST,
            corpus_records=[record, source],
        )
        self.assertEqual([doc.doc_id for doc in relevant_last.documents[-2:]], ["D001", "D002"])
        self.assertEqual(metadata["padding_doc_ids"][0], "D004")

    def test_ocr_only_and_account_visibility_prompt_rendering(self):
        record = _record()
        prompt = build_prompt(record, visibility_variant=VISIBILITY_VARIANT_OCR_ONLY)
        self.assertIn("Document ID: D001", prompt)
        self.assertIn("Invoice INV-001", prompt)
        self.assertNotIn("Document Type:", prompt)
        self.assertNotIn("Document Title:", prompt)

        prompt = build_prompt(record, visibility_variant=VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS)
        self.assertNotIn("Allowed account names:", prompt)
        self.assertNotIn("- Use only the allowed account names.", prompt)

    def test_tool_loop_valid_call_and_final_answer(self):
        record = _record()
        final_answer = _submission(record)
        client = _SequenceClient(
            [
                json.dumps({"tool": "calculator", "arguments": {"expression": "40 + 60"}}),
                final_answer,
            ]
        )
        result = run_tool_agent_completion(
            record,
            client,
            "Return the answer.",
            allowed_tools=(TOOL_CALCULATOR,),
            agent_max_steps=4,
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertEqual(len(result.tool_calls), 1)
        self.assertEqual(result.tool_calls[0]["result"]["result"], 100.0)
        self.assertEqual(result.tool_call_failures, 0)
        self.assertEqual(result.response_text, final_answer)

    def test_tool_loop_malformed_call_and_max_step_handling(self):
        record = _record()
        final_answer = _submission(record)
        malformed_client = _SequenceClient(["not json", final_answer])
        malformed = run_tool_agent_completion(
            record,
            malformed_client,
            "Return the answer.",
            allowed_tools=(TOOL_CALCULATOR,),
            agent_max_steps=2,
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertEqual(malformed.tool_call_failures, 1)

        max_step_client = _SequenceClient(
            [
                json.dumps({"tool": "calculator", "arguments": {"expression": "1 + 1"}}),
                final_answer,
            ]
        )
        exhausted = run_tool_agent_completion(
            record,
            max_step_client,
            "Return the answer.",
            allowed_tools=(TOOL_CALCULATOR,),
            agent_max_steps=1,
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertEqual(len(exhausted.tool_calls), 1)
        self.assertEqual(exhausted.tool_call_failures, 1)

    def test_forced_ledger_verifier_runs_draft_feedback_and_revision(self):
        record = _record()
        final_answer = _submission(record)
        client = _SequenceClient([_wrong_balance_submission(record), final_answer])
        result = run_forced_ledger_verifier_completion(
            record,
            client,
            "Return the answer.",
            verifier_passes=1,
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertEqual(result.response_text, final_answer)
        self.assertEqual(result.verifier_passes, 1)
        self.assertEqual(len(result.tool_calls), 1)
        self.assertFalse(result.verifier_feedback[0]["submitted_balance_sheet_matches_reconstructed"])
        self.assertGreater(result.verifier_feedback[0]["balance_sheet_delta_count"], 0)
        self.assertEqual(result.response_payload["usage"]["cost"], 0.02)

    def test_forced_ledger_verifier_handles_malformed_draft(self):
        record = _record()
        final_answer = _submission(record)
        client = _SequenceClient(["not json", final_answer])
        result = run_forced_ledger_verifier_completion(
            record,
            client,
            "Return the answer.",
            verifier_passes=1,
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertFalse(result.verifier_feedback[0]["parse_success"])
        self.assertIn("parse_error", result.verifier_feedback[0])

    def test_forced_ledger_verifier_skips_balance_comparison_for_inconsistency_claims(self):
        record = replace(
            _record(),
            expected_inconsistency=True,
            expected_inconsistency_codes=["bank_closing_mismatch"],
            expected_entries=[],
        )
        final_answer = _inconsistency_submission()
        client = _SequenceClient([final_answer, final_answer])
        result = run_forced_ledger_verifier_completion(
            record,
            client,
            "Return the answer.",
            verifier_passes=1,
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        feedback = result.verifier_feedback[0]
        self.assertTrue(feedback["claimed_inconsistency"])
        self.assertIsNone(feedback["submitted_balance_sheet_matches_reconstructed"])
        self.assertEqual(feedback["balance_sheet_delta_count"], 0)
        self.assertIn("skipped", feedback["note"])

    def test_tools_are_deterministic_and_robust(self):
        record = _record()
        self.assertEqual(calculator_tool({"expression": "(40 + 60) / 2"})["result"], 50.0)
        result = ledger_check_tool(
            {
                "entries": [
                    {
                        "doc_refs": ["D001"],
                        "debit_account": "Imaginary Asset",
                        "credit_account": "Service Revenue",
                        "amount": 100,
                    }
                ]
            },
            record,
        )
        self.assertFalse(result["ok"])
        self.assertIn("unknown accounts", result["errors"][0])

    def test_ablation_runner_and_outputs_with_fake_client(self):
        records = [_record("ABLATION_TEST_1"), _record("ABLATION_TEST_2")]
        client = _SequenceClient([_submission(records[0]), _submission(records[1])])
        evaluation = run_ablation_evaluation(
            records,
            client=client,
            dataset_path="unit.jsonl",
            spec=AblationSpec("unit_no_tools"),
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        self.assertEqual(evaluation["summary"]["records_evaluated"], 2)
        self.assertEqual(evaluation["summary"]["parse_success_rate"], 1.0)
        self.assertEqual(evaluation["results"][0]["ablation_name"], "unit_no_tools")
        self.assertIn("tool_calls", evaluation["results"][0])
        self.assertIn("error_taxonomy", evaluation["summary"])

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = write_ablation_outputs(evaluation, tmp_dir)
            self.assertTrue((output_dir / "evaluation.json").exists())
            self.assertTrue((output_dir / "summary.json").exists())
            self.assertTrue((output_dir / "per_record_results.jsonl").exists())
            self.assertTrue((output_dir / "slice_tables" / "by_difficulty_level.csv").exists())
            self.assertTrue((output_dir / "slice_tables" / "error_taxonomy.csv").exists())
            rows = (output_dir / "per_record_results.jsonl").read_text(encoding="utf-8").strip().splitlines()
            self.assertEqual(len(rows), 2)

    def test_ablation_runner_records_forced_verifier_metadata(self):
        record = _record("ABLATION_VERIFY")
        client = _SequenceClient([_wrong_balance_submission(record), _submission(record)])
        evaluation = run_ablation_evaluation(
            [record],
            client=client,
            dataset_path="unit.jsonl",
            spec=AblationSpec("forced_unit", tool_variant=TOOL_VARIANT_FORCED_LEDGER_VERIFIER),
            temperature=0.0,
            max_tokens=1024,
            timeout=30,
        )
        result = evaluation["results"][0]
        self.assertEqual(result["verifier_passes"], 1)
        self.assertEqual(evaluation["summary"]["verifier_passes_total"], 1)
        self.assertEqual(evaluation["summary"]["tool_call_count_total"], 1)
        self.assertIn("verifier_feedback", result)

    def test_coverage_matrix_names_are_selectable(self):
        names = [spec.name for spec in select_ablation_specs()]
        self.assertIn("prompt_self_check", names)
        self.assertIn("visibility_no_allowed_accounts", names)
        self.assertIn("tool_full_tool_agent", names)
        targeted_names = [spec.name for spec in select_ablation_specs(matrix="targeted")]
        self.assertIn("forced_ledger_verifier", targeted_names)
        self.assertIn("evidence_plus_30_distractors", targeted_names)
        context_names = [spec.name for spec in select_ablation_specs(matrix="context_stress")]
        self.assertEqual(context_names[0], "prompt_baseline")
        self.assertIn("evidence_relevant_last", context_names)
        selected = select_ablation_specs(names=["prompt_baseline", "tool_calculator"])
        self.assertEqual([spec.name for spec in selected], ["prompt_baseline", "tool_calculator"])
        selected = select_ablation_specs(names=["forced_ledger_verifier"])
        self.assertEqual(selected[0].tool_variant, TOOL_VARIANT_FORCED_LEDGER_VERIFIER)

    def test_bootstrap_analysis_outputs_paired_comparisons(self):
        baseline = [
            {
                "record_id": "R1",
                "metrics": {
                    "expected_inconsistency": False,
                    "predicted_entries_reconstruct_correct_final_balance_sheet": True,
                    "final_balance_sheet_matches": False,
                    "final_journal_entries_match_no_doc_refs": True,
                    "final_balance_sheet_and_journal_entries_match": False,
                    "doc_refs_mismatch_count": 1,
                    "expected_entry_count": 2,
                },
            },
            {
                "record_id": "R2",
                "metrics": {
                    "expected_inconsistency": True,
                    "inconsistency_code_matches": True,
                },
            },
        ]
        variant = [
            {
                "record_id": "R1",
                "metrics": {
                    "expected_inconsistency": False,
                    "predicted_entries_reconstruct_correct_final_balance_sheet": True,
                    "final_balance_sheet_matches": True,
                    "final_journal_entries_match_no_doc_refs": True,
                    "final_balance_sheet_and_journal_entries_match": True,
                    "doc_refs_mismatch_count": 0,
                    "expected_entry_count": 2,
                },
            },
            {
                "record_id": "R2",
                "metrics": {
                    "expected_inconsistency": True,
                    "inconsistency_code_matches": False,
                },
            },
        ]
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            (root / "prompt_baseline").mkdir()
            (root / "forced_ledger_verifier").mkdir()
            (root / "prompt_baseline" / "per_record_results.jsonl").write_text(
                "\n".join(json.dumps(row) for row in baseline) + "\n",
                encoding="utf-8",
            )
            (root / "forced_ledger_verifier" / "per_record_results.jsonl").write_text(
                "\n".join(json.dumps(row) for row in variant) + "\n",
                encoding="utf-8",
            )
            summary = analyze_ablation_bootstrap(root, iterations=20, seed=3)
            metrics = {(row["ablation_name"], row["metric"]): row for row in summary["comparisons"]}
            self.assertEqual(
                metrics[
                    ("forced_ledger_verifier", "final_balance_sheet_and_journal_entries_match_rate")
                ]["diff"],
                1.0,
            )
            self.assertTrue((root / "bootstrap_summary.json").exists())
            self.assertTrue((root / "bootstrap_summary.csv").exists())

    def test_stratified_sample_records_round_robins_groups(self):
        records = [
            replace(_record(f"R{index}"), difficulty_level=(index % 2) + 1, industry=f"industry_{index % 3}")
            for index in range(12)
        ]
        sampled = stratified_sample_records(records, 5)
        self.assertEqual(len(sampled), 5)
        self.assertEqual(len({(record.difficulty_level, record.industry) for record in sampled}), 5)


if __name__ == "__main__":
    unittest.main()
