# Verification Packet — COV_MAN_Q4_0098

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q3 FY 2024
- **Period start → end:** 2024-07-01 → 2024-09-30
- **Entity:** Atlas Software
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 21
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-07-01_

**Assets**
- Cash: 141,815.77
- Raw Materials Inventory: 94,584.47
- Work In Process: 50,390.22
- Finished Goods Inventory: 29,716.62
- Accounts Receivable: 22,794.85
- Equipment: 73,862.42

**Liabilities**
- Accounts Payable: 25,769.86
- Accrued Expenses: 7,489.49
- Notes Payable: 14,950.51
- Loans Payable: 41,524.32

**Equity**
- Retained Earnings: 27,230.27
- Share Capital: 296,199.90


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-07-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/07/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 141,815.77
  - Section assets | Account Raw Materials Inventory | Amount GBP 94,584.47
  - Section assets | Account Work In Process | Amount GBP 50,390.22
  - Section assets | Account Finished Goods Inventory | Amount GBP 29,716.62
  - Section assets | Account Accounts Receivable | Amount GBP 22,794.85
  - Section assets | Account Equipment | Amount GBP 73,862.42
  - Section liabilities | Account Accounts Payable | Amount GBP 25,769.86
  - Section liabilities | Account Accrued Expenses | Amount GBP 7,489.49
  - Section liabilities | Account Notes Payable | Amount GBP 14,950.51
  - Section liabilities | Account Loans Payable | Amount GBP 41,524.32
  - Section equity | Account Retained Earnings | Amount GBP 27,230.27
  - Section equity | Account Share Capital | Amount GBP 296,199.90

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D016 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-07

```
CUSTOMER INVOICE
================

From
----
Atlas Software
14 King Street, Pune
Date: 07/07/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D016
Document Type: customer_invoice
Period: Q3 FY 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 30/07/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0001

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 30/07/2024
Total: GBP 15,853.25

Line Items
----------
Items:
  - Description Implementation work | Amount GBP 6,278.97
  - Description Milestone 1 work | Amount GBP 9,574.28

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-08

```
CUSTOMER INVOICE
================

From
----
Atlas Software
14 King Street, Pune
Date: 08/07/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D017
Document Type: customer_invoice
Period: Q3 FY 2024
Contract Ref: CTR-0002

Terms
-----
Due Date: 22/07/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0002

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 22/07/2024
Total: GBP 33,888.64

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 13,090.96
  - Description Milestone 2 work | Amount GBP 20,797.68

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-26

```
SUPPLIER INVOICE
================

From
----
Atlas Software
14 King Street, Pune
Date: 26/07/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q3 FY 2024

Terms
-----
Due Date: 15/08/2024

Supplier Header
---------------
Supplier: Golden State Finance
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 15/08/2024
Subtotal: GBP 14,860.30
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 1,486.03
Total: GBP 16,346.33

Supplier Bill Lines
-------------------
Lines:
  - Description Packing film | Quantity 230 | Unit Cost GBP 64.61 | Amount GBP 14,860.30

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D018 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-08

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Atlas Software
14 King Street, Pune
Date: 08/08/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_invoice
Period: Q3 FY 2024
Contract Ref: CTR-0003

Terms
-----
Due Date: 24/08/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 24/08/2024
Total: GBP 32,148.63

Line Items
----------
Items:
  - Description Implementation work | Amount GBP 8,160.21
  - Description Milestone 3 work | Amount GBP 23,988.42

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-08-11

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: GBP 40,061.76
Draw Amount: GBP 148,831.45
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 188,893.21
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2024-08-13

```
DIRECT LABOR RECORD
===================

From
----
Atlas Software
14 King Street, Pune
Date: 13/08/2024

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: Q3 FY 2024

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 73
Labor Value: GBP 33,046.51
Labor Cash Paid: GBP 33,046.51

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-08-23

```
MATERIAL REQUISITION SLIP
=========================

From
----
Atlas Software
14 King Street, Pune
Date: 23/08/2024

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: Q3 FY 2024

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Packing film
Quantity Issued: 159
Issue Value: GBP 10,283.83
Warehouse: Main Warehouse

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-08-23

```
PRODUCTION BATCH SHEET
======================

From
----
Atlas Software
14 King Street, Pune
Document Date: 23/08/2024

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: Q3 FY 2024

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 51
Material Value: GBP 10,283.83
Labor Value: GBP 0.00
Overhead Value: GBP 0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D019 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-06

```
PAYMENT ADVICE
==============

From
----
Atlas Software
14 King Street, Pune
Date: 06/09/2024

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D019
Document Type: payment_advice
Period: Q3 FY 2024
Reference: Multiple invoice allocation

Payment Details
---------------
Advice Number: PAY-0003
Counterparty: Metro Edge Partners
Amount: GBP 70,839.65
Reference: Multiple invoice allocation
Payment Method: ACH
Payment For: Combined settlement against several invoices

Allocation Details
------------------
Allocations:
  - Reference INV-0001 | Allocated Amount GBP 15,853.25 | Status Closed
  - Reference INV-0002 | Allocated Amount GBP 33,888.64 | Status Closed
  - Reference INV-0003 | Allocated Amount GBP 21,097.76 | Status Partially paid

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-08

```
PAYROLL SUMMARY
===============

From
----
Atlas Software
14 King Street, Pune
Date: 08/09/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q3 FY 2024
Headcount: 9
Gross Pay: GBP 38,123.27
Employer Tax: 4,493.02
Cash Outflow: GBP 42,616.29

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-12

```
PAYMENT ADVICE
==============

From
----
Atlas Software
14 King Street, Pune
Document Date: 12/09/2024

To
--
Aster Point Services

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: Q3 FY 2024
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: GBP 103,880.23
Reference: FGINV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D010 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-12

```
PAYMENT ADVICE
==============

From
----
Atlas Software
14 King Street, Pune
Date: 12/09/2024

To
--
Golden State Finance

Reference Box
-------------
Document ID: D010
Document Type: payment_advice
Period: Q3 FY 2024
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: GBP 13,745.59
Reference: MAT-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-09-15

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Atlas Software
14 King Street, Pune
Date: 15/09/2024

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: Q3 FY 2024

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Retail Display
Units Completed: 40
Transfer Value: GBP 58,148.62

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-15

```
CUSTOMER INVOICE
================

From
----
Atlas Software
14 King Street, Pune
Document Date: 15/09/2024

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: Q3 FY 2024
Contract Ref: FGT-0001

Terms
-----
Due Date: 02/10/2024

Parties
-------
Customer: Aster Point Services
Contract Ref: FGT-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 02/10/2024
Subtotal: GBP 89,538.50
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 17,907.70
Total: GBP 107,446.20

Line Items
----------
Items:
  - Description Retail Display | Amount GBP 89,538.50

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D014 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-17

```
TRANSFER ADVICE
===============

From
----
Atlas Software
14 King Street, Pune
Date: 17/09/2024

Reference Box
-------------
Document ID: D014
Document Type: transfer_advice
Period: Q3 FY 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: GBP 220,641.81
Transfer Date: 17/09/2024
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-28

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Atlas Software
14 King Street, Pune
Document Date: 28/09/2024

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: Q3 FY 2024

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Retail Display
Planned Units: 73
Overhead Value: GBP 14,818.28
Accrued Overhead: GBP 14,818.28

Explanation
-----------
Narrative: Factory overhead incurred this period has been accrued into work in process.

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: GBP 73,862.42
Useful Life Months: 48
Current Period Charge: GBP 4,616.40
Accumulated Depreciation: 4,616.40
```

### Document D015 — Scrap Report

- **Type:** `scrap_report`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-30

```
SCRAP REPORT
============

From
----
Atlas Software
14 King Street, Pune
Date: 30/09/2024

Reference Box
-------------
Document ID: D015
Document Type: scrap_report
Period: Q3 FY 2024

Approval / Context
------------------
Reason: Failed quality test

Scrap Summary
-------------
Report Number: SCRAP-0001
Batch Or Lot: OPEN-FG
Reason: Failed quality test
Write Down: GBP 3,796.39

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Atlas Software
14 King Street, Pune
Date: 30/09/2024

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: Q3 FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0098
Statement Currency: GBP
Opening Balance: GBP 141,815.77
Closing Balance: GBP 155,316.90

Statement Rows
--------------
Rows:
  - Date 11/08/2024 | Description Loan draw LOAN-0001 | Amount GBP 148,831.45 | Running 
Balance GBP 290,647.22
  - Date 13/08/2024 | Description Direct labor BATCH-0001 | Amount GBP -33,046.51 | Running 
Balance GBP 257,600.71
  - Date 06/09/2024 | Description Combined customer settlement PAY-0003 | Amount GBP 
70,839.65 | Running Balance GBP 328,440.36
  - Date 08/09/2024 | Description Payroll PAYRUN-0001 | Amount GBP -42,616.29 | Running 
Balance GBP 285,824.07
  - Date 12/09/2024 | Description Customer settlement FGINV-0001 | Amount GBP 103,880.23 | 
Running Balance GBP 389,704.30
  - Date 12/09/2024 | Description Supplier settlement MAT-0001 | Amount GBP -13,745.59 | 
Running Balance GBP 375,958.71
  - Date 17/09/2024 | Description Transfer out TRX-0001 | Amount GBP -220,641.81 | Running 
Balance GBP 155,316.90

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Atlas Software
14 King Street, Pune
Date: 30/09/2024

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: Q3 FY 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-9899
Statement Currency: GBP
Opening Balance: GBP 0.00
Closing Balance: GBP 220,641.81

Statement Rows
--------------
Rows:
  - Date 17/09/2024 | Description Transfer in TRX-0001 | Amount GBP 220,641.81 | Running 
Balance GBP 220,641.81

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
| 1 | Raw Materials Inventory | Accounts Payable | 14,860.30 | D002 | 2024-07-26 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 1,486.03 | D002 | 2024-07-26 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 10,283.83 | D003, D004, D002 | 2024-08-23 | material_issue |
| 4 | Work In Process | Cash | 33,046.51 | D005, D004 | 2024-08-13 | direct_labor_labor |
| 5 | Work In Process | Accrued Expenses | 14,818.28 | D006, D004 | 2024-09-28 | overhead_accrual_overhead |
| 6 | Finished Goods Inventory | Work In Process | 58,148.62 | D007, D004 | 2024-09-15 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 89,538.50 | D008, D007 | 2024-09-15 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 58,148.62 | D008, D007 | 2024-09-15 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | Sales Tax Payable | 17,907.70 | D008, D007 | 2024-09-15 | finished_goods_sale_tax |
| 10 | Cash | Accounts Receivable | 103,880.23 | D009, D008 | 2024-09-12 | customer_payment |
| 11 | Accounts Payable | Cash | 13,745.59 | D010, D002 | 2024-09-12 | supplier_payment |
| 12 | Salaries Expense | Cash | 38,123.27 | D011 | 2024-09-08 | payroll_gross |
| 13 | Payroll Tax Expense | Cash | 4,493.02 | D011 | 2024-09-08 | payroll_tax |
| 14 | Cash | Loans Payable | 148,831.45 | D012 | 2024-08-11 | loan_draw |
| 15 | Depreciation Expense | Accumulated Depreciation | 4,616.40 | D013 | 2024-09-30 | depreciation |
| 16 | Reserve Cash | Cash | 220,641.81 | D014 | 2024-09-17 | interbank_transfer |
| 17 | Inventory Shrinkage Expense | Finished Goods Inventory | 3,796.39 | D015, D001 | 2024-09-30 | scrap_report |
| 18 | Accounts Receivable | Sales Revenue | 15,853.25 | D016 | 2024-07-07 | multi_invoice_payment_invoice_1 |
| 19 | Accounts Receivable | Sales Revenue | 33,888.64 | D017 | 2024-07-08 | multi_invoice_payment_invoice_2 |
| 20 | Accounts Receivable | Sales Revenue | 32,148.63 | D018 | 2024-08-08 | multi_invoice_payment_invoice_3 |
| 21 | Cash | Accounts Receivable | 15,853.25 | D019, D016 | 2024-09-06 | multi_invoice_payment_INV-0001 |
| 22 | Cash | Accounts Receivable | 33,888.64 | D019, D017 | 2024-09-06 | multi_invoice_payment_INV-0002 |
| 23 | Cash | Accounts Receivable | 21,097.76 | D019, D018 | 2024-09-06 | multi_invoice_payment_INV-0003 |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 155,316.90
- Raw Materials Inventory: 99,160.94
- Work In Process: 50,390.22
- Finished Goods Inventory: 25,920.23
- Accounts Receivable: 37,411.69
- Equipment: 73,862.42
- Input Tax Receivable: 1,486.03
- Accumulated Depreciation: -4,616.40
- Reserve Cash: 220,641.81

**Liabilities**
- Accounts Payable: 28,370.60
- Accrued Expenses: 22,307.77
- Notes Payable: 14,950.51
- Loans Payable: 190,355.77
- Sales Tax Payable: 17,907.70

**Equity**
- Retained Earnings: 89,481.59
- Share Capital: 296,199.90

**Totals:** Assets = 659,573.84; Liabilities = 273,892.35; Equity = 385,681.49
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
- Notes: Complex packet — entries hold up well on review.
