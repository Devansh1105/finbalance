# Verification Packet — COV_WHO_Y3_0057

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 3
- **Period type:** year
- **Period label:** FY 2025-26
- **Period start → end:** 2025-04-01 → 2026-03-31
- **Entity:** Summit Retail Group
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 21
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 260,908.82
- Inventory: 126,943.21
- Accounts Receivable: 28,893.04
- Office Supplies: 5,555.32

**Liabilities**
- Accounts Payable: 39,950.66
- Accrued Expenses: 11,803.48

**Equity**
- Retained Earnings: 37,341.82
- Owner's Equity: 333,204.43


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-04-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $260,908.82
  - Section assets | Account Inventory | Amount $126,943.21
  - Section assets | Account Accounts Receivable | Amount $28,893.04
  - Section assets | Account Office Supplies | Amount $5,555.32
  - Section liabilities | Account Accounts Payable | Amount $39,950.66
  - Section liabilities | Account Accrued Expenses | Amount $11,803.48
  - Section equity | Account Retained Earnings | Amount $37,341.82
  - Section equity | Account Owner's Equity | Amount $333,204.43

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-06-17

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Meridian Support LLP
Purchase Ref: PO-0001
Total Quantity: $62.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Premium Kit | Quantity 62 | Unit Cost $281.08
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-19

```
SUPPLIER INVOICE
================

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Date: 2025-06-19

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: FY 2025-26

Terms
-----
Due Date: 2025-06-30

Supplier Header
---------------
Supplier: Meridian Support LLP
Goods Receipt Ref: GRN-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 2025-06-30
Subtotal: $17,426.96
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $1,742.70
Total: $19,169.66

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 62 | Unit Cost $281.08 | Amount $17,426.96

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D018 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-06-19

```
SECONDARY COPY
==============

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-06-19

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D018
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: SUP-0001
Counterparty: Meridian Support LLP
Total: $19,169.66
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D020 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-06-19

```
SECONDARY COPY
==============

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Date: 2025-06-19

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D020
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: SUP-0001
Counterparty: Meridian Support LLP
Total: $19,169.66
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D014 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-07-27

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0002
Customer: Maple Ridge Trading
Shipment Ref: SHP-0002
Billed Amount: $15,376.80
Cost Basis Amount: $8,049.95
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0005 | Description Widget A | Quantity 36 | Unit Price $399.19 | Unit Cost 
$223.61 | Extended Cost $8,049.95
```

### Document D015 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-27

```
CUSTOMER INVOICE
================

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-07-27

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D015
Document Type: customer_invoice
Period: FY 2025-26
Shipment Ref: SHP-0002

Terms
-----
Due Date: 2025-08-16

Parties
-------
Customer: Maple Ridge Trading
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-08-16
Subtotal: $14,370.84
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $1,005.96
Total: $15,376.80

Line Items
----------
Items:
  - Description Widget A | Amount $14,370.84

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-08-17

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Maple Ridge Trading
Shipment Ref: SHP-0001
Billed Amount: $21,013.20
Cost Basis Amount: $12,403.49
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Filter Pack | Quantity 35 | Unit Price $561.10 | Unit Cost 
$354.39 | Extended Cost $12,403.49
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-17

```
CUSTOMER INVOICE
================

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Date: 2025-08-17

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: FY 2025-26
Shipment Ref: SHP-0001

Terms
-----
Due Date: 2025-08-30

Parties
-------
Customer: Maple Ridge Trading
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-08-30
Subtotal: $19,638.50
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $1,374.70
Total: $21,013.20

Line Items
----------
Items:
  - Description Filter Pack | Amount $19,638.50

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-14

```
PAYMENT ADVICE
==============

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-12-14

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2025-26
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: $19,169.66
Reference: SUP-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-26

```
UTILITY INVOICE
===============

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Date: 2025-12-26

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: FY 2025-26

Terms
-----
Due Date: 2026-01-02

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: FY 2025-26
Due Date: 2026-01-02
Total: $7,697.62

Charges
-------
Charges:
  - Description Electricity | Amount $1,750.81
  - Description Water | Amount $5,946.81

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-19

```
PAYMENT ADVICE
==============

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Document Date: 2026-01-19

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Maple Ridge Trading
Amount: $21,013.20
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-01-29

```
PAYROLL SUMMARY
===============

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Date: 2026-01-29

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025-26
Headcount: 12
Gross Pay: $97,362.71
Employer Tax: 8,728.44
Cash Outflow: $106,091.15

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Warehouse A

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Filter Pack | System Qty 100 | Counted Qty 95 | Unit Cost 
$76.95
```

### Document D009 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Date: 2026-03-31

Reference Box
-------------
Document ID: D009
Document Type: inventory_rollforward
Period: FY 2025-26

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0001
Opening Balance: $7,587.48
Additions: 5,773.31
Usage Or Sales: $3,606.67
Write Down: 384.75
Ending Balance: $9,369.37

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D012 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

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
  - Sku SKU-0004 | Description Widget A | System Qty 100 | Counted Qty 88 | Unit Cost $42.17
```

### Document D013 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Date: 2026-03-31

Reference Box
-------------
Document ID: D013
Document Type: inventory_rollforward
Period: FY 2025-26

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0002
Opening Balance: $9,736.31
Additions: 9,537.95
Usage Or Sales: $4,337.79
Write Down: 506.04
Ending Balance: $14,430.43

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D016 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0003
Location: Warehouse A

Counted Items
-------------
Items:
  - Sku SKU-0006 | Description Filter Pack | System Qty 100 | Counted Qty 94 | Unit Cost 
$46.20
```

### Document D017 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D017
Document Type: inventory_rollforward
Period: FY 2025-26

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0003
Opening Balance: $4,962.33
Additions: 3,262.34
Usage Or Sales: $4,810.77
Write Down: 277.20
Ending Balance: $3,136.70

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D019 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
VENDOR STATEMENT
================

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Document Date: 2026-03-31

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D019
Document Type: vendor_statement
Period: FY 2025-26

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Harbor Utilities
Closing Balance: $7,697.62

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount $7,697.62 | Status Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Summit Retail Group
220 Lake View Road, Bengaluru
Date: 2026-03-31

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0057
Statement Currency: USD
Opening Balance: $260,908.82
Closing Balance: $156,661.21

Statement Rows
--------------
Rows:
  - Date 2025-12-14 | Description Supplier settlement SUP-0001 | Amount $-19,169.66 | 
Running Balance $241,739.16
  - Date 2026-01-19 | Description Customer settlement INV-0001 | Amount $21,013.20 | Running
 Balance $262,752.36
  - Date 2026-01-29 | Description Payroll PAYRUN-0001 | Amount $-106,091.15 | Running 
Balance $156,661.21

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D021
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 17,426.96 | D002, D003 | 2025-06-19 | goods_receipt_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 1,742.70 | D002, D003 | 2025-06-19 | goods_receipt_purchase_tax |
| 3 | Accounts Receivable | Sales Revenue | 19,638.50 | D004, D005 | 2025-08-17 | delivery_sale_sale |
| 4 | Cost of Goods Sold | Inventory | 12,403.49 | D004, D005 | 2025-08-17 | delivery_sale_cogs |
| 5 | Accounts Receivable | Sales Tax Payable | 1,374.70 | D004, D005 | 2025-08-17 | delivery_sale_tax |
| 6 | Cash | Accounts Receivable | 21,013.20 | D006, D005 | 2026-01-19 | customer_payment |
| 7 | Accounts Payable | Cash | 19,169.66 | D007, D003 | 2025-12-14 | supplier_payment |
| 8 | Inventory Shrinkage Expense | Inventory | 384.75 | D008, D009 | 2026-03-31 | inventory_adjustment |
| 9 | Salaries Expense | Cash | 97,362.71 | D010 | 2026-01-29 | payroll_gross |
| 10 | Payroll Tax Expense | Cash | 8,728.44 | D010 | 2026-01-29 | payroll_tax |
| 11 | Utilities Expense | Accounts Payable | 7,697.62 | D011 | 2025-12-26 | utilities_bill |
| 12 | Inventory Shrinkage Expense | Inventory | 506.04 | D012, D013 | 2026-03-31 | inventory_adjustment |
| 13 | Accounts Receivable | Sales Revenue | 14,370.84 | D014, D015 | 2025-07-27 | delivery_sale_sale |
| 14 | Cost of Goods Sold | Inventory | 8,049.95 | D014, D015 | 2025-07-27 | delivery_sale_cogs |
| 15 | Accounts Receivable | Sales Tax Payable | 1,005.96 | D014, D015 | 2025-07-27 | delivery_sale_tax |
| 16 | Inventory Shrinkage Expense | Inventory | 277.20 | D016, D017 | 2026-03-31 | inventory_adjustment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 156,661.21
- Inventory: 122,748.74
- Accounts Receivable: 44,269.84
- Office Supplies: 5,555.32
- Input Tax Receivable: 1,742.70

**Liabilities**
- Accounts Payable: 47,648.28
- Accrued Expenses: 11,803.48
- Sales Tax Payable: 2,380.66

**Equity**
- Retained Earnings: -64,059.04
- Owner's Equity: 333,204.43

**Totals:** Assets = 330,977.81; Liabilities = 61,832.42; Equity = 269,145.39
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

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: All foots correctly.
