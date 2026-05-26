# Verification Packet — COV_MAN_M3_0092

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 3
- **Period type:** month
- **Period label:** December 2024
- **Period start → end:** 2024-12-01 → 2024-12-31
- **Entity:** Pioneer Retail Group
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 12
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-12-01_

**Assets**
- Cash: 61,393.58
- Raw Materials Inventory: 17,918.21
- Work In Process: 16,522.52
- Finished Goods Inventory: 26,747.81
- Accounts Receivable: 8,653.02

**Liabilities**
- Accounts Payable: 13,683.84
- Accrued Expenses: 2,217.84

**Equity**
- Retained Earnings: 14,930.90
- Share Capital: 100,402.56


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-12-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/12/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 61,393.58
  - Section assets | Account Raw Materials Inventory | Amount GBP 17,918.21
  - Section assets | Account Work In Process | Amount GBP 16,522.52
  - Section assets | Account Finished Goods Inventory | Amount GBP 26,747.81
  - Section assets | Account Accounts Receivable | Amount GBP 8,653.02
  - Section liabilities | Account Accounts Payable | Amount GBP 13,683.84
  - Section liabilities | Account Accrued Expenses | Amount GBP 2,217.84
  - Section equity | Account Retained Earnings | Amount GBP 14,930.90
  - Section equity | Account Share Capital | Amount GBP 100,402.56

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-08

```
SUPPLIER INVOICE
================

From
----
Pioneer Retail Group
14 King Street, Pune
Document Date: 08/12/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: December 2024

Terms
-----
Due Date: 22/12/2024

Supplier Header
---------------
Supplier: Meridian Support LLP
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 22/12/2024
Subtotal: GBP 9,151.01
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 1,830.20
Total: GBP 10,981.21

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 253 | Unit Cost GBP 36.17 | Amount GBP 9,151.01

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2024-12-15

```
DIRECT LABOR RECORD
===================

From
----
Pioneer Retail Group
14 King Street, Pune
Date: 15/12/2024

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: December 2024

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 56
Labor Value: GBP 6,350.48
Labor Cash Paid: GBP 6,350.48

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-12-16

```
MATERIAL REQUISITION SLIP
=========================

From
----
Pioneer Retail Group
14 King Street, Pune
Date: 16/12/2024

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: December 2024

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Control boards
Quantity Issued: 194
Issue Value: GBP 7,020.40
Warehouse: Plant Floor Store

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-12-16

```
PRODUCTION BATCH SHEET
======================

From
----
Pioneer Retail Group
14 King Street, Pune
Date: 16/12/2024

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: December 2024

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 66
Material Value: GBP 7,020.40
Labor Value: GBP 0.00
Overhead Value: GBP 0.00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-23

```
CUSTOMER INVOICE
================

From
----
Pioneer Retail Group
14 King Street, Pune
Document Date: 23/12/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: December 2024
Contract Ref: FGT-0001

Terms
-----
Due Date: 05/01/2025

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: FGT-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 05/01/2025
Subtotal: GBP 33,936.55
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 3,393.66
Total: GBP 37,330.21

Line Items
----------
Items:
  - Description Retail Display | Amount GBP 33,936.55

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-12-23

```
PAYROLL SUMMARY
===============

From
----
Pioneer Retail Group
14 King Street, Pune
Date: 23/12/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: December 2024
Headcount: 3
Gross Pay: GBP 13,942.24
Employer Tax: 1,283.23
Cash Outflow: GBP 15,225.47

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-12-24

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Pioneer Retail Group
14 King Street, Pune
Date: 24/12/2024

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: December 2024

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Retail Display
Units Completed: 33
Transfer Value: GBP 27,164.44

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-25

```
PAYMENT ADVICE
==============

From
----
Pioneer Retail Group
14 King Street, Pune
Date: 25/12/2024

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D010
Document Type: payment_advice
Period: December 2024
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: GBP 10,981.21
Reference: MAT-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-26

```
PAYMENT ADVICE
==============

From
----
Pioneer Retail Group
14 King Street, Pune
Document Date: 26/12/2024

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: December 2024
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: GBP 37,330.21
Reference: FGINV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-28

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Pioneer Retail Group
14 King Street, Pune
Document Date: 28/12/2024

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: December 2024

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 45
Overhead Value: GBP 13,793.56
Accrued Overhead: GBP 13,793.56

Explanation
-----------
Narrative: Factory overhead incurred this period has been accrued into work in process.

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D012 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Retail Group
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D012
Document Type: bank_statement
Period: December 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0092
Statement Currency: GBP
Opening Balance: GBP 61,393.58
Closing Balance: GBP 66,166.63

Statement Rows
--------------
Rows:
  - Date 15/12/2024 | Description Direct labor BATCH-0001 | Amount GBP -6,350.48 | Running 
Balance GBP 55,043.10
  - Date 23/12/2024 | Description Payroll PAYRUN-0001 | Amount GBP -15,225.47 | Running 
Balance GBP 39,817.63
  - Date 25/12/2024 | Description Supplier settlement MAT-0001 | Amount GBP -10,981.21 | 
Running Balance GBP 28,836.42
  - Date 26/12/2024 | Description Customer settlement FGINV-0001 | Amount GBP 37,330.21 | 
Running Balance GBP 66,166.63

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D012
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 9,151.01 | D002 | 2024-12-08 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 1,830.20 | D002 | 2024-12-08 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 7,020.40 | D003, D004, D002 | 2024-12-16 | material_issue |
| 4 | Work In Process | Cash | 6,350.48 | D005, D004 | 2024-12-15 | direct_labor_labor |
| 5 | Work In Process | Accrued Expenses | 13,793.56 | D006, D004 | 2024-12-28 | overhead_accrual_overhead |
| 6 | Finished Goods Inventory | Work In Process | 27,164.44 | D007, D004 | 2024-12-24 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 33,936.55 | D008, D007 | 2024-12-23 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 27,164.44 | D008, D007 | 2024-12-23 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | Sales Tax Payable | 3,393.66 | D008, D007 | 2024-12-23 | finished_goods_sale_tax |
| 10 | Cash | Accounts Receivable | 37,330.21 | D009, D008 | 2024-12-26 | customer_payment |
| 11 | Accounts Payable | Cash | 10,981.21 | D010, D002 | 2024-12-25 | supplier_payment |
| 12 | Salaries Expense | Cash | 13,942.24 | D011 | 2024-12-23 | payroll_gross |
| 13 | Payroll Tax Expense | Cash | 1,283.23 | D011 | 2024-12-23 | payroll_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 66,166.63
- Raw Materials Inventory: 20,048.82
- Work In Process: 16,522.52
- Finished Goods Inventory: 26,747.81
- Accounts Receivable: 8,653.02
- Input Tax Receivable: 1,830.20

**Liabilities**
- Accounts Payable: 13,683.84
- Accrued Expenses: 16,011.40
- Sales Tax Payable: 3,393.66

**Equity**
- Retained Earnings: 6,477.54
- Share Capital: 100,402.56

**Totals:** Assets = 139,969.00; Liabilities = 33,088.90; Equity = 106,880.10
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
- Notes: Support maps cleanly to the postings.
