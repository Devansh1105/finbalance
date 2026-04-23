"""Helpers for declarative document schemas."""

from __future__ import annotations

from docs_benchmark.types import DocSchema, DocSchemaVariant, FieldSpec, RenderSection


def req(name: str, kind: str, description: str) -> FieldSpec:
    return FieldSpec(name=name, kind=kind, description=description, required=True)


def opt(name: str, kind: str, description: str) -> FieldSpec:
    return FieldSpec(name=name, kind=kind, description=description, required=False)


def kv(title: str, *entries: tuple[str, str]) -> RenderSection:
    return RenderSection(title=title, entries=tuple(entries), kind="kv")


def listing(title: str, label: str, field_name: str) -> RenderSection:
    return RenderSection(title=title, entries=((label, field_name),), kind="list")


def narrative(title: str, label: str, field_name: str) -> RenderSection:
    return RenderSection(title=title, entries=((label, field_name),), kind="narrative")


def schema(
    *,
    doc_type: str,
    title: str,
    role: str,
    description: str,
    required_fields: tuple[FieldSpec, ...],
    optional_fields: tuple[FieldSpec, ...] = (),
    sections: tuple[RenderSection, ...] = (),
    list_field_orders: dict[str, tuple[str, ...]] | None = None,
    visible_fields: tuple[str, ...] = (),
    variants: dict[str, DocSchemaVariant] | None = None,
    template_variants: tuple[str, ...] = ("formal", "compact"),
    cosmetic_blocks: tuple[str, ...] = (),
    validation_rules: tuple[str, ...] = (),
) -> DocSchema:
    return DocSchema(
        doc_type=doc_type,
        title=title,
        role=role,
        description=description,
        required_fields=required_fields,
        optional_fields=optional_fields,
        sections=sections,
        list_field_orders=list_field_orders or {},
        visible_fields=visible_fields,
        variants=variants or {},
        template_variants=template_variants,
        cosmetic_blocks=cosmetic_blocks,
        validation_rules=validation_rules,
    )
