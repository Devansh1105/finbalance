# Verification Packet — COV_PRO_Q4_0083

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q3 FY 2024
- **Period start → end:** 2024-07-01 → 2024-09-30
- **Entity:** Silverline Retail Group
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 17
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-07-01_

**Assets**
- Cash: 63,888.80
- Accounts Receivable: 5,771.99
- Prepaid Insurance: 4,138.06
- Equipment: 11,496.89

**Liabilities**
- Accounts Payable: 4,432.97
- Accrued Expenses: 3,865.53
- Security Deposits Payable: 10,397.48
- Loans Payable: 3,683.26

**Equity**
- Retained Earnings: 14,953.36
- Owner's Equity: 47,963.14


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
  - Section assets | Account Cash | Amount GBP 63,888.80
  - Section assets | Account Accounts Receivable | Amount GBP 5,771.99
  - Section assets | Account Prepaid Insurance | Amount GBP 4,138.06
  - Section assets | Account Equipment | Amount GBP 11,496.89
  - Section liabilities | Account Accounts Payable | Amount GBP 4,432.97
  - Section liabilities | Account Accrued Expenses | Amount GBP 3,865.53
  - Section liabilities | Account Security Deposits Payable | Amount GBP 10,397.48
  - Section liabilities | Account Loans Payable | Amount GBP 3,683.26
  - Section equity | Account Retained Earnings | Amount GBP 14,953.36
  - Section equity | Account Owner's Equity | Amount GBP 47,963.14

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-07-03

```
RENT ROLL
=========

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 03/07/2024

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: Q3 FY 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Cedar Plaza
Period: Q3 FY 2024
Total Rent: GBP 8,095.30

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit B - Romero | Amount GBP 8,095.30

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D016 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-07-04

```
RENT ROLL
=========

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 04/07/2024

Reference Box
-------------
Document ID: D016
Document Type: rent_roll
Period: Q3 FY 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Park Lane Residences
Period: Q3 FY 2024
Total Rent: GBP 14,439.25

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit C - Shah | Amount GBP 14,439.25

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D015 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-05

```
VENDOR INVOICE
==============

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 05/07/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: vendor_invoice
Period: Q3 FY 2024

Terms
-----
Due Date: 16/07/2024

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 16/07/2024
Total: GBP 6,726.76

Bill Lines
----------
Lines:
  - Description Implementation work | Amount GBP 1,666.33
  - Description Support fee | Amount GBP 5,060.43

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D009 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2024-07-06

```
INSURANCE NOTICE / REFERENCE COPY
=================================

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Document Date: 06/07/2024

To
--
Shield Mutual
Vendor remittance address on file

Terms
-----
Service Start: 06/07/2024
Service End: 05/10/2024

Coverage Notice
---------------
Notice Number: PRE-0001
Carrier: Shield Mutual
Covered Item: Harbor View Offices
Coverage Start: 06/07/2024
Coverage End: 05/10/2024
Total Premium: GBP 8,916.10
Monthly Amount: GBP 2,972.03

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-17

```
VENDOR INVOICE
==============

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 17/07/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q3 FY 2024

Terms
-----
Due Date: 05/08/2024

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 05/08/2024
Total: GBP 14,975.77

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 4,800.05
  - Description Support fee | Amount GBP 10,175.72

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2024-07-18

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 18/07/2024

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: Q3 FY 2024

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit B - Romero
Unit: D-404
Amount: GBP 10,838.06
Due Date: 24/07/2024

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-08-15

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 13,343.17
Draw Amount: GBP 144,046.33
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 157,389.50
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-27

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Prime Utility Desk
Asset Name: Server rack
Asset Tag: TAG-0001
Useful Life Months: 24
Total: GBP 76,497.62
Paid Cash: GBP 24,964.08
Financed Amount: GBP 51,533.54
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-07

```
PAYMENT ADVICE
==============

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 07/09/2024

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q3 FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Pace Office Mart
Amount: GBP 11,084.09
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-08

```
PAYROLL SUMMARY
===============

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 08/09/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q3 FY 2024
Headcount: 10
Gross Pay: GBP 24,822.77
Employer Tax: 2,992.58
Cash Outflow: GBP 27,815.35

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D014 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-10

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 10/09/2024

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D014
Document Type: security_deposit_notice
Period: Q3 FY 2024

Security Deposit
----------------
Notice Number: DEPREF-0001
Tenant: Unit B - Romero
Unit: D-404
Amount: GBP 9,519.07
Due Date: 10/09/2024

Notes
-----
Refund of previously collected security deposit DEP-0001.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-16

```
UTILITY INVOICE
===============

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 16/09/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: Q3 FY 2024

Terms
-----
Due Date: 03/10/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: Q3 FY 2024
Due Date: 03/10/2024
Total: GBP 3,992.11

Charges
-------
Charges:
  - Description Electricity | Amount GBP 1,098.35
  - Description Water | Amount GBP 2,893.76

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-18

```
PAYMENT ADVICE
==============

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Document Date: 18/09/2024

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: Q3 FY 2024
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit B - Romero
Amount: GBP 7,089.49
Reference: ROLL-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D010 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-30

```
SERVICE PERIOD MEMO
===================

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Document Date: 30/09/2024

Reference Box
-------------
Document ID: D010
Document Type: service_period_memo
Period: Q3 FY 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Insurance coverage release
Reference: PRE-0001
Recognized Amount: GBP 2,972.03

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
- **Date:** 2024-09-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0002
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: GBP 11,496.89
Useful Life Months: 48
Current Period Charge: GBP 718.56
Accumulated Depreciation: 718.56
```

### Document D017 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Silverline Retail Group
18 Marina Avenue, Chennai
Date: 30/09/2024

Reference Box
-------------
Document ID: D017
Document Type: bank_statement
Period: Q3 FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0083
Statement Currency: GBP
Opening Balance: GBP 63,888.80
Closing Balance: GBP 143,563.99

Statement Rows
--------------
Rows:
  - Date 06/07/2024 | Description Insurance coverage prepayment PRE-0001 | Amount GBP 
-8,916.10 | Running Balance GBP 54,972.70
  - Date 18/07/2024 | Description Security deposit DEP-0001 | Amount GBP 10,838.06 | Running
 Balance GBP 65,810.76
  - Date 15/08/2024 | Description Loan draw LOAN-0001 | Amount GBP 144,046.33 | Running 
Balance GBP 209,857.09
  - Date 27/08/2024 | Description Asset purchase ASSET-0001 | Amount GBP -24,964.08 | 
Running Balance GBP 184,893.01
  - Date 07/09/2024 | Description Supplier settlement BILL-0001 | Amount GBP -11,084.09 | 
Running Balance GBP 173,808.92
  - Date 08/09/2024 | Description Payroll PAYRUN-0001 | Amount GBP -27,815.35 | Running 
Balance GBP 145,993.57
  - Date 10/09/2024 | Description Security deposit refund DEP-0001 | Amount GBP -9,519.07 | 
Running Balance GBP 136,474.50
  - Date 18/09/2024 | Description Customer settlement ROLL-0001 | Amount GBP 7,089.49 | 
Running Balance GBP 143,563.99

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
| 1 | Accounts Receivable | Rental Revenue | 8,095.30 | D002 | 2024-07-03 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 14,975.77 | D003 | 2024-07-17 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 7,089.49 | D004, D002 | 2024-09-18 | tenant_payment |
| 4 | Accounts Payable | Cash | 11,084.09 | D005, D003 | 2024-09-07 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 10,838.06 | D006 | 2024-07-18 | security_deposit |
| 6 | Salaries Expense | Cash | 24,822.77 | D007 | 2024-09-08 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 2,992.58 | D007 | 2024-09-08 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 3,992.11 | D008 | 2024-09-16 | utilities_bill |
| 9 | Prepaid Insurance | Cash | 8,916.10 | D009 | 2024-07-06 | prepaid_insurance_purchase |
| 10 | Insurance Expense | Prepaid Insurance | 2,972.03 | D009, D010 | 2024-09-30 | prepaid_insurance_release |
| 11 | Cash | Loans Payable | 144,046.33 | D011 | 2024-08-15 | loan_draw |
| 12 | Equipment | Cash | 24,964.08 | D012 | 2024-08-27 | equipment_purchase_cash |
| 13 | Equipment | Notes Payable | 51,533.54 | D012 | 2024-08-27 | equipment_purchase_financed |
| 14 | Depreciation Expense | Accumulated Depreciation | 718.56 | D013 | 2024-09-30 | depreciation |
| 15 | Security Deposits Payable | Cash | 9,519.07 | D014, D006 | 2024-09-10 | security_deposit_refund |
| 16 | Maintenance Expense | Accounts Payable | 6,726.76 | D015 | 2024-07-05 | maintenance_bill |
| 17 | Accounts Receivable | Rental Revenue | 14,439.25 | D016 | 2024-07-04 | rent_roll |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 143,563.99
- Accounts Receivable: 21,217.05
- Prepaid Insurance: 10,082.13
- Equipment: 87,994.51
- Accumulated Depreciation: -718.56

**Liabilities**
- Accounts Payable: 19,043.52
- Accrued Expenses: 3,865.53
- Security Deposits Payable: 11,716.47
- Loans Payable: 147,729.59
- Notes Payable: 51,533.54

**Equity**
- Retained Earnings: -19,712.67
- Owner's Equity: 47,963.14

**Totals:** Assets = 262,139.12; Liabilities = 233,888.65; Equity = 28,250.47
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
