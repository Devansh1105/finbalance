# Verification Packet — COV_FIE_Q5_0024

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q4 FY 2025
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Summit Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 22
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 123,097.28
- Accounts Receivable: 15,997.69
- Office Supplies: 2,622.92
- Vehicles: 17,470.97
- Equipment: 11,214.23
- Prepaid Insurance: 2,642.41

**Liabilities**
- Accounts Payable: 8,056.83
- Accrued Expenses: 3,722.47
- Notes Payable: 21,760.75
- Loans Payable: 18,860.55

**Equity**
- Retained Earnings: 21,969.96
- Owner's Equity: 98,674.94


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
  - Section assets | Account Cash | Amount $123,097.28
  - Section assets | Account Accounts Receivable | Amount $15,997.69
  - Section assets | Account Office Supplies | Amount $2,622.92
  - Section assets | Account Vehicles | Amount $17,470.97
  - Section assets | Account Equipment | Amount $11,214.23
  - Section assets | Account Prepaid Insurance | Amount $2,642.41
  - Section liabilities | Account Accounts Payable | Amount $8,056.83
  - Section liabilities | Account Accrued Expenses | Amount $3,722.47
  - Section liabilities | Account Notes Payable | Amount $21,760.75
  - Section liabilities | Account Loans Payable | Amount $18,860.55
  - Section equity | Account Retained Earnings | Amount $21,969.96
  - Section equity | Account Owner's Equity | Amount $98,674.94

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-10-10

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Riverfront Group
Job Site: Riverbank Plaza
Scope: Consulting sprint
Approved Amount: $10,777.44

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D021 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-10

```
SUPPLIER INVOICE
================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-10-10

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D021
Document Type: supplier_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-10-28

Supplier Header
---------------
Supplier: Golden State Finance
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0003
Due Date: 2025-10-28
Total: $24,243.07

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 18 | Unit Cost $359.54 | Amount 
$6,471.70
  - Description Preventive maintenance service parts | Quantity 27 | Unit Cost $658.20 | 
Amount $17,771.37

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-11

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-10-11

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 2025-11-02

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-11-02
Total: $10,777.44

Line Items
----------
Items:
  - Description Review pack | Amount $2,364.29
  - Description Follow-up support | Amount $8,413.15

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
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
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-10-13

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-10-23

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2025-10-23
Total: $16,613.71

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 21 | Unit Cost $227.60 | Amount 
$4,779.63
  - Description Preventive maintenance service parts | Quantity 15 | Unit Cost $788.94 | 
Amount $11,834.08

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D015 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-10-16

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0002
Customer: Aster Point Services
Job Site: East Tower
Scope: Monthly retainer
Approved Amount: $33,958.18

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D016 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-17

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-10-17

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D016
Document Type: customer_invoice
Period: Q4 FY 2025
Contract Ref: CTR-0002
Job Code: JOB-0002

Terms
-----
Due Date: 2025-11-07

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-11-07
Total: $33,958.18

Line Items
----------
Items:
  - Description Monthly retainer | Amount $10,974.87
  - Description Follow-up support | Amount $22,983.31

Field Job
---------
Job Code: JOB-0002

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D018 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-18

```
SUPPLIER INVOICE
================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 2025-10-18

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D018
Document Type: supplier_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-10-30

Supplier Header
---------------
Supplier: Meridian Support LLP
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 2025-10-30
Total: $7,092.00

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 13 | Unit Cost $165.69 | Amount 
$2,154.00
  - Description Preventive maintenance service parts | Quantity 26 | Unit Cost $189.92 | 
Amount $4,938.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-05

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: $563.37
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount $180.03
  - Description Fuel Incidentals | Amount $383.34
```

### Document D017 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-10

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Golden State Finance
Total: $330.85
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount $74.36
  - Description Fuel Incidentals | Amount $256.49
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-17

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $29,095.72
Draw Amount: $89,317.80
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $118,413.52
Note: Scheduled lender activity for the selected period.
```

### Document D011 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-22

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: Office laptops
Asset Tag: TAG-0001
Useful Life Months: 36
Total: $150,654.43
Paid Cash: $30,904.16
Financed Amount: $119,750.27
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D020 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-01

```
UTILITY INVOICE
===============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-12-01

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D020
Document Type: utilities_statement
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-12-09

Invoice Summary
---------------
Statement Number: UTIL-0003
Invoice Number: UTILINV-0003
Provider: City Power
Pay To: City Power
Service Period: Q4 FY 2025
Due Date: 2025-12-09
Total: $3,458.06

Charges
-------
Charges:
  - Description Electricity | Amount $1,167.61
  - Description Water | Amount $2,290.45

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-06

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: $16,322.34
Draw Amount: $0.00
Principal Paid: $20,962.77
Interest Paid: $2,314.34
Ending Principal: $-4,640.43
Note: Scheduled lender activity for the selected period.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-07

```
PAYMENT ADVICE
==============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 2025-12-07

To
--
Riverfront Group

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q4 FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: $9,764.23
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D019 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-07

```
UTILITY INVOICE
===============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 2025-12-07

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D019
Document Type: utilities_statement
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-12-17

Invoice Summary
---------------
Statement Number: UTIL-0002
Invoice Number: UTILINV-0002
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: Q4 FY 2025
Due Date: 2025-12-17
Total: $1,503.55

Charges
-------
Charges:
  - Description Electricity | Amount $658.82
  - Description Water | Amount $844.73

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-11

```
PAYMENT ADVICE
==============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 2025-12-11

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q4 FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $9,171.41
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
- **Date:** 2025-12-11

```
PAYROLL SUMMARY
===============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-12-11

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2025
Headcount: 12
Gross Pay: $44,160.72
Employer Tax: 4,282.17
Cash Outflow: $48,442.89

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D009 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-15

```
UTILITY INVOICE
===============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-12-15

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: utilities_statement
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-12-30

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: Q4 FY 2025
Due Date: 2025-12-30
Total: $1,017.65

Charges
-------
Charges:
  - Description Electricity | Amount $364.51
  - Description Water | Amount $653.14

Footer
------
Internal document packet copy.
Page marker: D009
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
Asset Name: Office laptops
Asset Tag: TAG-0001
Cost: $150,654.43
Useful Life Months: 36
Current Period Charge: $12,554.55
Accumulated Depreciation: 12,554.55
```

### Document D014 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-12-31

Reference Box
-------------
Document ID: D014
Document Type: service_period_memo
Period: Q4 FY 2025
Reference: Q4 FY 2025

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q4 FY 2025
Recognized Amount: $3,347.33

Explanation
-----------
Narrative: Accrue unpaid repairs expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D022 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 2025-12-31

Reference Box
-------------
Document ID: D022
Document Type: bank_statement
Period: Q4 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0024
Statement Currency: USD
Opening Balance: $123,097.28
Closing Balance: $109,489.52

Statement Rows
--------------
Rows:
  - Date 2025-11-05 | Description Meridian Support LLP receipt RCPT-0001 | Amount $-563.37 |
 Running Balance $122,533.91
  - Date 2025-11-10 | Description Golden State Finance receipt RCPT-0002 | Amount $-330.85 |
 Running Balance $122,203.06
  - Date 2025-11-17 | Description Loan draw LOAN-0001 | Amount $89,317.80 | Running Balance 
$211,520.86
  - Date 2025-11-22 | Description Asset purchase ASSET-0001 | Amount $-30,904.16 | Running 
Balance $180,616.70
  - Date 2025-12-06 | Description Loan payment LOAN-0002 | Amount $-23,277.11 | Running 
Balance $157,339.59
  - Date 2025-12-07 | Description Customer settlement INV-0001 | Amount $9,764.23 | Running 
Balance $167,103.82
  - Date 2025-12-11 | Description Payroll PAYRUN-0001 | Amount $-48,442.89 | Running Balance
 $118,660.93
  - Date 2025-12-11 | Description Supplier settlement BILL-0001 | Amount $-9,171.41 | 
Running Balance $109,489.52

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D022
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 10,777.44 | D002, D003 | 2025-10-11 | job_invoice |
| 2 | Repairs Expense | Accounts Payable | 16,613.71 | D004 | 2025-10-13 | supplier_bill |
| 3 | Fuel Expense | Cash | 563.37 | D005 | 2025-11-05 | fuel_receipt |
| 4 | Cash | Accounts Receivable | 9,764.23 | D006, D003 | 2025-12-07 | customer_payment |
| 5 | Accounts Payable | Cash | 9,171.41 | D007, D004 | 2025-12-11 | supplier_payment |
| 6 | Salaries Expense | Cash | 44,160.72 | D008 | 2025-12-11 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 4,282.17 | D008 | 2025-12-11 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 1,017.65 | D009 | 2025-12-15 | utilities_bill |
| 9 | Cash | Loans Payable | 89,317.80 | D010 | 2025-11-17 | loan_draw |
| 10 | Equipment | Cash | 30,904.16 | D011 | 2025-11-22 | equipment_purchase_cash |
| 11 | Equipment | Notes Payable | 119,750.27 | D011 | 2025-11-22 | equipment_purchase_financed |
| 12 | Depreciation Expense | Accumulated Depreciation | 12,554.55 | D012 | 2025-12-31 | depreciation |
| 13 | Loans Payable | Cash | 20,962.77 | D013 | 2025-12-06 | loan_repayment_principal |
| 14 | Interest Expense | Cash | 2,314.34 | D013 | 2025-12-06 | loan_repayment_interest |
| 15 | Repairs Expense | Accrued Expenses | 3,347.33 | D014 | 2025-12-31 | expense_accrual |
| 16 | Accounts Receivable | Service Revenue | 33,958.18 | D015, D016 | 2025-10-17 | job_invoice |
| 17 | Fuel Expense | Cash | 330.85 | D017 | 2025-11-10 | fuel_receipt |
| 18 | Repairs Expense | Accounts Payable | 7,092.00 | D018 | 2025-10-18 | supplier_bill |
| 19 | Utilities Expense | Accounts Payable | 1,503.55 | D019 | 2025-12-07 | utilities_bill |
| 20 | Utilities Expense | Accounts Payable | 3,458.06 | D020 | 2025-12-01 | utilities_bill |
| 21 | Repairs Expense | Accounts Payable | 24,243.07 | D021 | 2025-10-10 | supplier_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 109,489.52
- Accounts Receivable: 50,969.08
- Office Supplies: 2,622.92
- Vehicles: 17,470.97
- Equipment: 161,868.66
- Prepaid Insurance: 2,642.41
- Accumulated Depreciation: -12,554.55

**Liabilities**
- Accounts Payable: 52,813.46
- Accrued Expenses: 7,069.80
- Notes Payable: 141,511.02
- Loans Payable: 87,215.58

**Equity**
- Retained Earnings: -54,775.79
- Owner's Equity: 98,674.94

**Totals:** Assets = 332,509.01; Liabilities = 288,609.86; Equity = 43,899.15
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
- Notes: Looks fine for benchmark use.
