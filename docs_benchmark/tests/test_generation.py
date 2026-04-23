import json
import re
import tempfile
import unittest
from pathlib import Path

from docs_benchmark.generation.builder import DocumentBenchmarkBuilder
from docs_benchmark.generation.helpers import PERIOD_TYPES
from docs_benchmark.industry_schemas import INDUSTRIES


class GenerationTests(unittest.TestCase):
    def test_record_generation_balances_for_all_industries_and_periods(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            for industry in INDUSTRIES:
                for period_type in PERIOD_TYPES:
                    record = builder.generate_record(
                        record_id=f"TEST_{industry}_{period_type}",
                        industry=industry,
                        difficulty_level=4,
                        assets_root=tmp_dir,
                        period_type=period_type,
                    )
                    self.assertTrue(record.expected_balance_sheet.balanced, f"{industry}:{period_type}")
                    self.assertGreaterEqual(len(record.documents), 8, f"{industry}:{period_type}")
                    self.assertTrue(record.metadata["validation"]["ok"], f"{industry}:{period_type}")
                    self.assertEqual(record.metadata["period_type"], period_type)

    def test_dataset_generation_writes_jsonl(self):
        builder = DocumentBenchmarkBuilder(seed=7)
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "dataset.jsonl"
            assets_dir = Path(tmp_dir) / "assets"
            counts = {
                "professional_services": {"month": {1: 1}, "year": {2: 1}},
                "retail": {"quarter": {3: 1}},
            }
            records = builder.generate_dataset(counts, output_path, assets_dir, negative_control_rate=0.0)
            self.assertEqual(len(records), 3)
            lines = output_path.read_text(encoding="utf-8").strip().splitlines()
            self.assertEqual(len(lines), 3)
            first = json.loads(lines[0])
            self.assertEqual(first["metadata"]["version"], "v4_phase2_schema_driven")

    def test_property_management_rent_roll_posts_to_rental_revenue(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_PROPERTY_MONTH",
                industry="property_management",
                difficulty_level=1,
                assets_root=tmp_dir,
                period_type="month",
            )
            self.assertTrue(
                any(posting.credit_account == "Rental Revenue" for posting in record.expected_entries),
                "property_management month level 1 should include a rent-roll posting to Rental Revenue",
            )

    def test_professional_services_expense_receipt_lines_match_travel_account(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_PRO_MONTH",
                industry="professional_services",
                difficulty_level=1,
                assets_root=tmp_dir,
                period_type="month",
            )
            receipt_docs = [doc for doc in record.documents if doc.doc_type == "expense_receipt"]
            self.assertTrue(receipt_docs)
            ocr_text = receipt_docs[0].ocr_text
            self.assertIn("Travel Expense", ocr_text)
            self.assertIn("Travel Incidentals", ocr_text)
            self.assertNotIn("Description Incidentals |", ocr_text)

    def test_professional_services_retainer_support_doc_is_not_service_period_memo(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_PRO_QUARTER",
                industry="professional_services",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
            )
            self.assertTrue(any(doc.doc_type == "retainer_agreement_memo" for doc in record.documents))
            for doc in record.documents:
                if doc.doc_type == "service_period_memo":
                    self.assertNotIn("Subject: Retainer engagement", doc.ocr_text)

    def test_prepaid_purchase_posting_only_references_notice_doc(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_PRO_QUARTER_PREPAID",
                industry="professional_services",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
            )
            purchase_entries = [posting for posting in record.expected_entries if posting.label == "prepaid_rent_purchase"]
            self.assertTrue(purchase_entries)
            self.assertEqual(len(purchase_entries[0].doc_refs), 1)

    def test_manufacturing_uses_distinct_labor_and_overhead_docs(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_MAN_QUARTER",
                industry="manufacturing",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
            )
            doc_types = {doc.doc_type for doc in record.documents}
            self.assertIn("production_batch_sheet", doc_types)
            self.assertIn("direct_labor_record", doc_types)
            self.assertIn("overhead_accrual_memo", doc_types)

    def test_deferred_invoice_labels_do_not_imply_earned_vs_deferred_split(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            saas_record = builder.generate_record(
                record_id="TEST_SUB_MONTH",
                industry="subscription_saas",
                difficulty_level=1,
                assets_root=tmp_dir,
                period_type="month",
            )
            pro_record = builder.generate_record(
                record_id="TEST_PRO_YEAR",
                industry="professional_services",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="year",
            )
            deferred_docs = []
            for record in (saas_record, pro_record):
                for doc in record.documents:
                    if doc.doc_type == "customer_invoice" and "Unearned Revenue" in {
                        posting.credit_account for posting in record.expected_entries if doc.doc_id in posting.doc_refs
                    }:
                        deferred_docs.append(doc)
            self.assertTrue(deferred_docs)
            for doc in deferred_docs:
                self.assertNotIn("Deferred contract value", doc.ocr_text)
                self.assertIn("Service coverage under contract", doc.ocr_text)

    def test_year_records_include_distractor_docs(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_PRO_YEAR_DISTRACTORS",
                industry="professional_services",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="year",
            )
            distractors = [doc for doc in record.documents if doc.role == "distractor_doc"]
            self.assertTrue(distractors)
            self.assertTrue(any(doc.doc_type == "memo" for doc in distractors))
            self.assertFalse(any("Do not post again" in doc.ocr_text for doc in distractors))
            self.assertFalse(any("should not create a ledger entry" in doc.ocr_text for doc in distractors))

    def test_professional_services_quarter_has_multi_invoice_payment_and_reclassification(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_PRO_Q3_MULTI",
                industry="professional_services",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
            )
            payment_docs = [doc for doc in record.documents if doc.doc_type == "payment_advice" and "Allocation Details" in doc.ocr_text]
            self.assertTrue(payment_docs)
            self.assertIn("Allocated Amount", payment_docs[0].ocr_text)
            self.assertTrue(any(doc.doc_type == "reclassification_memo" for doc in record.documents))
            self.assertTrue(any(posting.label.startswith("multi_invoice_payment_") for posting in record.expected_entries))
            self.assertTrue(any(posting.label == "reclassification_correction_correction" for posting in record.expected_entries))

    def test_interbank_transfer_creates_reserve_cash_and_multiple_bank_statements(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_SUB_Q4_TRANSFER",
                industry="subscription_saas",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="quarter",
            )
            self.assertTrue(any(doc.doc_type == "transfer_advice" for doc in record.documents))
            self.assertTrue(any(posting.debit_account == "Reserve Cash" and posting.credit_account == "Cash" for posting in record.expected_entries))
            bank_docs = [doc for doc in record.documents if doc.doc_type == "bank_statement"]
            self.assertGreaterEqual(len(bank_docs), 2)
            self.assertTrue(any("Reserve Account" in doc.ocr_text for doc in bank_docs))

    def test_professional_services_month_level2_has_tax_fields_and_tax_postings(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_PRO_M2_TAX",
                industry="professional_services",
                difficulty_level=2,
                assets_root=tmp_dir,
                period_type="month",
            )
            self.assertNotEqual(record.metadata["tax_regime"], "none")
            invoice_docs = [doc for doc in record.documents if doc.doc_type == "customer_invoice"]
            self.assertTrue(invoice_docs)
            self.assertTrue(any("Tax Amount:" in doc.ocr_text for doc in invoice_docs))
            self.assertTrue(any(posting.credit_account == "Sales Tax Payable" for posting in record.expected_entries))

    def test_professional_services_year_level5_has_fx_support_docs(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_PRO_Y5_FX",
                industry="professional_services",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="year",
            )
            doc_types = {doc.doc_type for doc in record.documents}
            self.assertIn("exchange_rate_notice", doc_types)
            self.assertIn("fx_remeasurement_memo", doc_types)
            remeasurement_docs = [doc for doc in record.documents if doc.doc_type == "fx_remeasurement_memo"]
            self.assertTrue(remeasurement_docs)
            self.assertRegex(remeasurement_docs[0].ocr_text, r"Closing Rate:\s+1\.\d{4}")
            self.assertTrue(
                any(
                    posting.debit_account in {"Foreign Exchange Loss", "Accounts Receivable"}
                    or posting.credit_account in {"Foreign Exchange Gain", "Accounts Receivable"}
                    for posting in record.expected_entries
                )
            )

    def test_random_mismatch_offsets_are_large_enough(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        for _ in range(20):
            offset = builder._random_mismatch_offset()
            self.assertGreaterEqual(abs(offset), 500.0)
            self.assertLessEqual(abs(offset), 3000.0)

    def test_line_value_replacement_targets_closing_balance_line(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        original = "\n".join(
            [
                "Opening Balance: $78,206.59",
                "Closing Balance: $78,206.59",
            ]
        )
        updated, replaced = builder._replace_line_value_after_prefix(
            original,
            "Closing Balance:",
            "$78,206.59",
            "$76,024.52",
        )
        self.assertTrue(replaced)
        self.assertIn("Opening Balance: $78,206.59", updated)
        self.assertIn("Closing Balance: $76,024.52", updated)

    def test_vendor_statement_distractors_do_not_repeat_same_vendor(self):
        builder = DocumentBenchmarkBuilder(seed=2)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_MAN_Y5_VENDOR_DISTRACTORS",
                industry="manufacturing",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="year",
            )
            vendors = [doc.metadata.get("counterparty_name") for doc in record.documents if doc.doc_type == "vendor_statement"]
            self.assertEqual(len(vendors), len(set(vendors)))

    def test_cancellation_note_uses_explicit_replacement_instruction(self):
        builder = DocumentBenchmarkBuilder(seed=3)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_MAN_M4_CANCEL",
                industry="manufacturing",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
            )
            notes = [doc for doc in record.documents if doc.doc_type == "cancellation_note"]
            self.assertTrue(notes)
            for note in notes:
                normalized = " ".join(note.ocr_text.split())
                self.assertIn("is withdrawn and must not be posted.", normalized)
                self.assertRegex(normalized, r"Use .* as the only valid invoice\.")

    def test_negative_control_record_requires_inconsistency_flag(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_NEGATIVE_CONTROL",
                industry="subscription_saas",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
                negative_control=True,
            )
            self.assertTrue(record.expected_inconsistency)
            self.assertTrue(record.expected_inconsistency_codes)
            self.assertTrue(record.inconsistency_reasons)
            self.assertEqual(record.expected_entries, [])
            self.assertEqual(record.expected_balance_sheet.assets, {})
