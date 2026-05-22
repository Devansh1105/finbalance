import json
import re
import tempfile
import unittest
from pathlib import Path

from finbalance.generation.builder import DocumentBenchmarkBuilder
from finbalance.generation.helpers import PERIOD_TYPES
from finbalance.industry_schemas import INDUSTRIES
from finbalance.benchmark.manifests import record_manifest_row


class GenerationTests(unittest.TestCase):
    def _money_after(self, doc, label):
        match = re.search(rf"{re.escape(label)}:\s+([^\n]+)", doc.ocr_text)
        self.assertIsNotNone(match, f"{label} not found in {doc.doc_type}")
        raw = match.group(1).strip()
        symbol = str(doc.metadata.get("currency_symbol", "$"))
        cleaned = raw.replace(symbol, "").replace("EUR", "").replace("GBP", "").replace("$", "").strip()
        if doc.metadata.get("currency_format") == "symbol_prefix_eu":
            cleaned = cleaned.replace(".", "").replace(",", ".")
        else:
            cleaned = cleaned.replace(",", "")
        return round(float(cleaned), 2)

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

    def test_field_services_supplier_bill_exposes_repair_context(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_FIELD_SUPPLIER_REPAIRS",
                industry="field_services",
                difficulty_level=1,
                assets_root=tmp_dir,
                period_type="month",
            )
            supplier_docs = [doc for doc in record.documents if doc.doc_type == "supplier_invoice"]
            self.assertTrue(supplier_docs)
            supplier_text = "\n".join(doc.ocr_text.lower() for doc in supplier_docs)
            self.assertRegex(supplier_text, r"repair|maintenance|service parts")
            self.assertTrue(any(posting.label == "supplier_bill" and posting.debit_account == "Repairs Expense" for posting in record.expected_entries))

    def test_wholesale_delivery_sale_exposes_cogs_cost_basis(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_WHOLESALE_COGS_VISIBLE",
                industry="wholesale_distribution",
                difficulty_level=1,
                assets_root=tmp_dir,
                period_type="month",
            )
            delivery_doc = next(doc for doc in record.documents if doc.doc_type == "delivery_note")
            cogs_entry = next(posting for posting in record.expected_entries if posting.label == "delivery_sale_cogs")
            self.assertIn("Cost Basis Amount:", delivery_doc.ocr_text)
            self.assertIn("Extended Cost", delivery_doc.ocr_text)
            self.assertEqual(self._money_after(delivery_doc, "Cost Basis Amount"), cogs_entry.amount)

    def test_retail_sales_summary_exposes_cogs_cost_basis(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_RETAIL_COGS_VISIBLE",
                industry="retail",
                difficulty_level=1,
                assets_root=tmp_dir,
                period_type="month",
            )
            sales_doc = next(doc for doc in record.documents if doc.doc_type == "sales_summary")
            cogs_entry = next(posting for posting in record.expected_entries if posting.label == "retail_sale_cogs")
            self.assertIn("COGS Amount:", sales_doc.ocr_text)
            self.assertIn("COGS Source:", sales_doc.ocr_text)
            self.assertEqual(self._money_after(sales_doc, "COGS Amount"), cogs_entry.amount)

    def test_india_gst_legacy_wholesale_scenarios_use_split_accounts(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_WHOLESALE_INDIA_GST_SPLIT",
                industry="wholesale_distribution",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
                tax_regime_override="india_gst",
            )
            self.assertTrue(any(posting.label == "goods_receipt_purchase_tax_cgst" and posting.debit_account == "Input CGST Receivable" for posting in record.expected_entries))
            self.assertTrue(any(posting.label == "goods_receipt_purchase_tax_sgst" and posting.debit_account == "Input SGST Receivable" for posting in record.expected_entries))
            self.assertTrue(any(posting.label == "delivery_sale_tax_cgst" and posting.credit_account == "CGST Payable" for posting in record.expected_entries))
            self.assertTrue(any(posting.label == "delivery_sale_tax_sgst" and posting.credit_account == "SGST Payable" for posting in record.expected_entries))
            self.assertFalse(any(posting.label in {"goods_receipt_purchase_tax", "delivery_sale_tax"} and posting.credit_account == "Sales Tax Payable" for posting in record.expected_entries))
            self.assertTrue(any("CGST Amount:" in doc.ocr_text and "SGST Amount:" in doc.ocr_text for doc in record.documents if doc.doc_type in {"customer_invoice", "supplier_invoice"}))

    def test_india_gst_retail_sales_summary_uses_split_accounts(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_RETAIL_INDIA_GST_SPLIT",
                industry="retail",
                difficulty_level=2,
                assets_root=tmp_dir,
                period_type="year",
                tax_regime_override="india_gst",
            )
            self.assertTrue(any(posting.label == "retail_sale_cash_tax_cgst" and posting.credit_account == "CGST Payable" for posting in record.expected_entries))
            self.assertTrue(any(posting.label == "retail_sale_card_tax_sgst" and posting.credit_account == "SGST Payable" for posting in record.expected_entries))
            self.assertFalse(any(posting.label in {"retail_sale_cash_tax", "retail_sale_card_tax"} and posting.credit_account == "Sales Tax Payable" for posting in record.expected_entries))
            sales_doc = next(doc for doc in record.documents if doc.doc_type == "sales_summary")
            self.assertIn("CGST Amount:", sales_doc.ocr_text)
            self.assertIn("SGST Amount:", sales_doc.ocr_text)

    def test_generic_gst_keeps_generic_tax_accounts(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_FIELD_GENERIC_GST",
                industry="field_services",
                difficulty_level=2,
                assets_root=tmp_dir,
                period_type="month",
                tax_regime_override="gst",
            )
            self.assertTrue(any(posting.credit_account == "Sales Tax Payable" for posting in record.expected_entries))
            self.assertTrue(any(posting.debit_account == "Input Tax Receivable" for posting in record.expected_entries))
            self.assertFalse(any("CGST" in posting.debit_account or "CGST" in posting.credit_account for posting in record.expected_entries))

    def test_utilities_bill_and_equipment_financing_are_disambiguated(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_AP_NOTE_DISAMBIGUATION",
                industry="professional_services",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
            )
            utility_doc = next(doc for doc in record.documents if doc.doc_type == "utilities_statement")
            equipment_doc = next(doc for doc in record.documents if doc.doc_type == "equipment_invoice")
            self.assertIn("UTILITY INVOICE", utility_doc.ocr_text)
            self.assertIn("Invoice Number:", utility_doc.ocr_text)
            self.assertIn("Pay To:", utility_doc.ocr_text)
            self.assertIn("Promissory note payable", equipment_doc.ocr_text)
            self.assertTrue(any(posting.label == "equipment_purchase_financed" and posting.credit_account == "Notes Payable" for posting in record.expected_entries))

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

    def test_forced_negative_control_code_is_respected(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            clean_record = builder.generate_record(
                record_id="TEST_FORCED_NEG_CLEAN",
                industry="subscription_saas",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="year",
            )
            self.assertIn("remeasurement_mismatch", clean_record.metadata["available_inconsistency_codes"])
            forced_record = builder.generate_record(
                record_id="TEST_FORCED_NEG",
                industry="subscription_saas",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="year",
                negative_control=True,
                negative_control_code="remeasurement_mismatch",
            )
            self.assertEqual(forced_record.expected_inconsistency_codes, ["remeasurement_mismatch"])

    def test_tax_regime_override_is_respected(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_TAX_OVERRIDE",
                industry="professional_services",
                difficulty_level=3,
                assets_root=tmp_dir,
                period_type="quarter",
                tax_regime_override="vat",
            )
            self.assertEqual(record.metadata["tax_regime"], "vat")
            self.assertIn("vat", record.metadata["tax_label"].lower())

    def test_us_sales_tax_purchase_embeds_tax_into_inventory_cost(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_US_TAX",
                industry="wholesale_distribution",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
                tax_regime_override="us_sales_tax",
            )
            supplier_doc = next(doc for doc in record.documents if doc.doc_type == "supplier_invoice" and "TAXSUP" in doc.ocr_text)
            total = self._money_after(supplier_doc, "Total")
            embedded = [posting for posting in record.expected_entries if posting.label == "jurisdictional_tax_invoice_us_purchase_cost_includes_tax"]
            self.assertTrue(embedded)
            self.assertEqual(embedded[0].debit_account, "Inventory")
            self.assertEqual(embedded[0].amount, total)
            self.assertFalse(any(posting.debit_account.startswith("Input ") and "jurisdictional_tax_invoice" in posting.label for posting in record.expected_entries))

    def test_india_gst_same_state_uses_cgst_and_sgst(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = self._jurisdictional_tax_record(tmp_dir, same_state=True)
            jurisdictional_entries = [posting for posting in record.expected_entries if posting.label.startswith("jurisdictional_tax_invoice")]
            self.assertTrue(any(posting.debit_account == "Input CGST Receivable" for posting in jurisdictional_entries))
            self.assertTrue(any(posting.debit_account == "Input SGST Receivable" for posting in jurisdictional_entries))
            self.assertFalse(any(posting.debit_account == "Input IGST Receivable" for posting in jurisdictional_entries))

    def test_india_gst_different_state_uses_igst(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = self._jurisdictional_tax_record(tmp_dir, same_state=False)
            jurisdictional_entries = [posting for posting in record.expected_entries if posting.label.startswith("jurisdictional_tax_invoice")]
            self.assertTrue(any(posting.debit_account == "Input IGST Receivable" for posting in jurisdictional_entries))
            self.assertFalse(any(posting.debit_account == "Input CGST Receivable" for posting in jurisdictional_entries))
            self.assertFalse(any(posting.debit_account == "Input SGST Receivable" for posting in jurisdictional_entries))

    def test_exemption_certificate_overrides_default_tax(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_TAX_EXEMPTION",
                industry="wholesale_distribution",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
                tax_regime_override="us_sales_tax",
            )
            exempt_invoice = next(doc for doc in record.documents if doc.doc_type == "customer_invoice" and "Exemption Certificate:" in doc.ocr_text)
            self.assertIn("Tax Rate: 0.00%", exempt_invoice.ocr_text)
            self.assertIn("Tax Amount: $0.00", exempt_invoice.ocr_text)
            self.assertTrue(record.metadata["has_tax_exemption"])

    def _jurisdictional_tax_record(self, tmp_dir, *, same_state):
        for seed in range(40, 80):
            builder = DocumentBenchmarkBuilder(seed=seed)
            record = builder.generate_record(
                record_id=f"TEST_INDIA_GST_{seed}",
                industry="wholesale_distribution",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
                tax_regime_override="india_gst",
            )
            notes = record.metadata.get("scenario_notes", {}).get("jurisdictional_tax_invoice", {})
            if notes.get("same_state") is same_state:
                return record
        raise AssertionError(f"Could not generate India GST same_state={same_state}")

    def test_asc606_ssp_allocation_differs_from_invoice_line_split(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_ASC606",
                industry="subscription_saas",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
            )
            notes = record.metadata["scenario_notes"]["bundled_contract_allocation"]
            self.assertNotEqual(notes["invoice_implementation_line"], notes["implementation_allocated"])
            self.assertEqual(round(notes["implementation_allocated"] + notes["platform_allocated"], 2), notes["transaction_price"])
            impl = next(posting for posting in record.expected_entries if posting.label == "bundled_contract_allocation_implementation_release")
            platform = next(posting for posting in record.expected_entries if posting.label == "bundled_contract_allocation_platform_release")
            self.assertEqual(impl.amount, notes["implementation_allocated"])
            self.assertEqual(platform.amount, notes["platform_release"])

    def test_asset_disposal_removes_cost_accumulated_depreciation_and_records_gain_or_loss(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_ASSET_DISPOSAL",
                industry="professional_services",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
            )
            notice = next(doc for doc in record.documents if doc.doc_type == "asset_disposal_notice")
            cost = self._money_after(notice, "Original Cost")
            accumulated = self._money_after(notice, "Accumulated Depreciation")
            nbv = self._money_after(notice, "Net Book Value")
            proceeds = self._money_after(notice, "Proceeds Amount")
            gain_loss = self._money_after(notice, "Gain Loss Amount")
            self.assertEqual(round(cost - accumulated, 2), nbv)
            self.assertEqual(round(abs(proceeds - nbv), 2), gain_loss)
            self.assertTrue(any(posting.label == "asset_disposal_remove_accumulated_depreciation" for posting in record.expected_entries))
            self.assertTrue(any(posting.credit_account in {"Gain on Disposal", "Equipment", "Furniture"} or posting.debit_account == "Loss on Disposal" for posting in record.expected_entries))

    def test_deferred_tax_liability_ties_to_book_tax_difference(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_DEFERRED_TAX",
                industry="professional_services",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="month",
            )
            memo = next(doc for doc in record.documents if doc.doc_type == "deferred_tax_memo")
            movement = self._money_after(memo, "Current Period Deferred Tax Movement")
            expense = self._money_after(memo, "Deferred Tax Expense Amount")
            ending = self._money_after(memo, "Deferred Tax Liability Ending")
            self.assertEqual(movement, expense)
            self.assertEqual(movement, ending)
            posting = next(posting for posting in record.expected_entries if posting.label == "deferred_tax_depreciation")
            self.assertEqual(posting.debit_account, "Deferred Tax Expense")
            self.assertEqual(posting.credit_account, "Deferred Tax Liability")
            self.assertEqual(posting.amount, movement)

    def test_baseline_lease_schedule_ties_to_liability_and_rou_asset(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_LEASE",
                industry="professional_services",
                difficulty_level=4,
                assets_root=tmp_dir,
                period_type="month",
            )
            schedule = next(doc for doc in record.documents if doc.doc_type == "lease_amortization_schedule")
            opening = self._money_after(schedule, "Opening Liability Balance")
            payment = self._money_after(schedule, "Payment Amount")
            interest = self._money_after(schedule, "Interest Amount")
            principal = self._money_after(schedule, "Principal Amount")
            ending = self._money_after(schedule, "Ending Liability Balance")
            self.assertEqual(round(interest + principal, 2), payment)
            self.assertEqual(round(opening - principal, 2), ending)
            self.assertTrue(any(posting.debit_account == "Right-of-Use Asset" and posting.credit_account == "Lease Liability" for posting in record.expected_entries))

    def test_lease_modification_adjusts_liability_and_rou_asset_by_same_delta(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_LEASE_MOD",
                industry="professional_services",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="month",
            )
            notice = next(doc for doc in record.documents if doc.doc_type == "lease_modification_notice")
            liability_delta = self._money_after(notice, "Liability Remeasurement Delta Amount")
            rou_delta = self._money_after(notice, "ROU Asset Adjustment Amount")
            self.assertEqual(liability_delta, rou_delta)
            posting = next(posting for posting in record.expected_entries if posting.label == "lease_modification")
            self.assertEqual(posting.amount, liability_delta)
            self.assertEqual(posting.debit_account, "Right-of-Use Asset")
            self.assertEqual(posting.credit_account, "Lease Liability")

    def test_new_inconsistency_codes_can_be_forced(self):
        cases = {
            "jurisdiction_tax_mismatch": ("wholesale_distribution", 4, "month", "us_sales_tax"),
            "tax_exemption_conflict": ("wholesale_distribution", 4, "month", "us_sales_tax"),
            "ssp_allocation_mismatch": ("subscription_saas", 4, "month", None),
            "performance_obligation_release_mismatch": ("subscription_saas", 4, "month", None),
            "asset_disposal_mismatch": ("professional_services", 4, "month", None),
            "deferred_tax_rollforward_mismatch": ("professional_services", 5, "month", None),
            "lease_schedule_mismatch": ("professional_services", 4, "month", None),
            "lease_remeasurement_mismatch": ("professional_services", 5, "month", None),
        }
        with tempfile.TemporaryDirectory() as tmp_dir:
            for offset, (code, (industry, level, period_type, tax_regime)) in enumerate(cases.items()):
                builder = DocumentBenchmarkBuilder(seed=42 + offset)
                record = builder.generate_record(
                    record_id=f"TEST_FORCE_{code}",
                    industry=industry,
                    difficulty_level=level,
                    assets_root=tmp_dir,
                    period_type=period_type,
                    negative_control=True,
                    negative_control_code=code,
                    tax_regime_override=tax_regime,
                )
                self.assertEqual(record.expected_inconsistency_codes, [code])

    def test_new_scenarios_appear_only_at_intended_difficulty_levels(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            pro_l3 = DocumentBenchmarkBuilder(seed=42).generate_record("TEST_PRO_L3", "professional_services", 3, tmp_dir, period_type="month")
            pro_l4 = DocumentBenchmarkBuilder(seed=42).generate_record("TEST_PRO_L4", "professional_services", 4, tmp_dir, period_type="month")
            pro_l5 = DocumentBenchmarkBuilder(seed=42).generate_record("TEST_PRO_L5", "professional_services", 5, tmp_dir, period_type="month")
            sub_l3 = DocumentBenchmarkBuilder(seed=42).generate_record("TEST_SUB_L3", "subscription_saas", 3, tmp_dir, period_type="month")
            sub_l4 = DocumentBenchmarkBuilder(seed=42).generate_record("TEST_SUB_L4", "subscription_saas", 4, tmp_dir, period_type="month")
            wh_l3 = DocumentBenchmarkBuilder(seed=42).generate_record("TEST_WH_L3", "wholesale_distribution", 3, tmp_dir, period_type="month")
            wh_l4 = DocumentBenchmarkBuilder(seed=42).generate_record("TEST_WH_L4", "wholesale_distribution", 4, tmp_dir, period_type="month")
            self.assertNotIn("asset_disposal", pro_l3.metadata["scenario_sequence"])
            self.assertIn("asset_disposal", pro_l4.metadata["scenario_sequence"])
            self.assertIn("baseline_lease", pro_l4.metadata["scenario_sequence"])
            self.assertNotIn("lease_modification", pro_l4.metadata["scenario_sequence"])
            self.assertIn("lease_modification", pro_l5.metadata["scenario_sequence"])
            self.assertIn("deferred_tax_depreciation", pro_l5.metadata["scenario_sequence"])
            self.assertNotIn("bundled_contract_allocation", sub_l3.metadata["scenario_sequence"])
            self.assertIn("bundled_contract_allocation", sub_l4.metadata["scenario_sequence"])
            self.assertNotIn("jurisdictional_tax_invoice", wh_l3.metadata["scenario_sequence"])
            self.assertIn("jurisdictional_tax_invoice", wh_l4.metadata["scenario_sequence"])

    def test_new_metadata_tags_appear_in_record_manifest(self):
        builder = DocumentBenchmarkBuilder(seed=42)
        with tempfile.TemporaryDirectory() as tmp_dir:
            record = builder.generate_record(
                record_id="TEST_METADATA_TAGS",
                industry="professional_services",
                difficulty_level=5,
                assets_root=tmp_dir,
                period_type="month",
            )
            row = record_manifest_row(record)
            for key in ("reasoning_depth", "doc_dependency_depth", "subledger_count", "jurisdictional_depth", "temporal_lookback_depth"):
                self.assertIn(key, row)
            self.assertTrue(row["has_asset_disposal"])
            self.assertTrue(row["has_deferred_tax"])
            self.assertTrue(row["has_lease"])
