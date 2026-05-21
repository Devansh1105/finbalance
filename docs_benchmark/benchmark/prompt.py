"""Prompt construction for the document benchmark."""

from __future__ import annotations

import json
from typing import Final

from docs_benchmark.inconsistencies import INCONSISTENCY_CODE_DETAILS
from docs_benchmark.schemas import DocumentRecord


PROMPT_VARIANT_BASELINE: Final = "baseline"
PROMPT_VARIANT_GUIDED_PRIVATE_SOLVE: Final = "guided_private_solve"
PROMPT_VARIANT_SELF_CHECK: Final = "self_check"
PROMPT_VARIANT_BALANCE_RECONSTRUCTION: Final = "balance_reconstruction_prompt"
PROMPT_VARIANTS: Final = (
    PROMPT_VARIANT_BASELINE,
    PROMPT_VARIANT_GUIDED_PRIVATE_SOLVE,
    PROMPT_VARIANT_SELF_CHECK,
    PROMPT_VARIANT_BALANCE_RECONSTRUCTION,
)

VISIBILITY_VARIANT_NORMAL: Final = "normal"
VISIBILITY_VARIANT_OCR_ONLY: Final = "ocr_only"
VISIBILITY_VARIANT_NO_DISTRACTORS_ORACLE: Final = "no_distractors_oracle"
VISIBILITY_VARIANT_SUPPORT_DOCS_REMOVED: Final = "support_docs_removed"
VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS: Final = "no_allowed_accounts"
VISIBILITY_VARIANT_EVIDENCE_ONLY: Final = "evidence_only"
VISIBILITY_VARIANT_EVIDENCE_PLUS_5_DISTRACTORS: Final = "evidence_plus_5_distractors"
VISIBILITY_VARIANT_EVIDENCE_PLUS_15_DISTRACTORS: Final = "evidence_plus_15_distractors"
VISIBILITY_VARIANT_EVIDENCE_PLUS_30_DISTRACTORS: Final = "evidence_plus_30_distractors"
VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST: Final = "evidence_relevant_last"
VISIBILITY_VARIANTS: Final = (
    VISIBILITY_VARIANT_NORMAL,
    VISIBILITY_VARIANT_OCR_ONLY,
    VISIBILITY_VARIANT_NO_DISTRACTORS_ORACLE,
    VISIBILITY_VARIANT_SUPPORT_DOCS_REMOVED,
    VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS,
    VISIBILITY_VARIANT_EVIDENCE_ONLY,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_5_DISTRACTORS,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_15_DISTRACTORS,
    VISIBILITY_VARIANT_EVIDENCE_PLUS_30_DISTRACTORS,
    VISIBILITY_VARIANT_EVIDENCE_RELEVANT_LAST,
)


def build_prompt(
    record: DocumentRecord,
    *,
    prompt_variant: str = PROMPT_VARIANT_BASELINE,
    visibility_variant: str = VISIBILITY_VARIANT_NORMAL,
) -> str:
    if prompt_variant not in PROMPT_VARIANTS:
        raise ValueError(f"Unknown prompt variant '{prompt_variant}'")
    if visibility_variant not in VISIBILITY_VARIANTS:
        raise ValueError(f"Unknown visibility variant '{visibility_variant}'")

    include_allowed_accounts = visibility_variant != VISIBILITY_VARIANT_NO_ALLOWED_ACCOUNTS and bool(record.allowed_accounts)
    account_list = json.dumps(record.allowed_accounts, indent=2)
    inconsistency_code_list = json.dumps(INCONSISTENCY_CODE_DETAILS, indent=2)
    lines = [
        "You are given a packet of accounting documents for one reporting period.",
        "Read the documents, infer the journal entries, and produce the final balance sheet.",
        "Some packets may contain distractor documents, secondary copies, cancellation notes, statements, or other non-posting paperwork.",
        "A small number of packets may be internally inconsistent and cannot be reconciled into a sound answer.",
        "Some postings require multiple documents together, such as one payment applied across several invoices, inter-bank transfers, or internal reclassification memos.",
        "Some invoices and bills include indirect tax such as sales tax, VAT, or GST.",
        "Packets may contain country-specific tax rules, exemption certificates, and jurisdiction profiles.",
        "Packets may contain ASC 606 bundled contracts where invoice line items do not equal the accounting allocation.",
        "Packets may contain fixed asset disposals, deferred tax from book/tax depreciation differences, lease accounting, or lease modifications.",
        "Some documents may be denominated in a foreign currency while the final answer still needs to be expressed in the functional currency for the record.",
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
        "- Do not fold indirect tax into revenue, inventory, or expense when the document shows tax separately.",
        "- US sales tax on purchases is embedded in the asset, inventory, or expense cost unless a visible support document says otherwise.",
        "- India GST uses CGST plus SGST for same-state transactions and IGST for different-state transactions.",
        "- Exemption certificates can override the default tax treatment when the certificate is valid for the counterparty and period.",
        "- For ASC 606 bundled contracts, use visible SSP rate cards and performance-obligation schedules; invoice line splits may differ from accounting allocation.",
        "- Implementation revenue is released on acceptance when an implementation acceptance memo supports it.",
        "- Platform or subscription revenue is released ratably only when the schedule supports the release amount.",
        "- For fixed asset disposals, compute net book value from original cost less accumulated depreciation, remove both cost and accumulated depreciation, and record proceeds plus gain or loss.",
        "- For deferred tax, use only visible book depreciation, tax depreciation, tax rates, and deferred tax rollforward support.",
        "- For leases, use visible lease agreements, amortization schedules, payment notices, and modification notices for ROU asset, liability, interest, principal, amortization, and remeasurement entries.",
        "- Use the exchange-rate evidence shown in the packet when a document is denominated in a foreign currency.",
        "- Use only visible rates, SSPs, tax rules, schedules, and support documents; do not invent missing exchange rates, tax rates, SSPs, lease rates, or assumptions.",
        "- Return all journal entries and the final balance sheet in the functional currency shown in the record context.",
        "- If the packet is internally inconsistent, set has_inconsistency to true, choose one or more values from inconsistency_codes, explain briefly in inconsistency_notes, and leave entries as [] and balance_sheet sections empty.",
        "- If has_inconsistency is true, inconsistency_codes must contain at least one key from the allowed list below.",
        "- If the packet is reconcilable, set has_inconsistency to false, set inconsistency_codes to [], and provide the full entries and final balance sheet.",
        "- Use only inconsistency codes from the allowed list below. Do not invent new codes.",
        "- Amounts must be JSON numbers, not strings, and must not contain thousands separators.",
        "- Do not round except to cents for final monetary amounts.",
        "- Return strict JSON only. Do not add markdown or prose.",
        "- The top-level JSON must have exactly these keys: has_inconsistency, inconsistency_codes, inconsistency_notes, entries, balance_sheet.",
        "- Each entry must have doc_refs, debit_account, credit_account, and amount.",
        "- doc_refs must list the document ids that support the posting.",
        "- If one posting depends on multiple documents, include all relevant document ids.",
        "- Use the document ids that are primary evidence for the posting; support-only docs may also be included when needed.",
        "- The final balance sheet must balance: assets = liabilities + equity.",
        "- The balance_sheet object must have exactly these keys: assets, liabilities, equity.",
    ]
    if not include_allowed_accounts:
        lines.remove("- Use only the allowed account names.")
    if prompt_variant in {PROMPT_VARIANT_GUIDED_PRIVATE_SOLVE, PROMPT_VARIANT_SELF_CHECK}:
        lines.extend(
            [
                "",
                "Private workflow before the final JSON:",
                "- Identify posting documents, support documents, adjustment documents, and distractors.",
                "- Link each posting to the primary and support documents that determine it.",
                "- Compute journal entries from visible amounts, rates, allocations, schedules, and rollforwards.",
                "- Reconstruct the balance sheet from the opening trial balance plus proposed entries.",
                "- Check whether visible documents contradict each other before deciding inconsistency codes.",
                "- Return only the strict JSON answer after this private workflow.",
            ]
        )
    if prompt_variant == PROMPT_VARIANT_SELF_CHECK:
        lines.extend(
            [
                "",
                "Private final verification:",
                "- Verify that the journal entries reconstruct the submitted balance sheet.",
                "- Verify that any inconsistency code is supported by a visible contradiction.",
                "- Verify that reconcilable packets have no missing or extra period activity.",
            ]
        )
    if prompt_variant == PROMPT_VARIANT_BALANCE_RECONSTRUCTION:
        lines.extend(
            [
                "",
                "Private balance reconstruction workflow:",
                "- First derive the journal entries from the visible documents.",
                "- Compute the final balance sheet only by applying those entries to the opening trial balance.",
                "- Do not independently estimate or restate the final balance sheet.",
                "- Verify that assets equal liabilities plus equity before returning the strict JSON answer.",
            ]
        )
    lines.extend(
        [
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
            f"- Functional currency for the answer: {record.metadata.get('functional_currency_code', record.metadata.get('currency_code', 'USD'))}",
            f"- Document date format: {record.metadata.get('date_format', 'YYYY-MM-DD')}",
            f"- Indirect tax regime for this packet: {record.metadata.get('tax_regime', 'none')}",
            "- Some packets may show ISO currency prefixes such as GBP or EUR instead of symbols like $ or £.",
            "",
        ]
    )
    if include_allowed_accounts:
        lines.extend(
            [
                "Allowed account names:",
                account_list,
                "",
            ]
        )
    lines.extend(
        [
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
    )

    for document in record.documents:
        if visibility_variant == VISIBILITY_VARIANT_OCR_ONLY:
            lines.extend(
                [
                    "",
                    f"Document ID: {document.doc_id}",
                    "Document OCR Text:",
                    document.ocr_text.strip() or "(empty document text)",
                ]
            )
        else:
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
