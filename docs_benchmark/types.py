"""Core types for the schema-driven synthetic dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from docs_benchmark.schemas import DocumentSeed, OpeningBalance, Posting


@dataclass(frozen=True)
class FieldSpec:
    name: str
    kind: str
    description: str
    required: bool = True


@dataclass(frozen=True)
class RenderSection:
    title: str
    entries: tuple[tuple[str, str], ...]
    kind: str = "kv"


@dataclass(frozen=True)
class DocSchemaVariant:
    extra_required_fields: tuple[FieldSpec, ...] = ()
    extra_optional_fields: tuple[FieldSpec, ...] = ()
    extra_sections: tuple[RenderSection, ...] = ()
    title_override: str | None = None
    template_variants: tuple[str, ...] = ()
    cosmetic_blocks: tuple[str, ...] = ()


@dataclass(frozen=True)
class DocSchema:
    doc_type: str
    title: str
    role: str
    description: str
    required_fields: tuple[FieldSpec, ...]
    optional_fields: tuple[FieldSpec, ...] = ()
    sections: tuple[RenderSection, ...] = ()
    list_field_orders: dict[str, tuple[str, ...]] = field(default_factory=dict)
    visible_fields: tuple[str, ...] = ()
    variants: dict[str, DocSchemaVariant] = field(default_factory=dict)
    template_variants: tuple[str, ...] = ("formal", "compact")
    cosmetic_blocks: tuple[str, ...] = ()
    validation_rules: tuple[str, ...] = ()

    def title_for(self, industry: str) -> str:
        variant = self.variants.get(industry)
        if variant and variant.title_override:
            return variant.title_override
        return self.title

    def field_specs_for(self, industry: str) -> tuple[FieldSpec, ...]:
        variant = self.variants.get(industry)
        specs = list(self.required_fields) + list(self.optional_fields)
        if variant:
            specs.extend(variant.extra_required_fields)
            specs.extend(variant.extra_optional_fields)
        return tuple(specs)

    def required_field_names_for(self, industry: str) -> tuple[str, ...]:
        variant = self.variants.get(industry)
        names = [spec.name for spec in self.required_fields if spec.required]
        if variant:
            names.extend(spec.name for spec in variant.extra_required_fields if spec.required)
        return tuple(names)

    def sections_for(self, industry: str) -> tuple[RenderSection, ...]:
        variant = self.variants.get(industry)
        if not variant:
            return self.sections
        return tuple(list(self.sections) + list(variant.extra_sections))

    def template_variants_for(self, industry: str) -> tuple[str, ...]:
        variant = self.variants.get(industry)
        if variant and variant.template_variants:
            return variant.template_variants
        return self.template_variants

    def cosmetic_blocks_for(self, industry: str) -> tuple[str, ...]:
        variant = self.variants.get(industry)
        if not variant:
            return self.cosmetic_blocks
        merged = list(self.cosmetic_blocks)
        merged.extend(block for block in variant.cosmetic_blocks if block not in merged)
        return tuple(merged)


@dataclass(frozen=True)
class PeriodSpec:
    period_type: str
    start_date: str
    end_date: str
    label: str
    month_count: int
    fiscal_start_month: int


@dataclass
class ScenarioResult:
    documents: list[DocumentSeed]
    postings: list[Posting]
    bank_rows: list[dict[str, Any]] = field(default_factory=list)
    notes: dict[str, Any] = field(default_factory=dict)


ScenarioBuilder = Callable[["BusinessState", Any], ScenarioResult]
OpeningBuilder = Callable[[Any, int, PeriodSpec], OpeningBalance]
MasterDataBuilder = Callable[[str, Any, PeriodSpec], dict[str, Any]]


@dataclass(frozen=True)
class BusinessScenario:
    name: str
    description: str
    doc_types: tuple[str, ...]
    doc_count_hint: int
    builder: ScenarioBuilder
    allow_repeat: bool = False
    period_types: tuple[str, ...] = ("month", "quarter", "year")


@dataclass(frozen=True)
class DifficultyPlan:
    mandatory: tuple[str, ...]
    optional: tuple[str, ...] = ()


@dataclass(frozen=True)
class IndustrySchema:
    name: str
    display_name: str
    description: str
    allowed_accounts: list[str]
    opening_builder: OpeningBuilder
    master_data_builder: MasterDataBuilder
    scenarios: dict[str, BusinessScenario]
    period_plans: dict[str, dict[int, DifficultyPlan]]
    distractor_doc_types: tuple[str, ...] = ()


@dataclass
class ValidationIssue:
    level: str
    scope: str
    message: str


@dataclass
class ValidationReport:
    issues: list[ValidationIssue] = field(default_factory=list)

    def add(self, level: str, scope: str, message: str) -> None:
        self.issues.append(ValidationIssue(level=level, scope=scope, message=message))

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.level == "error"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.level == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "errors": [issue.__dict__ for issue in self.errors],
            "warnings": [issue.__dict__ for issue in self.warnings],
        }


@dataclass
class BusinessState:
    record_id: str
    industry: str
    difficulty_level: int
    period_spec: PeriodSpec
    period_start: str
    period_end: str
    entity_name: str
    entity_address: str
    functional_currency_code: str
    functional_currency_symbol: str
    functional_currency_format: str
    currency_code: str
    currency_symbol: str
    currency_format: str
    date_format: str
    tax_regime: str
    tax_label: str
    opening_balance: OpeningBalance
    master_data: dict[str, Any]
    documents: list[DocumentSeed] = field(default_factory=list)
    postings: list[Posting] = field(default_factory=list)
    bank_rows: list[dict[str, Any]] = field(default_factory=list)
    bank_accounts: dict[str, dict[str, Any]] = field(default_factory=dict)
    open_receivables: list[dict[str, Any]] = field(default_factory=list)
    open_payables: list[dict[str, Any]] = field(default_factory=list)
    open_fx_receivables: list[dict[str, Any]] = field(default_factory=list)
    open_fx_payables: list[dict[str, Any]] = field(default_factory=list)
    contract_subledger: list[dict[str, Any]] = field(default_factory=list)
    asset_register: list[dict[str, Any]] = field(default_factory=list)
    lease_subledger: list[dict[str, Any]] = field(default_factory=list)
    jurisdiction_profile: dict[str, Any] = field(default_factory=dict)
    tax_context: dict[str, Any] = field(default_factory=dict)
    scenario_log: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    expected_inconsistency: bool = False
    expected_inconsistency_codes: list[str] = field(default_factory=list)
    inconsistency_reasons: list[str] = field(default_factory=list)
    _doc_counter: int = 0
    _number_counters: dict[str, int] = field(default_factory=dict)

    def next_doc_id(self) -> str:
        self._doc_counter += 1
        return f"D{self._doc_counter:03d}"

    def next_number(self, prefix: str) -> str:
        current = self._number_counters.get(prefix, 0) + 1
        self._number_counters[prefix] = current
        return f"{prefix}-{current:04d}"
