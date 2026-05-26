# Verification Packet — COV_PRO_Q5_0084

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q2 FY 2025
- **Period start → end:** 2025-04-01 → 2025-06-30
- **Entity:** Northwind Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 22
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 101,593.36
- Accounts Receivable: 11,747.38
- Prepaid Insurance: 3,922.83
- Equipment: 10,420.52

**Liabilities**
- Accounts Payable: 3,703.25
- Accrued Expenses: 2,277.87
- Security Deposits Payable: 12,575.03
- Loans Payable: 4,588.55

**Equity**
- Retained Earnings: 10,787.49
- Owner's Equity: 93,751.90


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
  - Section assets | Account Cash | Amount $101,593.36
  - Section assets | Account Accounts Receivable | Amount $11,747.38
  - Section assets | Account Prepaid Insurance | Amount $3,922.83
  - Section assets | Account Equipment | Amount $10,420.52
  - Section liabilities | Account Accounts Payable | Amount $3,703.25
  - Section liabilities | Account Accrued Expenses | Amount $2,277.87
  - Section liabilities | Account Security Deposits Payable | Amount $12,575.03
  - Section liabilities | Account Loans Payable | Amount $4,588.55
  - Section equity | Account Retained Earnings | Amount $10,787.49
  - Section equity | Account Owner's Equity | Amount $93,751.90

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D020 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-01

```
RENT ROLL
=========

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-04-01

Reference Box
-------------
Document ID: D020
Document Type: rent_roll
Period: Q2 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0004
Property: Cedar Plaza
Period: Q2 FY 2025
Total Rent: $19,180.07

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit B - Romero | Amount $19,180.07

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D009 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-03

```
INSURANCE NOTICE
================

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-04-03

To
--
Shield Mutual
Vendor remittance address on file

Terms
-----
Service Start: 2025-04-03
Service End: 2025-07-02

Coverage Notice
---------------
Notice Number: PRE-0001
Carrier: Shield Mutual
Covered Item: Cedar Plaza
Coverage Start: 2025-04-03
Coverage End: 2025-07-02
Total Premium: $26,775.02
Monthly Amount: $8,925.01

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-04

```
RENT ROLL
=========

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Document Date: 2025-04-04

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: Q2 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Cedar Plaza
Period: Q2 FY 2025
Total Rent: $17,748.96

Tenant Rows
-----------
Rows:
  - Unit B-202 | Tenant Unit D - Khan | Amount $17,748.96

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D018 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-04

```
RENT ROLL
=========

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-04-04

Reference Box
-------------
Document ID: D018
Document Type: rent_roll
Period: Q2 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0003
Property: Park Lane Residences
Period: Q2 FY 2025
Total Rent: $17,601.11

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit D - Khan | Amount $17,601.11

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D017 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-05

```
RENT ROLL
=========

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Document Date: 2025-04-05

Reference Box
-------------
Document ID: D017
Document Type: rent_roll
Period: Q2 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Marina Heights
Period: Q2 FY 2025
Total Rent: $19,199.17

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit D - Khan | Amount $19,199.17

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D021 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-10

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Document Date: 2025-04-10

To
--
Unit C - Shah

Reference Box
-------------
Document ID: D021
Document Type: security_deposit_notice
Period: Q2 FY 2025

Security Deposit
----------------
Notice Number: DEP-0005
Tenant: Unit C - Shah
Unit: D-404
Amount: $9,736.73
Due Date: 2025-04-16

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D016 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-16

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Document Date: 2025-04-16

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D016
Document Type: security_deposit_notice
Period: Q2 FY 2025

Security Deposit
----------------
Notice Number: DEP-0003
Tenant: Unit D - Khan
Unit: C-303
Amount: $4,598.47
Due Date: 2025-04-24

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-20

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Document Date: 2025-04-20

To
--
Unit C - Shah

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: Q2 FY 2025

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit C - Shah
Unit: D-404
Amount: $9,603.70
Due Date: 2025-04-27

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-22

```
VENDOR INVOICE
==============

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Document Date: 2025-04-22

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q2 FY 2025

Terms
-----
Due Date: 2025-05-12

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-05-12
Total: $18,266.44

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $4,351.95
  - Description Support fee | Amount $13,914.49

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D019 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-22

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-04-22

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D019
Document Type: security_deposit_notice
Period: Q2 FY 2025

Security Deposit
----------------
Notice Number: DEP-0004
Tenant: Unit D - Khan
Unit: A-101
Amount: $13,678.89
Due Date: 2025-04-29

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-03

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Beacon Industrial Supply
Asset Name: Office laptops
Asset Tag: TAG-0001
Useful Life Months: 48
Total: $176,361.53
Paid Cash: $80,641.37
Financed Amount: $95,720.16
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-05-18

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $9,914.09
Draw Amount: $50,092.63
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $60,006.72
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-03

```
PAYMENT ADVICE
==============

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-06-03

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q2 FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: $17,620.04
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D014 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-06-07

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: $22,442.04
Draw Amount: $0.00
Principal Paid: $24,531.49
Interest Paid: $2,352.04
Ending Principal: $-2,089.45
Note: Scheduled lender activity for the selected period.
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-06-12

```
PAYMENT ADVICE
==============

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-06-12

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: Q2 FY 2025
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit D - Khan
Amount: $17,234.36
Reference: ROLL-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-06-12

```
PAYROLL SUMMARY
===============

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-06-12

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q2 FY 2025
Headcount: 3
Gross Pay: $44,306.85
Employer Tax: 5,439.86
Cash Outflow: $49,746.71

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-06-16

```
UTILITY INVOICE
===============

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-06-16

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: Q2 FY 2025

Terms
-----
Due Date: 2025-06-30

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: Q2 FY 2025
Due Date: 2025-06-30
Total: $4,178.75

Charges
-------
Charges:
  - Description Electricity | Amount $1,578.27
  - Description Water | Amount $2,600.48

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D015 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-06-19

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Document Date: 2025-06-19

To
--
Unit C - Shah

Reference Box
-------------
Document ID: D015
Document Type: security_deposit_notice
Period: Q2 FY 2025

Security Deposit
----------------
Notice Number: DEPREF-0001
Tenant: Unit C - Shah
Unit: B-202
Amount: $9,060.69
Due Date: 2025-06-19

Notes
-----
Refund of previously collected security deposit DEP-0001.

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D010 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-06-30

```
SERVICE PERIOD MEMO
===================

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Document Date: 2025-06-30

Reference Box
-------------
Document ID: D010
Document Type: service_period_memo
Period: Q2 FY 2025
Reference: PRE-0001

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Insurance coverage release
Reference: PRE-0001
Recognized Amount: $8,925.01

Explanation
-----------
Narrative: One month of insurance coverage has expired and should be expensed this period.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
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
Schedule ID: DEP-0002
Asset Name: Office laptops
Asset Tag: TAG-0001
Cost: $176,361.53
Useful Life Months: 48
Current Period Charge: $11,022.60
Accumulated Depreciation: 11,022.60
```

### Document D022 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-06-30

```
BANK STATEMENT
==============

From
----
Northwind Manufacturing
75 Market Road, Mumbai
Date: 2025-06-30

Reference Box
-------------
Document ID: D022
Document Type: bank_statement
Period: Q2 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0084
Statement Currency: USD
Opening Balance: $101,593.36
Closing Balance: $-4,189.22

Statement Rows
--------------
Rows:
  - Date 2025-04-03 | Description Insurance coverage prepayment PRE-0001 | Amount 
$-26,775.02 | Running Balance $74,818.34
  - Date 2025-04-10 | Description Security deposit DEP-0005 | Amount $9,736.73 | Running 
Balance $84,555.07
  - Date 2025-04-16 | Description Security deposit DEP-0003 | Amount $4,598.47 | Running 
Balance $89,153.54
  - Date 2025-04-20 | Description Security deposit DEP-0001 | Amount $9,603.70 | Running 
Balance $98,757.24
  - Date 2025-04-22 | Description Security deposit DEP-0004 | Amount $13,678.89 | Running 
Balance $112,436.13
  - Date 2025-05-03 | Description Asset purchase ASSET-0001 | Amount $-80,641.37 | Running 
Balance $31,794.76
  - Date 2025-05-18 | Description Loan draw LOAN-0001 | Amount $50,092.63 | Running Balance 
$81,887.39
  - Date 2025-06-03 | Description Supplier settlement BILL-0001 | Amount $-17,620.04 | 
Running Balance $64,267.35
  - Date 2025-06-07 | Description Loan payment LOAN-0002 | Amount $-26,883.53 | Running 
Balance $37,383.82
  - Date 2025-06-12 | Description Customer settlement ROLL-0001 | Amount $17,234.36 | 
Running Balance $54,618.18
  - Date 2025-06-12 | Description Payroll PAYRUN-0001 | Amount $-49,746.71 | Running Balance
 $4,871.47
  - Date 2025-06-19 | Description Security deposit refund DEP-0001 | Amount $-9,060.69 | 
Running Balance $-4,189.22

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
| 1 | Accounts Receivable | Rental Revenue | 17,748.96 | D002 | 2025-04-04 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 18,266.44 | D003 | 2025-04-22 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 17,234.36 | D004, D002 | 2025-06-12 | tenant_payment |
| 4 | Accounts Payable | Cash | 17,620.04 | D005, D003 | 2025-06-03 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 9,603.70 | D006 | 2025-04-20 | security_deposit |
| 6 | Salaries Expense | Cash | 44,306.85 | D007 | 2025-06-12 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 5,439.86 | D007 | 2025-06-12 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 4,178.75 | D008 | 2025-06-16 | utilities_bill |
| 9 | Prepaid Insurance | Cash | 26,775.02 | D009 | 2025-04-03 | prepaid_insurance_purchase |
| 10 | Insurance Expense | Prepaid Insurance | 8,925.01 | D009, D010 | 2025-06-30 | prepaid_insurance_release |
| 11 | Cash | Loans Payable | 50,092.63 | D011 | 2025-05-18 | loan_draw |
| 12 | Equipment | Cash | 80,641.37 | D012 | 2025-05-03 | equipment_purchase_cash |
| 13 | Equipment | Notes Payable | 95,720.16 | D012 | 2025-05-03 | equipment_purchase_financed |
| 14 | Depreciation Expense | Accumulated Depreciation | 11,022.60 | D013 | 2025-06-30 | depreciation |
| 15 | Loans Payable | Cash | 24,531.49 | D014 | 2025-06-07 | loan_repayment_principal |
| 16 | Interest Expense | Cash | 2,352.04 | D014 | 2025-06-07 | loan_repayment_interest |
| 17 | Security Deposits Payable | Cash | 9,060.69 | D015, D006 | 2025-06-19 | security_deposit_refund |
| 18 | Cash | Security Deposits Payable | 4,598.47 | D016 | 2025-04-16 | security_deposit |
| 19 | Accounts Receivable | Rental Revenue | 19,199.17 | D017 | 2025-04-05 | rent_roll |
| 20 | Accounts Receivable | Rental Revenue | 17,601.11 | D018 | 2025-04-04 | rent_roll |
| 21 | Cash | Security Deposits Payable | 13,678.89 | D019 | 2025-04-22 | security_deposit |
| 22 | Accounts Receivable | Rental Revenue | 19,180.07 | D020 | 2025-04-01 | rent_roll |
| 23 | Cash | Security Deposits Payable | 9,736.73 | D021 | 2025-04-10 | security_deposit |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: -4,189.22
- Accounts Receivable: 68,242.33
- Prepaid Insurance: 21,772.84
- Equipment: 186,782.05
- Accumulated Depreciation: -11,022.60

**Liabilities**
- Accounts Payable: 8,528.40
- Accrued Expenses: 2,277.87
- Security Deposits Payable: 41,132.13
- Loans Payable: 30,149.69
- Notes Payable: 95,720.16

**Equity**
- Retained Earnings: -9,974.75
- Owner's Equity: 93,751.90

**Totals:** Assets = 261,585.40; Liabilities = 177,808.25; Equity = 83,777.15
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
