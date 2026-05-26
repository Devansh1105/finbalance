# Verification Packet — COV_SUB_Y2_0116

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 2
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Atlas Operations
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 15
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 478,349.41
- Accounts Receivable: 76,451.93
- Prepaid Insurance: 12,058.62
- Office Supplies: 4,219.53

**Liabilities**
- Accounts Payable: 46,228.85
- Accrued Expenses: 17,424.33
- Unearned Revenue: 154,009.15

**Equity**
- Retained Earnings: 131,546.18
- Share Capital: 221,870.98


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
  - Section assets | Account Cash | Amount GBP 478,349.41
  - Section assets | Account Accounts Receivable | Amount GBP 76,451.93
  - Section assets | Account Prepaid Insurance | Amount GBP 12,058.62
  - Section assets | Account Office Supplies | Amount GBP 4,219.53
  - Section liabilities | Account Accounts Payable | Amount GBP 46,228.85
  - Section liabilities | Account Accrued Expenses | Amount GBP 17,424.33
  - Section liabilities | Account Unearned Revenue | Amount GBP 154,009.15
  - Section equity | Account Retained Earnings | Amount GBP 131,546.18
  - Section equity | Account Share Capital | Amount GBP 221,870.98

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-01

```
VENDOR INVOICE
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 01/02/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 19/02/2024

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Utilities Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 19/02/2024
Subtotal: GBP 51,811.68
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 10,362.34
Total: GBP 62,174.02

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount GBP 14,583.68
  - Description Support fee | Amount GBP 37,228.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D013 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-02-01

```
SECONDARY COPY
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 01/02/2024

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D013
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: BILL-0001
Counterparty: Meridian Support LLP
Total: GBP 62,174.02
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D009 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2024-02-05

```
RENEWAL NOTICE
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 05/02/2024

To
--
Riverfront Group
Customer account on file

Terms
-----
Renewal Start: 20/02/2024

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Riverfront Group
Contract Reference: SOF-0002
Renewal Start: 20/02/2024
Renewal Amount: GBP 606,863.09

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D011 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-02-08

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 08/02/2024

To
--
Metro Edge Partners
Customer account on file

Terms
-----
Contract Start: 08/02/2024

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: SOF-0003
Customer: Metro Edge Partners
Plan Name: Business Suite
Term Months: 12
Contract Start: 08/02/2024
Contract Value: GBP 376,142.54

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D012 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-08

```
CUSTOMER INVOICE
================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 08/02/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D012
Document Type: customer_invoice
Period: FY 2024
Contract Ref: SOF-0003

Terms
-----
Due Date: 24/02/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: SOF-0003
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 24/02/2024
Subtotal: GBP 313,452.12
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 62,690.42
Total: GBP 376,142.54

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount GBP 96,901.89
  - Description Service coverage under contract | Amount GBP 216,550.23

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D008 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-02-20

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 20/02/2024

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 20/02/2024

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: SOF-0002
Customer: Riverfront Group
Plan Name: Business Suite
Term Months: 12
Contract Start: 20/02/2024
Contract Value: GBP 606,863.09

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D010 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-20

```
CUSTOMER INVOICE
================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 20/02/2024

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D010
Document Type: customer_invoice
Period: FY 2024
Contract Ref: SOF-0002

Terms
-----
Due Date: 08/03/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: SOF-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 08/03/2024
Subtotal: GBP 539,433.86
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: GBP 67,429.23
Total: GBP 606,863.09

Line Items
----------
Items:
  - Description Enterprise License | Amount GBP 164,507.33
  - Description Service coverage under contract | Amount GBP 374,926.53

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-03-08

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 08/03/2024

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 08/03/2024

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Riverfront Group
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 08/03/2024
Contract Value: GBP 537,209.22

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-08

```
CUSTOMER INVOICE
================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 08/03/2024

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2024
Contract Ref: SOF-0001

Terms
-----
Due Date: 17/03/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: SOF-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 17/03/2024
Subtotal: GBP 447,674.35
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 89,534.87
Total: GBP 537,209.22

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount GBP 182,534.98
  - Description Service coverage under contract | Amount GBP 265,139.37

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-14

```
PAYMENT ADVICE
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 14/10/2024

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: GBP 62,174.02
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-19

```
PAYMENT ADVICE
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 19/11/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: GBP 537,209.22
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Atlas Operations
90 Hill Park, Hyderabad
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: FY 2024

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: FY 2024
Opening Deferred: GBP 447,674.35
Added Deferred: GBP 0.00
Released This Period: 447,674.35
Ending Deferred: GBP 0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D014 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 31/12/2024

Reference Box
-------------
Document ID: D014
Document Type: memo
Period: FY 2024

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
Narrative: The packet may include supporting correspondence gathered during the close 
review.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D015 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Atlas Operations
90 Hill Park, Hyderabad
Date: 31/12/2024

Reference Box
-------------
Document ID: D015
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0116
Statement Currency: GBP
Opening Balance: GBP 478,349.41
Closing Balance: GBP 1,329,527.15

Statement Rows
--------------
Rows:
  - Date 08/02/2024 | Description Advance collection INV-0003 | Amount GBP 376,142.54 | 
Running Balance GBP 854,491.95
  - Date 14/10/2024 | Description Supplier settlement BILL-0001 | Amount GBP -62,174.02 | 
Running Balance GBP 792,317.93
  - Date 19/11/2024 | Description Customer settlement INV-0001 | Amount GBP 537,209.22 | 
Running Balance GBP 1,329,527.15

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D015
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 447,674.35 | D002, D003 | 2024-03-08 | subscription_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 89,534.87 | D002, D003 | 2024-03-08 | subscription_invoice_tax |
| 3 | Unearned Revenue | Service Revenue | 447,674.35 | D004, D003 | 2024-12-31 | revenue_release |
| 4 | Cash | Accounts Receivable | 537,209.22 | D005, D003 | 2024-11-19 | customer_payment |
| 5 | Utilities Expense | Accounts Payable | 51,811.68 | D006 | 2024-02-01 | hosting_bill |
| 6 | Input Tax Receivable | Accounts Payable | 10,362.34 | D006 | 2024-02-01 | hosting_bill_tax |
| 7 | Accounts Payable | Cash | 62,174.02 | D007, D006 | 2024-10-14 | vendor_payment |
| 8 | Accounts Receivable | Unearned Revenue | 539,433.86 | D009, D008, D010 | 2024-02-20 | renewal_invoice |
| 9 | Accounts Receivable | Sales Tax Payable | 67,429.23 | D009, D008, D010 | 2024-02-20 | renewal_invoice_tax |
| 10 | Cash | Unearned Revenue | 313,452.12 | D011, D012 | 2024-02-08 | subscription_cash_invoice |
| 11 | Cash | Sales Tax Payable | 62,690.42 | D011, D012 | 2024-02-08 | subscription_cash_invoice_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 1,329,527.15
- Accounts Receivable: 683,315.02
- Prepaid Insurance: 12,058.62
- Office Supplies: 4,219.53
- Input Tax Receivable: 10,362.34

**Liabilities**
- Accounts Payable: 46,228.85
- Accrued Expenses: 17,424.33
- Unearned Revenue: 1,006,895.13
- Sales Tax Payable: 219,654.52

**Equity**
- Retained Earnings: 527,408.85
- Share Capital: 221,870.98

**Totals:** Assets = 2,039,482.66; Liabilities = 1,290,202.83; Equity = 749,279.83
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
- Notes: Support maps cleanly to the postings.
