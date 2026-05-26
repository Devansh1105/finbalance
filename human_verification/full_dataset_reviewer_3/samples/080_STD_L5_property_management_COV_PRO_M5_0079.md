# Verification Packet — COV_PRO_M5_0079

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** October 2024
- **Period start → end:** 2024-10-01 → 2024-10-31
- **Entity:** Beacon Retail Group
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 19
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-10-01_

**Assets**
- Cash: 32,357.13
- Accounts Receivable: 3,943.43
- Prepaid Insurance: 1,240.97
- Equipment: 9,879.29

**Liabilities**
- Accounts Payable: 3,131.19
- Accrued Expenses: 1,447.17
- Security Deposits Payable: 5,780.40
- Loans Payable: 5,541.50

**Equity**
- Retained Earnings: 4,703.46
- Owner's Equity: 26,817.10


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/10/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 32.357,13
  - Section assets | Account Accounts Receivable | Amount EUR 3.943,43
  - Section assets | Account Prepaid Insurance | Amount EUR 1.240,97
  - Section assets | Account Equipment | Amount EUR 9.879,29
  - Section liabilities | Account Accounts Payable | Amount EUR 3.131,19
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.447,17
  - Section liabilities | Account Security Deposits Payable | Amount EUR 5.780,40
  - Section liabilities | Account Loans Payable | Amount EUR 5.541,50
  - Section equity | Account Retained Earnings | Amount EUR 4.703,46
  - Section equity | Account Owner's Equity | Amount EUR 26.817,10

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D016 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-10-01

```
RENT ROLL
=========

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 01/10/2024

Reference Box
-------------
Document ID: D016
Document Type: rent_roll
Period: October 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Marina Heights
Period: October 2024
Total Rent: EUR 8.498,57

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit C - Shah | Amount EUR 8.498,57

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-10-03

```
RENT ROLL
=========

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 03/10/2024

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: October 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Park Lane Residences
Period: October 2024
Total Rent: EUR 5.368,70

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit D - Khan | Amount EUR 5.368,70

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-03

```
VENDOR INVOICE
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 03/10/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: October 2024

Terms
-----
Due Date: 18/10/2024

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 18/10/2024
Total: EUR 1.273,10

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount EUR 401,28
  - Description Support fee | Amount EUR 871,82

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D009 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2024-10-03

```
INSURANCE NOTICE
================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 03/10/2024

To
--
Shield Mutual
Vendor remittance address on file

Terms
-----
Service Start: 03/10/2024
Service End: 02/01/2025

Coverage Notice
---------------
Notice Number: PRE-0001
Carrier: Shield Mutual
Covered Item: Cedar Plaza
Coverage Start: 03/10/2024
Coverage End: 02/01/2025
Total Premium: EUR 11.046,58
Monthly Amount: EUR 3.682,19

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D018 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-10-03

```
SECONDARY COPY
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 03/10/2024

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D018
Document Type: secondary_copy
Period: October 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Pace Office Mart
Total: EUR 1.273,10
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2024-10-06

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 06/10/2024

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: October 2024

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit D - Khan
Unit: B-202
Amount: EUR 5.270,28
Due Date: 12/10/2024

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D015 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2024-10-06

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 06/10/2024

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D015
Document Type: security_deposit_notice
Period: October 2024

Security Deposit
----------------
Notice Number: DEP-0003
Tenant: Unit D - Khan
Unit: D-404
Amount: EUR 7.449,31
Due Date: 16/10/2024

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D017 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2024-10-09

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 09/10/2024

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D017
Document Type: security_deposit_notice
Period: October 2024

Security Deposit
----------------
Notice Number: DEP-0004
Tenant: Unit B - Romero
Unit: D-404
Amount: EUR 5.756,59
Due Date: 13/10/2024

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-10-12

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: EUR 3.203,89
Draw Amount: EUR 34.270,12
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 37.474,01
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-12

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Pace Office Mart
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 60
Total: EUR 21.386,78
Paid Cash: EUR 9.832,29
Financed Amount: EUR 11.554,49
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-21

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 21/10/2024

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: October 2024
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit D - Khan
Amount: EUR 5.144,41
Reference: ROLL-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-21

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 21/10/2024

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: October 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Pace Office Mart
Amount: EUR 778,51
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-10-23

```
PAYROLL SUMMARY
===============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 23/10/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: October 2024
Headcount: 3
Gross Pay: EUR 25.269,87
Employer Tax: 3.229,05
Cash Outflow: EUR 28.498,92

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-10-24

```
UTILITY INVOICE
===============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 24/10/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: October 2024

Terms
-----
Due Date: 03/11/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: October 2024
Due Date: 03/11/2024
Total: EUR 2.488,22

Charges
-------
Charges:
  - Description Electricity | Amount EUR 804,04
  - Description Water | Amount EUR 1.684,18

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-10-26

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: EUR 46.932,88
Draw Amount: EUR 0,00
Principal Paid: EUR 15.039,29
Interest Paid: EUR 1.342,30
Ending Principal: EUR 31.893,59
Note: Scheduled lender activity for the selected period.
```

### Document D010 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-10-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 31/10/2024

Reference Box
-------------
Document ID: D010
Document Type: service_period_memo
Period: October 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Insurance coverage release
Reference: PRE-0001
Recognized Amount: EUR 3.682,19

Explanation
-----------
Narrative: One month of insurance coverage has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-10-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0002
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 9.879,29
Useful Life Months: 48
Current Period Charge: EUR 205,82
Accumulated Depreciation: 205,82
```

### Document D019 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-10-31

```
BANK STATEMENT
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 31/10/2024

Reference Box
-------------
Document ID: D019
Document Type: bank_statement
Period: October 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0079
Statement Currency: EUR
Opening Balance: EUR 32.357,13
Closing Balance: EUR 23.709,95

Statement Rows
--------------
Rows:
  - Date 03/10/2024 | Description Insurance coverage prepayment PRE-0001 | Amount EUR 
-11.046,58 | Running Balance EUR 21.310,55
  - Date 06/10/2024 | Description Security deposit DEP-0001 | Amount EUR 5.270,28 | Running 
Balance EUR 26.580,83
  - Date 06/10/2024 | Description Security deposit DEP-0003 | Amount EUR 7.449,31 | Running 
Balance EUR 34.030,14
  - Date 09/10/2024 | Description Security deposit DEP-0004 | Amount EUR 5.756,59 | Running 
Balance EUR 39.786,73
  - Date 12/10/2024 | Description Asset purchase ASSET-0001 | Amount EUR -9.832,29 | Running
 Balance EUR 29.954,44
  - Date 12/10/2024 | Description Loan draw LOAN-0001 | Amount EUR 34.270,12 | Running 
Balance EUR 64.224,56
  - Date 21/10/2024 | Description Customer settlement ROLL-0001 | Amount EUR 5.144,41 | 
Running Balance EUR 69.368,97
  - Date 21/10/2024 | Description Supplier settlement BILL-0001 | Amount EUR -778,51 | 
Running Balance EUR 68.590,46
  - Date 23/10/2024 | Description Payroll PAYRUN-0001 | Amount EUR -28.498,92 | Running 
Balance EUR 40.091,54
  - Date 26/10/2024 | Description Loan payment LOAN-0002 | Amount EUR -16.381,59 | Running 
Balance EUR 23.709,95

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D019
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 5,368.70 | D002 | 2024-10-03 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 1,273.10 | D003 | 2024-10-03 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 5,144.41 | D004, D002 | 2024-10-21 | tenant_payment |
| 4 | Accounts Payable | Cash | 778.51 | D005, D003 | 2024-10-21 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 5,270.28 | D006 | 2024-10-06 | security_deposit |
| 6 | Salaries Expense | Cash | 25,269.87 | D007 | 2024-10-23 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 3,229.05 | D007 | 2024-10-23 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 2,488.22 | D008 | 2024-10-24 | utilities_bill |
| 9 | Prepaid Insurance | Cash | 11,046.58 | D009 | 2024-10-03 | prepaid_insurance_purchase |
| 10 | Insurance Expense | Prepaid Insurance | 3,682.19 | D009, D010 | 2024-10-31 | prepaid_insurance_release |
| 11 | Cash | Loans Payable | 34,270.12 | D011 | 2024-10-12 | loan_draw |
| 12 | Equipment | Cash | 9,832.29 | D012 | 2024-10-12 | equipment_purchase_cash |
| 13 | Equipment | Notes Payable | 11,554.49 | D012 | 2024-10-12 | equipment_purchase_financed |
| 14 | Depreciation Expense | Accumulated Depreciation | 205.82 | D013 | 2024-10-31 | depreciation |
| 15 | Loans Payable | Cash | 15,039.29 | D014 | 2024-10-26 | loan_repayment_principal |
| 16 | Interest Expense | Cash | 1,342.30 | D014 | 2024-10-26 | loan_repayment_interest |
| 17 | Cash | Security Deposits Payable | 7,449.31 | D015 | 2024-10-06 | security_deposit |
| 18 | Accounts Receivable | Rental Revenue | 8,498.57 | D016 | 2024-10-01 | rent_roll |
| 19 | Cash | Security Deposits Payable | 5,756.59 | D017 | 2024-10-09 | security_deposit |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 23,709.95
- Accounts Receivable: 12,666.29
- Prepaid Insurance: 8,605.36
- Equipment: 31,266.07
- Accumulated Depreciation: -205.82

**Liabilities**
- Accounts Payable: 6,114.00
- Accrued Expenses: 1,447.17
- Security Deposits Payable: 24,256.58
- Loans Payable: 24,772.33
- Notes Payable: 11,554.49

**Equity**
- Retained Earnings: -18,919.82
- Owner's Equity: 26,817.10

**Totals:** Assets = 76,041.85; Liabilities = 68,144.57; Equity = 7,897.28
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
