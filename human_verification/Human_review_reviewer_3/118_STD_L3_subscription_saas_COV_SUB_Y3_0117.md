# Verification Packet — COV_SUB_Y3_0117

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 3
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Willow Distribution
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 18
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 696,069.94
- Accounts Receivable: 94,308.89
- Prepaid Insurance: 11,907.07
- Office Supplies: 7,470.61

**Liabilities**
- Accounts Payable: 38,600.34
- Accrued Expenses: 15,279.26
- Unearned Revenue: 166,935.22

**Equity**
- Retained Earnings: 125,136.07
- Share Capital: 463,805.62


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
  - Section assets | Account Cash | Amount $696,069.94
  - Section assets | Account Accounts Receivable | Amount $94,308.89
  - Section assets | Account Prepaid Insurance | Amount $11,907.07
  - Section assets | Account Office Supplies | Amount $7,470.61
  - Section liabilities | Account Accounts Payable | Amount $38,600.34
  - Section liabilities | Account Accrued Expenses | Amount $15,279.26
  - Section liabilities | Account Unearned Revenue | Amount $166,935.22
  - Section equity | Account Retained Earnings | Amount $125,136.07
  - Section equity | Account Share Capital | Amount $463,805.62

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-04-30

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2024-04-30

To
--
Crescent Labs
Customer account on file

Terms
-----
Contract Start: 2024-04-30

Approval / Context
------------------
Plan Name: Team Support Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Crescent Labs
Plan Name: Team Support Plan
Term Months: 12
Contract Start: 2024-04-30
Contract Value: $653,263.26

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-30

```
CUSTOMER INVOICE
================

From
----
Willow Distribution
90 Hill Park, Hyderabad
Document Date: 2024-04-30

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: SOF-0001

Terms
-----
Due Date: 2024-05-15

Parties
-------
Customer: Crescent Labs
Contract Ref: SOF-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-05-15
Subtotal: $610,526.41
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $42,736.85
Total: $653,263.26

Line Items
----------
Items:
  - Description Business Suite | Amount $153,526.36
  - Description Service coverage under contract | Amount $457,000.05

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D016 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-04-30

```
SECONDARY COPY
==============

From
----
Willow Distribution
90 Hill Park, Hyderabad
Document Date: 2024-04-30

To
--
Crescent Labs

Reference Box
-------------
Document ID: D016
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0001
Counterparty: Crescent Labs
Total: $653,263.26
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-21

```
VENDOR INVOICE
==============

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2024-05-21

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-06-08

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Utilities Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-06-08
Subtotal: $14,111.88
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $705.59
Total: $14,817.47

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $3,419.09
  - Description Support fee | Amount $10,692.79

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D011 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2024-05-31

```
RENEWAL NOTICE / REFERENCE COPY
===============================

From
----
Willow Distribution
90 Hill Park, Hyderabad
Document Date: 2024-05-31

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Renewal Start: 2024-06-15

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Blue Finch Holdings
Contract Reference: SOF-0002
Renewal Start: 2024-06-15
Renewal Amount: $695,164.35

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D013 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-06-09

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2024-06-09

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 2024-06-09

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0003
Customer: Riverfront Group
Plan Name: Enterprise License
Term Months: 12
Contract Start: 2024-06-09
Contract Value: $318,339.57

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D014 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-09

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2024-06-09

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: SOF-0003

Terms
-----
Due Date: 2024-06-20

Parties
-------
Customer: Riverfront Group
Contract Ref: SOF-0003
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2024-06-20
Subtotal: $297,513.62
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $20,825.95
Total: $318,339.57

Line Items
----------
Items:
  - Description Enterprise License | Amount $71,115.44
  - Description Service coverage under contract | Amount $226,398.18

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D010 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-06-15

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2024-06-15

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Contract Start: 2024-06-15

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: SOF-0002
Customer: Blue Finch Holdings
Plan Name: Business Suite
Term Months: 12
Contract Start: 2024-06-15
Contract Value: $695,164.35

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D012 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-15

```
CUSTOMER INVOICE
================

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2024-06-15

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D012
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: SOF-0002

Terms
-----
Due Date: 2024-06-28

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: SOF-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-06-28
Subtotal: $662,061.29
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $33,103.06
Total: $695,164.35

Line Items
----------
Items:
  - Description Business Suite | Amount $239,774.99
  - Description Service coverage under contract | Amount $422,286.30

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-13

```
PAYMENT ADVICE
==============

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2024-12-13

To
--
Golden State Finance

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: $14,817.47
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-12-29

```
PAYROLL SUMMARY
===============

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2024-12-29

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 10
Gross Pay: $151,410.27
Employer Tax: 12,694.27
Cash Outflow: $164,104.54

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-02-10

```
PAYMENT ADVICE
==============

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2025-02-10

To
--
Crescent Labs

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2024-25
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: $653,263.26
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
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
Willow Distribution
90 Hill Park, Hyderabad
Document Date: 2025-03-31

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
Opening Deferred: $610,526.41
Added Deferred: $0.00
Released This Period: 610,526.41
Ending Deferred: $0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Willow Distribution
90 Hill Park, Hyderabad
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: FY 2024-25
Reference: FY 2024-25

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2024-25
Recognized Amount: $18,455.29

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D015 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Willow Distribution
90 Hill Park, Hyderabad
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D015
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0001
Subject: Scanning checklist for back-office staff
Audience: Operations Team

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
Page marker: D015
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
Willow Distribution
90 Hill Park, Hyderabad
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D017
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Document retention reminder
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
Page marker: D017
```

### Document D018 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Willow Distribution
90 Hill Park, Hyderabad
Date: 2025-03-31

Reference Box
-------------
Document ID: D018
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0117
Statement Currency: USD
Opening Balance: $696,069.94
Closing Balance: $1,488,750.76

Statement Rows
--------------
Rows:
  - Date 2024-06-09 | Description Advance collection INV-0003 | Amount $318,339.57 | Running
 Balance $1,014,409.51
  - Date 2024-12-13 | Description Supplier settlement BILL-0001 | Amount $-14,817.47 | 
Running Balance $999,592.04
  - Date 2024-12-29 | Description Payroll PAYRUN-0001 | Amount $-164,104.54 | Running 
Balance $835,487.50
  - Date 2025-02-10 | Description Customer settlement INV-0001 | Amount $653,263.26 | 
Running Balance $1,488,750.76

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D018
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 610,526.41 | D002, D003 | 2024-04-30 | subscription_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 42,736.85 | D002, D003 | 2024-04-30 | subscription_invoice_tax |
| 3 | Unearned Revenue | Service Revenue | 610,526.41 | D004, D003 | 2025-03-31 | revenue_release |
| 4 | Cash | Accounts Receivable | 653,263.26 | D005, D003 | 2025-02-10 | customer_payment |
| 5 | Utilities Expense | Accounts Payable | 14,111.88 | D006 | 2024-05-21 | hosting_bill |
| 6 | Input Tax Receivable | Accounts Payable | 705.59 | D006 | 2024-05-21 | hosting_bill_tax |
| 7 | Accounts Payable | Cash | 14,817.47 | D007, D006 | 2024-12-13 | vendor_payment |
| 8 | Salaries Expense | Cash | 151,410.27 | D008 | 2024-12-29 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 12,694.27 | D008 | 2024-12-29 | payroll_tax |
| 10 | Utilities Expense | Accrued Expenses | 18,455.29 | D009 | 2025-03-31 | expense_accrual |
| 11 | Accounts Receivable | Unearned Revenue | 662,061.29 | D011, D010, D012 | 2024-06-15 | renewal_invoice |
| 12 | Accounts Receivable | Sales Tax Payable | 33,103.06 | D011, D010, D012 | 2024-06-15 | renewal_invoice_tax |
| 13 | Cash | Unearned Revenue | 297,513.62 | D013, D014 | 2024-06-09 | subscription_cash_invoice |
| 14 | Cash | Sales Tax Payable | 20,825.95 | D013, D014 | 2024-06-09 | subscription_cash_invoice_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 1,488,750.76
- Accounts Receivable: 789,473.24
- Prepaid Insurance: 11,907.07
- Office Supplies: 7,470.61
- Input Tax Receivable: 705.59

**Liabilities**
- Accounts Payable: 38,600.34
- Accrued Expenses: 33,734.55
- Unearned Revenue: 1,126,510.13
- Sales Tax Payable: 96,665.86

**Equity**
- Retained Earnings: 538,990.77
- Share Capital: 463,805.62

**Totals:** Assets = 2,298,307.27; Liabilities = 1,295,510.88; Equity = 1,002,796.39
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
- [ ] Yes, doc_refs are correct
- [x] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes: FX remeasurement refs could be tighter.

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [x] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [x] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Small ref cleanup, content is sound.
