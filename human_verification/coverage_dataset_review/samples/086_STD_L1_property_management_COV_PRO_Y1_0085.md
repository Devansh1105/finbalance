# Verification Packet — COV_PRO_Y1_0085

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 1
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Atlas Advisors
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `none`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 108,305.09
- Accounts Receivable: 18,164.15

**Liabilities**
- Accounts Payable: 7,348.88

**Equity**
- Owner's Equity: 119,120.36


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 108.305,09
  - Section assets | Account Accounts Receivable | Amount EUR 18.164,15
  - Section liabilities | Account Accounts Payable | Amount EUR 7.348,88
  - Section equity | Account Owner's Equity | Amount EUR 119.120,36

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D007 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-01-07

```
RENT ROLL
=========

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Document Date: 07/01/2024

Reference Box
-------------
Document ID: D007
Document Type: rent_roll
Period: FY 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0005
Property: Marina Heights
Period: FY 2024
Total Rent: EUR 14.136,06

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit A - Ellis | Amount EUR 14.136,06

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D005 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-01-09

```
RENT ROLL
=========

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Date: 09/01/2024

Reference Box
-------------
Document ID: D005
Document Type: rent_roll
Period: FY 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0003
Property: Cedar Plaza
Period: FY 2024
Total Rent: EUR 17.422,78

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit A - Ellis | Amount EUR 17.422,78

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-01-09

```
RENT ROLL
=========

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Date: 09/01/2024

Reference Box
-------------
Document ID: D006
Document Type: rent_roll
Period: FY 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0004
Property: Harbor View Offices
Period: FY 2024
Total Rent: EUR 16.053,55

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit B - Romero | Amount EUR 16.053,55

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D004 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-01-28

```
RENT ROLL
=========

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Date: 28/01/2024

Reference Box
-------------
Document ID: D004
Document Type: rent_roll
Period: FY 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Cedar Plaza
Period: FY 2024
Total Rent: EUR 13.459,09

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit D - Khan | Amount EUR 13.459,09

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D008 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-01-29

```
RENT ROLL
=========

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Date: 29/01/2024

Reference Box
-------------
Document ID: D008
Document Type: rent_roll
Period: FY 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0006
Property: Marina Heights
Period: FY 2024
Total Rent: EUR 14.710,64

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit B - Romero | Amount EUR 14.710,64

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-01-30

```
RENT ROLL
=========

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Date: 30/01/2024

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: FY 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Park Lane Residences
Period: FY 2024
Total Rent: EUR 24.203,45

Tenant Rows
-----------
Rows:
  - Unit A-101 | Tenant Unit D - Khan | Amount EUR 24.203,45

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-03

```
VENDOR INVOICE
==============

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Document Date: 03/03/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 24/03/2024

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 24/03/2024
Total: EUR 17.989,91

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 6.892,93
  - Description Support fee | Amount EUR 11.096,98

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D009 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Date: 31/12/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Vertex Supply Co.
Closing Balance: EUR 17.989,91

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount EUR 17.989,91 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D010 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Atlas Advisors
18 Marina Avenue, Chennai
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D010
Document Type: memo
Period: FY 2024

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
Audience: Back Office

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
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
Atlas Advisors
18 Marina Avenue, Chennai
Date: 31/12/2024

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0085
Statement Currency: EUR
Opening Balance: EUR 108.305,09
Closing Balance: EUR 108.305,09

Statement Rows
--------------
Rows: None

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
| 1 | Accounts Receivable | Rental Revenue | 24,203.45 | D002 | 2024-01-30 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 17,989.91 | D003 | 2024-03-03 | maintenance_bill |
| 3 | Accounts Receivable | Rental Revenue | 13,459.09 | D004 | 2024-01-28 | rent_roll |
| 4 | Accounts Receivable | Rental Revenue | 17,422.78 | D005 | 2024-01-09 | rent_roll |
| 5 | Accounts Receivable | Rental Revenue | 16,053.55 | D006 | 2024-01-09 | rent_roll |
| 6 | Accounts Receivable | Rental Revenue | 14,136.06 | D007 | 2024-01-07 | rent_roll |
| 7 | Accounts Receivable | Rental Revenue | 14,710.64 | D008 | 2024-01-29 | rent_roll |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 108,305.09
- Accounts Receivable: 118,149.72

**Liabilities**
- Accounts Payable: 25,338.79

**Equity**
- Owner's Equity: 119,120.36
- Retained Earnings: 81,995.66

**Totals:** Assets = 226,454.81; Liabilities = 25,338.79; Equity = 201,116.02
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
