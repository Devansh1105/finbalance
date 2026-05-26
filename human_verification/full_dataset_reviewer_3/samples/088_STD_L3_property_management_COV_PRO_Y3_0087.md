# Verification Packet — COV_PRO_Y3_0087

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 3
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Beacon Distribution
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 21
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 118,017.97
- Accounts Receivable: 12,979.54
- Prepaid Insurance: 6,346.17

**Liabilities**
- Accounts Payable: 16,703.93
- Accrued Expenses: 5,767.38
- Security Deposits Payable: 20,942.09

**Equity**
- Retained Earnings: 33,511.36
- Owner's Equity: 60,418.92


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-04-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $118,017.97
  - Section assets | Account Accounts Receivable | Amount $12,979.54
  - Section assets | Account Prepaid Insurance | Amount $6,346.17
  - Section liabilities | Account Accounts Payable | Amount $16,703.93
  - Section liabilities | Account Accrued Expenses | Amount $5,767.38
  - Section liabilities | Account Security Deposits Payable | Amount $20,942.09
  - Section equity | Account Retained Earnings | Amount $33,511.36
  - Section equity | Account Owner's Equity | Amount $60,418.92

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-04-08

```
RENT ROLL
=========

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-04-08

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: FY 2024-25

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Park Lane Residences
Period: FY 2024-25
Total Rent: $19,924.41

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit D - Khan | Amount $19,924.41

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D012 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-04-12

```
RENT ROLL
=========

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-04-12

Reference Box
-------------
Document ID: D012
Document Type: rent_roll
Period: FY 2024-25

Rent Roll Summary
-----------------
Roll Number: ROLL-0003
Property: Marina Heights
Period: FY 2024-25
Total Rent: $15,140.89

Tenant Rows
-----------
Rows:
  - Unit B-202 | Tenant Unit D - Khan | Amount $15,140.89

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D011 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-04-14

```
RENT ROLL
=========

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-04-14

Reference Box
-------------
Document ID: D011
Document Type: rent_roll
Period: FY 2024-25

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Cedar Plaza
Period: FY 2024-25
Total Rent: $14,941.84

Tenant Rows
-----------
Rows:
  - Unit B-202 | Tenant Unit B - Romero | Amount $14,941.84

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D010 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-18

```
VENDOR INVOICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-05-18

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-05-29

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 2024-05-29
Total: $12,186.59

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $4,086.09
  - Description Support fee | Amount $8,100.50

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D014 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-18

```
VENDOR INVOICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-05-18

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D014
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-06-03

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 2024-06-03
Total: $11,999.21

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $4,250.57
  - Description Support fee | Amount $7,748.64

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-30

```
VENDOR INVOICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-05-30

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-06-10

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-06-10
Total: $16,391.25

Bill Lines
----------
Lines:
  - Description Support package | Amount $5,818.37
  - Description Support fee | Amount $10,572.88

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D016 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-10

```
VENDOR INVOICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 2024-06-10

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-06-27

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0006
Due Date: 2024-06-27
Total: $11,580.24

Bill Lines
----------
Lines:
  - Description Review pack | Amount $2,640.91
  - Description Support fee | Amount $8,939.33

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2024-06-15

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-06-15

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: FY 2024-25

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit B - Romero
Unit: C-303
Amount: $19,518.20
Due Date: 2024-06-22

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D015 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-25

```
VENDOR INVOICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-06-25

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-07-09

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0005
Due Date: 2024-07-09
Total: $33,864.04

Bill Lines
----------
Lines:
  - Description Review pack | Amount $13,427.27
  - Description Support fee | Amount $20,436.77

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D013 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-30

```
VENDOR INVOICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 2024-06-30

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-07-16

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 2024-07-16
Total: $18,947.21

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $5,702.42
  - Description Support fee | Amount $13,244.79

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-22

```
PAYMENT ADVICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-12-22

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: FY 2024-25
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit D - Khan
Amount: $19,924.41
Reference: ROLL-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-24

```
PAYMENT ADVICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-12-24

To
--
Oakline Services

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: $16,391.25
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D009 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2024-12-31

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D009
Document Type: security_deposit_notice
Period: FY 2024-25

Security Deposit
----------------
Notice Number: DEPREF-0001
Tenant: Unit B - Romero
Unit: A-101
Amount: $18,805.43
Due Date: 2024-12-31

Notes
-----
Refund of previously collected security deposit DEP-0001.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-18

```
UTILITY INVOICE
===============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2025-01-18

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: FY 2024-25

Terms
-----
Due Date: 2025-02-02

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: FY 2024-25
Due Date: 2025-02-02
Total: $6,563.39

Charges
-------
Charges:
  - Description Electricity | Amount $1,603.42
  - Description Water | Amount $4,959.97

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-01-29

```
PAYROLL SUMMARY
===============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 2025-01-29

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 8
Gross Pay: $80,678.48
Employer Tax: 8,228.62
Cash Outflow: $88,907.10

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D017 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D017
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Annual leave policy reminder
Audience: Operations Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D018 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2025-03-31

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D018
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Prime Utility Desk
Closing Balance: $18,947.21

Statement Lines
---------------
Lines:
  - Reference BILL-0003 | Document Type Open invoice | Amount $18,947.21 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D019
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Document retention reminder
Audience: All Staff

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D020 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D020
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0003
Subject: Quarter-end packet routing note
Audience: Back Office

Memo Body
---------
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 2025-03-31

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0087
Statement Currency: USD
Opening Balance: $118,017.97
Closing Balance: $33,356.80

Statement Rows
--------------
Rows:
  - Date 2024-06-15 | Description Security deposit DEP-0001 | Amount $19,518.20 | Running 
Balance $137,536.17
  - Date 2024-12-22 | Description Customer settlement ROLL-0001 | Amount $19,924.41 | 
Running Balance $157,460.58
  - Date 2024-12-24 | Description Supplier settlement BILL-0001 | Amount $-16,391.25 | 
Running Balance $141,069.33
  - Date 2024-12-31 | Description Security deposit refund DEP-0001 | Amount $-18,805.43 | 
Running Balance $122,263.90
  - Date 2025-01-29 | Description Payroll PAYRUN-0001 | Amount $-88,907.10 | Running Balance
 $33,356.80

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
| 1 | Accounts Receivable | Rental Revenue | 19,924.41 | D002 | 2024-04-08 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 16,391.25 | D003 | 2024-05-30 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 19,924.41 | D004, D002 | 2024-12-22 | tenant_payment |
| 4 | Accounts Payable | Cash | 16,391.25 | D005, D003 | 2024-12-24 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 19,518.20 | D006 | 2024-06-15 | security_deposit |
| 6 | Salaries Expense | Cash | 80,678.48 | D007 | 2025-01-29 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 8,228.62 | D007 | 2025-01-29 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 6,563.39 | D008 | 2025-01-18 | utilities_bill |
| 9 | Security Deposits Payable | Cash | 18,805.43 | D009, D006 | 2024-12-31 | security_deposit_refund |
| 10 | Maintenance Expense | Accounts Payable | 12,186.59 | D010 | 2024-05-18 | maintenance_bill |
| 11 | Accounts Receivable | Rental Revenue | 14,941.84 | D011 | 2024-04-14 | rent_roll |
| 12 | Accounts Receivable | Rental Revenue | 15,140.89 | D012 | 2024-04-12 | rent_roll |
| 13 | Maintenance Expense | Accounts Payable | 18,947.21 | D013 | 2024-06-30 | maintenance_bill |
| 14 | Maintenance Expense | Accounts Payable | 11,999.21 | D014 | 2024-05-18 | maintenance_bill |
| 15 | Maintenance Expense | Accounts Payable | 33,864.04 | D015 | 2024-06-25 | maintenance_bill |
| 16 | Maintenance Expense | Accounts Payable | 11,580.24 | D016 | 2024-06-10 | maintenance_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 33,356.80
- Accounts Receivable: 43,062.27
- Prepaid Insurance: 6,346.17

**Liabilities**
- Accounts Payable: 111,844.61
- Accrued Expenses: 5,767.38
- Security Deposits Payable: 21,654.86

**Equity**
- Retained Earnings: -116,920.53
- Owner's Equity: 60,418.92

**Totals:** Assets = 82,765.24; Liabilities = 139,266.85; Equity = -56,501.61
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
