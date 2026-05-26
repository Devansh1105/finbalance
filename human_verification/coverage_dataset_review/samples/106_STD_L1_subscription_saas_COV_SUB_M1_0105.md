# Verification Packet — COV_SUB_M1_0105

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** August 2025
- **Period start → end:** 2025-08-01 → 2025-08-31
- **Entity:** Silverline Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 5
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-08-01_

**Assets**
- Cash: 73,604.42

**Liabilities**
- Accounts Payable: 6,319.61

**Equity**
- Share Capital: 67,284.81


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-08-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-08-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $73,604.42
  - Section liabilities | Account Accounts Payable | Amount $6,319.61
  - Section equity | Account Share Capital | Amount $67,284.81

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-08-06

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Silverline Manufacturing
220 Lake View Road, Bengaluru
Document Date: 2025-08-06

To
--
Maple Ridge Trading
Customer account on file

Terms
-----
Contract Start: 2025-08-06

Approval / Context
------------------
Plan Name: Team Support Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Maple Ridge Trading
Plan Name: Team Support Plan
Term Months: 6
Contract Start: 2025-08-06
Contract Value: $62,367.51

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-06

```
CUSTOMER INVOICE
================

From
----
Silverline Manufacturing
220 Lake View Road, Bengaluru
Document Date: 2025-08-06

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: August 2025
Contract Ref: SOF-0001

Terms
-----
Due Date: 2025-08-18

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: SOF-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-08-18
Total: $62,367.51

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount $25,749.78
  - Description Service coverage under contract | Amount $36,617.73

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-08-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Silverline Manufacturing
220 Lake View Road, Bengaluru
Document Date: 2025-08-31

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: August 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: August 2025
Opening Deferred: $62,367.51
Added Deferred: $0.00
Released This Period: 10,394.59
Ending Deferred: $51,972.92

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-08-31

```
BANK STATEMENT
==============

From
----
Silverline Manufacturing
220 Lake View Road, Bengaluru
Date: 2025-08-31

Reference Box
-------------
Document ID: D005
Document Type: bank_statement
Period: August 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0105
Statement Currency: USD
Opening Balance: $73,604.42
Closing Balance: $73,604.42

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
| 1 | Accounts Receivable | Unearned Revenue | 62,367.51 | D002, D003 | 2025-08-06 | subscription_invoice |
| 2 | Unearned Revenue | Service Revenue | 10,394.59 | D004, D003 | 2025-08-31 | revenue_release |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 73,604.42
- Accounts Receivable: 62,367.51

**Liabilities**
- Accounts Payable: 6,319.61
- Unearned Revenue: 51,972.92

**Equity**
- Share Capital: 67,284.81
- Retained Earnings: 10,394.59

**Totals:** Assets = 135,971.93; Liabilities = 58,292.53; Equity = 77,679.40
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
