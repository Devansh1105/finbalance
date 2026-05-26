# Verification Packet — COV_WHO_M3_0047

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 3
- **Period type:** month
- **Period label:** March 2025
- **Period start → end:** 2025-03-01 → 2025-03-31
- **Entity:** Granite Builders
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-03-01_

**Assets**
- Cash: 38,039.50
- Inventory: 34,036.16
- Accounts Receivable: 6,080.15
- Office Supplies: 1,305.10

**Liabilities**
- Accounts Payable: 7,972.06
- Accrued Expenses: 801.50

**Equity**
- Retained Earnings: 11,170.34
- Owner's Equity: 59,517.01


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-03-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/03/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 38,039.50
  - Section assets | Account Inventory | Amount GBP 34,036.16
  - Section assets | Account Accounts Receivable | Amount GBP 6,080.15
  - Section assets | Account Office Supplies | Amount GBP 1,305.10
  - Section liabilities | Account Accounts Payable | Amount GBP 7,972.06
  - Section liabilities | Account Accrued Expenses | Amount GBP 801.50
  - Section equity | Account Retained Earnings | Amount GBP 11,170.34
  - Section equity | Account Owner's Equity | Amount GBP 59,517.01

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-03-08

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Pace Office Mart
Purchase Ref: PO-0001
Total Quantity: GBP 50.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Premium Kit | Quantity 50 | Unit Cost GBP 33.01
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-10

```
SUPPLIER INVOICE
================

From
----
Granite Builders
220 Lake View Road, Bengaluru
Date: 10/03/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: March 2025

Terms
-----
Due Date: 31/03/2025

Supplier Header
---------------
Supplier: Pace Office Mart
Goods Receipt Ref: GRN-0001
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 31/03/2025
Subtotal: GBP 1,650.50
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 198.06
CGST Amount: GBP 99.03
SGST Amount: GBP 99.03
Total: GBP 1,848.56

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 50 | Unit Cost GBP 33.01 | Amount GBP 1,650.50

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-03-12

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Blue Finch Holdings
Shipment Ref: SHP-0001
Billed Amount: GBP 2,700.77
Cost Basis Amount: GBP 1,594.97
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Refill Pack | Quantity 16 | Unit Price GBP 160.76 | Unit Cost
 GBP 99.69 | Extended Cost GBP 1,594.97
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-12

```
CUSTOMER INVOICE
================

From
----
Granite Builders
220 Lake View Road, Bengaluru
Date: 12/03/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: March 2025
Shipment Ref: SHP-0001

Terms
-----
Due Date: 23/03/2025

Parties
-------
Customer: Blue Finch Holdings
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 23/03/2025
Subtotal: GBP 2,572.16
Tax Label: India GST
Tax Rate: 5.00%
Tax Amount: GBP 128.61
CGST Amount: GBP 64.31
SGST Amount: GBP 64.30
Total: GBP 2,700.77

Line Items
----------
Items:
  - Description Refill Pack | Amount GBP 2,572.16

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
- **Date:** 2025-03-21

```
PAYMENT ADVICE
==============

From
----
Granite Builders
220 Lake View Road, Bengaluru
Document Date: 21/03/2025

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: March 2025
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Pace Office Mart
Amount: GBP 1,848.56
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
- **Date:** 2025-03-23

```
PAYMENT ADVICE
==============

From
----
Granite Builders
220 Lake View Road, Bengaluru
Date: 23/03/2025

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: March 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: GBP 2,700.77
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-03-23

```
PAYROLL SUMMARY
===============

From
----
Granite Builders
220 Lake View Road, Bengaluru
Date: 23/03/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: March 2025
Headcount: 11
Gross Pay: GBP 14,817.16
Employer Tax: 1,462.19
Cash Outflow: GBP 16,279.35

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-03-31

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
  - Sku SKU-0003 | Description Refill Pack | System Qty 100 | Counted Qty 90 | Unit Cost GBP
 11.29
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: GBP 112.90
Reference Sheet: COUNT-0001
```

### Document D011 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Granite Builders
220 Lake View Road, Bengaluru
Date: 31/03/2025

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: March 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0047
Statement Currency: GBP
Opening Balance: GBP 38,039.50
Closing Balance: GBP 22,612.36

Statement Rows
--------------
Rows:
  - Date 21/03/2025 | Description Supplier settlement SUP-0001 | Amount GBP -1,848.56 | 
Running Balance GBP 36,190.94
  - Date 23/03/2025 | Description Customer settlement INV-0001 | Amount GBP 2,700.77 | 
Running Balance GBP 38,891.71
  - Date 23/03/2025 | Description Payroll PAYRUN-0001 | Amount GBP -16,279.35 | Running 
Balance GBP 22,612.36

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D011
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 1,650.50 | D002, D003 | 2025-03-10 | goods_receipt_purchase |
| 2 | Input CGST Receivable | Accounts Payable | 99.03 | D002, D003 | 2025-03-10 | goods_receipt_purchase_tax_cgst |
| 3 | Input SGST Receivable | Accounts Payable | 99.03 | D002, D003 | 2025-03-10 | goods_receipt_purchase_tax_sgst |
| 4 | Accounts Receivable | Sales Revenue | 2,572.16 | D004, D005 | 2025-03-12 | delivery_sale_sale |
| 5 | Cost of Goods Sold | Inventory | 1,594.97 | D004, D005 | 2025-03-12 | delivery_sale_cogs |
| 6 | Accounts Receivable | CGST Payable | 64.31 | D004, D005 | 2025-03-12 | delivery_sale_tax_cgst |
| 7 | Accounts Receivable | SGST Payable | 64.30 | D004, D005 | 2025-03-12 | delivery_sale_tax_sgst |
| 8 | Cash | Accounts Receivable | 2,700.77 | D006, D005 | 2025-03-23 | customer_payment |
| 9 | Accounts Payable | Cash | 1,848.56 | D007, D003 | 2025-03-21 | supplier_payment |
| 10 | Inventory Shrinkage Expense | Inventory | 112.90 | D008, D009 | 2025-03-31 | inventory_adjustment |
| 11 | Salaries Expense | Cash | 14,817.16 | D010 | 2025-03-23 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 1,462.19 | D010 | 2025-03-23 | payroll_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 22,612.36
- Inventory: 33,978.79
- Accounts Receivable: 6,080.15
- Office Supplies: 1,305.10
- Input CGST Receivable: 99.03
- Input SGST Receivable: 99.03

**Liabilities**
- Accounts Payable: 7,972.06
- Accrued Expenses: 801.50
- CGST Payable: 64.31
- SGST Payable: 64.30

**Equity**
- Retained Earnings: -4,244.72
- Owner's Equity: 59,517.01

**Totals:** Assets = 64,174.46; Liabilities = 8,902.17; Equity = 55,272.29
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
- Notes: Reviewed, no material concerns.
