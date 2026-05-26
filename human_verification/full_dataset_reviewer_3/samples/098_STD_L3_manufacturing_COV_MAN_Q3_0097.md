# Verification Packet — COV_MAN_Q3_0097

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q1 FY 2025
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Pioneer Property Services
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 13
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 208,717.75
- Raw Materials Inventory: 72,634.04
- Work In Process: 28,225.14
- Finished Goods Inventory: 36,735.98
- Accounts Receivable: 14,282.34

**Liabilities**
- Accounts Payable: 19,224.61
- Accrued Expenses: 7,144.74

**Equity**
- Retained Earnings: 21,034.86
- Share Capital: 313,191.04


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 208.717,75
  - Section assets | Account Raw Materials Inventory | Amount EUR 72.634,04
  - Section assets | Account Work In Process | Amount EUR 28.225,14
  - Section assets | Account Finished Goods Inventory | Amount EUR 36.735,98
  - Section assets | Account Accounts Receivable | Amount EUR 14.282,34
  - Section liabilities | Account Accounts Payable | Amount EUR 19.224,61
  - Section liabilities | Account Accrued Expenses | Amount EUR 7.144,74
  - Section equity | Account Retained Earnings | Amount EUR 21.034,86
  - Section equity | Account Share Capital | Amount EUR 313.191,04

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-21

```
SUPPLIER INVOICE
================

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Document Date: 21/01/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q1 FY 2025

Terms
-----
Due Date: 14/02/2025

Supplier Header
---------------
Supplier: Vertex Supply Co.
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 14/02/2025
Subtotal: EUR 27.953,10
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 1.397,65
Total: EUR 29.350,75

Supplier Bill Lines
-------------------
Lines:
  - Description Steel sheets | Quantity 406 | Unit Cost EUR 68,85 | Amount EUR 27.953,10

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2025-02-25

```
DIRECT LABOR RECORD
===================

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Document Date: 25/02/2025

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: Q1 FY 2025

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 45
Labor Value: EUR 19.587,26
Labor Cash Paid: EUR 19.587,26

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2025-03-02

```
MATERIAL REQUISITION SLIP
=========================

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Date: 02/03/2025

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: Q1 FY 2025

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Steel sheets
Quantity Issued: 214
Issue Value: EUR 14.756,92
Warehouse: Main Warehouse

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2025-03-02

```
PRODUCTION BATCH SHEET
======================

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Date: 02/03/2025

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: Q1 FY 2025

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 57
Material Value: EUR 14.756,92
Labor Value: EUR 0,00
Overhead Value: EUR 0,00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-03-09

```
PAYMENT ADVICE
==============

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Date: 09/03/2025

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: Q1 FY 2025
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: EUR 102.875,93
Reference: FGINV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2025-03-11

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Document Date: 11/03/2025

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: Q1 FY 2025

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Panel Kit
Units Completed: 40
Transfer Value: EUR 61.988,11

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D010 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-03-11

```
PAYMENT ADVICE
==============

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Document Date: 11/03/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D010
Document Type: payment_advice
Period: Q1 FY 2025
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: EUR 29.350,75
Reference: MAT-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-03-17

```
PAYROLL SUMMARY
===============

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Date: 17/03/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q1 FY 2025
Headcount: 8
Gross Pay: EUR 29.216,67
Employer Tax: 3.155,18
Cash Outflow: EUR 32.371,85

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-18

```
CUSTOMER INVOICE
================

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Date: 18/03/2025

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: Q1 FY 2025
Contract Ref: FGT-0001

Terms
-----
Due Date: 10/04/2025

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: FGT-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 10/04/2025
Subtotal: EUR 95.035,50
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 7.840,43
Total: EUR 102.875,93

Line Items
----------
Items:
  - Description Panel Kit | Amount EUR 95.035,50

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: Q1 FY 2025

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 20
Overhead Value: EUR 27.643,93
Accrued Overhead: EUR 27.643,93

Explanation
-----------
Narrative: Factory overhead incurred this period has been accrued into work in process.

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D012 — Scrap Report

- **Type:** `scrap_report`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SCRAP REPORT
============

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D012
Document Type: scrap_report
Period: Q1 FY 2025

Approval / Context
------------------
Reason: Failed quality test

Scrap Summary
-------------
Report Number: SCRAP-0001
Batch Or Lot: OPEN-FG
Reason: Failed quality test
Write Down: EUR 6.824,97

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D013 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Pioneer Property Services
18 Marina Avenue, Chennai
Date: 31/03/2025

Reference Box
-------------
Document ID: D013
Document Type: bank_statement
Period: Q1 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0097
Statement Currency: EUR
Opening Balance: EUR 208.717,75
Closing Balance: EUR 230.283,82

Statement Rows
--------------
Rows:
  - Date 25/02/2025 | Description Direct labor BATCH-0001 | Amount EUR -19.587,26 | Running 
Balance EUR 189.130,49
  - Date 09/03/2025 | Description Customer settlement FGINV-0001 | Amount EUR 102.875,93 | 
Running Balance EUR 292.006,42
  - Date 11/03/2025 | Description Supplier settlement MAT-0001 | Amount EUR -29.350,75 | 
Running Balance EUR 262.655,67
  - Date 17/03/2025 | Description Payroll PAYRUN-0001 | Amount EUR -32.371,85 | Running 
Balance EUR 230.283,82

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D013
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 27,953.10 | D002 | 2025-01-21 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 1,397.65 | D002 | 2025-01-21 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 14,756.92 | D003, D004, D002 | 2025-03-02 | material_issue |
| 4 | Work In Process | Cash | 19,587.26 | D005, D004 | 2025-02-25 | direct_labor_labor |
| 5 | Work In Process | Accrued Expenses | 27,643.93 | D006, D004 | 2025-03-31 | overhead_accrual_overhead |
| 6 | Finished Goods Inventory | Work In Process | 61,988.11 | D007, D004 | 2025-03-11 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 95,035.50 | D008, D007 | 2025-03-18 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 61,988.11 | D008, D007 | 2025-03-18 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | Sales Tax Payable | 7,840.43 | D008, D007 | 2025-03-18 | finished_goods_sale_tax |
| 10 | Cash | Accounts Receivable | 102,875.93 | D009, D008 | 2025-03-09 | customer_payment |
| 11 | Accounts Payable | Cash | 29,350.75 | D010, D002 | 2025-03-11 | supplier_payment |
| 12 | Salaries Expense | Cash | 29,216.67 | D011 | 2025-03-17 | payroll_gross |
| 13 | Payroll Tax Expense | Cash | 3,155.18 | D011 | 2025-03-17 | payroll_tax |
| 14 | Inventory Shrinkage Expense | Finished Goods Inventory | 6,824.97 | D012, D001 | 2025-03-31 | scrap_report |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 230,283.82
- Raw Materials Inventory: 85,830.22
- Work In Process: 28,225.14
- Finished Goods Inventory: 29,911.01
- Accounts Receivable: 14,282.34
- Input Tax Receivable: 1,397.65

**Liabilities**
- Accounts Payable: 19,224.61
- Accrued Expenses: 34,788.67
- Sales Tax Payable: 7,840.43

**Equity**
- Retained Earnings: 14,885.43
- Share Capital: 313,191.04

**Totals:** Assets = 389,930.18; Liabilities = 61,853.71; Equity = 328,076.47
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
