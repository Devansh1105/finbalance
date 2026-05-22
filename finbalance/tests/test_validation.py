import unittest

from finbalance.schemas import BalanceSheet, DocumentAsset, DocumentSeed, Posting
from finbalance.types import PeriodSpec, ValidationReport
from finbalance.validation.doc_validation import validate_document_seed
from finbalance.validation.record_validation import validate_record_bundle


class ValidationTests(unittest.TestCase):
    def test_missing_required_field_is_reported(self):
        seed = DocumentSeed(
            doc_id="D001",
            doc_type="customer_invoice",
            role="posting_doc",
            title="Customer Invoice",
            date="2024-04-10",
            fields={
                "number": "INV-0001",
                "customer": "Blue Finch Holdings",
                "line_items": [{"description": "Consulting", "amount": 500.0}],
                "total": 500.0,
            },
            metadata={},
        )
        report = ValidationReport()
        validate_document_seed(seed, "professional_services", report)
        self.assertFalse(report.ok)
        self.assertTrue(any("due_date" in issue.message for issue in report.errors))

    def test_posting_account_outside_allowed_accounts_is_reported(self):
        report = validate_record_bundle(
            industry="professional_services",
            period_spec=PeriodSpec(
                period_type="month",
                start_date="2024-04-01",
                end_date="2024-04-30",
                label="April 2024",
                month_count=1,
                fiscal_start_month=1,
            ),
            allowed_accounts=["Cash", "Owner's Equity"],
            documents=[
                DocumentSeed(
                    doc_id="D001",
                    doc_type="opening_trial_balance",
                    role="posting_doc",
                    title="Opening Trial Balance",
                    date="2024-04-01",
                    fields={
                        "statement_date": "2024-04-01",
                        "account_lines": [{"section": "assets", "account": "Cash", "amount": 1000.0}],
                        "prepared_by": "Test Harness",
                    },
                    metadata={},
                )
            ],
            rendered_documents=[
                DocumentAsset(
                    doc_id="D001",
                    doc_type="opening_trial_balance",
                    role="posting_doc",
                    title="Opening Trial Balance",
                    date="2024-04-01",
                    asset_path="/tmp/D001.pdf",
                    ocr_text="Statement Date: 2024-04-01",
                    metadata={},
                )
            ],
            postings=[
                Posting(
                    doc_refs=["D001"],
                    debit_account="Cash",
                    credit_account="Service Revenue",
                    amount=100.0,
                    posting_date="2024-04-02",
                )
            ],
            balance_sheet=BalanceSheet(
                date="2024-04-30",
                assets={"Cash": 1000.0},
                liabilities={},
                equity={"Owner's Equity": 1000.0},
                total_assets=1000.0,
                total_liabilities=0.0,
                total_equity=1000.0,
                balanced=True,
            ),
        )
        self.assertFalse(report.ok)
        self.assertTrue(any("outside the allowed account list" in issue.message for issue in report.errors))

    def test_self_posting_is_reported(self):
        report = validate_record_bundle(
            industry="professional_services",
            period_spec=PeriodSpec(
                period_type="month",
                start_date="2024-04-01",
                end_date="2024-04-30",
                label="April 2024",
                month_count=1,
                fiscal_start_month=1,
            ),
            allowed_accounts=["Cash"],
            documents=[
                DocumentSeed(
                    doc_id="D001",
                    doc_type="opening_trial_balance",
                    role="posting_doc",
                    title="Opening Trial Balance",
                    date="2024-04-01",
                    fields={
                        "statement_date": "2024-04-01",
                        "account_lines": [{"section": "assets", "account": "Cash", "amount": 1000.0}],
                    },
                    metadata={},
                )
            ],
            rendered_documents=[
                DocumentAsset(
                    doc_id="D001",
                    doc_type="opening_trial_balance",
                    role="posting_doc",
                    title="Opening Trial Balance",
                    date="2024-04-01",
                    asset_path="/tmp/D001.pdf",
                    ocr_text="Statement Date: 2024-04-01",
                    metadata={},
                )
            ],
            postings=[
                Posting(
                    doc_refs=["D001"],
                    debit_account="Cash",
                    credit_account="Cash",
                    amount=100.0,
                    posting_date="2024-04-02",
                )
            ],
            balance_sheet=BalanceSheet(
                date="2024-04-30",
                assets={"Cash": 1000.0},
                liabilities={},
                equity={"Owner's Equity": 1000.0},
                total_assets=1000.0,
                total_liabilities=0.0,
                total_equity=1000.0,
                balanced=True,
            ),
        )
        self.assertFalse(report.ok)
        self.assertTrue(any("same account on both sides" in issue.message for issue in report.errors))
