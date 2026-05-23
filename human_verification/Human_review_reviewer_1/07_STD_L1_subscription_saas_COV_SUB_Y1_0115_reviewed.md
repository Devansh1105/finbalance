# Verification Packet — COV_SUB_Y1_0115

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 1
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Northwind Advisors
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `none`
- **Document count:** 12
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 392,351.72

**Liabilities**
- Accounts Payable: 22,764.70

**Equity**
- Share Capital: 369,587.02


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
Statement Date: 01/04/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 392.351,72
  - Section liabilities | Account Accounts Payable | Amount EUR 22.764,70
  - Section equity | Account Share Capital | Amount EUR 369.587,02

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-05-17

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Northwind Advisors
14 King Street, Pune
Date: 17/05/2024

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Contract Start: 17/05/2024

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Oak Harbor Foods
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 17/05/2024
Contract Value: EUR 157.481,56

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-17

```
CUSTOMER INVOICE
================

From
----
Northwind Advisors
14 King Street, Pune
Document Date: 17/05/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: SOF-0001

Terms
-----
Due Date: 04/06/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: SOF-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 04/06/2024
Total: EUR 157.481,56

Line Items
----------
Items:
  - Description Team Support Plan | Amount EUR 47.494,62
  - Description Service coverage under contract | Amount EUR 109.986,94

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D006 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2024-06-14

```
RENEWAL NOTICE / REFERENCE COPY
===============================

From
----
Northwind Advisors
14 King Street, Pune
Document Date: 14/06/2024

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Renewal Start: 29/06/2024

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Blue Finch Holdings
Contract Reference: SOF-0002
Renewal Start: 29/06/2024
Renewal Amount: EUR 338.602,16

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-06-29

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Northwind Advisors
14 King Street, Pune
Date: 29/06/2024

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Contract Start: 29/06/2024

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: SOF-0002
Customer: Blue Finch Holdings
Plan Name: Business Suite
Term Months: 12
Contract Start: 29/06/2024
Contract Value: EUR 338.602,16

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-29

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Northwind Advisors
14 King Street, Pune
Date: 29/06/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: SOF-0002

Terms
-----
Due Date: 06/07/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: SOF-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 06/07/2024
Total: EUR 338.602,16

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount EUR 95.724,33
  - Description Service coverage under contract | Amount EUR 242.877,83

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-07-01

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Northwind Advisors
14 King Street, Pune
Date: 01/07/2024

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 01/07/2024

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: SOF-0003
Customer: Riverfront Group
Plan Name: Business Suite
Term Months: 12
Contract Start: 01/07/2024
Contract Value: EUR 430.071,29

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D009 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-01

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Northwind Advisors
14 King Street, Pune
Date: 01/07/2024

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D009
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: SOF-0003

Terms
-----
Due Date: 12/07/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: SOF-0003
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 12/07/2024
Total: EUR 430.071,29

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount EUR 179.710,62
  - Description Service coverage under contract | Amount EUR 250.360,67

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D011 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-07-01

```
SECONDARY COPY
==============

From
----
Northwind Advisors
14 King Street, Pune
Date: 01/07/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D011
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0003
Counterparty: Riverfront Group
Total: EUR 430.071,29
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D011
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
Northwind Advisors
14 King Street, Pune
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: FY 2024-25

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: FY 2024-25
Opening Deferred: EUR 157.481,56
Added Deferred: EUR 0,00
Released This Period: 157.481,56
Ending Deferred: EUR 0,00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D010 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Northwind Advisors
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D010
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
Internal document packet copy.
Page marker: D010
```

### Document D012 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Northwind Advisors
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D012
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0115
Statement Currency: EUR
Opening Balance: EUR 392.351,72
Closing Balance: EUR 822.423,01

Statement Rows
--------------
Rows:
  - Date 01/07/2024 | Description Advance collection INV-0003 | Amount EUR 430.071,29 | 
Running Balance EUR 822.423,01

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D012
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 157,481.56 | D002, D003 | 2024-05-17 | subscription_invoice |
| 2 | Unearned Revenue | Service Revenue | 157,481.56 | D004, D003 | 2025-03-31 | revenue_release |
| 3 | Accounts Receivable | Unearned Revenue | 338,602.16 | D006, D005, D007 | 2024-06-29 | renewal_invoice |
| 4 | Cash | Unearned Revenue | 430,071.29 | D008, D009 | 2024-07-01 | subscription_cash_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 822,423.01
- Accounts Receivable: 496,083.72

**Liabilities**
- Accounts Payable: 22,764.70
- Unearned Revenue: 768,673.45

**Equity**
- Share Capital: 369,587.02
- Retained Earnings: 157,481.56

**Totals:** Assets = 1,318,506.73; Liabilities = 791,438.15; Equity = 527,068.58
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
- Notes: Acceptable as-is.
