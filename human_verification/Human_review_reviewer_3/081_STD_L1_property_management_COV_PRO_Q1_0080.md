# Verification Packet — COV_PRO_Q1_0080

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 1
- **Period type:** quarter
- **Period label:** Q1 FY 2025
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Granite Distribution
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `none`
- **Document count:** 8
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 57,028.77
- Accounts Receivable: 4,437.03

**Liabilities**
- Accounts Payable: 4,768.40

**Equity**
- Owner's Equity: 56,697.40


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 57,028.77
  - Section assets | Account Accounts Receivable | Amount GBP 4,437.03
  - Section liabilities | Account Accounts Payable | Amount GBP 4,768.40
  - Section equity | Account Owner's Equity | Amount GBP 56,697.40

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D005 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-06

```
RENT ROLL
=========

From
----
Granite Distribution
75 Market Road, Mumbai
Document Date: 06/01/2025

Reference Box
-------------
Document ID: D005
Document Type: rent_roll
Period: Q1 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0003
Property: Park Lane Residences
Period: Q1 FY 2025
Total Rent: GBP 11,566.48

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit D - Khan | Amount GBP 11,566.48

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-07

```
RENT ROLL
=========

From
----
Granite Distribution
75 Market Road, Mumbai
Date: 07/01/2025

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: Q1 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Harbor View Offices
Period: Q1 FY 2025
Total Rent: GBP 6,898.94

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit B - Romero | Amount GBP 6,898.94

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-07

```
VENDOR INVOICE
==============

From
----
Granite Distribution
75 Market Road, Mumbai
Document Date: 07/01/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q1 FY 2025

Terms
-----
Due Date: 24/01/2025

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Maintenance Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 24/01/2025
Total: GBP 12,392.73

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 4,094.48
  - Description Support fee | Amount GBP 8,298.25

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D006 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-07

```
RENT ROLL
=========

From
----
Granite Distribution
75 Market Road, Mumbai
Date: 07/01/2025

Reference Box
-------------
Document ID: D006
Document Type: rent_roll
Period: Q1 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0004
Property: Cedar Plaza
Period: Q1 FY 2025
Total Rent: GBP 5,576.71

Tenant Rows
-----------
Rows:
  - Unit D-404 | Tenant Unit A - Ellis | Amount GBP 5,576.71

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D004 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-01-08

```
RENT ROLL
=========

From
----
Granite Distribution
75 Market Road, Mumbai
Date: 08/01/2025

Reference Box
-------------
Document ID: D004
Document Type: rent_roll
Period: Q1 FY 2025

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Cedar Plaza
Period: Q1 FY 2025
Total Rent: GBP 11,263.15

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit C - Shah | Amount GBP 11,263.15

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D007 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Granite Distribution
75 Market Road, Mumbai
Date: 31/03/2025

Reference Box
-------------
Document ID: D007
Document Type: memo
Period: Q1 FY 2025

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Document retention reminder
Audience: Back Office

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Granite Distribution
75 Market Road, Mumbai
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: Q1 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0080
Statement Currency: GBP
Opening Balance: GBP 57,028.77
Closing Balance: GBP 57,028.77

Statement Rows
--------------
Rows: None

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 6,898.94 | D002 | 2025-01-07 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 12,392.73 | D003 | 2025-01-07 | maintenance_bill |
| 3 | Accounts Receivable | Rental Revenue | 11,263.15 | D004 | 2025-01-08 | rent_roll |
| 4 | Accounts Receivable | Rental Revenue | 11,566.48 | D005 | 2025-01-06 | rent_roll |
| 5 | Accounts Receivable | Rental Revenue | 5,576.71 | D006 | 2025-01-07 | rent_roll |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 57,028.77
- Accounts Receivable: 39,742.31

**Liabilities**
- Accounts Payable: 17,161.13

**Equity**
- Owner's Equity: 56,697.40
- Retained Earnings: 22,912.55

**Totals:** Assets = 96,771.08; Liabilities = 17,161.13; Equity = 79,609.95
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
- Notes:
