# Verification Packet — COV_MAN_M4_0093

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** August 2025
- **Period start → end:** 2025-08-01 → 2025-08-31
- **Entity:** Cedar Builders
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 16
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-08-01_

**Assets**
- Cash: 78,441.04
- Raw Materials Inventory: 29,943.42
- Work In Process: 23,963.74
- Finished Goods Inventory: 28,889.56
- Accounts Receivable: 6,402.06
- Equipment: 17,220.64

**Liabilities**
- Accounts Payable: 9,817.08
- Accrued Expenses: 4,791.66
- Notes Payable: 13,165.14

**Equity**
- Retained Earnings: 13,649.88
- Share Capital: 143,436.70


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
Statement Date: 2025-08-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $78,441.04
  - Section assets | Account Raw Materials Inventory | Amount $29,943.42
  - Section assets | Account Work In Process | Amount $23,963.74
  - Section assets | Account Finished Goods Inventory | Amount $28,889.56
  - Section assets | Account Accounts Receivable | Amount $6,402.06
  - Section assets | Account Equipment | Amount $17,220.64
  - Section liabilities | Account Accounts Payable | Amount $9,817.08
  - Section liabilities | Account Accrued Expenses | Amount $4,791.66
  - Section liabilities | Account Notes Payable | Amount $13,165.14
  - Section equity | Account Retained Earnings | Amount $13,649.88
  - Section equity | Account Share Capital | Amount $143,436.70

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-05

```
SUPPLIER INVOICE
================

From
----
Cedar Builders
75 Market Road, Mumbai
Document Date: 2025-08-05

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: August 2025

Terms
-----
Due Date: 2025-08-17

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 2025-08-17
Subtotal: $12,080.53
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $1,208.05
Total: $13,288.58

Supplier Bill Lines
-------------------
Lines:
  - Description Resin pellets | Quantity 319 | Unit Cost $37.87 | Amount $12,080.53

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-08-13

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: $16,418.20
Draw Amount: $59,315.53
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $75,733.73
Note: Scheduled lender activity for the selected period.
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2025-08-20

```
MATERIAL REQUISITION SLIP
=========================

From
----
Cedar Builders
75 Market Road, Mumbai
Date: 2025-08-20

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
Quantity Issued: 245
Issue Value: $9,303.54
Warehouse: Overflow Storage

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2025-08-20

```
PRODUCTION BATCH SHEET
======================

From
----
Cedar Builders
75 Market Road, Mumbai
Document Date: 2025-08-20

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: August 2025

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 30
Material Value: $9,303.54
Labor Value: $0.00
Overhead Value: $0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2025-08-21

```
DIRECT LABOR RECORD
===================

From
----
Cedar Builders
75 Market Road, Mumbai
Date: 2025-08-21

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: August 2025

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 39
Labor Value: $3,722.92
Labor Cash Paid: $3,722.92

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2025-08-23

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Cedar Builders
75 Market Road, Mumbai
Document Date: 2025-08-23

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: August 2025

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Retail Display
Units Completed: 69
Transfer Value: $18,239.51

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-23

```
PAYMENT ADVICE
==============

From
----
Cedar Builders
75 Market Road, Mumbai
Date: 2025-08-23

To
--
Riverfront Group

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: August 2025
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: $15,369.62
Reference: FGINV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D014 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-24

```
TRANSFER ADVICE
===============

From
----
Cedar Builders
75 Market Road, Mumbai
Document Date: 2025-08-24

Reference Box
-------------
Document ID: D014
Document Type: transfer_advice
Period: August 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $57,538.10
Transfer Date: 2025-08-24
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-08-25

```
PAYROLL SUMMARY
===============

From
----
Cedar Builders
75 Market Road, Mumbai
Document Date: 2025-08-25

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: August 2025
Headcount: 11
Gross Pay: $26,302.42
Employer Tax: 3,141.21
Cash Outflow: $29,443.63

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-26

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Cedar Builders
75 Market Road, Mumbai
Date: 2025-08-26

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: August 2025
Contract Ref: FGT-0001

Terms
-----
Due Date: 2025-09-08

Parties
-------
Customer: Riverfront Group
Contract Ref: FGT-0001
Currency: USD

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 2025-09-08
Subtotal: $22,630.63
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $1,584.14
Total: $24,214.77

Line Items
----------
Items:
  - Description Retail Display | Amount $22,630.63

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D010 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-28

```
PAYMENT ADVICE
==============

From
----
Cedar Builders
75 Market Road, Mumbai
Document Date: 2025-08-28

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D010
Document Type: payment_advice
Period: August 2025
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: $13,165.64
Reference: MAT-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-08-29

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Cedar Builders
75 Market Road, Mumbai
Date: 2025-08-29

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: August 2025

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 50
Overhead Value: $5,213.05
Accrued Overhead: $5,213.05

Explanation
-----------
Narrative: Factory overhead incurred this period has been accrued into work in process.

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-08-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $17,220.64
Useful Life Months: 48
Current Period Charge: $358.76
Accumulated Depreciation: 358.76
```

### Document D015 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-08-31

```
BANK STATEMENT
==============

From
----
Cedar Builders
75 Market Road, Mumbai
Date: 2025-08-31

Reference Box
-------------
Document ID: D015
Document Type: bank_statement
Period: August 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0093
Statement Currency: USD
Opening Balance: $78,441.04
Closing Balance: $49,255.90

Statement Rows
--------------
Rows:
  - Date 2025-08-13 | Description Loan draw LOAN-0001 | Amount $59,315.53 | Running Balance 
$137,756.57
  - Date 2025-08-21 | Description Direct labor BATCH-0001 | Amount $-3,722.92 | Running 
Balance $134,033.65
  - Date 2025-08-23 | Description Customer settlement FGINV-0001 | Amount $15,369.62 | 
Running Balance $149,403.27
  - Date 2025-08-24 | Description Transfer out TRX-0001 | Amount $-57,538.10 | Running 
Balance $91,865.17
  - Date 2025-08-25 | Description Payroll PAYRUN-0001 | Amount $-29,443.63 | Running Balance
 $62,421.54
  - Date 2025-08-28 | Description Supplier settlement MAT-0001 | Amount $-13,165.64 | 
Running Balance $49,255.90

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-08-31

```
BANK STATEMENT
==============

From
----
Cedar Builders
75 Market Road, Mumbai
Document Date: 2025-08-31

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: August 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-9399
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $57,538.10

Statement Rows
--------------
Rows:
  - Date 2025-08-24 | Description Transfer in TRX-0001 | Amount $57,538.10 | Running Balance
 $57,538.10

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 12,080.53 | D002 | 2025-08-05 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 1,208.05 | D002 | 2025-08-05 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 9,303.54 | D003, D004, D002 | 2025-08-20 | material_issue |
| 4 | Work In Process | Cash | 3,722.92 | D005, D004 | 2025-08-21 | direct_labor_labor |
| 5 | Work In Process | Accrued Expenses | 5,213.05 | D006, D004 | 2025-08-29 | overhead_accrual_overhead |
| 6 | Finished Goods Inventory | Work In Process | 18,239.51 | D007, D004 | 2025-08-23 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 22,630.63 | D008, D007 | 2025-08-26 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 18,239.51 | D008, D007 | 2025-08-26 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | Sales Tax Payable | 1,584.14 | D008, D007 | 2025-08-26 | finished_goods_sale_tax |
| 10 | Cash | Accounts Receivable | 15,369.62 | D009, D008 | 2025-08-23 | customer_payment |
| 11 | Accounts Payable | Cash | 13,165.64 | D010, D002 | 2025-08-28 | supplier_payment |
| 12 | Salaries Expense | Cash | 26,302.42 | D011 | 2025-08-25 | payroll_gross |
| 13 | Payroll Tax Expense | Cash | 3,141.21 | D011 | 2025-08-25 | payroll_tax |
| 14 | Cash | Loans Payable | 59,315.53 | D012 | 2025-08-13 | loan_draw |
| 15 | Depreciation Expense | Accumulated Depreciation | 358.76 | D013 | 2025-08-31 | depreciation |
| 16 | Reserve Cash | Cash | 57,538.10 | D014 | 2025-08-24 | interbank_transfer |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 49,255.90
- Raw Materials Inventory: 32,720.41
- Work In Process: 23,963.74
- Finished Goods Inventory: 28,889.56
- Accounts Receivable: 15,247.21
- Equipment: 17,220.64
- Input Tax Receivable: 1,208.05
- Accumulated Depreciation: -358.76
- Reserve Cash: 57,538.10

**Liabilities**
- Accounts Payable: 9,940.02
- Accrued Expenses: 10,004.71
- Notes Payable: 13,165.14
- Sales Tax Payable: 1,584.14
- Loans Payable: 59,315.53

**Equity**
- Retained Earnings: -11,761.39
- Share Capital: 143,436.70

**Totals:** Assets = 225,684.85; Liabilities = 94,009.54; Equity = 131,675.31
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
