# Verification Packet — COV_MAN_M5_0094

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** July 2024
- **Period start → end:** 2024-07-01 → 2024-07-31
- **Entity:** Willow Distribution
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 21
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-07-01_

**Assets**
- Cash: 62,902.34
- Raw Materials Inventory: 23,398.09
- Work In Process: 23,087.42
- Finished Goods Inventory: 35,622.74
- Accounts Receivable: 7,573.48
- Equipment: 37,873.23

**Liabilities**
- Accounts Payable: 8,436.32
- Accrued Expenses: 4,677.56
- Notes Payable: 16,140.80

**Equity**
- Retained Earnings: 10,404.61
- Share Capital: 150,798.01


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
  - Section assets | Account Cash | Amount EUR 62.902,34
  - Section assets | Account Raw Materials Inventory | Amount EUR 23.398,09
  - Section assets | Account Work In Process | Amount EUR 23.087,42
  - Section assets | Account Finished Goods Inventory | Amount EUR 35.622,74
  - Section assets | Account Accounts Receivable | Amount EUR 7.573,48
  - Section assets | Account Equipment | Amount EUR 37.873,23
  - Section liabilities | Account Accounts Payable | Amount EUR 8.436,32
  - Section liabilities | Account Accrued Expenses | Amount EUR 4.677,56
  - Section liabilities | Account Notes Payable | Amount EUR 16.140,80
  - Section equity | Account Retained Earnings | Amount EUR 10.404,61
  - Section equity | Account Share Capital | Amount EUR 150.798,01

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-05

```
SUPPLIER INVOICE
================

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 05/07/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: July 2024

Terms
-----
Due Date: 27/07/2024

Supplier Header
---------------
Supplier: Prime Utility Desk
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 27/07/2024
Subtotal: EUR 20.920,96
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 1.725,98
Total: EUR 22.646,94

Supplier Bill Lines
-------------------
Lines:
  - Description Control boards | Quantity 337 | Unit Cost EUR 62,08 | Amount EUR 20.920,96

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D017 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2024-07-05

```
CUSTOMER INVOICE
================

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 05/07/2024

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D017
Document Type: customer_invoice
Period: July 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 22/07/2024

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0001

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 22/07/2024
Total: EUR 15.872,16

Line Items
----------
Items:
  - Description Monthly retainer | Amount EUR 5.592,96
  - Description Draft billing copy | Amount EUR 10.279,20

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-07

```
SUPPLIER INVOICE
================

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 07/07/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: July 2024

Terms
-----
Due Date: 19/07/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: MAT-0002
Due Date: 19/07/2024
Subtotal: EUR 17.146,08
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 1.414,55
Total: EUR 18.560,63

Supplier Bill Lines
-------------------
Lines:
  - Description Steel sheets | Quantity 294 | Unit Cost EUR 58,32 | Amount EUR 17.146,08

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D018 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2024-07-11

```
CANCELLATION NOTE
=================

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 11/07/2024

Reference Box
-------------
Document ID: D018
Document Type: cancellation_note
Period: July 2024

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0001 is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-11

```
CUSTOMER INVOICE
================

From
----
Willow Distribution
75 Market Road, Mumbai
Document Date: 11/07/2024

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: July 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 28/07/2024

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0001

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 28/07/2024
Total: EUR 15.095,01

Line Items
----------
Items:
  - Description Implementation work | Amount EUR 6.615,22
  - Description Reissued billing | Amount EUR 8.479,79

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2024-07-16

```
MATERIAL REQUISITION SLIP
=========================

From
----
Willow Distribution
75 Market Road, Mumbai
Document Date: 16/07/2024

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: July 2024

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Control boards
Quantity Issued: 219
Issue Value: EUR 13.638,09
Warehouse: Main Warehouse

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2024-07-16

```
PRODUCTION BATCH SHEET
======================

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 16/07/2024

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: July 2024

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 78
Material Value: EUR 13.638,09
Labor Value: EUR 0,00
Overhead Value: EUR 0,00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-07-17

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: EUR 4.288,08
Draw Amount: EUR 59.356,86
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 63.644,94
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2024-07-20

```
DIRECT LABOR RECORD
===================

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 20/07/2024

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: July 2024

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 34
Labor Value: EUR 12.611,84
Labor Cash Paid: EUR 12.611,84

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-21

```
CUSTOMER INVOICE
================

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 21/07/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: July 2024
Contract Ref: FGT-0001

Terms
-----
Due Date: 04/08/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: FGT-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 04/08/2024
Subtotal: EUR 49.037,27
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 3.064,83
Total: EUR 52.102,10

Line Items
----------
Items:
  - Description Panel Kit | Amount EUR 49.037,27

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2024-07-23

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 23/07/2024

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: July 2024

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Panel Kit
Units Completed: 50
Transfer Value: EUR 34.169,61

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-07-24

```
PAYMENT ADVICE
==============

From
----
Willow Distribution
75 Market Road, Mumbai
Document Date: 24/07/2024

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: July 2024
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: EUR 51.293,04
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
- **Date:** 2024-07-24

```
PAYMENT ADVICE
==============

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 24/07/2024

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D010
Document Type: payment_advice
Period: July 2024
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: EUR 18.888,73
Reference: MAT-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-07-24

```
PAYROLL SUMMARY
===============

From
----
Willow Distribution
75 Market Road, Mumbai
Document Date: 24/07/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: July 2024
Headcount: 9
Gross Pay: EUR 32.759,88
Employer Tax: 3.537,54
Cash Outflow: EUR 36.297,42

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-07-28

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: First City Bank
Opening Principal: EUR 94.696,90
Draw Amount: EUR 0,00
Principal Paid: EUR 11.199,46
Interest Paid: EUR 731,08
Ending Principal: EUR 83.497,44
Note: Scheduled lender activity for the selected period.
```

### Document D015 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-07-28

```
TRANSFER ADVICE
===============

From
----
Willow Distribution
75 Market Road, Mumbai
Document Date: 28/07/2024

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: July 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: EUR 69.991,49
Transfer Date: 28/07/2024
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-07-30

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Willow Distribution
75 Market Road, Mumbai
Document Date: 30/07/2024

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: July 2024

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Panel Kit
Planned Units: 57
Overhead Value: EUR 7.919,68
Accrued Overhead: EUR 7.919,68

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
- **Date:** 2024-07-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 37.873,23
Useful Life Months: 48
Current Period Charge: EUR 789,03
Accumulated Depreciation: 789,03
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-07-31

```
BANK STATEMENT
==============

From
----
Willow Distribution
75 Market Road, Mumbai
Document Date: 31/07/2024

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: July 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0094
Statement Currency: EUR
Opening Balance: EUR 62.902,34
Closing Balance: EUR 23.832,22

Statement Rows
--------------
Rows:
  - Date 17/07/2024 | Description Loan draw LOAN-0001 | Amount EUR 59.356,86 | Running 
Balance EUR 122.259,20
  - Date 20/07/2024 | Description Direct labor BATCH-0001 | Amount EUR -12.611,84 | Running 
Balance EUR 109.647,36
  - Date 24/07/2024 | Description Customer settlement FGINV-0001 | Amount EUR 51.293,04 | 
Running Balance EUR 160.940,40
  - Date 24/07/2024 | Description Payroll PAYRUN-0001 | Amount EUR -36.297,42 | Running 
Balance EUR 124.642,98
  - Date 24/07/2024 | Description Supplier settlement MAT-0001 | Amount EUR -18.888,73 | 
Running Balance EUR 105.754,25
  - Date 28/07/2024 | Description Loan payment LOAN-0002 | Amount EUR -11.930,54 | Running 
Balance EUR 93.823,71
  - Date 28/07/2024 | Description Transfer out TRX-0001 | Amount EUR -69.991,49 | Running 
Balance EUR 23.832,22

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-07-31

```
BANK STATEMENT
==============

From
----
Willow Distribution
75 Market Road, Mumbai
Date: 31/07/2024

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: July 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-9499
Statement Currency: EUR
Opening Balance: EUR 0,00
Closing Balance: EUR 69.991,49

Statement Rows
--------------
Rows:
  - Date 28/07/2024 | Description Transfer in TRX-0001 | Amount EUR 69.991,49 | Running 
Balance EUR 69.991,49

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
| 1 | Raw Materials Inventory | Accounts Payable | 20,920.96 | D002 | 2024-07-05 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 1,725.98 | D002 | 2024-07-05 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 13,638.09 | D003, D004, D002 | 2024-07-16 | material_issue |
| 4 | Work In Process | Cash | 12,611.84 | D005, D004 | 2024-07-20 | direct_labor_labor |
| 5 | Work In Process | Accrued Expenses | 7,919.68 | D006, D004 | 2024-07-30 | overhead_accrual_overhead |
| 6 | Finished Goods Inventory | Work In Process | 34,169.61 | D007, D004 | 2024-07-23 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 49,037.27 | D008, D007 | 2024-07-21 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 34,169.61 | D008, D007 | 2024-07-21 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | Sales Tax Payable | 3,064.83 | D008, D007 | 2024-07-21 | finished_goods_sale_tax |
| 10 | Cash | Accounts Receivable | 51,293.04 | D009, D008 | 2024-07-24 | customer_payment |
| 11 | Accounts Payable | Cash | 18,888.73 | D010, D002 | 2024-07-24 | supplier_payment |
| 12 | Salaries Expense | Cash | 32,759.88 | D011 | 2024-07-24 | payroll_gross |
| 13 | Payroll Tax Expense | Cash | 3,537.54 | D011 | 2024-07-24 | payroll_tax |
| 14 | Cash | Loans Payable | 59,356.86 | D012 | 2024-07-17 | loan_draw |
| 15 | Depreciation Expense | Accumulated Depreciation | 789.03 | D013 | 2024-07-31 | depreciation |
| 16 | Loans Payable | Cash | 11,199.46 | D014 | 2024-07-28 | loan_repayment_principal |
| 17 | Interest Expense | Cash | 731.08 | D014 | 2024-07-28 | loan_repayment_interest |
| 18 | Reserve Cash | Cash | 69,991.49 | D015 | 2024-07-28 | interbank_transfer |
| 19 | Raw Materials Inventory | Accounts Payable | 17,146.08 | D016 | 2024-07-07 | raw_material_purchase |
| 20 | Input Tax Receivable | Accounts Payable | 1,414.55 | D016 | 2024-07-07 | raw_material_purchase_tax |
| 21 | Accounts Receivable | Sales Revenue | 15,095.01 | D017, D018, D019 | 2024-07-11 | reissued_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 23,832.22
- Raw Materials Inventory: 47,827.04
- Work In Process: 23,087.42
- Finished Goods Inventory: 35,622.74
- Accounts Receivable: 23,477.55
- Equipment: 37,873.23
- Input Tax Receivable: 3,140.53
- Accumulated Depreciation: -789.03
- Reserve Cash: 69,991.49

**Liabilities**
- Accounts Payable: 30,755.16
- Accrued Expenses: 12,597.24
- Notes Payable: 16,140.80
- Sales Tax Payable: 3,064.83
- Loans Payable: 48,157.40

**Equity**
- Retained Earnings: 2,549.75
- Share Capital: 150,798.01

**Totals:** Assets = 264,063.19; Liabilities = 110,715.43; Equity = 153,347.76
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
