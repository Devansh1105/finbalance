# Verification Packet — COV_SUB_M5_0109

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** June 2024
- **Period start → end:** 2024-06-01 → 2024-06-30
- **Entity:** Cedar Property Services
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 20
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-06-01_

**Assets**
- Cash: 109,487.63
- Accounts Receivable: 7,353.05
- Prepaid Insurance: 3,164.48
- Equipment: 16,941.26
- Office Supplies: 1,126.30

**Liabilities**
- Accounts Payable: 10,275.86
- Accrued Expenses: 2,738.65
- Unearned Revenue: 27,068.82
- Loans Payable: 15,537.78

**Equity**
- Retained Earnings: 22,559.69
- Share Capital: 59,891.92


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-06-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/06/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 109.487,63
  - Section assets | Account Accounts Receivable | Amount EUR 7.353,05
  - Section assets | Account Prepaid Insurance | Amount EUR 3.164,48
  - Section assets | Account Equipment | Amount EUR 16.941,26
  - Section assets | Account Office Supplies | Amount EUR 1.126,30
  - Section liabilities | Account Accounts Payable | Amount EUR 10.275,86
  - Section liabilities | Account Accrued Expenses | Amount EUR 2.738,65
  - Section liabilities | Account Unearned Revenue | Amount EUR 27.068,82
  - Section liabilities | Account Loans Payable | Amount EUR 15.537,78
  - Section equity | Account Retained Earnings | Amount EUR 22.559,69
  - Section equity | Account Share Capital | Amount EUR 59.891,92

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D011 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-06-03

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Document Date: 03/06/2024

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Contract Start: 03/06/2024

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: ASC606-0001
Customer: Blue Finch Holdings
Plan Name: Enterprise License
Term Months: 12
Contract Start: 03/06/2024
Contract Value: EUR 431.219,12

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D012 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-03

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 03/06/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D012
Document Type: customer_invoice
Period: June 2024
Contract Ref: ASC606-0001

Terms
-----
Due Date: 14/06/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: ASC606-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 14/06/2024
Total: EUR 431.219,12

Line Items
----------
Items:
  - Description Implementation invoice line | Amount EUR 64.682,87
  - Description Platform access invoice line | Amount EUR 366.536,25

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D013 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2024-06-03

```
SSP RATE CARD / REFERENCE COPY
==============================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Document Date: 03/06/2024

Reference Box
-------------
Document ID: D013
Document Type: ssp_rate_card
Period: June 2024

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 03/06/2024
Total SSP: EUR 470.084,56

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount EUR 91.761,88
  - Obligation Platform access | Ssp Amount EUR 378.322,68

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-06-05

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 05/06/2024

To
--
Metro Edge Partners
Customer account on file

Terms
-----
Contract Start: 05/06/2024

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Metro Edge Partners
Plan Name: Annual Growth Plan
Term Months: 3
Contract Start: 05/06/2024
Contract Value: EUR 70.184,02

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-05

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 05/06/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: June 2024
Contract Ref: SOF-0001

Terms
-----
Due Date: 19/06/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: SOF-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 19/06/2024
Subtotal: EUR 64.095,00
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 6.089,02
Total: EUR 70.184,02

Line Items
----------
Items:
  - Description Team Support Plan | Amount EUR 15.902,62
  - Description Service coverage under contract | Amount EUR 48.192,38

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D014 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2024-06-06

```
IMPLEMENTATION ACCEPTANCE MEMO
==============================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Document Date: 06/06/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: implementation_acceptance_memo
Period: June 2024

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Blue Finch Holdings
Acceptance Date: 06/06/2024
Accepted Obligation: Implementation
Accepted Amount: EUR 84.175,23

Narrative
---------
Details: Customer accepted implementation. Only the implementation performance obligation is
 released on acceptance.

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D017 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-06-06

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 06/06/2024

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Contract Start: 06/06/2024

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0002
Customer: Blue Finch Holdings
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 06/06/2024
Contract Value: EUR 88.387,82

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D018 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-06

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 06/06/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_invoice
Period: June 2024
Contract Ref: SOF-0002

Terms
-----
Due Date: 24/06/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: SOF-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 24/06/2024
Subtotal: EUR 84.178,88
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 4.208,94
Total: EUR 88.387,82

Line Items
----------
Items:
  - Description Team Support Plan | Amount EUR 28.097,38
  - Description Service coverage under contract | Amount EUR 56.081,50

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-09

```
VENDOR INVOICE
==============

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 09/06/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: June 2024

Terms
-----
Due Date: 22/06/2024

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Utilities Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 22/06/2024
Subtotal: EUR 3.139,06
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 227,58
Total: EUR 3.366,64

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 783,86
  - Description Support fee | Amount EUR 2.355,20

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D009 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-17

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: EUR 19.540,01
Draw Amount: EUR 84.058,33
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 103.598,34
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-20

```
PAYMENT ADVICE
==============

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Document Date: 20/06/2024

To
--
Golden State Finance

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: June 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: EUR 2.893,45
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-21

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: EUR 66.800,43
Draw Amount: EUR 0,00
Principal Paid: EUR 17.415,42
Interest Paid: EUR 2.594,19
Ending Principal: EUR 49.385,01
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-23

```
PAYMENT ADVICE
==============

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 23/06/2024

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: June 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Metro Edge Partners
Amount: EUR 69.238,23
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-06-27

```
PAYROLL SUMMARY
===============

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 27/06/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: June 2024
Headcount: 4
Gross Pay: EUR 14.490,94
Employer Tax: 1.821,94
Cash Outflow: EUR 16.312,88

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D016 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-27

```
TRANSFER ADVICE
===============

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Document Date: 27/06/2024

Reference Box
-------------
Document ID: D016
Document Type: transfer_advice
Period: June 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: EUR 67.227,01
Transfer Date: 27/06/2024
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Document Date: 30/06/2024

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: June 2024

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: June 2024
Opening Deferred: EUR 64.095,00
Added Deferred: EUR 0,00
Released This Period: 21.365,00
Ending Deferred: EUR 42.730,00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D015 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
PERFORMANCE OBLIGATION SCHEDULE
===============================

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Document Date: 30/06/2024

Reference Box
-------------
Document ID: D015
Document Type: performance_obligation_schedule
Period: June 2024

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: EUR 431.219,12
Total SSP: EUR 470.084,56
Allocation Total: EUR 431.219,12
Released This Period: 113.095,55
Ending Deferred: EUR 318.123,57

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount EUR 91.761,88 | Invoice Line Amount EUR 64.682,87
 | Allocated Transaction Price EUR 84.175,23 | Release Pattern On acceptance | Released This
 Period 84.175,23
  - Obligation Platform access | Ssp Amount EUR 378.322,68 | Invoice Line Amount EUR 
366.536,25 | Allocated Transaction Price EUR 347.043,89 | Release Pattern Ratable over 12 
months | Released This Period 28.920,32

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D019 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Document Date: 30/06/2024

Reference Box
-------------
Document ID: D019
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0109
Statement Currency: EUR
Opening Balance: EUR 109.487,63
Closing Balance: EUR 244.729,06

Statement Rows
--------------
Rows:
  - Date 06/06/2024 | Description Advance collection INV-0003 | Amount EUR 88.387,82 | 
Running Balance EUR 197.875,45
  - Date 17/06/2024 | Description Loan draw LOAN-0001 | Amount EUR 84.058,33 | Running 
Balance EUR 281.933,78
  - Date 20/06/2024 | Description Supplier settlement BILL-0001 | Amount EUR -2.893,45 | 
Running Balance EUR 279.040,33
  - Date 21/06/2024 | Description Loan payment LOAN-0002 | Amount EUR -20.009,61 | Running 
Balance EUR 259.030,72
  - Date 23/06/2024 | Description Customer settlement INV-0001 | Amount EUR 69.238,23 | 
Running Balance EUR 328.268,95
  - Date 27/06/2024 | Description Payroll PAYRUN-0001 | Amount EUR -16.312,88 | Running 
Balance EUR 311.956,07
  - Date 27/06/2024 | Description Transfer out TRX-0001 | Amount EUR -67.227,01 | Running 
Balance EUR 244.729,06

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Cedar Property Services
90 Hill Park, Hyderabad
Date: 30/06/2024

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-0999
Statement Currency: EUR
Opening Balance: EUR 0,00
Closing Balance: EUR 67.227,01

Statement Rows
--------------
Rows:
  - Date 27/06/2024 | Description Transfer in TRX-0001 | Amount EUR 67.227,01 | Running 
Balance EUR 67.227,01

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 64,095.00 | D002, D003 | 2024-06-05 | subscription_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 6,089.02 | D002, D003 | 2024-06-05 | subscription_invoice_tax |
| 3 | Unearned Revenue | Service Revenue | 21,365.00 | D004, D003 | 2024-06-30 | revenue_release |
| 4 | Cash | Accounts Receivable | 69,238.23 | D005, D003 | 2024-06-23 | customer_payment |
| 5 | Utilities Expense | Accounts Payable | 3,139.06 | D006 | 2024-06-09 | hosting_bill |
| 6 | Input Tax Receivable | Accounts Payable | 227.58 | D006 | 2024-06-09 | hosting_bill_tax |
| 7 | Accounts Payable | Cash | 2,893.45 | D007, D006 | 2024-06-20 | vendor_payment |
| 8 | Salaries Expense | Cash | 14,490.94 | D008 | 2024-06-27 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 1,821.94 | D008 | 2024-06-27 | payroll_tax |
| 10 | Cash | Loans Payable | 84,058.33 | D009 | 2024-06-17 | loan_draw |
| 11 | Loans Payable | Cash | 17,415.42 | D010 | 2024-06-21 | loan_repayment_principal |
| 12 | Interest Expense | Cash | 2,594.19 | D010 | 2024-06-21 | loan_repayment_interest |
| 13 | Accounts Receivable | Unearned Revenue | 431,219.12 | D011, D012, D013 | 2024-06-03 | bundled_contract_allocation_invoice |
| 14 | Unearned Revenue | Service Revenue | 84,175.23 | D012, D013, D014, D015 | 2024-06-06 | bundled_contract_allocation_implementation_release |
| 15 | Unearned Revenue | Service Revenue | 28,920.32 | D012, D013, D014, D015 | 2024-06-30 | bundled_contract_allocation_platform_release |
| 16 | Reserve Cash | Cash | 67,227.01 | D016 | 2024-06-27 | interbank_transfer |
| 17 | Cash | Unearned Revenue | 84,178.88 | D017, D018 | 2024-06-06 | subscription_cash_invoice |
| 18 | Cash | Sales Tax Payable | 4,208.94 | D017, D018 | 2024-06-06 | subscription_cash_invoice_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 244,729.06
- Accounts Receivable: 439,517.96
- Prepaid Insurance: 3,164.48
- Equipment: 16,941.26
- Office Supplies: 1,126.30
- Input Tax Receivable: 227.58
- Reserve Cash: 67,227.01

**Liabilities**
- Accounts Payable: 10,749.05
- Accrued Expenses: 2,738.65
- Unearned Revenue: 472,101.27
- Loans Payable: 82,180.69
- Sales Tax Payable: 10,297.96

**Equity**
- Retained Earnings: 134,974.11
- Share Capital: 59,891.92

**Totals:** Assets = 772,933.65; Liabilities = 578,067.62; Equity = 194,866.03
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
- Notes: Ties out, accept.
