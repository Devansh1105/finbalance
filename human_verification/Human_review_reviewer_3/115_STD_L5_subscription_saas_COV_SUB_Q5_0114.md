# Verification Packet — COV_SUB_Q5_0114

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q2 FY 2025-26
- **Period start → end:** 2025-07-01 → 2025-09-30
- **Entity:** Granite Retail Group
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 25
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-07-01_

**Assets**
- Cash: 379,864.98
- Accounts Receivable: 45,048.93
- Prepaid Insurance: 8,900.95
- Equipment: 34,633.84
- Office Supplies: 8,563.15

**Liabilities**
- Accounts Payable: 19,824.77
- Accrued Expenses: 13,604.72
- Unearned Revenue: 56,934.63
- Loans Payable: 26,559.56

**Equity**
- Retained Earnings: 64,714.36
- Share Capital: 295,373.81


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-07-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-07-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $379,864.98
  - Section assets | Account Accounts Receivable | Amount $45,048.93
  - Section assets | Account Prepaid Insurance | Amount $8,900.95
  - Section assets | Account Equipment | Amount $34,633.84
  - Section assets | Account Office Supplies | Amount $8,563.15
  - Section liabilities | Account Accounts Payable | Amount $19,824.77
  - Section liabilities | Account Accrued Expenses | Amount $13,604.72
  - Section liabilities | Account Unearned Revenue | Amount $56,934.63
  - Section liabilities | Account Loans Payable | Amount $26,559.56
  - Section equity | Account Retained Earnings | Amount $64,714.36
  - Section equity | Account Share Capital | Amount $295,373.81

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-07-10

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-07-10

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 2025-07-10

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Riverfront Group
Plan Name: Annual Growth Plan
Term Months: 3
Contract Start: 2025-07-10
Contract Value: $72,173.25

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-10

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-07-10

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q2 FY 2025-26
Contract Ref: SOF-0001

Terms
-----
Due Date: 2025-07-18

Parties
-------
Customer: Riverfront Group
Contract Ref: SOF-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-07-18
Total: $72,173.25

Line Items
----------
Items:
  - Description Business Suite | Amount $28,804.14
  - Description Service coverage under contract | Amount $43,369.11

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D021 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-12

```
VENDOR INVOICE
==============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-07-12

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D021
Document Type: vendor_invoice
Period: Q2 FY 2025-26

Terms
-----
Due Date: 2025-08-05

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Utilities Expense
Currency: EUR

Bill Details
------------
Invoice Number: FXBILL-0001
Due Date: 2025-08-05
Total: EUR 48.366,46

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 11.456,99
  - Description Foreign-currency support | Amount EUR 36.909,47

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D022 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2025-07-12

```
EXCHANGE RATE NOTICE
====================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-07-12

Reference Box
-------------
Document ID: D022
Document Type: exchange_rate_notice
Period: Q2 FY 2025-26
Reference: FXBILL-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXBILL-0001
Rate Date: 2025-07-12
Rate Type: Spot rate at bill date

Conversion Details
------------------
Source Currency: EUR
Source Amount: EUR 48.366,46
Functional Currency: USD
Exchange Rate: 1.0570
Functional Amount: $51,123.35

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D011 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-07-17

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-07-17

To
--
Crescent Labs
Customer account on file

Terms
-----
Contract Start: 2025-07-17

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: ASC606-0001
Customer: Crescent Labs
Plan Name: Enterprise License
Term Months: 12
Contract Start: 2025-07-17
Contract Value: $1,245,077.29

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D012 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-17

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-07-17

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D012
Document Type: customer_invoice
Period: Q2 FY 2025-26
Contract Ref: ASC606-0001

Terms
-----
Due Date: 2025-08-04

Parties
-------
Customer: Crescent Labs
Contract Ref: ASC606-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-08-04
Total: $1,245,077.29

Line Items
----------
Items:
  - Description Implementation invoice line | Amount $186,761.59
  - Description Platform access invoice line | Amount $1,058,315.70

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D013 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2025-07-17

```
SSP RATE CARD
=============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-07-17

Reference Box
-------------
Document ID: D013
Document Type: ssp_rate_card
Period: Q2 FY 2025-26

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 2025-07-17
Total SSP: $1,412,703.81

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount $361,954.32
  - Obligation Platform access | Ssp Amount $1,050,749.49

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-24

```
VENDOR INVOICE
==============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-07-24

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: Q2 FY 2025-26

Terms
-----
Due Date: 2025-08-12

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Utilities Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-08-12
Total: $11,763.33

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $4,028.36
  - Description Support fee | Amount $7,734.97

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D014 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2025-07-26

```
IMPLEMENTATION ACCEPTANCE MEMO / REFERENCE COPY
===============================================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-07-26

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D014
Document Type: implementation_acceptance_memo
Period: Q2 FY 2025-26

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Crescent Labs
Acceptance Date: 2025-07-26
Accepted Obligation: Implementation
Accepted Amount: $319,006.08

Narrative
---------
Details: Customer accepted implementation. Only the implementation performance obligation is
 released on acceptance.

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D009 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-08-07

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $34,453.71
Draw Amount: $251,735.50
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $286,189.21
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-31

```
PAYMENT ADVICE
==============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-08-31

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q2 FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: $11,211.15
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D018 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `posting_doc`
- **Date:** 2025-09-02

```
CREDIT MEMO
===========

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-09-02

To
--
Riverfront Group

Reference Box
-------------
Document ID: D018
Document Type: credit_memo
Period: Q2 FY 2025-26
Reference: INV-0001

Approval / Context
------------------
Reason: Contract revision

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Riverfront Group
Currency: USD
Reference: INV-0001
Reason: Contract revision
Amount: $4,509.64

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-09-11

```
PAYMENT ADVICE
==============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-09-11

To
--
Riverfront Group

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q2 FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: $48,968.90
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D016 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-09-14

```
TRANSFER ADVICE
===============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-09-14

Reference Box
-------------
Document ID: D016
Document Type: transfer_advice
Period: Q2 FY 2025-26
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $396,981.76
Transfer Date: 2025-09-14
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-09-16

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: $328,793.65
Draw Amount: $0.00
Principal Paid: $83,379.61
Interest Paid: $7,499.17
Ending Principal: $245,414.04
Note: Scheduled lender activity for the selected period.
```

### Document D023 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `posting_doc`
- **Date:** 2025-09-17

```
PAYMENT ADVICE
==============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-09-17

To
--
Golden State Finance

Reference Box
-------------
Document ID: D023
Document Type: payment_advice
Period: Q2 FY 2025-26
Reference: FXBILL-0001

Payment Details
---------------
Advice Number: FXPAY-0001
Counterparty: Golden State Finance
Currency: USD
Amount: $50,175.37
Reference: FXBILL-0001
Payment Method: Wire
Payment For: Foreign-currency payable settlement

Foreign Currency Details
------------------------
Source Amount: EUR 48.366,46
Source Currency: EUR
Functional Currency: USD
Functional Amount: $50,175.37
Exchange Rate: 1.0374
FX Difference: 947.98

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-09-20

```
PAYROLL SUMMARY
===============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-09-20

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q2 FY 2025-26
Headcount: 11
Gross Pay: $108,453.28
Employer Tax: 14,965.32
Cash Outflow: $123,418.60

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-09-30

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-09-30

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: Q2 FY 2025-26

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: Q2 FY 2025-26
Opening Deferred: $72,173.25
Added Deferred: $0.00
Released This Period: 72,173.25
Ending Deferred: $0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D015 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-09-30

```
PERFORMANCE OBLIGATION SCHEDULE / REFERENCE COPY
================================================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-09-30

Reference Box
-------------
Document ID: D015
Document Type: performance_obligation_schedule
Period: Q2 FY 2025-26

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: $1,245,077.29
Total SSP: $1,412,703.81
Allocation Total: $1,245,077.29
Released This Period: 550,523.88
Ending Deferred: $694,553.41

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount $361,954.32 | Invoice Line Amount $186,761.59 | 
Allocated Transaction Price $319,006.08 | Release Pattern On acceptance | Released This 
Period 319,006.08
  - Obligation Platform access | Ssp Amount $1,050,749.49 | Invoice Line Amount 
$1,058,315.70 | Allocated Transaction Price $926,071.21 | Release Pattern Ratable over 12 
months | Released This Period 231,517.80

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D017 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-09-30

```
SERVICE PERIOD MEMO
===================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-09-30

Reference Box
-------------
Document ID: D017
Document Type: service_period_memo
Period: Q2 FY 2025-26
Reference: Q2 FY 2025-26

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q2 FY 2025-26
Recognized Amount: $16,690.69

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D019 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2025-09-30

```
AR AGING SUMMARY
================

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Document Date: 2025-09-30

Reference Box
-------------
Document ID: D019
Document Type: ar_aging_summary
Period: Q2 FY 2025-26

Aging Summary
-------------
Summary ID: AGING-0001
Period: Q2 FY 2025-26
Total Open: $18,694.71

Customer Lines
--------------
Lines:
  - Customer Riverfront Group | Reference INV-0001 | Current $12,556.95 | Past Due 6,137.76

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D020 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-09-30

```
CREDIT MEMO
===========

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-09-30

To
--
Riverfront Group

Reference Box
-------------
Document ID: D020
Document Type: credit_memo
Period: Q2 FY 2025-26
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0002
Counterparty: Riverfront Group
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: $6,137.76

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D024 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-09-30

```
BANK STATEMENT
==============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-09-30

Reference Box
-------------
Document ID: D024
Document Type: bank_statement
Period: Q2 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0114
Statement Currency: USD
Opening Balance: $379,864.98
Closing Balance: $7,903.72

Statement Rows
--------------
Rows:
  - Date 2025-08-07 | Description Loan draw LOAN-0001 | Amount $251,735.50 | Running Balance
 $631,600.48
  - Date 2025-08-31 | Description Supplier settlement BILL-0001 | Amount $-11,211.15 | 
Running Balance $620,389.33
  - Date 2025-09-11 | Description Customer settlement INV-0001 | Amount $48,968.90 | Running
 Balance $669,358.23
  - Date 2025-09-14 | Description Transfer out TRX-0001 | Amount $-396,981.76 | Running 
Balance $272,376.47
  - Date 2025-09-16 | Description Loan payment LOAN-0002 | Amount $-90,878.78 | Running 
Balance $181,497.69
  - Date 2025-09-17 | Description Foreign payment FXBILL-0001 | Amount $-50,175.37 | Running
 Balance $131,322.32
  - Date 2025-09-20 | Description Payroll PAYRUN-0001 | Amount $-123,418.60 | Running 
Balance $7,903.72

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D025 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-09-30

```
BANK STATEMENT
==============

From
----
Granite Retail Group
220 Lake View Road, Bengaluru
Date: 2025-09-30

Reference Box
-------------
Document ID: D025
Document Type: bank_statement
Period: Q2 FY 2025-26

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-1499
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $396,981.76

Statement Rows
--------------
Rows:
  - Date 2025-09-14 | Description Transfer in TRX-0001 | Amount $396,981.76 | Running 
Balance $396,981.76

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D025
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 72,173.25 | D002, D003 | 2025-07-10 | subscription_invoice |
| 2 | Unearned Revenue | Service Revenue | 72,173.25 | D004, D003 | 2025-09-30 | revenue_release |
| 3 | Cash | Accounts Receivable | 48,968.90 | D005, D003 | 2025-09-11 | customer_payment |
| 4 | Utilities Expense | Accounts Payable | 11,763.33 | D006 | 2025-07-24 | hosting_bill |
| 5 | Accounts Payable | Cash | 11,211.15 | D007, D006 | 2025-08-31 | vendor_payment |
| 6 | Salaries Expense | Cash | 108,453.28 | D008 | 2025-09-20 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 14,965.32 | D008 | 2025-09-20 | payroll_tax |
| 8 | Cash | Loans Payable | 251,735.50 | D009 | 2025-08-07 | loan_draw |
| 9 | Loans Payable | Cash | 83,379.61 | D010 | 2025-09-16 | loan_repayment_principal |
| 10 | Interest Expense | Cash | 7,499.17 | D010 | 2025-09-16 | loan_repayment_interest |
| 11 | Accounts Receivable | Unearned Revenue | 1,245,077.29 | D011, D012, D013 | 2025-07-17 | bundled_contract_allocation_invoice |
| 12 | Unearned Revenue | Service Revenue | 319,006.08 | D012, D013, D014, D015 | 2025-07-26 | bundled_contract_allocation_implementation_release |
| 13 | Unearned Revenue | Service Revenue | 231,517.80 | D012, D013, D014, D015 | 2025-09-30 | bundled_contract_allocation_platform_release |
| 14 | Reserve Cash | Cash | 396,981.76 | D016 | 2025-09-14 | interbank_transfer |
| 15 | Utilities Expense | Accrued Expenses | 16,690.69 | D017 | 2025-09-30 | expense_accrual |
| 16 | Service Revenue | Accounts Receivable | 4,509.64 | D003, D018 | 2025-09-02 | credit_memo |
| 17 | Bad Debt Expense | Accounts Receivable | 6,137.76 | D019, D020, D003 | 2025-09-30 | bad_debt_review |
| 18 | Utilities Expense | Accounts Payable | 51,123.35 | D021, D022 | 2025-07-12 | fx_hosting_bill |
| 19 | Accounts Payable | Cash | 50,175.37 | D023, D021 | 2025-09-17 | fx_vendor_payment |
| 20 | Accounts Payable | Foreign Exchange Gain | 947.98 | D023, D021 | 2025-09-17 | fx_vendor_payment_gain |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 7,903.72
- Accounts Receivable: 1,302,683.17
- Prepaid Insurance: 8,900.95
- Equipment: 34,633.84
- Office Supplies: 8,563.15
- Reserve Cash: 396,981.76

**Liabilities**
- Accounts Payable: 20,376.95
- Accrued Expenses: 30,295.41
- Unearned Revenue: 751,488.04
- Loans Payable: 194,915.45

**Equity**
- Retained Earnings: 467,216.93
- Share Capital: 295,373.81

**Totals:** Assets = 1,759,666.59; Liabilities = 997,075.85; Equity = 762,590.74
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
- Notes: Fine as ground truth.
