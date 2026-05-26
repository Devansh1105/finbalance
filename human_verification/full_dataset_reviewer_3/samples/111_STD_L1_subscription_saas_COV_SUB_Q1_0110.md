# Verification Packet — COV_SUB_Q1_0110

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 1
- **Period type:** quarter
- **Period label:** Q4 FY 2025-26
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Summit Builders
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `none`
- **Document count:** 8
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 116,779.44

**Liabilities**
- Accounts Payable: 10,709.84

**Equity**
- Share Capital: 106,069.60


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
  - Section assets | Account Cash | Amount GBP 116,779.44
  - Section liabilities | Account Accounts Payable | Amount GBP 10,709.84
  - Section equity | Account Share Capital | Amount GBP 106,069.60

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D006 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2025-01-01

```
RENEWAL NOTICE
==============

From
----
Summit Builders
90 Hill Park, Hyderabad
Document Date: 01/01/2025

To
--
Aster Point Services
Customer account on file

Terms
-----
Renewal Start: 06/01/2025

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Aster Point Services
Contract Reference: SOF-0002
Renewal Start: 06/01/2025
Renewal Amount: GBP 143,844.79

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-01-06

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Builders
90 Hill Park, Hyderabad
Document Date: 06/01/2025

To
--
Aster Point Services
Customer account on file

Terms
-----
Contract Start: 06/01/2025

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0002
Customer: Aster Point Services
Plan Name: Enterprise License
Term Months: 6
Contract Start: 06/01/2025
Contract Value: GBP 143,844.79

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-06

```
CUSTOMER INVOICE
================

From
----
Summit Builders
90 Hill Park, Hyderabad
Document Date: 06/01/2025

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: Q4 FY 2025-26
Contract Ref: SOF-0002

Terms
-----
Due Date: 20/01/2025

Parties
-------
Customer: Aster Point Services
Contract Ref: SOF-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 20/01/2025
Total: GBP 143,844.79

Line Items
----------
Items:
  - Description Enterprise License | Amount GBP 38,317.69
  - Description Service coverage under contract | Amount GBP 105,527.10

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-01-20

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Builders
90 Hill Park, Hyderabad
Document Date: 20/01/2025

To
--
Aster Point Services
Customer account on file

Terms
-----
Contract Start: 20/01/2025

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: SOF-0001
Customer: Aster Point Services
Plan Name: Business Suite
Term Months: 3
Contract Start: 20/01/2025
Contract Value: GBP 193,247.37

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-20

```
CUSTOMER INVOICE
================

From
----
Summit Builders
90 Hill Park, Hyderabad
Document Date: 20/01/2025

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q4 FY 2025-26
Contract Ref: SOF-0001

Terms
-----
Due Date: 30/01/2025

Parties
-------
Customer: Aster Point Services
Contract Ref: SOF-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 30/01/2025
Total: GBP 193,247.37

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount GBP 52,880.84
  - Description Service coverage under contract | Amount GBP 140,366.53

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Summit Builders
90 Hill Park, Hyderabad
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: Q4 FY 2025-26

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: Q4 FY 2025-26
Opening Deferred: GBP 193,247.37
Added Deferred: GBP 0.00
Released This Period: 193,247.37
Ending Deferred: GBP 0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
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
Summit Builders
90 Hill Park, Hyderabad
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: Q4 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0110
Statement Currency: GBP
Opening Balance: GBP 116,779.44
Closing Balance: GBP 116,779.44

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
| 1 | Accounts Receivable | Unearned Revenue | 193,247.37 | D002, D003 | 2025-01-20 | subscription_invoice |
| 2 | Unearned Revenue | Service Revenue | 193,247.37 | D004, D003 | 2025-03-31 | revenue_release |
| 3 | Accounts Receivable | Unearned Revenue | 143,844.79 | D006, D005, D007 | 2025-01-06 | renewal_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 116,779.44
- Accounts Receivable: 337,092.16

**Liabilities**
- Accounts Payable: 10,709.84
- Unearned Revenue: 143,844.79

**Equity**
- Share Capital: 106,069.60
- Retained Earnings: 193,247.37

**Totals:** Assets = 453,871.60; Liabilities = 154,554.63; Equity = 299,316.97
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
