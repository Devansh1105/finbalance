from finbalance.doc_schemas.base import kv, listing, opt, req, schema


SCHEMA = schema(
    doc_type="opening_trial_balance",
    title="Opening Trial Balance",
    role="posting_doc",
    description="Opening balances that set the starting point for the month.",
    required_fields=(
        req("statement_date", "date", "Date of the opening balance"),
        req("account_lines", "list", "Account rows with section, account, and amount"),
    ),
    optional_fields=(opt("prepared_by", "string", "Who prepared the statement"),),
    sections=(
        kv("Summary", ("Statement Date", "statement_date"), ("Prepared By", "prepared_by")),
        listing("Account Lines", "Accounts", "account_lines"),
    ),
    list_field_orders={"account_lines": ("section", "account", "amount")},
    visible_fields=("statement_date",),
)
