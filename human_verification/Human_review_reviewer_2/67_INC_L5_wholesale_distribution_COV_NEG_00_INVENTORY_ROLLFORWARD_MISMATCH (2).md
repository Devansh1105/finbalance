# Verification Packet — COV_NEG_00_INVENTORY_ROLLFORWARD_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Pioneer Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `vat`
- **Document count:** 33
- **Labeled as inconsistent:** True
- **Inconsistency codes:** inventory_rollforward_mismatch
- **Inconsistency reasons:** Inventory rollforward does not reconcile from opening through ending balance.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 236,374.13
- Inventory: 253,042.18
- Accounts Receivable: 42,356.58
- Office Supplies: 6,058.08
- Equipment: 75,458.92

**Liabilities**
- Accounts Payable: 62,789.41
- Accrued Expenses: 10,869.82
- Loans Payable: 56,611.63
- Notes Payable: 30,402.92

**Equity**
- Retained Earnings: 60,848.66
- Owner's Equity: 391,767.45


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-01-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $236,374.13
  - Section assets | Account Inventory | Amount $253,042.18
  - Section assets | Account Accounts Receivable | Amount $42,356.58
  - Section assets | Account Office Supplies | Amount $6,058.08
  - Section assets | Account Equipment | Amount $75,458.92
  - Section liabilities | Account Accounts Payable | Amount $62,789.41
  - Section liabilities | Account Accrued Expenses | Amount $10,869.82
  - Section liabilities | Account Loans Payable | Amount $56,611.63
  - Section liabilities | Account Notes Payable | Amount $30,402.92
  - Section equity | Account Retained Earnings | Amount $60,848.66
  - Section equity | Account Owner's Equity | Amount $391,767.45

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2024-01-23

```
TAX REGIME NOTICE
=================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-01-23

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: FY 2024

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: india_gst
Company Jurisdiction: Maharashtra
Counterparty Jurisdiction: Maharashtra
Tax Rate: 12.00%
Jurisdiction Tax Amount: $15,057.99
Treatment: India GST same-state CGST+SGST input credit

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-23

```
SUPPLIER INVOICE
================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-01-23

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-02-12

Supplier Header
---------------
Supplier: Oakline Services
Goods Receipt Ref: GRN-TAX-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 2024-02-12
Subtotal: $125,483.26
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: $15,057.99
CGST Amount: $7,528.99
SGST Amount: $7,529.00
Total: $140,541.25

Supplier Bill Lines
-------------------
Lines:
  - Description Widget A | Quantity 1 | Unit Cost $125,483.26 | Amount $125,483.26

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-03-12

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Vertex Supply Co.
Purchase Ref: PO-0001
Total Quantity: $56.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Premium Kit | Quantity 56 | Unit Cost $241.25
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-14

```
SUPPLIER INVOICE
================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-03-14

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-03-25

Supplier Header
---------------
Supplier: Vertex Supply Co.
Goods Receipt Ref: GRN-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 2024-03-25
Subtotal: $13,510.00
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: $1,688.75
Total: $15,198.75

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 56 | Unit Cost $241.25 | Amount $13,510.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D025 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-03-26

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0002
Supplier: Vertex Supply Co.
Purchase Ref: PO-0002
Total Quantity: $151.00

Received Items
--------------
Items:
  - Sku SKU-0005 | Description Filter Pack | Quantity 151 | Unit Cost $145.04
```

### Document D026 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-28

```
SUPPLIER INVOICE
================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-03-28

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D026
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-14

Supplier Header
---------------
Supplier: Vertex Supply Co.
Goods Receipt Ref: GRN-0002
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0002
Due Date: 2024-04-14
Subtotal: $21,901.04
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: $2,190.10
Total: $24,091.14

Supplier Bill Lines
-------------------
Lines:
  - Description Filter Pack | Quantity 151 | Unit Cost $145.04 | Amount $21,901.04

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D032 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-03-28

```
SECONDARY COPY
==============

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-03-28

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D032
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: SUP-0002
Counterparty: Vertex Supply Co.
Total: $24,091.14
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D032
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2024-04-28

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-04-28

To
--
Aster Point Services

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: FY 2024

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Aster Point Services
Tax Regime: india_gst
Effective Date: 2024-01-01
Expiration Date: 2024-12-31
Exemption Status: Valid
Exempt Reason: Resale exemption certificate overrides default invoice tax treatment.

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D018 — Customer Tax Profile

- **Type:** `customer_tax_profile`
- **Role:** `support_doc`
- **Date:** 2024-04-28

```
CUSTOMER TAX PROFILE
====================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-04-28

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: FY 2024

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Aster Point Services
Customer Jurisdiction: Maharashtra
Company Jurisdiction: Maharashtra
Same State: True
Exemption Certificate: EXEMPT-0001

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-28

```
CUSTOMER INVOICE
================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-04-28

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: FY 2024
Shipment Ref: SHP-0002

Terms
-----
Due Date: 2024-05-18

Parties
-------
Customer: Aster Point Services
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-05-18
Subtotal: $158,347.52
Tax Label: India GST
Tax Rate: 0.00%
Tax Amount: $0.00
Exemption Certificate: EXEMPT-0001
Total: $158,347.52

Line Items
----------
Items:
  - Description Widget A | Amount $158,347.52

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D023 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2024-05-19

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0002
Customer: Metro Edge Partners
Shipment Ref: SHP-0003
Billed Amount: $72,950.13
Cost Basis Amount: $46,321.26
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0004 | Description Refill Pack | Quantity 62 | Unit Price $1,069.65 | Unit Cost 
$747.12 | Extended Cost $46,321.26
```

### Document D024 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-19

```
CUSTOMER INVOICE
================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-05-19

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D024
Document Type: customer_invoice
Period: FY 2024
Shipment Ref: SHP-0003

Terms
-----
Due Date: 2024-05-29

Parties
-------
Customer: Metro Edge Partners
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2024-05-29
Subtotal: $66,318.30
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: $6,631.83
Total: $72,950.13

Line Items
----------
Items:
  - Description Refill Pack | Amount $66,318.30

Shipment Link
-------------
Shipment Ref: SHP-0003

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-05-31

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $3,808.00
Draw Amount: $295,734.23
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $299,542.23
Note: Scheduled lender activity for the selected period.
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-29

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: Office laptops
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $472,295.90
Paid Cash: $234,753.21
Financed Amount: $237,542.69
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2024-08-13

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Maple Ridge Trading
Shipment Ref: SHP-0001
Billed Amount: $28,274.69
Cost Basis Amount: $15,424.89
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Filter Pack | Quantity 52 | Unit Price $453.12 | Unit Cost 
$296.63 | Extended Cost $15,424.89
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-13

```
CUSTOMER INVOICE
================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-08-13

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: FY 2024
Shipment Ref: SHP-0001

Terms
-----
Due Date: 2024-08-26

Parties
-------
Customer: Maple Ridge Trading
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-08-26
Subtotal: $23,562.24
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $4,712.45
Total: $28,274.69

Line Items
----------
Items:
  - Description Filter Pack | Amount $23,562.24

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D030 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-08-13

```
CANCELLATION NOTE
=================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-08-13

Reference Box
-------------
Document ID: D030
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D020 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-09

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: $195,260.15
Draw Amount: $0.00
Principal Paid: $64,218.11
Interest Paid: $4,703.64
Ending Principal: $131,042.04
Note: Scheduled lender activity for the selected period.
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-22

```
PAYROLL SUMMARY
===============

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-09-22

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024
Headcount: 8
Gross Pay: $45,690.38
Employer Tax: 5,932.10
Cash Outflow: $51,622.48

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-24

```
PAYMENT ADVICE
==============

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-09-24

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $12,381.18
Reference: SUP-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-22

```
PAYMENT ADVICE
==============

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-10-22

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Maple Ridge Trading
Amount: $27,939.60
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-16

```
UTILITY INVOICE
===============

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-11-16

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: FY 2024

Terms
-----
Due Date: 2024-11-23

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: FY 2024
Due Date: 2024-11-23
Total: $14,554.04

Charges
-------
Charges:
  - Description Electricity | Amount $6,346.18
  - Description Water | Amount $8,207.86

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Front store

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Refill Pack | System Qty 100 | Counted Qty 88 | Unit Cost 
$60.62
```

### Document D009 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D009
Document Type: inventory_rollforward
Period: FY 2024

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0001
Opening Balance: $10,972.12
Additions: 7,971.32
Usage Or Sales: $7,861.48
Write Down: 727.44
Ending Balance: $11,360.88

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D014 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D014
Document Type: fixed_asset_rollforward
Period: FY 2024

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Office laptops
Asset Tag: TAG-0001
Cost: $472,295.90
Useful Life: 60
Current Charge: $94,459.20
Accumulated Depreciation: 94,459.20
Opening Balance: $472,295.90
Additions: 0.00
Disposals: 0.00
Ending Balance: $472,295.90

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D021 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
AR AGING SUMMARY
================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D021
Document Type: ar_aging_summary
Period: FY 2024

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2024
Total Open: $335.09

Customer Lines
--------------
Lines:
  - Customer Maple Ridge Trading | Reference INV-0001 | Current $212.99 | Past Due 122.10

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D022 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
CREDIT MEMO
===========

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-12-31

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D022
Document Type: credit_memo
Period: FY 2024
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Maple Ridge Trading
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: $122.10

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D027 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0002
Location: Back room

Counted Items
-------------
Items:
  - Sku SKU-0006 | Description Widget B | System Qty 100 | Counted Qty 91 | Unit Cost $80.73
```

### Document D028 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D028
Document Type: inventory_rollforward
Period: FY 2024

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0002
Opening Balance: $12,923.89
Additions: 10,728.79
Usage Or Sales: $10,636.64
Write Down: 726.57
Ending Balance: $12,289.47

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D029 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Pioneer Software
18 Marina Avenue, Chennai
Date: 2024-12-31

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D029
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Metro Water
Closing Balance: $14,554.04

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount $14,554.04 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D029
```

### Document D031 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D031
Document Type: memo
Period: FY 2024

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Document retention reminder
Audience: Finance Team

Memo Body
---------
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D031
```

### Document D033 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Software
18 Marina Avenue, Chennai
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D033
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $236,374.13
Closing Balance: $192,369.34

Statement Rows
--------------
Rows:
  - Date 2024-05-31 | Description Loan draw LOAN-0001 | Amount $295,734.23 | Running Balance
 $532,108.36
  - Date 2024-06-29 | Description Asset purchase ASSET-0001 | Amount $-234,753.21 | Running 
Balance $297,355.15
  - Date 2024-09-09 | Description Loan payment LOAN-0002 | Amount $-68,921.75 | Running 
Balance $228,433.40
  - Date 2024-09-22 | Description Payroll PAYRUN-0001 | Amount $-51,622.48 | Running Balance
 $176,810.92
  - Date 2024-09-24 | Description Supplier settlement SUP-0001 | Amount $-12,381.18 | 
Running Balance $164,429.74
  - Date 2024-10-22 | Description Customer settlement INV-0001 | Amount $27,939.60 | Running
 Balance $192,369.34

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D033
```

## 5. Expected Journal Entries (ground truth)

_(no expected entries — packet is labeled inconsistent)_

## 6. Expected Final Balance Sheet (ground truth)

_Packet is labeled inconsistent — the expected balance sheet should be empty._

**Totals:** Assets = 0.00; Liabilities = 0.00; Equity = 0.00
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [x] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [x] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:

### Q3 — Are entries complete?
Are there any entries you would book that are MISSING from section 5? Or any entries in section 5 that should NOT be there?
- [x] Complete and exact
- [ ] Missing entries (list them in notes)
- [ ] Extra entries that should not be booked (list them)
- Notes:

### Q4 — Are document references correct?
For each expected entry, is `doc_refs` the set of documents that actually support that posting?
- [x] Yes, doc_refs are correct
- [ ] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes:

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [x] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `inventory_rollforward_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
