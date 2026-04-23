from docs_benchmark.doc_schemas.base import kv, listing, req, schema


SCHEMA = schema(
    doc_type="delivery_note",
    title="Delivery Note",
    role="support_doc",
    description="Customer shipment or delivery notice.",
    required_fields=(
        req("delivery_number", "string", "Delivery note number"),
        req("customer", "string", "Customer"),
        req("shipment_ref", "string", "Shipment reference"),
        req("items", "list", "Delivered items"),
        req("billed_amount", "number", "Billed amount"),
    ),
    sections=(
        kv(
            "Delivery Summary",
            ("Delivery Number", "delivery_number"),
            ("Customer", "customer"),
            ("Shipment Ref", "shipment_ref"),
            ("Billed Amount", "billed_amount"),
        ),
        listing("Delivered Items", "Items", "items"),
    ),
    list_field_orders={"items": ("sku", "description", "quantity", "unit_price")},
    visible_fields=("delivery_number", "customer", "billed_amount"),
)
