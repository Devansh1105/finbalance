# Verification Packet — COV_FIE_Q4_0023

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q3 FY 2025-26
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Pioneer Distribution
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 17
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 75,242.60
- Accounts Receivable: 14,525.33
- Office Supplies: 1,452.99
- Vehicles: 21,662.91
- Equipment: 15,059.93
- Prepaid Insurance: 2,562.51

**Liabilities**
- Accounts Payable: 8,738.82
- Accrued Expenses: 3,724.10
- Notes Payable: 14,524.44
- Loans Payable: 13,082.83

**Equity**
- Retained Earnings: 24,019.61
- Owner's Equity: 66,416.47


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
Statement Date: 01/10/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 75,242.60
  - Section assets | Account Accounts Receivable | Amount GBP 14,525.33
  - Section assets | Account Office Supplies | Amount GBP 1,452.99
  - Section assets | Account Vehicles | Amount GBP 21,662.91
  - Section assets | Account Equipment | Amount GBP 15,059.93
  - Section assets | Account Prepaid Insurance | Amount GBP 2,562.51
  - Section liabilities | Account Accounts Payable | Amount GBP 8,738.82
  - Section liabilities | Account Accrued Expenses | Amount GBP 3,724.10
  - Section liabilities | Account Notes Payable | Amount GBP 14,524.44
  - Section liabilities | Account Loans Payable | Amount GBP 13,082.83
  - Section equity | Account Retained Earnings | Amount GBP 24,019.61
  - Section equity | Account Owner's Equity | Amount GBP 66,416.47

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-13

```
SUPPLIER INVOICE
================

From
----
Pioneer Distribution
75 Market Road, Mumbai
Document Date: 13/10/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: Q3 FY 2025-26

Terms
-----
Due Date: 31/10/2025

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 31/10/2025
Subtotal: GBP 5,169.54
Tax Label: India GST
Tax Rate: 5.00%
Tax Amount: GBP 258.48
CGST Amount: GBP 129.24
SGST Amount: GBP 129.24
Total: GBP 5,428.02

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 10 | Unit Cost GBP 158.98 | 
Amount GBP 1,589.78
  - Description Preventive maintenance service parts | Quantity 30 | Unit Cost GBP 119.33 | 
Amount GBP 3,579.76

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-10-18

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Maple Ridge Trading
Job Site: East Tower
Scope: Monthly retainer
Approved Amount: GBP 8,585.68

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D014 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-18

```
SUPPLIER INVOICE
================

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 18/10/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D014
Document Type: supplier_invoice
Period: Q3 FY 2025-26

Terms
-----
Due Date: 04/11/2025

Supplier Header
---------------
Supplier: Oakline Services
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 04/11/2025
Subtotal: GBP 4,980.53
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 896.50
CGST Amount: GBP 448.25
SGST Amount: GBP 448.25
Total: GBP 5,877.03

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 17 | Unit Cost GBP 120.11 | 
Amount GBP 2,041.79
  - Description Preventive maintenance service parts | Quantity 29 | Unit Cost GBP 101.34 | 
Amount GBP 2,938.74

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-19

```
CUSTOMER INVOICE
================

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 19/10/2025

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 10/11/2025

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 10/11/2025
Subtotal: GBP 8,585.68
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 1,030.28
CGST Amount: GBP 515.14
SGST Amount: GBP 515.14
Total: GBP 9,615.96

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 2,254.43
  - Description Follow-up support | Amount GBP 6,331.25

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-09

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Golden State Finance
Total: GBP 481.55
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 112.18
  - Description Fuel Incidentals | Amount GBP 369.37
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-09

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 3,764.20
Draw Amount: GBP 66,919.49
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 70,683.69
Note: Scheduled lender activity for the selected period.
```

### Document D015 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-20

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Beacon Industrial Supply
Total: GBP 677.72
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 188.03
  - Description Fuel Incidentals | Amount GBP 489.69
```

### Document D011 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-26

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Golden State Finance
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 24
Total: GBP 102,746.48
Paid Cash: GBP 32,775.43
Financed Amount: GBP 69,971.05
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D016 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-29

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0003
Merchant: Meridian Support LLP
Total: GBP 990.99
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 242.95
  - Description Fuel Incidentals | Amount GBP 748.04
```

### Document D009 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-10

```
UTILITY INVOICE
===============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 10/12/2025

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: utilities_statement
Period: Q3 FY 2025-26

Terms
-----
Due Date: 21/12/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: Q3 FY 2025-26
Due Date: 21/12/2025
Total: GBP 972.61

Charges
-------
Charges:
  - Description Electricity | Amount GBP 304.75
  - Description Water | Amount GBP 667.86

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-11

```
PAYMENT ADVICE
==============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 11/12/2025

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Maple Ridge Trading
Amount: GBP 8,494.63
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-18

```
PAYMENT ADVICE
==============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Document Date: 18/12/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: GBP 3,566.07
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-12-21

```
PAYROLL SUMMARY
===============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 21/12/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q3 FY 2025-26
Headcount: 3
Gross Pay: GBP 17,344.25
Employer Tax: 1,988.08
Cash Outflow: GBP 19,332.33

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D012 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Cost: GBP 102,746.48
Useful Life Months: 24
Current Period Charge: GBP 12,843.30
Accumulated Depreciation: 12,843.30
```

### Document D013 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 31/12/2025

Reference Box
-------------
Document ID: D013
Document Type: service_period_memo
Period: Q3 FY 2025-26
Reference: Q3 FY 2025-26

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q3 FY 2025-26
Recognized Amount: GBP 4,531.75

Explanation
-----------
Narrative: Accrue unpaid repairs expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D017 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Distribution
75 Market Road, Mumbai
Date: 31/12/2025

Reference Box
-------------
Document ID: D017
Document Type: bank_statement
Period: Q3 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0023
Statement Currency: GBP
Opening Balance: GBP 75,242.60
Closing Balance: GBP 92,832.63

Statement Rows
--------------
Rows:
  - Date 09/11/2025 | Description Golden State Finance receipt RCPT-0001 | Amount GBP 
-481.55 | Running Balance GBP 74,761.05
  - Date 09/11/2025 | Description Loan draw LOAN-0001 | Amount GBP 66,919.49 | Running 
Balance GBP 141,680.54
  - Date 20/11/2025 | Description Beacon Industrial Supply receipt RCPT-0002 | Amount GBP 
-677.72 | Running Balance GBP 141,002.82
  - Date 26/11/2025 | Description Asset purchase ASSET-0001 | Amount GBP -32,775.43 | 
Running Balance GBP 108,227.39
  - Date 29/11/2025 | Description Meridian Support LLP receipt RCPT-0003 | Amount GBP 
-990.99 | Running Balance GBP 107,236.40
  - Date 11/12/2025 | Description Customer settlement INV-0001 | Amount GBP 8,494.63 | 
Running Balance GBP 115,731.03
  - Date 18/12/2025 | Description Supplier settlement BILL-0001 | Amount GBP -3,566.07 | 
Running Balance GBP 112,164.96
  - Date 21/12/2025 | Description Payroll PAYRUN-0001 | Amount GBP -19,332.33 | Running 
Balance GBP 92,832.63

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D017
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 8,585.68 | D002, D003 | 2025-10-19 | job_invoice |
| 2 | Accounts Receivable | CGST Payable | 515.14 | D002, D003 | 2025-10-19 | job_invoice_tax_cgst |
| 3 | Accounts Receivable | SGST Payable | 515.14 | D002, D003 | 2025-10-19 | job_invoice_tax_sgst |
| 4 | Repairs Expense | Accounts Payable | 5,169.54 | D004 | 2025-10-13 | supplier_bill |
| 5 | Input CGST Receivable | Accounts Payable | 129.24 | D004 | 2025-10-13 | supplier_bill_tax_cgst |
| 6 | Input SGST Receivable | Accounts Payable | 129.24 | D004 | 2025-10-13 | supplier_bill_tax_sgst |
| 7 | Fuel Expense | Cash | 481.55 | D005 | 2025-11-09 | fuel_receipt |
| 8 | Cash | Accounts Receivable | 8,494.63 | D006, D003 | 2025-12-11 | customer_payment |
| 9 | Accounts Payable | Cash | 3,566.07 | D007, D004 | 2025-12-18 | supplier_payment |
| 10 | Salaries Expense | Cash | 17,344.25 | D008 | 2025-12-21 | payroll_gross |
| 11 | Payroll Tax Expense | Cash | 1,988.08 | D008 | 2025-12-21 | payroll_tax |
| 12 | Utilities Expense | Accounts Payable | 972.61 | D009 | 2025-12-10 | utilities_bill |
| 13 | Cash | Loans Payable | 66,919.49 | D010 | 2025-11-09 | loan_draw |
| 14 | Equipment | Cash | 32,775.43 | D011 | 2025-11-26 | equipment_purchase_cash |
| 15 | Equipment | Notes Payable | 69,971.05 | D011 | 2025-11-26 | equipment_purchase_financed |
| 16 | Depreciation Expense | Accumulated Depreciation | 12,843.30 | D012 | 2025-12-31 | depreciation |
| 17 | Repairs Expense | Accrued Expenses | 4,531.75 | D013 | 2025-12-31 | expense_accrual |
| 18 | Repairs Expense | Accounts Payable | 4,980.53 | D014 | 2025-10-18 | supplier_bill |
| 19 | Input CGST Receivable | Accounts Payable | 448.25 | D014 | 2025-10-18 | supplier_bill_tax_cgst |
| 20 | Input SGST Receivable | Accounts Payable | 448.25 | D014 | 2025-10-18 | supplier_bill_tax_sgst |
| 21 | Fuel Expense | Cash | 677.72 | D015 | 2025-11-20 | fuel_receipt |
| 22 | Fuel Expense | Cash | 990.99 | D016 | 2025-11-29 | fuel_receipt |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 92,832.63
- Accounts Receivable: 15,646.66
- Office Supplies: 1,452.99
- Vehicles: 21,662.91
- Equipment: 117,806.41
- Prepaid Insurance: 2,562.51
- Input CGST Receivable: 577.49
- Input SGST Receivable: 577.49
- Accumulated Depreciation: -12,843.30

**Liabilities**
- Accounts Payable: 17,450.41
- Accrued Expenses: 8,255.85
- Notes Payable: 84,495.49
- Loans Payable: 80,002.32
- CGST Payable: 515.14
- SGST Payable: 515.14

**Equity**
- Retained Earnings: -17,375.03
- Owner's Equity: 66,416.47

**Totals:** Assets = 240,275.79; Liabilities = 191,234.35; Equity = 49,041.44
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
- Notes: Entries generally align with source support.
