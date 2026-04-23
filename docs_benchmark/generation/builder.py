"""Schema-driven dataset builder for docs_benchmark."""

from __future__ import annotations

import json
import random
from pathlib import Path

from docs_benchmark.doc_schemas import get_doc_schema
from docs_benchmark.generation.helpers import (
    PERIOD_TYPES,
    choose_display_profile,
    choose_nonstandard_display_profile,
    choose_period_spec,
    doc_seed,
    ensure_period_doc_range,
)
from docs_benchmark.generation.master_data import default_address, default_company_name
from docs_benchmark.industry_schemas import INDUSTRIES, get_industry_schema
from docs_benchmark.inconsistencies import inconsistency_description
from docs_benchmark.ledger import Ledger
from docs_benchmark.render import make_ocr_text, write_text_pdf
from docs_benchmark.rendering import render_document
from docs_benchmark.schemas import BalanceSheet, DocumentAsset, DocumentRecord, ensure_parent
from docs_benchmark.types import BusinessState
from docs_benchmark.validation import validate_record_bundle


DEFAULT_DISTRACTOR_DOC_TYPES = ("secondary_copy", "vendor_statement", "memo", "cancellation_note")


class DocumentBenchmarkBuilder:
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    def generate_record(
        self,
        record_id: str,
        industry: str,
        difficulty_level: int,
        assets_root: str | Path,
        period_type: str = "month",
        negative_control: bool = False,
        display_profile_override: dict[str, str] | None = None,
    ) -> DocumentRecord:
        if industry not in INDUSTRIES:
            raise ValueError(f"Unknown industry '{industry}'")
        if period_type not in PERIOD_TYPES:
            raise ValueError(f"Unknown period type '{period_type}'")
        try:
            ensure_period_doc_range(period_type, difficulty_level)
        except KeyError as exc:
            raise ValueError(f"Unknown difficulty level '{difficulty_level}' for period type '{period_type}'") from exc

        industry_schema = get_industry_schema(industry)
        period_spec = choose_period_spec(self.rng, period_type)
        display_profile = display_profile_override or choose_display_profile(self.rng)
        master_data = industry_schema.master_data_builder(industry, self.rng, period_spec)
        entity_name = default_company_name(self.rng)
        entity_address = default_address(self.rng)
        opening_balance = industry_schema.opening_builder(self.rng, difficulty_level, period_spec)
        state = BusinessState(
            record_id=record_id,
            industry=industry,
            difficulty_level=difficulty_level,
            period_spec=period_spec,
            period_start=period_spec.start_date,
            period_end=period_spec.end_date,
            entity_name=entity_name,
            entity_address=entity_address,
            currency_code=display_profile["currency_code"],
            currency_symbol=display_profile["currency_symbol"],
            currency_format=display_profile["currency_format"],
            date_format=display_profile["date_format"],
            opening_balance=opening_balance,
            master_data=master_data,
            bank_accounts={
                "Cash": {
                    "account_number": f"1002-{record_id[-4:]}",
                    "display_name": "Operating Account",
                }
            },
        )
        self._seed_asset_register_from_opening(state)

        state.documents.append(self._opening_trial_balance_doc(state))
        scenario_names = self._select_scenarios(industry_schema, difficulty_level, period_type)
        for scenario_name in scenario_names:
            scenario = industry_schema.scenarios[scenario_name]
            bundle = scenario.builder(state, self.rng)
            state.documents.extend(bundle.documents)
            state.postings.extend(bundle.postings)
            state.bank_rows.extend(bundle.bank_rows)
            state.scenario_log.append(scenario_name)
            if bundle.notes:
                state.metadata.setdefault("scenario_notes", {})[scenario_name] = bundle.notes

        self._add_distractors(state, industry_schema)
        state.documents.extend(self._bank_statement_docs(state))
        ordered_documents = self._sorted_documents(state.documents)
        asset_dir = Path(assets_root) / record_id
        rendered_documents = [render_document(seed, asset_dir, self.rng, industry) for seed in ordered_documents]

        ledger = Ledger(opening_balance)
        ledger.apply_all(state.postings)
        balance_sheet = ledger.build_balance_sheet(state.period_end)
        validation = validate_record_bundle(
            industry=industry,
            period_spec=period_spec,
            allowed_accounts=industry_schema.allowed_accounts,
            documents=ordered_documents,
            rendered_documents=rendered_documents,
            postings=state.postings,
            balance_sheet=balance_sheet,
        )
        if not validation.ok:
            lines = [f"{issue.scope}: {issue.message}" for issue in validation.errors]
            raise ValueError(f"Record '{record_id}' failed validation:\n" + "\n".join(lines))

        expected_entries = state.postings
        expected_balance_sheet = balance_sheet
        expected_inconsistency = False
        inconsistency_codes: list[str] = []
        inconsistency_reasons: list[str] = []
        if negative_control:
            rendered_documents, inconsistency_codes, inconsistency_reasons = self._inject_negative_control(rendered_documents, state)
            expected_entries = []
            expected_balance_sheet = self._empty_balance_sheet(state.period_end)
            expected_inconsistency = True

        return DocumentRecord(
            record_id=record_id,
            industry=industry,
            difficulty_level=difficulty_level,
            period_start=state.period_start,
            period_end=state.period_end,
            opening_balance=opening_balance,
            allowed_accounts=industry_schema.allowed_accounts,
            documents=rendered_documents,
            expected_entries=expected_entries,
            expected_balance_sheet=expected_balance_sheet,
            expected_inconsistency=expected_inconsistency,
            expected_inconsistency_codes=inconsistency_codes,
            inconsistency_reasons=inconsistency_reasons,
            metadata={
                "version": "v3_schema_driven",
                "entity_name": entity_name,
                "entity_address": entity_address,
                "industry_label": industry_schema.display_name,
                "scenario_sequence": state.scenario_log,
                "validation": validation.to_dict(),
                "target_doc_range": ensure_period_doc_range(period_type, difficulty_level),
                "period_type": period_type,
                "period_label": period_spec.label,
                "fiscal_start_month": period_spec.fiscal_start_month,
                "currency_code": state.currency_code,
                "currency_symbol": state.currency_symbol,
                "currency_format": state.currency_format,
                "date_format": state.date_format,
                "expected_inconsistency": expected_inconsistency,
                "expected_inconsistency_codes": inconsistency_codes,
                "inconsistency_reasons": inconsistency_reasons,
            },
        )

    def generate_dataset(
        self,
        counts: dict[str, dict[str, dict[int, int]] | dict[int, int]],
        output_path: str | Path,
        assets_root: str | Path,
        negative_control_rate: float = 0.05,
    ) -> list[DocumentRecord]:
        path = ensure_parent(output_path)
        records: list[DocumentRecord] = []
        next_id = 1
        total_records = sum(
            count
            for period_counts in counts.values()
            for level_counts in self._normalize_counts(period_counts).values()
            for count in level_counts.values()
        )
        negative_target = max(1, round(total_records * negative_control_rate)) if total_records and negative_control_rate > 0 else 0
        negative_indices = set(self.rng.sample(range(total_records), k=min(negative_target, total_records))) if negative_target else set()
        nonstandard_target = max(1, round(total_records * 0.05)) if total_records else 0
        nonstandard_indices = set(self.rng.sample(range(total_records), k=min(nonstandard_target, total_records))) if nonstandard_target else set()
        current_index = 0
        with Path(path).open("w", encoding="utf-8") as handle:
            for industry, period_counts in counts.items():
                normalized = self._normalize_counts(period_counts)
                for period_type, level_counts in normalized.items():
                    for level, count in sorted(level_counts.items()):
                        for _ in range(count):
                            prefix = industry.split("_")[0][:3].upper()
                            period_code = period_type[0].upper()
                            record_id = f"DB_{prefix}_{period_code}{level}_{next_id:05d}"
                            next_id += 1
                            record = self.generate_record(
                                record_id,
                                industry,
                                level,
                                assets_root,
                                period_type=period_type,
                                negative_control=current_index in negative_indices,
                                display_profile_override=choose_nonstandard_display_profile(self.rng) if current_index in nonstandard_indices else None,
                            )
                            current_index += 1
                            handle.write(json.dumps(record.to_dict(), ensure_ascii=True) + "\n")
                            records.append(record)
        return records

    def _normalize_counts(self, counts_for_industry):
        if not counts_for_industry:
            return {period_type: {} for period_type in PERIOD_TYPES}
        sample_key = next(iter(counts_for_industry))
        if isinstance(sample_key, int):
            return {period_type: dict(counts_for_industry) for period_type in PERIOD_TYPES}
        return counts_for_industry

    def _select_scenarios(self, industry_schema, difficulty_level: int, period_type: str) -> list[str]:
        plan = industry_schema.period_plans[period_type][difficulty_level]
        selected = [name for name in plan.mandatory if period_type in industry_schema.scenarios[name].period_types]
        use_counts: dict[str, int] = {}
        for name in selected:
            use_counts[name] = use_counts.get(name, 0) + 1

        target_min, target_max = ensure_period_doc_range(period_type, difficulty_level)
        current_docs = 2 + sum(industry_schema.scenarios[name].doc_count_hint for name in selected)
        unique_pool = [name for name in dict.fromkeys(plan.optional) if period_type in industry_schema.scenarios[name].period_types]
        self.rng.shuffle(unique_pool)
        for name in unique_pool:
            if current_docs >= target_min:
                break
            scenario = industry_schema.scenarios[name]
            if not scenario.allow_repeat and use_counts.get(name, 0) >= 1:
                continue
            selected.append(name)
            use_counts[name] = use_counts.get(name, 0) + 1
            current_docs += scenario.doc_count_hint

        repeatable_pool = [name for name in unique_pool if industry_schema.scenarios[name].allow_repeat]
        attempts = 0
        while current_docs < target_min and repeatable_pool and attempts < 100:
            attempts += 1
            name = self.rng.choice(repeatable_pool)
            scenario = industry_schema.scenarios[name]
            selected.append(name)
            use_counts[name] = use_counts.get(name, 0) + 1
            current_docs += scenario.doc_count_hint
            if current_docs >= target_max and self.rng.random() < 0.7:
                break
        return selected

    def _opening_trial_balance_doc(self, state: BusinessState):
        rows = []
        for section_name, accounts in (
            ("assets", state.opening_balance.assets),
            ("liabilities", state.opening_balance.liabilities),
            ("equity", state.opening_balance.equity),
        ):
            for account, amount in accounts.items():
                rows.append({"section": section_name, "account": account, "amount": round(float(amount), 2)})
        schema = get_doc_schema("opening_trial_balance")
        return doc_seed(
            state,
            doc_type=schema.doc_type,
            title=schema.title,
            date=state.period_start,
            role="posting_doc",
            fields={"statement_date": state.period_start, "account_lines": rows, "prepared_by": "Synthetic finance engine"},
            metadata={"footer_note": "Opening balances are source inputs and should tie to the rest of the packet."},
        )

    def _bank_statement_docs(self, state: BusinessState):
        schema = get_doc_schema("bank_statement")
        rows_by_account: dict[str, list[dict[str, object]]] = {}
        for raw in sorted(state.bank_rows, key=lambda row: (row["date"], row["description"], row.get("account", "Cash"))):
            account_name = str(raw.get("account", "Cash"))
            rows_by_account.setdefault(account_name, []).append(raw)
            self._ensure_bank_account(state, account_name)

        account_names = []
        for account_name, details in state.bank_accounts.items():
            opening_balance = round(float(state.opening_balance.assets.get(account_name, 0.0)), 2)
            if opening_balance > 0.0 or rows_by_account.get(account_name):
                account_names.append(account_name)
        if not account_names:
            account_names = ["Cash"]
            self._ensure_bank_account(state, "Cash")

        ordered_accounts = sorted(account_names, key=lambda name: (0 if name == "Cash" else 1, name))
        documents = []
        for account_name in ordered_accounts:
            opening_balance = round(float(state.opening_balance.assets.get(account_name, 0.0)), 2)
            running_balance = opening_balance
            rows = []
            for raw in rows_by_account.get(account_name, []):
                running_balance = round(running_balance + float(raw["amount"]), 2)
                rows.append(
                    {
                        "date": raw["date"],
                        "description": raw["description"],
                        "amount": round(float(raw["amount"]), 2),
                        "running_balance": running_balance,
                    }
                )
            bank_account = state.bank_accounts[account_name]
            documents.append(
                doc_seed(
                    state,
                    doc_type=schema.doc_type,
                    title=schema.title,
                    date=state.period_end,
                    role="support_doc",
                    fields={
                        "account_name": bank_account["display_name"],
                        "account_number": bank_account["account_number"],
                        "opening_balance": opening_balance,
                        "closing_balance": running_balance,
                        "rows": rows,
                    },
                    metadata={
                        "footer_note": "Generated from the internal cash ledger so that every listed movement is consistent.",
                        "bank_account_name": account_name,
                    },
                )
            )
        return documents

    def _sorted_documents(self, documents):
        opening = [doc for doc in documents if doc.doc_type == "opening_trial_balance"]
        bank = [doc for doc in documents if doc.doc_type == "bank_statement"]
        rest = [doc for doc in documents if doc.doc_type not in {"opening_trial_balance", "bank_statement"}]
        rest.sort(key=lambda item: (item.date, item.doc_id))
        return opening + rest + bank

    def _seed_asset_register_from_opening(self, state: BusinessState) -> None:
        useful_life_months = {
            "Equipment": 48,
            "Furniture": 60,
            "Vehicles": 48,
            "Store Fixtures": 60,
        }
        for account, life in useful_life_months.items():
            cost = round(float(state.opening_balance.assets.get(account, 0.0)), 2)
            if cost <= 0:
                continue
            state.asset_register.append(
                {
                    "asset_name": account,
                    "asset_tag": f"OPEN-{account[:3].upper()}",
                    "cost": cost,
                    "useful_life_months": life,
                    "monthly_charge": round(cost / life, 2),
                }
            )

    def _add_distractors(self, state: BusinessState, industry_schema) -> None:
        distractor_types = industry_schema.distractor_doc_types or DEFAULT_DISTRACTOR_DOC_TYPES
        if not distractor_types:
            return
        core_doc_count = len(state.documents)
        target_count = 0
        if state.period_spec.period_type == "year":
            ratio = self.rng.uniform(0.10, 0.25)
            target_count = max(1, round(core_doc_count * ratio))
        elif state.period_spec.period_type == "quarter" and self.rng.random() < 0.5:
            target_count = max(1, round(core_doc_count * self.rng.uniform(0.05, 0.12)))
        elif state.period_spec.period_type == "month" and self.rng.random() < 0.2:
            target_count = 1

        builders = {
            "secondary_copy": self._secondary_copy_doc,
            "vendor_statement": self._vendor_statement_doc,
            "memo": self._memo_doc,
            "cancellation_note": self._cancellation_note_doc,
        }
        added = 0
        attempts = 0
        while added < target_count and attempts < target_count * 6:
            attempts += 1
            doc_type = self.rng.choice(distractor_types)
            builder = builders.get(doc_type)
            if not builder:
                continue
            seed = builder(state)
            if seed is None:
                continue
            state.documents.append(seed)
            added += 1

    def _secondary_copy_doc(self, state: BusinessState):
        candidates = [doc for doc in state.documents if doc.doc_type in {"customer_invoice", "vendor_invoice", "supplier_invoice", "patient_invoice"}]
        if not candidates:
            return None
        source = self.rng.choice(candidates)
        reference = source.fields.get("number") or source.fields.get("invoice_number")
        counterparty = source.fields.get("customer") or source.fields.get("vendor") or source.fields.get("supplier") or source.fields.get("patient_name")
        total = source.fields.get("total")
        if not (reference and counterparty and total):
            return None
        return doc_seed(
            state,
            doc_type="secondary_copy",
            title=get_doc_schema("secondary_copy").title,
            date=source.date,
            role="distractor_doc",
            fields={
                "copy_id": state.next_number("COPY"),
                "source_reference": reference,
                "counterparty": counterparty,
                "total": total,
                "copy_context": self.rng.choice(
                    [
                        "Scanned from the archive packet after the month-end close.",
                        "Forwarded copy attached to the customer correspondence bundle.",
                        "Second scan captured during the filing review.",
                    ]
                ),
            },
            metadata={"counterparty_name": counterparty, "footer_note": "Filed with the scanned month-end paperwork."},
        )

    def _vendor_statement_doc(self, state: BusinessState):
        payables = [item for item in state.open_payables if item.get("category") in {"vendor", "utility"}]
        if not payables:
            return None
        vendor = self.rng.choice(payables)["counterparty"]
        lines = [
            {
                "reference": item["reference"],
                "document_type": "Open invoice",
                "amount": round(float(item["remaining"]), 2),
                "status": "Outstanding",
            }
            for item in payables
            if item["counterparty"] == vendor
        ]
        if not lines:
            return None
        closing_balance = round(sum(line["amount"] for line in lines), 2)
        return doc_seed(
            state,
            doc_type="vendor_statement",
            title=get_doc_schema("vendor_statement").title,
            date=state.period_end,
            role="distractor_doc",
            fields={
                "statement_number": state.next_number("VSTMT"),
                "vendor": vendor,
                "closing_balance": closing_balance,
                "lines": lines,
            },
            metadata={"counterparty_name": vendor, "footer_note": "Period-end statement received from the vendor billing desk."},
        )

    def _memo_doc(self, state: BusinessState):
        subjects = [
            "Annual leave policy reminder",
            "Quarter-end packet routing note",
            "Document retention reminder",
            "Scanning checklist for back-office staff",
        ]
        audiences = ["Operations Team", "Finance Team", "All Staff", "Back Office"]
        narratives = [
            "Please route scanned paperwork to the shared archive after the period binder is complete.",
            "The packet may include supporting correspondence gathered during the close review.",
            "Follow the internal document-retention checklist before the binder is archived.",
        ]
        memo_date = state.period_end if state.period_spec.period_type != "month" else state.period_start
        return doc_seed(
            state,
            doc_type="memo",
            title=get_doc_schema("memo").title,
            date=memo_date,
            role="distractor_doc",
            fields={
                "memo_id": state.next_number("INFO"),
                "subject": self.rng.choice(subjects),
                "audience": self.rng.choice(audiences),
                "narrative": self.rng.choice(narratives),
            },
            metadata={"footer_note": "Administrative note included in the scanned packet."},
        )

    def _cancellation_note_doc(self, state: BusinessState):
        candidates = [doc for doc in state.documents if doc.doc_type == "customer_invoice"]
        if not candidates:
            return None
        source = self.rng.choice(candidates)
        source_reference = source.fields.get("number")
        if not source_reference:
            return None
        return doc_seed(
            state,
            doc_type="cancellation_note",
            title=get_doc_schema("cancellation_note").title,
            date=min(state.period_end, source.date),
            role="distractor_doc",
            fields={
                "note_number": state.next_number("CNCL"),
                "withdrawn_reference": f"{source_reference}-OLD",
                "replacement_reference": source_reference,
                "reason": self.rng.choice(
                    [
                        "Earlier billing reference was withdrawn after the customer requested a corrected copy.",
                        "Prior draft billing reference was superseded during the review cycle.",
                        "Billing desk replaced the earlier reference after an internal review.",
                    ]
                ),
            },
            metadata={"counterparty_name": source.fields.get("customer")},
        )

    def _inject_negative_control(self, rendered_documents: list[DocumentAsset], state: BusinessState) -> tuple[list[DocumentAsset], list[str], list[str]]:
        invoice_docs = [doc for doc in rendered_documents if doc.doc_type in {"customer_invoice", "vendor_invoice", "supplier_invoice", "patient_invoice"}]
        candidates = []
        if invoice_docs:
            candidates.append("invoice_total_mismatch")
        if any(doc.doc_type == "bank_statement" for doc in rendered_documents):
            candidates.append("bank_closing_mismatch")
        if any(doc.doc_type == "vendor_statement" for doc in rendered_documents):
            candidates.append("statement_balance_mismatch")
        if any(doc.doc_type == "payment_advice" and "Allocation Details" in doc.ocr_text for doc in rendered_documents):
            candidates.append("payment_allocation_mismatch")
        if any(doc.doc_type == "secondary_copy" for doc in rendered_documents):
            candidates.append("duplicate_reference_conflict")
        if any(doc.doc_type in {"revenue_recognition_schedule", "fixed_asset_rollforward"} for doc in rendered_documents):
            candidates.append("schedule_rollforward_mismatch")
        if any(doc.doc_type == "inventory_rollforward" for doc in rendered_documents):
            candidates.append("inventory_rollforward_mismatch")
        if any(doc.doc_type == "transfer_advice" for doc in rendered_documents):
            candidates.append("transfer_mismatch")
        if any(doc.doc_type == "reclassification_memo" for doc in rendered_documents):
            candidates.append("reclassification_support_mismatch")
        if not candidates:
            return rendered_documents, [], []
        issue = self.rng.choice(candidates)
        if issue == "invoice_total_mismatch":
            doc = self.rng.choice(invoice_docs)
            return self._replace_in_document(
                rendered_documents,
                doc,
                issue,
                self._invoice_total_mismatch_replacement(doc),
            )
        if issue == "bank_closing_mismatch":
            bank_doc = next(doc for doc in rendered_documents if doc.doc_type == "bank_statement")
            return self._replace_in_document(
                rendered_documents,
                bank_doc,
                issue,
                self._bank_closing_mismatch_replacement(bank_doc),
            )
        if issue == "statement_balance_mismatch":
            doc = next(doc for doc in rendered_documents if doc.doc_type == "vendor_statement")
            return self._replace_in_document(rendered_documents, doc, issue, self._statement_balance_mismatch_replacement(doc))
        if issue == "payment_allocation_mismatch":
            doc = next(doc for doc in rendered_documents if doc.doc_type == "payment_advice" and "Allocation Details" in doc.ocr_text)
            return self._replace_in_document(rendered_documents, doc, issue, self._payment_allocation_mismatch_replacement(doc))
        if issue == "duplicate_reference_conflict":
            doc = next(doc for doc in rendered_documents if doc.doc_type == "secondary_copy")
            return self._replace_in_document(rendered_documents, doc, issue, self._duplicate_reference_conflict_replacement(doc))
        if issue == "schedule_rollforward_mismatch":
            doc = next(doc for doc in rendered_documents if doc.doc_type in {"revenue_recognition_schedule", "fixed_asset_rollforward"})
            return self._replace_in_document(rendered_documents, doc, issue, self._schedule_rollforward_mismatch_replacement(doc))
        if issue == "inventory_rollforward_mismatch":
            doc = next(doc for doc in rendered_documents if doc.doc_type == "inventory_rollforward")
            return self._replace_in_document(rendered_documents, doc, issue, self._inventory_rollforward_mismatch_replacement(doc))
        if issue == "transfer_mismatch":
            doc = next(doc for doc in rendered_documents if doc.doc_type == "transfer_advice")
            return self._replace_in_document(rendered_documents, doc, issue, self._transfer_mismatch_replacement(doc))
        doc = next(doc for doc in rendered_documents if doc.doc_type == "reclassification_memo")
        return self._replace_in_document(rendered_documents, doc, issue, self._reclassification_support_mismatch_replacement(doc))

    def _replace_in_document(
        self,
        rendered_documents: list[DocumentAsset],
        target: DocumentAsset,
        inconsistency_code: str,
        replacement: tuple[str, str],
    ) -> tuple[list[DocumentAsset], list[str], list[str]]:
        old_text, new_text = replacement
        if not old_text or old_text == new_text:
            return rendered_documents, [], []
        updated_documents: list[DocumentAsset] = []
        for document in rendered_documents:
            if document.doc_id != target.doc_id:
                updated_documents.append(document)
                continue
            updated_ocr = document.ocr_text.replace(old_text, new_text, 1)
            write_text_pdf(document.asset_path, updated_ocr.splitlines())
            updated_documents.append(
                DocumentAsset(
                    doc_id=document.doc_id,
                    doc_type=document.doc_type,
                    role=document.role,
                    title=document.title,
                    date=document.date,
                    asset_path=document.asset_path,
                    ocr_text=make_ocr_text(updated_ocr.splitlines()),
                    metadata=dict(document.metadata),
                )
            )
        return updated_documents, [inconsistency_code], [inconsistency_description(inconsistency_code)]

    def _invoice_total_mismatch_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_total = self._first_money_token_after_prefix(document.ocr_text, "Total:")
        if not old_total:
            return ("", "")
        numeric = self._parse_display_amount(old_total, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_total, self._format_display_amount(adjusted, document.metadata)

    def _bank_closing_mismatch_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_balance = self._first_money_token_after_prefix(document.ocr_text, "Closing Balance:")
        if not old_balance:
            return ("", "")
        numeric = self._parse_display_amount(old_balance, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_balance, self._format_display_amount(adjusted, document.metadata)

    def _statement_balance_mismatch_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_balance = self._first_money_token_after_prefix(document.ocr_text, "Closing Balance:")
        if not old_balance:
            return ("", "")
        numeric = self._parse_display_amount(old_balance, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_balance, self._format_display_amount(adjusted, document.metadata)

    def _payment_allocation_mismatch_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_amount = self._first_money_token_after_prefix(document.ocr_text, "Amount:")
        if not old_amount:
            return ("", "")
        numeric = self._parse_display_amount(old_amount, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_amount, self._format_display_amount(adjusted, document.metadata)

    def _duplicate_reference_conflict_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_total = self._first_money_token_after_prefix(document.ocr_text, "Total:")
        if not old_total:
            return ("", "")
        numeric = self._parse_display_amount(old_total, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_total, self._format_display_amount(adjusted, document.metadata)

    def _schedule_rollforward_mismatch_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_ending = self._first_money_token_after_prefix(document.ocr_text, "Ending Deferred:")
        if not old_ending:
            old_ending = self._first_money_token_after_prefix(document.ocr_text, "Ending Balance:")
            if not old_ending:
                return ("", "")
        numeric = self._parse_display_amount(old_ending, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_ending, self._format_display_amount(adjusted, document.metadata)

    def _inventory_rollforward_mismatch_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_ending = self._first_money_token_after_prefix(document.ocr_text, "Ending Balance:")
        if not old_ending:
            return ("", "")
        numeric = self._parse_display_amount(old_ending, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_ending, self._format_display_amount(adjusted, document.metadata)

    def _transfer_mismatch_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_amount = self._first_money_token_after_prefix(document.ocr_text, "Amount:")
        if not old_amount:
            return ("", "")
        numeric = self._parse_display_amount(old_amount, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_amount, self._format_display_amount(adjusted, document.metadata)

    def _reclassification_support_mismatch_replacement(self, document: DocumentAsset) -> tuple[str, str]:
        old_amount = self._first_money_token_after_prefix(document.ocr_text, "Amount:")
        if not old_amount:
            return ("", "")
        numeric = self._parse_display_amount(old_amount, document.metadata)
        adjusted = round(max(0.01, numeric + self._random_mismatch_offset()), 2)
        return old_amount, self._format_display_amount(adjusted, document.metadata)

    def _first_money_token_after_prefix(self, text: str, prefix: str) -> str | None:
        for line in text.splitlines():
            if prefix in line:
                return line.split(prefix, 1)[1].strip()
        return None

    def _format_display_amount(self, value: float, metadata: dict[str, object]) -> str:
        raw = f"{value:,.2f}"
        if metadata.get("currency_format") == "symbol_prefix_eu":
            raw = raw.replace(",", "_").replace(".", ",").replace("_", ".")
        return f"{metadata.get('currency_symbol', '$')}{raw}".strip()

    def _parse_display_amount(self, raw: str, metadata: dict[str, object]) -> float:
        cleaned = raw.replace(str(metadata.get("currency_symbol", "$")), "").strip()
        if metadata.get("currency_format") == "symbol_prefix_eu":
            cleaned = cleaned.replace(".", "").replace(",", ".")
        else:
            cleaned = cleaned.replace(",", "")
        return float(cleaned)

    def _random_mismatch_offset(self) -> float:
        sign = self.rng.choice((-1, 1))
        return round(sign * self.rng.uniform(80.0, 400.0), 2)

    def _ensure_bank_account(self, state: BusinessState, account_name: str) -> dict[str, object]:
        if account_name in state.bank_accounts:
            return state.bank_accounts[account_name]
        suffix = f"{len(state.bank_accounts) + 1:02d}"
        account_number = f"1002-{state.record_id[-2:]}{suffix}"
        display_name = "Reserve Account" if account_name == "Reserve Cash" else f"{account_name} Account"
        state.bank_accounts[account_name] = {
            "account_number": account_number,
            "display_name": display_name,
        }
        return state.bank_accounts[account_name]

    def _empty_balance_sheet(self, date: str) -> BalanceSheet:
        return BalanceSheet(
            date=date,
            assets={},
            liabilities={},
            equity={},
            total_assets=0.0,
            total_liabilities=0.0,
            total_equity=0.0,
            balanced=True,
        )
