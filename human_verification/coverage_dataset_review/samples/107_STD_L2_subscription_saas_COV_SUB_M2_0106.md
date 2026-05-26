# Verification Packet — COV_SUB_M2_0106

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** November 2024
- **Period start → end:** 2024-11-01 → 2024-11-30
- **Entity:** Beacon Property Services
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 8
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-11-01_

**Assets**
- Cash: 52,489.36
- Accounts Receivable: 12,480.58
- Prepaid Insurance: 2,641.52
- Office Supplies: 815.25

**Liabilities**
- Accounts Payable: 5,807.96
- Accrued Expenses: 2,827.95
- Unearned Revenue: 11,450.06

**Equity**
- Retained Earnings: 10,654.58
- Share Capital: 37,686.16


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-11-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/11/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 52.489,36
  - Section assets | Account Accounts Receivable | Amount EUR 12.480,58
  - Section assets | Account Prepaid Insurance | Amount EUR 2.641,52
  - Section assets | Account Office Supplies | Amount EUR 815,25
  - Section liabilities | Account Accounts Payable | Amount EUR 5.807,96
  - Section liabilities | Account Accrued Expenses | Amount EUR 2.827,95
  - Section liabilities | Account Unearned Revenue | Amount EUR 11.450,06
  - Section equity | Account Retained Earnings | Amount EUR 10.654,58
  - Section equity | Account Share Capital | Amount EUR 37.686,16

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-11-04

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Property Services
18 Marina Avenue, Chennai
Date: 04/11/2024

To
--
Aster Point Services
Customer account on file

Terms
-----
Contract Start: 04/11/2024

Approval / Context
------------------
Plan Name: Team Support Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Aster Point Services
Plan Name: Team Support Plan
Term Months: 3
Contract Start: 04/11/2024
Contract Value: EUR 97.128,17

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-04

```
CUSTOMER INVOICE
================

From
----
Beacon Property Services
18 Marina Avenue, Chennai
Document Date: 04/11/2024

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: November 2024
Contract Ref: SOF-0001

Terms
-----
Due Date: 22/11/2024

Parties
-------
Customer: Aster Point Services
Contract Ref: SOF-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 22/11/2024
Subtotal: EUR 90.562,40
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 6.565,77
Total: EUR 97.128,17

Line Items
----------
Items:
  - Description Team Support Plan | Amount EUR 32.359,24
  - Description Service coverage under contract | Amount EUR 58.203,16

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-07

```
VENDOR INVOICE
==============

From
----
Beacon Property Services
18 Marina Avenue, Chennai
Date: 07/11/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: November 2024

Terms
-----
Due Date: 26/11/2024

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Utilities Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 26/11/2024
Subtotal: EUR 15.536,13
Tax Label: US Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 1.475,93
Total: EUR 17.012,06

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 5.825,82
  - Description Support fee | Amount EUR 9.710,31

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-22

```
PAYMENT ADVICE
==============

From
----
Beacon Property Services
18 Marina Avenue, Chennai
Date: 22/11/2024

To
--
Aster Point Services

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: November 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: EUR 97.128,17
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-22

```
PAYMENT ADVICE
==============

From
----
Beacon Property Services
18 Marina Avenue, Chennai
Date: 22/11/2024

To
--
Golden State Finance

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: November 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: EUR 17.012,06
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-11-30

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Beacon Property Services
18 Marina Avenue, Chennai
Date: 30/11/2024

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: November 2024

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: November 2024
Opening Deferred: EUR 90.562,40
Added Deferred: EUR 0,00
Released This Period: 30.187,47
Ending Deferred: EUR 60.374,93

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D008 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-11-30

```
BANK STATEMENT
==============

From
----
Beacon Property Services
18 Marina Avenue, Chennai
Document Date: 30/11/2024

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: November 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0106
Statement Currency: EUR
Opening Balance: EUR 52.489,36
Closing Balance: EUR 132.605,47

Statement Rows
--------------
Rows:
  - Date 22/11/2024 | Description Customer settlement INV-0001 | Amount EUR 97.128,17 | 
Running Balance EUR 149.617,53
  - Date 22/11/2024 | Description Supplier settlement BILL-0001 | Amount EUR -17.012,06 | 
Running Balance EUR 132.605,47

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
| 1 | Accounts Receivable | Unearned Revenue | 90,562.40 | D002, D003 | 2024-11-04 | subscription_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 6,565.77 | D002, D003 | 2024-11-04 | subscription_invoice_tax |
| 3 | Unearned Revenue | Service Revenue | 30,187.47 | D004, D003 | 2024-11-30 | revenue_release |
| 4 | Cash | Accounts Receivable | 97,128.17 | D005, D003 | 2024-11-22 | customer_payment |
| 5 | Utilities Expense | Accounts Payable | 15,536.13 | D006 | 2024-11-07 | hosting_bill |
| 6 | Input Tax Receivable | Accounts Payable | 1,475.93 | D006 | 2024-11-07 | hosting_bill_tax |
| 7 | Accounts Payable | Cash | 17,012.06 | D007, D006 | 2024-11-22 | vendor_payment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 132,605.47
- Accounts Receivable: 12,480.58
- Prepaid Insurance: 2,641.52
- Office Supplies: 815.25
- Input Tax Receivable: 1,475.93

**Liabilities**
- Accounts Payable: 5,807.96
- Accrued Expenses: 2,827.95
- Unearned Revenue: 71,824.99
- Sales Tax Payable: 6,565.77

**Equity**
- Retained Earnings: 25,305.92
- Share Capital: 37,686.16

**Totals:** Assets = 150,018.75; Liabilities = 87,026.67; Equity = 62,992.08
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
