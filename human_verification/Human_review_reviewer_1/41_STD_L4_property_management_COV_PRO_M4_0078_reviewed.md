# Verification Packet — COV_PRO_M4_0078

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** November 2024
- **Period start → end:** 2024-11-01 → 2024-11-30
- **Entity:** Silverline Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 14
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-11-01_

**Assets**
- Cash: 28,268.56
- Accounts Receivable: 5,928.60
- Prepaid Insurance: 1,283.00
- Equipment: 7,104.57

**Liabilities**
- Accounts Payable: 2,211.93
- Accrued Expenses: 793.90
- Security Deposits Payable: 4,355.18
- Loans Payable: 6,644.63

**Equity**
- Retained Earnings: 2,840.80
- Owner's Equity: 25,738.29


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-11-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-11-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $28,268.56
  - Section assets | Account Accounts Receivable | Amount $5,928.60
  - Section assets | Account Prepaid Insurance | Amount $1,283.00
  - Section assets | Account Equipment | Amount $7,104.57
  - Section liabilities | Account Accounts Payable | Amount $2,211.93
  - Section liabilities | Account Accrued Expenses | Amount $793.90
  - Section liabilities | Account Security Deposits Payable | Amount $4,355.18
  - Section liabilities | Account Loans Payable | Amount $6,644.63
  - Section equity | Account Retained Earnings | Amount $2,840.80
  - Section equity | Account Owner's Equity | Amount $25,738.29

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-11-02

```
RENT ROLL
=========

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2024-11-02

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: November 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Harbor View Offices
Period: November 2024
Total Rent: $8,005.25

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit D - Khan | Amount $8,005.25

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-03

```
VENDOR INVOICE
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2024-11-03

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: November 2024

Terms
-----
Due Date: 2024-11-24

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-11-24
Total: $1,150.99

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $441.38
  - Description Support fee | Amount $709.61

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D009 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2024-11-03

```
INSURANCE NOTICE
================

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2024-11-03

To
--
Beacon General
Vendor remittance address on file

Terms
-----
Service Start: 2024-11-03
Service End: 2025-02-02

Coverage Notice
---------------
Notice Number: PRE-0001
Carrier: Beacon General
Covered Item: Marina Heights
Coverage Start: 2024-11-03
Coverage End: 2025-02-02
Total Premium: $10,880.39
Monthly Amount: $3,626.80

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2024-11-06

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2024-11-06

To
--
Unit C - Shah

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: November 2024

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit C - Shah
Unit: C-303
Amount: $5,034.62
Due Date: 2024-11-13

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-18

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $13,089.99
Draw Amount: $20,987.56
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $34,077.55
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-20

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: Delivery van
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $36,500.83
Paid Cash: $13,809.27
Financed Amount: $22,691.56
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-22

```
PAYMENT ADVICE
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2024-11-22

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: November 2024
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit D - Khan
Amount: $6,592.14
Reference: ROLL-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-25

```
PAYMENT ADVICE
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2024-11-25

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: November 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $851.26
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-11-25

```
PAYROLL SUMMARY
===============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2024-11-25

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: November 2024
Headcount: 3
Gross Pay: $21,333.21
Employer Tax: 2,191.66
Cash Outflow: $23,524.87

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-25

```
UTILITY INVOICE
===============

From
----
Silverline Manufacturing
14 King Street, Pune
Document Date: 2024-11-25

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: November 2024

Terms
-----
Due Date: 2024-12-05

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: November 2024
Due Date: 2024-12-05
Total: $775.11

Charges
-------
Charges:
  - Description Electricity | Amount $220.01
  - Description Water | Amount $555.10

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D010 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-11-30

```
SERVICE PERIOD MEMO
===================

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2024-11-30

Reference Box
-------------
Document ID: D010
Document Type: service_period_memo
Period: November 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Insurance coverage release
Reference: PRE-0001
Recognized Amount: $3,626.80

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
- **Date:** 2024-11-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0002
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $7,104.57
Useful Life Months: 48
Current Period Charge: $148.01
Accumulated Depreciation: 148.01
```

### Document D014 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-11-30

```
BANK STATEMENT
==============

From
----
Silverline Manufacturing
14 King Street, Pune
Date: 2024-11-30

Reference Box
-------------
Document ID: D014
Document Type: bank_statement
Period: November 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0078
Statement Currency: USD
Opening Balance: $28,268.56
Closing Balance: $11,817.09

Statement Rows
--------------
Rows:
  - Date 2024-11-03 | Description Insurance coverage prepayment PRE-0001 | Amount 
$-10,880.39 | Running Balance $17,388.17
  - Date 2024-11-06 | Description Security deposit DEP-0001 | Amount $5,034.62 | Running 
Balance $22,422.79
  - Date 2024-11-18 | Description Loan draw LOAN-0001 | Amount $20,987.56 | Running Balance 
$43,410.35
  - Date 2024-11-20 | Description Asset purchase ASSET-0001 | Amount $-13,809.27 | Running 
Balance $29,601.08
  - Date 2024-11-22 | Description Customer settlement ROLL-0001 | Amount $6,592.14 | Running
 Balance $36,193.22
  - Date 2024-11-25 | Description Payroll PAYRUN-0001 | Amount $-23,524.87 | Running Balance
 $12,668.35
  - Date 2024-11-25 | Description Supplier settlement BILL-0001 | Amount $-851.26 | Running 
Balance $11,817.09

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D014
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 8,005.25 | D002 | 2024-11-02 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 1,150.99 | D003 | 2024-11-03 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 6,592.14 | D004, D002 | 2024-11-22 | tenant_payment |
| 4 | Accounts Payable | Cash | 851.26 | D005, D003 | 2024-11-25 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 5,034.62 | D006 | 2024-11-06 | security_deposit |
| 6 | Salaries Expense | Cash | 21,333.21 | D007 | 2024-11-25 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 2,191.66 | D007 | 2024-11-25 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 775.11 | D008 | 2024-11-25 | utilities_bill |
| 9 | Prepaid Insurance | Cash | 10,880.39 | D009 | 2024-11-03 | prepaid_insurance_purchase |
| 10 | Insurance Expense | Prepaid Insurance | 3,626.80 | D009, D010 | 2024-11-30 | prepaid_insurance_release |
| 11 | Cash | Loans Payable | 20,987.56 | D011 | 2024-11-18 | loan_draw |
| 12 | Equipment | Cash | 13,809.27 | D012 | 2024-11-20 | equipment_purchase_cash |
| 13 | Equipment | Notes Payable | 22,691.56 | D012 | 2024-11-20 | equipment_purchase_financed |
| 14 | Depreciation Expense | Accumulated Depreciation | 148.01 | D013 | 2024-11-30 | depreciation |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 11,817.09
- Accounts Receivable: 7,341.71
- Prepaid Insurance: 8,536.59
- Equipment: 43,605.40
- Accumulated Depreciation: -148.01

**Liabilities**
- Accounts Payable: 3,286.77
- Accrued Expenses: 793.90
- Security Deposits Payable: 9,389.80
- Loans Payable: 27,632.19
- Notes Payable: 22,691.56

**Equity**
- Retained Earnings: -18,379.73
- Owner's Equity: 25,738.29

**Totals:** Assets = 71,152.78; Liabilities = 63,794.22; Equity = 7,358.56
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
- Notes: Support ties reasonably well to postings.
