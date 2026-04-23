"""Central registry for document schemas."""

from docs_benchmark.doc_schemas.ap_aging_summary import SCHEMA as AP_AGING_SUMMARY
from docs_benchmark.doc_schemas.ar_aging_summary import SCHEMA as AR_AGING_SUMMARY
from docs_benchmark.doc_schemas.bank_statement import SCHEMA as BANK_STATEMENT
from docs_benchmark.doc_schemas.card_settlement_report import SCHEMA as CARD_SETTLEMENT_REPORT
from docs_benchmark.doc_schemas.cancellation_note import SCHEMA as CANCELLATION_NOTE
from docs_benchmark.doc_schemas.copay_receipt import SCHEMA as COPAY_RECEIPT
from docs_benchmark.doc_schemas.credit_memo import SCHEMA as CREDIT_MEMO
from docs_benchmark.doc_schemas.customer_invoice import SCHEMA as CUSTOMER_INVOICE
from docs_benchmark.doc_schemas.delivery_note import SCHEMA as DELIVERY_NOTE
from docs_benchmark.doc_schemas.depreciation_schedule import SCHEMA as DEPRECIATION_SCHEDULE
from docs_benchmark.doc_schemas.direct_labor_record import SCHEMA as DIRECT_LABOR_RECORD
from docs_benchmark.doc_schemas.equipment_invoice import SCHEMA as EQUIPMENT_INVOICE
from docs_benchmark.doc_schemas.expense_receipt import SCHEMA as EXPENSE_RECEIPT
from docs_benchmark.doc_schemas.exchange_rate_notice import SCHEMA as EXCHANGE_RATE_NOTICE
from docs_benchmark.doc_schemas.finished_goods_transfer_note import SCHEMA as FINISHED_GOODS_TRANSFER_NOTE
from docs_benchmark.doc_schemas.fixed_asset_rollforward import SCHEMA as FIXED_ASSET_ROLLFORWARD
from docs_benchmark.doc_schemas.fx_remeasurement_memo import SCHEMA as FX_REMEASUREMENT_MEMO
from docs_benchmark.doc_schemas.goods_receipt_note import SCHEMA as GOODS_RECEIPT_NOTE
from docs_benchmark.doc_schemas.insurance_notice import SCHEMA as INSURANCE_NOTICE
from docs_benchmark.doc_schemas.insurer_remittance import SCHEMA as INSURER_REMITTANCE
from docs_benchmark.doc_schemas.inventory_adjustment_note import SCHEMA as INVENTORY_ADJUSTMENT_NOTE
from docs_benchmark.doc_schemas.inventory_rollforward import SCHEMA as INVENTORY_ROLLFORWARD
from docs_benchmark.doc_schemas.loan_statement import SCHEMA as LOAN_STATEMENT
from docs_benchmark.doc_schemas.material_requisition_slip import SCHEMA as MATERIAL_REQUISITION_SLIP
from docs_benchmark.doc_schemas.memo import SCHEMA as MEMO
from docs_benchmark.doc_schemas.opening_trial_balance import SCHEMA as OPENING_TRIAL_BALANCE
from docs_benchmark.doc_schemas.overhead_accrual_memo import SCHEMA as OVERHEAD_ACCRUAL_MEMO
from docs_benchmark.doc_schemas.patient_invoice import SCHEMA as PATIENT_INVOICE
from docs_benchmark.doc_schemas.payment_advice import SCHEMA as PAYMENT_ADVICE
from docs_benchmark.doc_schemas.payroll_summary import SCHEMA as PAYROLL_SUMMARY
from docs_benchmark.doc_schemas.pos_batch_report import SCHEMA as POS_BATCH_REPORT
from docs_benchmark.doc_schemas.production_batch_sheet import SCHEMA as PRODUCTION_BATCH_SHEET
from docs_benchmark.doc_schemas.rent_notice import SCHEMA as RENT_NOTICE
from docs_benchmark.doc_schemas.rent_roll import SCHEMA as RENT_ROLL
from docs_benchmark.doc_schemas.reclassification_memo import SCHEMA as RECLASSIFICATION_MEMO
from docs_benchmark.doc_schemas.retainer_agreement_memo import SCHEMA as RETAINER_AGREEMENT_MEMO
from docs_benchmark.doc_schemas.renewal_notice import SCHEMA as RENEWAL_NOTICE
from docs_benchmark.doc_schemas.revenue_recognition_schedule import SCHEMA as REVENUE_RECOGNITION_SCHEDULE
from docs_benchmark.doc_schemas.return_note import SCHEMA as RETURN_NOTE
from docs_benchmark.doc_schemas.sales_summary import SCHEMA as SALES_SUMMARY
from docs_benchmark.doc_schemas.scrap_report import SCHEMA as SCRAP_REPORT
from docs_benchmark.doc_schemas.security_deposit_notice import SCHEMA as SECURITY_DEPOSIT_NOTICE
from docs_benchmark.doc_schemas.secondary_copy import SCHEMA as SECONDARY_COPY
from docs_benchmark.doc_schemas.service_period_memo import SCHEMA as SERVICE_PERIOD_MEMO
from docs_benchmark.doc_schemas.stock_count_sheet import SCHEMA as STOCK_COUNT_SHEET
from docs_benchmark.doc_schemas.subscription_order_form import SCHEMA as SUBSCRIPTION_ORDER_FORM
from docs_benchmark.doc_schemas.supplier_invoice import SCHEMA as SUPPLIER_INVOICE
from docs_benchmark.doc_schemas.transfer_advice import SCHEMA as TRANSFER_ADVICE
from docs_benchmark.doc_schemas.utilities_statement import SCHEMA as UTILITIES_STATEMENT
from docs_benchmark.doc_schemas.vendor_invoice import SCHEMA as VENDOR_INVOICE
from docs_benchmark.doc_schemas.vendor_statement import SCHEMA as VENDOR_STATEMENT
from docs_benchmark.doc_schemas.work_order import SCHEMA as WORK_ORDER


DOC_SCHEMAS = {
    schema.doc_type: schema
    for schema in (
        OPENING_TRIAL_BALANCE,
        AP_AGING_SUMMARY,
        AR_AGING_SUMMARY,
        BANK_STATEMENT,
        CANCELLATION_NOTE,
        CREDIT_MEMO,
        CUSTOMER_INVOICE,
        VENDOR_INVOICE,
        VENDOR_STATEMENT,
        SUPPLIER_INVOICE,
        DIRECT_LABOR_RECORD,
        EXPENSE_RECEIPT,
        EXCHANGE_RATE_NOTICE,
        INSURANCE_NOTICE,
        UTILITIES_STATEMENT,
        PAYMENT_ADVICE,
        PAYROLL_SUMMARY,
        RENT_NOTICE,
        SERVICE_PERIOD_MEMO,
        RETAINER_AGREEMENT_MEMO,
        LOAN_STATEMENT,
        EQUIPMENT_INVOICE,
        DEPRECIATION_SCHEDULE,
        FIXED_ASSET_ROLLFORWARD,
        FX_REMEASUREMENT_MEMO,
        SALES_SUMMARY,
        POS_BATCH_REPORT,
        CARD_SETTLEMENT_REPORT,
        STOCK_COUNT_SHEET,
        INVENTORY_ADJUSTMENT_NOTE,
        INVENTORY_ROLLFORWARD,
        RETURN_NOTE,
        GOODS_RECEIPT_NOTE,
        DELIVERY_NOTE,
        PATIENT_INVOICE,
        INSURER_REMITTANCE,
        MEMO,
        COPAY_RECEIPT,
        RENT_ROLL,
        SECURITY_DEPOSIT_NOTICE,
        MATERIAL_REQUISITION_SLIP,
        OVERHEAD_ACCRUAL_MEMO,
        PRODUCTION_BATCH_SHEET,
        FINISHED_GOODS_TRANSFER_NOTE,
        SCRAP_REPORT,
        SECONDARY_COPY,
        RECLASSIFICATION_MEMO,
        SUBSCRIPTION_ORDER_FORM,
        TRANSFER_ADVICE,
        REVENUE_RECOGNITION_SCHEDULE,
        RENEWAL_NOTICE,
        WORK_ORDER,
    )
}


def get_doc_schema(doc_type: str):
    if doc_type not in DOC_SCHEMAS:
        raise KeyError(f"Unknown document schema '{doc_type}'")
    return DOC_SCHEMAS[doc_type]
