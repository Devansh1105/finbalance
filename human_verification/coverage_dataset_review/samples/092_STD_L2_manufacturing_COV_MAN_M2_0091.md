# Verification Packet — COV_MAN_M2_0091

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** August 2025
- **Period start → end:** 2025-08-01 → 2025-08-31
- **Entity:** Granite Property Services
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-08-01_

**Assets**
- Cash: 64,654.15
- Raw Materials Inventory: 12,516.81
- Work In Process: 9,937.63
- Finished Goods Inventory: 23,521.42

**Liabilities**
- Accounts Payable: 8,390.43
- Accrued Expenses: 1,416.58

**Equity**
- Retained Earnings: 17,910.77
- Share Capital: 82,912.23


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-08-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/08/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 64.654,15
  - Section assets | Account Raw Materials Inventory | Amount EUR 12.516,81
  - Section assets | Account Work In Process | Amount EUR 9.937,63
  - Section assets | Account Finished Goods Inventory | Amount EUR 23.521,42
  - Section liabilities | Account Accounts Payable | Amount EUR 8.390,43
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.416,58
  - Section equity | Account Retained Earnings | Amount EUR 17.910,77
  - Section equity | Account Share Capital | Amount EUR 82.912,23

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-07

```
SUPPLIER INVOICE
================

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 07/08/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: August 2025

Terms
-----
Due Date: 21/08/2025

Supplier Header
---------------
Supplier: Meridian Support LLP
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 21/08/2025
Subtotal: EUR 2.830,08
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 141,50
Total: EUR 2.971,58

Supplier Bill Lines
-------------------
Lines:
  - Description Resin pellets | Quantity 268 | Unit Cost EUR 10,56 | Amount EUR 2.830,08

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2025-08-11

```
DIRECT LABOR RECORD
===================

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 11/08/2025

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: August 2025

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 75
Labor Value: EUR 7.539,12
Labor Cash Paid: EUR 7.539,12

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2025-08-15

```
MATERIAL REQUISITION SLIP
=========================

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 15/08/2025

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: August 2025

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Resin pellets
Quantity Issued: 212
Issue Value: EUR 2.248,10
Warehouse: Main Warehouse

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2025-08-15

```
PRODUCTION BATCH SHEET
======================

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 15/08/2025

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: August 2025

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 36
Material Value: EUR 2.248,10
Labor Value: EUR 0,00
Overhead Value: EUR 0,00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D006 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2025-08-22

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 22/08/2025

Reference Box
-------------
Document ID: D006
Document Type: finished_goods_transfer_note
Period: August 2025

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Retail Display
Units Completed: 50
Transfer Value: EUR 9.787,22

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D008 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-25

```
PAYMENT ADVICE
==============

From
----
Granite Property Services
90 Hill Park, Hyderabad
Document Date: 25/08/2025

To
--
Crescent Labs

Reference Box
-------------
Document ID: D008
Document Type: payment_advice
Period: August 2025
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: EUR 15.195,50
Reference: FGINV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-27

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 27/08/2025

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: August 2025
Contract Ref: FGT-0001

Terms
-----
Due Date: 10/09/2025

Parties
-------
Customer: Crescent Labs
Contract Ref: FGT-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 10/09/2025
Subtotal: EUR 14.168,30
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 1.027,20
Total: EUR 15.195,50

Line Items
----------
Items:
  - Description Retail Display | Amount EUR 14.168,30

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-27

```
PAYMENT ADVICE
==============

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 27/08/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: August 2025
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: EUR 2.971,58
Reference: MAT-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-08-31

```
BANK STATEMENT
==============

From
----
Granite Property Services
90 Hill Park, Hyderabad
Date: 31/08/2025

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: August 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0091
Statement Currency: EUR
Opening Balance: EUR 64.654,15
Closing Balance: EUR 69.338,95

Statement Rows
--------------
Rows:
  - Date 11/08/2025 | Description Direct labor BATCH-0001 | Amount EUR -7.539,12 | Running 
Balance EUR 57.115,03
  - Date 25/08/2025 | Description Customer settlement FGINV-0001 | Amount EUR 15.195,50 | 
Running Balance EUR 72.310,53
  - Date 27/08/2025 | Description Supplier settlement MAT-0001 | Amount EUR -2.971,58 | 
Running Balance EUR 69.338,95

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D010
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 2,830.08 | D002 | 2025-08-07 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 141.50 | D002 | 2025-08-07 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 2,248.10 | D003, D004, D002 | 2025-08-15 | material_issue |
| 4 | Work In Process | Cash | 7,539.12 | D005, D004 | 2025-08-11 | direct_labor_labor |
| 5 | Finished Goods Inventory | Work In Process | 9,787.22 | D006, D004 | 2025-08-22 | finished_goods_transfer |
| 6 | Accounts Receivable | Sales Revenue | 14,168.30 | D007, D006 | 2025-08-27 | finished_goods_sale_sale |
| 7 | Cost of Goods Sold | Finished Goods Inventory | 9,787.22 | D007, D006 | 2025-08-27 | finished_goods_sale_cogs |
| 8 | Accounts Receivable | Sales Tax Payable | 1,027.20 | D007, D006 | 2025-08-27 | finished_goods_sale_tax |
| 9 | Cash | Accounts Receivable | 15,195.50 | D008, D007 | 2025-08-25 | customer_payment |
| 10 | Accounts Payable | Cash | 2,971.58 | D009, D002 | 2025-08-27 | supplier_payment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 69,338.95
- Raw Materials Inventory: 13,098.79
- Work In Process: 9,937.63
- Finished Goods Inventory: 23,521.42
- Input Tax Receivable: 141.50

**Liabilities**
- Accounts Payable: 8,390.43
- Accrued Expenses: 1,416.58
- Sales Tax Payable: 1,027.20

**Equity**
- Retained Earnings: 22,291.85
- Share Capital: 82,912.23

**Totals:** Assets = 116,038.29; Liabilities = 10,834.21; Equity = 105,204.08
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [ ] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:

### Q3 — Are entries complete?
Are there any entries you would book that are MISSING from section 5? Or any entries in section 5 that should NOT be there?
- [ ] Complete and exact
- [ ] Missing entries (list them in notes)
- [ ] Extra entries that should not be booked (list them)
- Notes:

### Q4 — Are document references correct?
For each expected entry, is `doc_refs` the set of documents that actually support that posting?
- [ ] Yes, doc_refs are correct
- [ ] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes:

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [ ] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
