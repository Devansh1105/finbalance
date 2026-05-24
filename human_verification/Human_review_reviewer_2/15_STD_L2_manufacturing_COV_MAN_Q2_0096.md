# Verification Packet — COV_MAN_Q2_0096

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 2
- **Period type:** quarter
- **Period label:** Q4 FY 2025
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Cedar Distribution
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 107,254.99
- Raw Materials Inventory: 47,721.70
- Work In Process: 40,120.47
- Finished Goods Inventory: 58,472.43

**Liabilities**
- Accounts Payable: 23,488.65
- Accrued Expenses: 6,260.98

**Equity**
- Retained Earnings: 21,721.00
- Share Capital: 202,098.96


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-10-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $107,254.99
  - Section assets | Account Raw Materials Inventory | Amount $47,721.70
  - Section assets | Account Work In Process | Amount $40,120.47
  - Section assets | Account Finished Goods Inventory | Amount $58,472.43
  - Section liabilities | Account Accounts Payable | Amount $23,488.65
  - Section liabilities | Account Accrued Expenses | Amount $6,260.98
  - Section equity | Account Retained Earnings | Amount $21,721.00
  - Section equity | Account Share Capital | Amount $202,098.96

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-05

```
SUPPLIER INVOICE
================

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Date: 2025-10-05

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-10-21

Supplier Header
---------------
Supplier: Meridian Support LLP
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 2025-10-21
Total: $5,970.22

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 239 | Unit Cost $24.98 | Amount $5,970.22

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2025-11-03

```
DIRECT LABOR RECORD
===================

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Date: 2025-11-03

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: Q4 FY 2025

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 65
Labor Value: $23,262.00
Labor Cash Paid: $23,262.00

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2025-11-07

```
MATERIAL REQUISITION SLIP
=========================

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Date: 2025-11-07

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: Q4 FY 2025

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Control boards
Quantity Issued: 157
Issue Value: $3,940.56
Warehouse: Plant Floor Store

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2025-11-07

```
PRODUCTION BATCH SHEET
======================

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Document Date: 2025-11-07

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: Q4 FY 2025

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 45
Material Value: $3,940.56
Labor Value: $0.00
Overhead Value: $0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-12-01

```
CUSTOMER INVOICE
================

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Document Date: 2025-12-01

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: FGT-0001

Terms
-----
Due Date: 2025-12-25

Parties
-------
Customer: Aster Point Services
Contract Ref: FGT-0001
Currency: USD

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 2025-12-25
Total: $44,937.87

Line Items
----------
Items:
  - Description Retail Display | Amount $44,937.87

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D006 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2025-12-13

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Document Date: 2025-12-13

Reference Box
-------------
Document ID: D006
Document Type: finished_goods_transfer_note
Period: Q4 FY 2025

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Retail Display
Units Completed: 51
Transfer Value: $27,202.56

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D008 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-13

```
PAYMENT ADVICE
==============

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Date: 2025-12-13

To
--
Aster Point Services

Reference Box
-------------
Document ID: D008
Document Type: payment_advice
Period: Q4 FY 2025
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: $44,937.87
Reference: FGINV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-21

```
PAYMENT ADVICE
==============

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Date: 2025-12-21

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: Q4 FY 2025
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: $5,970.22
Reference: MAT-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Cedar Distribution
90 Hill Park, Hyderabad
Date: 2025-12-31

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: Q4 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0096
Statement Currency: USD
Opening Balance: $107,254.99
Closing Balance: $122,960.64

Statement Rows
--------------
Rows:
  - Date 2025-11-03 | Description Direct labor BATCH-0001 | Amount $-23,262.00 | Running 
Balance $83,992.99
  - Date 2025-12-13 | Description Customer settlement FGINV-0001 | Amount $44,937.87 | 
Running Balance $128,930.86
  - Date 2025-12-21 | Description Supplier settlement MAT-0001 | Amount $-5,970.22 | Running
 Balance $122,960.64

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
| 1 | Raw Materials Inventory | Accounts Payable | 5,970.22 | D002 | 2025-10-05 | raw_material_purchase |
| 2 | Work In Process | Raw Materials Inventory | 3,940.56 | D003, D004, D002 | 2025-11-07 | material_issue |
| 3 | Work In Process | Cash | 23,262.00 | D005, D004 | 2025-11-03 | direct_labor_labor |
| 4 | Finished Goods Inventory | Work In Process | 27,202.56 | D006, D004 | 2025-12-13 | finished_goods_transfer |
| 5 | Accounts Receivable | Sales Revenue | 44,937.87 | D007, D006 | 2025-12-01 | finished_goods_sale_sale |
| 6 | Cost of Goods Sold | Finished Goods Inventory | 27,202.56 | D007, D006 | 2025-12-01 | finished_goods_sale_cogs |
| 7 | Cash | Accounts Receivable | 44,937.87 | D008, D007 | 2025-12-13 | customer_payment |
| 8 | Accounts Payable | Cash | 5,970.22 | D009, D002 | 2025-12-21 | supplier_payment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 122,960.64
- Raw Materials Inventory: 49,751.36
- Work In Process: 40,120.47
- Finished Goods Inventory: 58,472.43

**Liabilities**
- Accounts Payable: 23,488.65
- Accrued Expenses: 6,260.98

**Equity**
- Retained Earnings: 39,456.31
- Share Capital: 202,098.96

**Totals:** Assets = 271,304.90; Liabilities = 29,749.63; Equity = 241,555.27
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
- Notes:
