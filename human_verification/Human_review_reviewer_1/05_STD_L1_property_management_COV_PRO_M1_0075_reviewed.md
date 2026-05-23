# Verification Packet — COV_PRO_M1_0075

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** March 2024
- **Period start → end:** 2024-03-01 → 2024-03-31
- **Entity:** Summit Operations
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 5
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-03-01_

**Assets**
- Cash: 41,648.69
- Accounts Receivable: 6,949.49

**Liabilities**
- Accounts Payable: 2,679.03

**Equity**
- Owner's Equity: 45,919.15


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-03-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-03-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $41,648.69
  - Section assets | Account Accounts Receivable | Amount $6,949.49
  - Section liabilities | Account Accounts Payable | Amount $2,679.03
  - Section equity | Account Owner's Equity | Amount $45,919.15

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-03-03

```
RENT ROLL
=========

From
----
Summit Operations
220 Lake View Road, Bengaluru
Document Date: 2024-03-03

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: March 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Harbor View Offices
Period: March 2024
Total Rent: $5,590.23

Tenant Rows
-----------
Rows:
  - Unit B-202 | Tenant Unit A - Ellis | Amount $5,590.23

Footer
------
Generated for synthetic accounting research use.
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
Summit Operations
220 Lake View Road, Bengaluru
Date: 2024-03-03

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: March 2024

Terms
-----
Due Date: 2024-03-15

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Maintenance Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-03-15
Total: $3,499.11

Bill Lines
----------
Lines:
  - Description Review pack | Amount $1,062.36
  - Description Support fee | Amount $2,436.75

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2024-03-03

```
RENT ROLL
=========

From
----
Summit Operations
220 Lake View Road, Bengaluru
Document Date: 2024-03-03

Reference Box
-------------
Document ID: D004
Document Type: rent_roll
Period: March 2024

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Harbor View Offices
Period: March 2024
Total Rent: $3,996.36

Tenant Rows
-----------
Rows:
  - Unit B-202 | Tenant Unit B - Romero | Amount $3,996.36

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-03-31

```
BANK STATEMENT
==============

From
----
Summit Operations
220 Lake View Road, Bengaluru
Date: 2024-03-31

Reference Box
-------------
Document ID: D005
Document Type: bank_statement
Period: March 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0075
Statement Currency: USD
Opening Balance: $41,648.69
Closing Balance: $41,648.69

Statement Rows
--------------
Rows: None

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D005
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 5,590.23 | D002 | 2024-03-03 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 3,499.11 | D003 | 2024-03-03 | maintenance_bill |
| 3 | Accounts Receivable | Rental Revenue | 3,996.36 | D004 | 2024-03-03 | rent_roll |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 41,648.69
- Accounts Receivable: 16,536.08

**Liabilities**
- Accounts Payable: 6,178.14

**Equity**
- Owner's Equity: 45,919.15
- Retained Earnings: 6,087.48

**Totals:** Assets = 58,184.77; Liabilities = 6,178.14; Equity = 52,006.63
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
