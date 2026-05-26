# Verification Packet — COV_PRO_M3_0077

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 3
- **Period type:** month
- **Period label:** December 2024
- **Period start → end:** 2024-12-01 → 2024-12-31
- **Entity:** Pioneer Software
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-12-01_

**Assets**
- Cash: 47,310.56
- Accounts Receivable: 3,567.94
- Prepaid Insurance: 3,063.56

**Liabilities**
- Accounts Payable: 2,719.14
- Accrued Expenses: 1,558.59
- Security Deposits Payable: 4,349.99

**Equity**
- Retained Earnings: 7,341.70
- Owner's Equity: 37,972.64


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-12-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/12/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 47,310.56
  - Section assets | Account Accounts Receivable | Amount GBP 3,567.94
  - Section assets | Account Prepaid Insurance | Amount GBP 3,063.56
  - Section liabilities | Account Accounts Payable | Amount GBP 2,719.14
  - Section liabilities | Account Accrued Expenses | Amount GBP 1,558.59
  - Section liabilities | Account Security Deposits Payable | Amount GBP 4,349.99
  - Section equity | Account Retained Earnings | Amount GBP 7,341.70
  - Section equity | Account Owner's Equity | Amount GBP 37,972.64

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-12-01

```
RENT ROLL
=========

From
----
Pioneer Software
75 Market Road, Mumbai
Date: 01/12/2024

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: December 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Harbor View Offices
Period: December 2024
Total Rent: GBP 6,452.79

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit D - Khan | Amount GBP 6,452.79

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D010 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-01

```
MEMO
====

From
----
Pioneer Software
75 Market Road, Mumbai
Date: 01/12/2024

Reference Box
-------------
Document ID: D010
Document Type: memo
Period: December 2024

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Annual leave policy reminder
Audience: All Staff

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2024-12-03

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Pioneer Software
75 Market Road, Mumbai
Date: 03/12/2024

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: December 2024

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit B - Romero
Unit: C-303
Amount: GBP 3,944.42
Due Date: 13/12/2024

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D009 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-04

```
VENDOR INVOICE
==============

From
----
Pioneer Software
75 Market Road, Mumbai
Document Date: 04/12/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: vendor_invoice
Period: December 2024

Terms
-----
Due Date: 21/12/2024

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 21/12/2024
Total: GBP 3,354.75

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 687.65
  - Description Support fee | Amount GBP 2,667.10

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-08

```
VENDOR INVOICE
==============

From
----
Pioneer Software
75 Market Road, Mumbai
Date: 08/12/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: December 2024

Terms
-----
Due Date: 24/12/2024

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 24/12/2024
Total: GBP 1,120.99

Bill Lines
----------
Lines:
  - Description Implementation work | Amount GBP 496.57
  - Description Support fee | Amount GBP 624.42

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-21

```
PAYMENT ADVICE
==============

From
----
Pioneer Software
75 Market Road, Mumbai
Date: 21/12/2024

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: December 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: GBP 1,120.99
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-23

```
PAYMENT ADVICE
==============

From
----
Pioneer Software
75 Market Road, Mumbai
Document Date: 23/12/2024

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: December 2024
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit D - Khan
Amount: GBP 6,452.79
Reference: ROLL-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-12-24

```
PAYROLL SUMMARY
===============

From
----
Pioneer Software
75 Market Road, Mumbai
Date: 24/12/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: December 2024
Headcount: 11
Gross Pay: GBP 9,416.58
Employer Tax: 1,097.03
Cash Outflow: GBP 10,513.61

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-24

```
UTILITY INVOICE
===============

From
----
Pioneer Software
75 Market Road, Mumbai
Date: 24/12/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: December 2024

Terms
-----
Due Date: 03/01/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: December 2024
Due Date: 03/01/2025
Total: GBP 1,837.68

Charges
-------
Charges:
  - Description Electricity | Amount GBP 560.01
  - Description Water | Amount GBP 1,277.67

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D011 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Software
75 Market Road, Mumbai
Date: 31/12/2024

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: December 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0077
Statement Currency: GBP
Opening Balance: GBP 47,310.56
Closing Balance: GBP 46,073.17

Statement Rows
--------------
Rows:
  - Date 03/12/2024 | Description Security deposit DEP-0001 | Amount GBP 3,944.42 | Running 
Balance GBP 51,254.98
  - Date 21/12/2024 | Description Supplier settlement BILL-0001 | Amount GBP -1,120.99 | 
Running Balance GBP 50,133.99
  - Date 23/12/2024 | Description Customer settlement ROLL-0001 | Amount GBP 6,452.79 | 
Running Balance GBP 56,586.78
  - Date 24/12/2024 | Description Payroll PAYRUN-0001 | Amount GBP -10,513.61 | Running 
Balance GBP 46,073.17

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D011
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 6,452.79 | D002 | 2024-12-01 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 1,120.99 | D003 | 2024-12-08 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 6,452.79 | D004, D002 | 2024-12-23 | tenant_payment |
| 4 | Accounts Payable | Cash | 1,120.99 | D005, D003 | 2024-12-21 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 3,944.42 | D006 | 2024-12-03 | security_deposit |
| 6 | Salaries Expense | Cash | 9,416.58 | D007 | 2024-12-24 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 1,097.03 | D007 | 2024-12-24 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 1,837.68 | D008 | 2024-12-24 | utilities_bill |
| 9 | Maintenance Expense | Accounts Payable | 3,354.75 | D009 | 2024-12-04 | maintenance_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 46,073.17
- Accounts Receivable: 3,567.94
- Prepaid Insurance: 3,063.56

**Liabilities**
- Accounts Payable: 7,911.57
- Accrued Expenses: 1,558.59
- Security Deposits Payable: 8,294.41

**Equity**
- Retained Earnings: -3,032.54
- Owner's Equity: 37,972.64

**Totals:** Assets = 52,704.67; Liabilities = 17,764.57; Equity = 34,940.10
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
- Notes: Balances tie — accept.
