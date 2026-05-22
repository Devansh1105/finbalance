from finbalance.doc_schemas.base import kv, listing, opt, req, schema


SCHEMA = schema(
    doc_type="bank_statement",
    title="Bank Statement",
    role="support_doc",
    description="Cash movement and ending balance for the month.",
    required_fields=(
        req("account_name", "string", "Bank account name"),
        req("account_number", "string", "Bank account number"),
        req("opening_balance", "number", "Opening bank balance"),
        req("closing_balance", "number", "Closing bank balance"),
        req("rows", "list", "Statement rows"),
    ),
    optional_fields=(opt("statement_currency", "string", "Statement currency code"),),
    sections=(
        kv(
            "Account Summary",
            ("Account Name", "account_name"),
            ("Account Number", "account_number"),
            ("Statement Currency", "statement_currency"),
            ("Opening Balance", "opening_balance"),
            ("Closing Balance", "closing_balance"),
        ),
        listing("Statement Rows", "Rows", "rows"),
    ),
    list_field_orders={"rows": ("date", "description", "amount", "running_balance")},
    visible_fields=("account_name", "account_number"),
    template_variants=("formal", "ledger", "summary"),
    cosmetic_blocks=("issuer_block", "reference_block", "footer_block"),
)
