"""Prompt construction for the document benchmark."""

from __future__ import annotations

import json

from docs_benchmark.inconsistencies import INCONSISTENCY_CODE_DETAILS
from docs_benchmark.schemas import DocumentRecord


def build_prompt(record: DocumentRecord) -> str:
    account_list = json.dumps(record.allowed_accounts, indent=2)
    inconsistency_code_list = json.dumps(INCONSISTENCY_CODE_DETAILS, indent=2)
    lines = [
        "You are given a packet of accounting documents for one reporting period.",
        "Read the documents, infer the journal entries, and produce the final balance sheet.",
        "Some packets may contain distractor documents, secondary copies, cancellation notes, statements, or other non-posting paperwork.",
        "A small number of packets may be internally inconsistent and cannot be reconciled into a sound answer.",
        "Some postings require multiple documents together, such as one payment applied across several invoices, inter-bank transfers, or internal reclassification memos.",
        "",
        "Rules:",
        "- Use only the allowed account names.",
        "- The opening trial balance is starting state only. Do not turn it into journal entries.",
        "- Do not use 'Opening Balance' as an account name.",
        "- Create entries only for period activity and period-end adjustments supported by the documents.",
        "- Some documents are support-only or distractors and should not create entries by themselves.",
        "- One payment document may settle multiple references, and some allocations may be only partial.",
        "- Some cash movements may be transfers between company-controlled bank accounts and should not create revenue or expense.",
        "- Some entries may be internal corrections or reclassifications with no external counterparty.",
        "- If the packet is internally inconsistent, set has_inconsistency to true, choose one or more values from inconsistency_codes, explain briefly in inconsistency_notes, and leave entries as [] and balance_sheet sections empty.",
        "- If has_inconsistency is true, inconsistency_codes must contain at least one key from the allowed list below.",
        "- If the packet is reconcilable, set has_inconsistency to false, set inconsistency_codes to [], and provide the full entries and final balance sheet.",
        "- Use only inconsistency codes from the allowed list below. Do not invent new codes.",
        "- Amounts must be JSON numbers, not strings, and must not contain thousands separators.",
        "- Do not round off any source amounts or final balances beyond normal currency decimals already shown in the documents.",
        "- Return strict JSON only. Do not add markdown or prose.",
        "- The top-level JSON must have exactly these keys: has_inconsistency, inconsistency_codes, inconsistency_notes, entries, balance_sheet.",
        "- Each entry must have doc_refs, debit_account, credit_account, and amount.",
        "- doc_refs must list the document ids that support the posting.",
        "- If one posting depends on multiple documents, include all relevant document ids.",
        "- Use the document ids that are primary evidence for the posting; support-only docs may also be included when needed.",
        "- The final balance sheet must balance: assets = liabilities + equity.",
        "- The balance_sheet object must have exactly these keys: assets, liabilities, equity.",
        "",
        "Record context:",
        f"- Record ID: {record.record_id}",
        f"- Industry: {record.industry}",
        f"- Difficulty level: {record.difficulty_level}",
        f"- Period: {record.metadata.get('period_label', record.period_end)}",
        f"- Period start: {record.period_start}",
        f"- Period end: {record.period_end}",
        f"- Entity: {record.metadata.get('entity_name', 'Unknown Entity')}",
        f"- Document display currency: {record.metadata.get('currency_code', 'USD')} ({record.metadata.get('currency_symbol', '$')})",
        f"- Document date format: {record.metadata.get('date_format', 'YYYY-MM-DD')}",
        "- Some packets may show ISO currency prefixes such as GBP or EUR instead of symbols like $ or £.",
        "",
        "Allowed account names:",
        account_list,
        "",
        "Allowed inconsistency codes:",
        inconsistency_code_list,
        "",
        "Output JSON shape:",
        "{",
        '  "has_inconsistency": false,',
        '  "inconsistency_codes": [],',
        '  "inconsistency_notes": [],',
        '  "entries": [',
        "    {",
        '      "doc_refs": ["D003"],',
        '      "debit_account": "Accounts Receivable",',
        '      "credit_account": "Service Revenue",',
        '      "amount": 1250.0',
        "    }",
        "  ],",
        '  "balance_sheet": {',
        '    "assets": {},',
        '    "liabilities": {},',
        '    "equity": {}',
        "  }",
        "}",
        "",
        "Example for an inconsistent packet:",
        "{",
        '  "has_inconsistency": true,',
        '  "inconsistency_codes": ["bank_closing_mismatch"],',
        '  "inconsistency_notes": ["Bank closing balance does not tie to the listed statement rows."],',
        '  "entries": [],',
        '  "balance_sheet": {',
        '    "assets": {},',
        '    "liabilities": {},',
        '    "equity": {}',
        "  }",
        "}",
        "",
        "Documents:",
    ]

    for document in record.documents:
        lines.extend(
            [
                "",
                f"Document ID: {document.doc_id}",
                f"Document Type: {document.doc_type}",
                f"Document Title: {document.title}",
                "Document OCR Text:",
                document.ocr_text.strip() or "(empty document text)",
            ]
        )

    return "\n".join(lines).strip() + "\n"
