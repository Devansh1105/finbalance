# Verification Packet — COV_MAN_Q5_0099

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `manufacturing`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q2 FY 2025
- **Period start → end:** 2025-04-01 → 2025-06-30
- **Entity:** Silverline Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 24
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Raw Materials Inventory`, `Work In Process`, `Finished Goods Inventory`, `Equipment`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Share Capital`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 242,574.01
- Raw Materials Inventory: 110,742.08
- Work In Process: 37,368.35
- Finished Goods Inventory: 71,595.44
- Accounts Receivable: 25,479.08
- Equipment: 81,072.12

**Liabilities**
- Accounts Payable: 41,903.51
- Accrued Expenses: 9,355.44
- Notes Payable: 31,326.16
- Loans Payable: 46,915.74

**Equity**
- Retained Earnings: 41,619.57
- Share Capital: 397,710.66


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
  - Section assets | Account Cash | Amount $242,574.01
  - Section assets | Account Raw Materials Inventory | Amount $110,742.08
  - Section assets | Account Work In Process | Amount $37,368.35
  - Section assets | Account Finished Goods Inventory | Amount $71,595.44
  - Section assets | Account Accounts Receivable | Amount $25,479.08
  - Section assets | Account Equipment | Amount $81,072.12
  - Section liabilities | Account Accounts Payable | Amount $41,903.51
  - Section liabilities | Account Accrued Expenses | Amount $9,355.44
  - Section liabilities | Account Notes Payable | Amount $31,326.16
  - Section liabilities | Account Loans Payable | Amount $46,915.74
  - Section equity | Account Retained Earnings | Amount $41,619.57
  - Section equity | Account Share Capital | Amount $397,710.66

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D020 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2025-04-10

```
CUSTOMER INVOICE
================

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-04-10

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D020
Document Type: customer_invoice
Period: Q2 FY 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-04-24

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0001

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-04-24
Total: $17,931.20

Line Items
----------
Items:
  - Description Monthly retainer | Amount $5,599.02
  - Description Draft billing copy | Amount $12,332.18

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2025-04-14

```
CANCELLATION NOTE
=================

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-04-14

Reference Box
-------------
Document ID: D021
Document Type: cancellation_note
Period: Q2 FY 2025

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
Page marker: D021
```

### Document D022 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-14

```
CUSTOMER INVOICE
================

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-04-14

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D022
Document Type: customer_invoice
Period: Q2 FY 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-05-05

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0001

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-05-05
Total: $17,627.57

Line Items
----------
Items:
  - Description Implementation work | Amount $3,758.40
  - Description Reissued billing | Amount $13,869.17

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D002 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-22

```
SUPPLIER INVOICE
================

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2025-04-22

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D002
Document Type: supplier_invoice
Period: Q2 FY 2025

Terms
-----
Due Date: 2025-05-08

Supplier Header
---------------
Supplier: Meridian Support LLP
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: MAT-0001
Due Date: 2025-05-08
Subtotal: $5,944.32
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $297.22
Total: $6,241.54

Supplier Bill Lines
-------------------
Lines:
  - Description Packing film | Quantity 128 | Unit Cost $46.44 | Amount $5,944.32

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D017 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-25

```
SUPPLIER INVOICE
================

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-04-25

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D017
Document Type: supplier_invoice
Period: Q2 FY 2025

Terms
-----
Due Date: 2025-05-18

Supplier Header
---------------
Supplier: Oakline Services
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: FXBILL-0001
Due Date: 2025-05-18
Total: GBP 37,480.16

Supplier Bill Lines
-------------------
Lines:
  - Description Consulting sprint | Amount GBP 9,173.27
  - Description Foreign-currency support | Amount GBP 28,306.89

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D018 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2025-04-25

```
EXCHANGE RATE NOTICE
====================

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2025-04-25

Reference Box
-------------
Document ID: D018
Document Type: exchange_rate_notice
Period: Q2 FY 2025
Reference: FXBILL-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXBILL-0001
Rate Date: 2025-04-25
Rate Type: Spot rate at bill date

Conversion Details
------------------
Source Currency: GBP
Source Amount: GBP 37,480.16
Functional Currency: USD
Exchange Rate: 1.3234
Functional Amount: $49,601.24

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-05-03

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $6,547.30
Draw Amount: $199,892.67
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $206,439.97
Note: Scheduled lender activity for the selected period.
```

### Document D003 — Material Requisition Slip

- **Type:** `material_requisition_slip`
- **Role:** `posting_doc`
- **Date:** 2025-05-28

```
MATERIAL REQUISITION SLIP
=========================

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-05-28

Reference Box
-------------
Document ID: D003
Document Type: material_requisition_slip
Period: Q2 FY 2025

Material Issue
--------------
Slip Number: REQ-0001
Batch ID: BATCH-0001
Material: Packing film
Quantity Issued: 72
Issue Value: $3,349.68
Warehouse: Overflow Storage

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Production Batch Sheet

- **Type:** `production_batch_sheet`
- **Role:** `support_doc`
- **Date:** 2025-05-28

```
PRODUCTION BATCH SHEET
======================

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-05-28

Reference Box
-------------
Document ID: D004
Document Type: production_batch_sheet
Period: Q2 FY 2025

Batch Summary
-------------
Batch ID: BATCH-0001
Product: Subscription Bundle
Planned Units: 43
Material Value: $3,349.68
Labor Value: $0.00
Overhead Value: $0.00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D005 — Direct Labor Record

- **Type:** `direct_labor_record`
- **Role:** `posting_doc`
- **Date:** 2025-05-28

```
DIRECT LABOR RECORD
===================

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2025-05-28

Reference Box
-------------
Document ID: D005
Document Type: direct_labor_record
Period: Q2 FY 2025

Labor Summary
-------------
Batch ID: BATCH-0001
Product: Subscription Bundle
Planned Units: 64
Labor Value: $17,331.20
Labor Cash Paid: $17,331.20

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-02

```
CUSTOMER INVOICE
================

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-06-02

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: Q2 FY 2025
Contract Ref: FGT-0001

Terms
-----
Due Date: 2025-06-18

Parties
-------
Customer: Riverfront Group
Contract Ref: FGT-0001
Currency: USD

Invoice Details
---------------
Invoice Number: FGINV-0001
Due Date: 2025-06-18
Subtotal: $62,649.54
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $3,132.48
Total: $65,782.02

Line Items
----------
Items:
  - Description Subscription Bundle | Amount $62,649.54

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D011 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-06-02

```
PAYROLL SUMMARY
===============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-06-02

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q2 FY 2025
Headcount: 12
Gross Pay: $60,098.63
Employer Tax: 7,303.54
Cash Outflow: $67,402.17

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D007 — Finished Goods Transfer Note

- **Type:** `finished_goods_transfer_note`
- **Role:** `posting_doc`
- **Date:** 2025-06-03

```
FINISHED GOODS TRANSFER NOTE
============================

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2025-06-03

Reference Box
-------------
Document ID: D007
Document Type: finished_goods_transfer_note
Period: Q2 FY 2025

Transfer Summary
----------------
Transfer Number: FGT-0001
Batch ID: BATCH-0001
Product: Subscription Bundle
Units Completed: 48
Transfer Value: $46,137.68

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D019 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `posting_doc`
- **Date:** 2025-06-06

```
PAYMENT ADVICE
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2025-06-06

To
--
Oakline Services

Reference Box
-------------
Document ID: D019
Document Type: payment_advice
Period: Q2 FY 2025
Reference: FXBILL-0001

Payment Details
---------------
Advice Number: FXPAY-0001
Counterparty: Oakline Services
Currency: USD
Amount: $51,422.78
Reference: FXBILL-0001
Payment Method: Bank transfer
Payment For: Foreign-currency payable settlement

Foreign Currency Details
------------------------
Source Amount: GBP 37,480.16
Source Currency: GBP
Functional Currency: USD
Functional Amount: $51,422.78
Exchange Rate: 1.3720
FX Difference: 1,821.54

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D010 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-11

```
PAYMENT ADVICE
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-06-11

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D010
Document Type: payment_advice
Period: Q2 FY 2025
Reference: MAT-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: $4,326.01
Reference: MAT-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-06-12

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: $170,218.72
Draw Amount: $0.00
Principal Paid: $29,840.38
Interest Paid: $2,211.89
Ending Principal: $140,378.34
Note: Scheduled lender activity for the selected period.
```

### Document D009 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-21

```
PAYMENT ADVICE
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-06-21

To
--
Riverfront Group

Reference Box
-------------
Document ID: D009
Document Type: payment_advice
Period: Q2 FY 2025
Reference: FGINV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: $56,484.01
Reference: FGINV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D015 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-21

```
TRANSFER ADVICE
===============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-06-21

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: Q2 FY 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $284,220.61
Transfer Date: 2025-06-21
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D006 — Overhead Accrual Memo

- **Type:** `overhead_accrual_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-06-24

```
OVERHEAD ACCRUAL MEMO
=====================

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2025-06-24

Reference Box
-------------
Document ID: D006
Document Type: overhead_accrual_memo
Period: Q2 FY 2025

Overhead Summary
----------------
Batch ID: BATCH-0001
Product: Subscription Bundle
Planned Units: 37
Overhead Value: $25,456.80
Accrued Overhead: $25,456.80

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
- **Date:** 2025-06-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $81,072.12
Useful Life Months: 48
Current Period Charge: $5,067.00
Accumulated Depreciation: 5,067.00
```

### Document D016 — Scrap Report

- **Type:** `scrap_report`
- **Role:** `adjustment_doc`
- **Date:** 2025-06-30

```
SCRAP REPORT
============

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2025-06-30

Reference Box
-------------
Document ID: D016
Document Type: scrap_report
Period: Q2 FY 2025

Approval / Context
------------------
Reason: Obsolete units

Scrap Summary
-------------
Report Number: SCRAP-0001
Batch Or Lot: OPEN-FG
Reason: Obsolete units
Write Down: $7,397.89

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D023 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-06-30

```
BANK STATEMENT
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-06-30

Reference Box
-------------
Document ID: D023
Document Type: bank_statement
Period: Q2 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0099
Statement Currency: USD
Opening Balance: $242,574.01
Closing Balance: $42,195.65

Statement Rows
--------------
Rows:
  - Date 2025-05-03 | Description Loan draw LOAN-0001 | Amount $199,892.67 | Running Balance
 $442,466.68
  - Date 2025-05-28 | Description Direct labor BATCH-0001 | Amount $-17,331.20 | Running 
Balance $425,135.48
  - Date 2025-06-02 | Description Payroll PAYRUN-0001 | Amount $-67,402.17 | Running Balance
 $357,733.31
  - Date 2025-06-06 | Description Foreign payment FXBILL-0001 | Amount $-51,422.78 | Running
 Balance $306,310.53
  - Date 2025-06-11 | Description Supplier settlement MAT-0001 | Amount $-4,326.01 | Running
 Balance $301,984.52
  - Date 2025-06-12 | Description Loan payment LOAN-0002 | Amount $-32,052.27 | Running 
Balance $269,932.25
  - Date 2025-06-21 | Description Customer settlement FGINV-0001 | Amount $56,484.01 | 
Running Balance $326,416.26
  - Date 2025-06-21 | Description Transfer out TRX-0001 | Amount $-284,220.61 | Running 
Balance $42,195.65

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D024 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-06-30

```
BANK STATEMENT
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2025-06-30

Reference Box
-------------
Document ID: D024
Document Type: bank_statement
Period: Q2 FY 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-9999
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $284,220.61

Statement Rows
--------------
Rows:
  - Date 2025-06-21 | Description Transfer in TRX-0001 | Amount $284,220.61 | Running 
Balance $284,220.61

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D024
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Raw Materials Inventory | Accounts Payable | 5,944.32 | D002 | 2025-04-22 | raw_material_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 297.22 | D002 | 2025-04-22 | raw_material_purchase_tax |
| 3 | Work In Process | Raw Materials Inventory | 3,349.68 | D003, D004, D002 | 2025-05-28 | material_issue |
| 4 | Work In Process | Cash | 17,331.20 | D005, D004 | 2025-05-28 | direct_labor_labor |
| 5 | Work In Process | Accrued Expenses | 25,456.80 | D006, D004 | 2025-06-24 | overhead_accrual_overhead |
| 6 | Finished Goods Inventory | Work In Process | 46,137.68 | D007, D004 | 2025-06-03 | finished_goods_transfer |
| 7 | Accounts Receivable | Sales Revenue | 62,649.54 | D008, D007 | 2025-06-02 | finished_goods_sale_sale |
| 8 | Cost of Goods Sold | Finished Goods Inventory | 46,137.68 | D008, D007 | 2025-06-02 | finished_goods_sale_cogs |
| 9 | Accounts Receivable | Sales Tax Payable | 3,132.48 | D008, D007 | 2025-06-02 | finished_goods_sale_tax |
| 10 | Cash | Accounts Receivable | 56,484.01 | D009, D008 | 2025-06-21 | customer_payment |
| 11 | Accounts Payable | Cash | 4,326.01 | D010, D002 | 2025-06-11 | supplier_payment |
| 12 | Salaries Expense | Cash | 60,098.63 | D011 | 2025-06-02 | payroll_gross |
| 13 | Payroll Tax Expense | Cash | 7,303.54 | D011 | 2025-06-02 | payroll_tax |
| 14 | Cash | Loans Payable | 199,892.67 | D012 | 2025-05-03 | loan_draw |
| 15 | Depreciation Expense | Accumulated Depreciation | 5,067.00 | D013 | 2025-06-30 | depreciation |
| 16 | Loans Payable | Cash | 29,840.38 | D014 | 2025-06-12 | loan_repayment_principal |
| 17 | Interest Expense | Cash | 2,211.89 | D014 | 2025-06-12 | loan_repayment_interest |
| 18 | Reserve Cash | Cash | 284,220.61 | D015 | 2025-06-21 | interbank_transfer |
| 19 | Inventory Shrinkage Expense | Finished Goods Inventory | 7,397.89 | D016, D001 | 2025-06-30 | scrap_report |
| 20 | Raw Materials Inventory | Accounts Payable | 49,601.24 | D017, D018 | 2025-04-25 | fx_material_purchase |
| 21 | Accounts Payable | Cash | 49,601.24 | D019, D017 | 2025-06-06 | fx_supplier_payment |
| 22 | Foreign Exchange Loss | Cash | 1,821.54 | D019, D017 | 2025-06-06 | fx_supplier_payment_loss |
| 23 | Accounts Receivable | Sales Revenue | 17,627.57 | D020, D021, D022 | 2025-04-14 | reissued_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 42,195.65
- Raw Materials Inventory: 162,937.96
- Work In Process: 37,368.35
- Finished Goods Inventory: 64,197.55
- Accounts Receivable: 52,404.66
- Equipment: 81,072.12
- Input Tax Receivable: 297.22
- Accumulated Depreciation: -5,067.00
- Reserve Cash: 284,220.61

**Liabilities**
- Accounts Payable: 43,819.04
- Accrued Expenses: 34,812.24
- Notes Payable: 31,326.16
- Loans Payable: 216,968.03
- Sales Tax Payable: 3,132.48

**Equity**
- Retained Earnings: -8,141.49
- Share Capital: 397,710.66

**Totals:** Assets = 719,627.12; Liabilities = 330,057.95; Equity = 389,569.17
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
- Notes: No concerns here.
