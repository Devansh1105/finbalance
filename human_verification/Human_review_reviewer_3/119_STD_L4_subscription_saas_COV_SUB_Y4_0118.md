# Verification Packet — COV_SUB_Y4_0118

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 4
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Beacon Retail Group
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 29
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 972,814.89
- Accounts Receivable: 130,026.21
- Prepaid Insurance: 25,479.50
- Equipment: 171,894.56
- Office Supplies: 8,934.27

**Liabilities**
- Accounts Payable: 80,268.08
- Accrued Expenses: 17,213.67
- Unearned Revenue: 286,505.73
- Loans Payable: 101,011.30

**Equity**
- Retained Earnings: 194,840.99
- Share Capital: 629,309.66


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
  - Section assets | Account Cash | Amount EUR 972.814,89
  - Section assets | Account Accounts Receivable | Amount EUR 130.026,21
  - Section assets | Account Prepaid Insurance | Amount EUR 25.479,50
  - Section assets | Account Equipment | Amount EUR 171.894,56
  - Section assets | Account Office Supplies | Amount EUR 8.934,27
  - Section liabilities | Account Accounts Payable | Amount EUR 80.268,08
  - Section liabilities | Account Accrued Expenses | Amount EUR 17.213,67
  - Section liabilities | Account Unearned Revenue | Amount EUR 286.505,73
  - Section liabilities | Account Loans Payable | Amount EUR 101.011,30
  - Section equity | Account Retained Earnings | Amount EUR 194.840,99
  - Section equity | Account Share Capital | Amount EUR 629.309,66

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D021 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2025-01-27

```
RENEWAL NOTICE
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 27/01/2025

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Renewal Start: 11/02/2025

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Oak Harbor Foods
Contract Reference: SOF-0003
Renewal Start: 11/02/2025
Renewal Amount: EUR 791.286,85

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D018 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-02-01

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 01/02/2025

To
--
Maple Ridge Trading
Customer account on file

Terms
-----
Contract Start: 01/02/2025

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0002
Customer: Maple Ridge Trading
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 01/02/2025
Contract Value: EUR 773.658,69

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-01

```
CUSTOMER INVOICE
================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 01/02/2025

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: FY 2025
Contract Ref: SOF-0002

Terms
-----
Due Date: 09/02/2025

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: SOF-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 09/02/2025
Subtotal: EUR 721.360,08
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 52.298,61
Total: EUR 773.658,69

Line Items
----------
Items:
  - Description Business Suite | Amount EUR 226.715,48
  - Description Service coverage under contract | Amount EUR 494.644,60

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-02-11

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 11/02/2025

To
--
Maple Ridge Trading
Customer account on file

Terms
-----
Contract Start: 11/02/2025

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: SOF-0001
Customer: Maple Ridge Trading
Plan Name: Business Suite
Term Months: 12
Contract Start: 11/02/2025
Contract Value: EUR 814.230,49

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-11

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 11/02/2025

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2025
Contract Ref: SOF-0001

Terms
-----
Due Date: 20/02/2025

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: SOF-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 20/02/2025
Subtotal: EUR 766.334,58
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 47.895,91
Total: EUR 814.230,49

Line Items
----------
Items:
  - Description Business Suite | Amount EUR 232.068,25
  - Description Service coverage under contract | Amount EUR 534.266,33

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D020 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-02-11

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 11/02/2025

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Contract Start: 11/02/2025

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0003
Customer: Oak Harbor Foods
Plan Name: Enterprise License
Term Months: 12
Contract Start: 11/02/2025
Contract Value: EUR 791.286,85

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D022 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-11

```
CUSTOMER INVOICE
================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 11/02/2025

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D022
Document Type: customer_invoice
Period: FY 2025
Contract Ref: SOF-0003

Terms
-----
Due Date: 26/02/2025

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: SOF-0003
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 26/02/2025
Subtotal: EUR 737.796,60
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 53.490,25
Total: EUR 791.286,85

Line Items
----------
Items:
  - Description Team Support Plan | Amount EUR 219.382,21
  - Description Service coverage under contract | Amount EUR 518.414,39

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D024 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-02-11

```
CANCELLATION NOTE
=================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 11/02/2025

Reference Box
-------------
Document ID: D024
Document Type: cancellation_note
Period: FY 2025

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D010 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2025-03-28

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 28/03/2025

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 28/03/2025

Approval / Context
------------------
Plan Name: Business Suite

Order Summary
-------------
Form Number: ASC606-0001
Customer: Riverfront Group
Plan Name: Business Suite
Term Months: 12
Contract Start: 28/03/2025
Contract Value: EUR 2.167.896,95

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-28

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 28/03/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: FY 2025
Contract Ref: ASC606-0001

Terms
-----
Due Date: 06/04/2025

Parties
-------
Customer: Riverfront Group
Contract Ref: ASC606-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 06/04/2025
Total: EUR 2.167.896,95

Line Items
----------
Items:
  - Description Implementation invoice line | Amount EUR 325.184,54
  - Description Platform access invoice line | Amount EUR 1.842.712,41

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D012 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2025-03-28

```
SSP RATE CARD / REFERENCE COPY
==============================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 28/03/2025

Reference Box
-------------
Document ID: D012
Document Type: ssp_rate_card
Period: FY 2025

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 28/03/2025
Total SSP: EUR 2.391.061,81

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount EUR 711.809,05
  - Obligation Platform access | Ssp Amount EUR 1.679.252,76

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D027 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-03-28

```
SECONDARY COPY
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 28/03/2025

To
--
Riverfront Group

Reference Box
-------------
Document ID: D027
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0002
Counterparty: Riverfront Group
Total: EUR 2.167.896,95
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D027
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-03

```
VENDOR INVOICE
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 03/04/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: FY 2025

Terms
-----
Due Date: 13/04/2025

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Utilities Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 13/04/2025
Subtotal: EUR 73.302,41
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 5.314,42
Total: EUR 78.616,83

Bill Lines
----------
Lines:
  - Description Support package | Amount EUR 27.644,20
  - Description Support fee | Amount EUR 45.658,21

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D013 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2025-04-11

```
IMPLEMENTATION ACCEPTANCE MEMO / REFERENCE COPY
===============================================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 11/04/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: implementation_acceptance_memo
Period: FY 2025

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Riverfront Group
Acceptance Date: 11/04/2025
Accepted Obligation: Implementation
Accepted Amount: EUR 645.373,81

Narrative
---------
Details: Customer accepted implementation. Only the implementation performance obligation is
 released on acceptance.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D009 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-05-28

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: EUR 138.308,99
Draw Amount: EUR 643.591,27
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 781.900,26
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-09-05

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 05/09/2025

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Maple Ridge Trading
Amount: EUR 700.156,24
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D017 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `posting_doc`
- **Date:** 2025-09-08

```
CREDIT MEMO
===========

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 08/09/2025

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D017
Document Type: credit_memo
Period: FY 2025
Reference: INV-0001

Approval / Context
------------------
Reason: Pricing adjustment

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Maple Ridge Trading
Currency: EUR
Reference: INV-0001
Reason: Pricing adjustment
Amount: EUR 14.612,39

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D015 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-10-03

```
TRANSFER ADVICE
===============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 03/10/2025

Reference Box
-------------
Document ID: D015
Document Type: transfer_advice
Period: FY 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: EUR 898.241,40
Transfer Date: 03/10/2025
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-10-12

```
PAYROLL SUMMARY
===============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 12/10/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025
Headcount: 12
Gross Pay: EUR 187.725,20
Employer Tax: 20.966,71
Cash Outflow: EUR 208.691,91

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-01

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 01/11/2025

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: EUR 71.809,43
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D004 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D004
Document Type: revenue_recognition_schedule
Period: FY 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0001
Period: FY 2025
Opening Deferred: EUR 766.334,58
Added Deferred: EUR 0,00
Released This Period: 766.334,58
Ending Deferred: EUR 0,00

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D014 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
PERFORMANCE OBLIGATION SCHEDULE
===============================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D014
Document Type: performance_obligation_schedule
Period: FY 2025

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: EUR 2.167.896,95
Total SSP: EUR 2.391.061,81
Allocation Total: EUR 2.167.896,95
Released This Period: 2.167.896,95
Ending Deferred: EUR 0,00

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount EUR 711.809,05 | Invoice Line Amount EUR 
325.184,54 | Allocated Transaction Price EUR 645.373,81 | Release Pattern On acceptance | 
Released This Period 645.373,81
  - Obligation Platform access | Ssp Amount EUR 1.679.252,76 | Invoice Line Amount EUR 
1.842.712,41 | Allocated Transaction Price EUR 1.522.523,14 | Release Pattern Ratable over 
12 months | Released This Period 1.522.523,14

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D016 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D016
Document Type: service_period_memo
Period: FY 2025
Reference: FY 2025

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2025
Recognized Amount: EUR 39.623,26

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D023 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 31/12/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D023
Document Type: vendor_statement
Period: FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Prime Utility Desk
Closing Balance: EUR 6.807,40

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount EUR 6.807,40 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D025 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D025
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
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
Generated for synthetic accounting research use.
Page marker: D025
```

### Document D026 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D026
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0002
Subject: Scanning checklist for back-office staff
Audience: Finance Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D028 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D028
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0118
Statement Currency: EUR
Opening Balance: EUR 972.814,89
Closing Balance: EUR 1.911.478,35

Statement Rows
--------------
Rows:
  - Date 01/02/2025 | Description Advance collection INV-0003 | Amount EUR 773.658,69 | 
Running Balance EUR 1.746.473,58
  - Date 28/05/2025 | Description Loan draw LOAN-0001 | Amount EUR 643.591,27 | Running 
Balance EUR 2.390.064,85
  - Date 05/09/2025 | Description Customer settlement INV-0001 | Amount EUR 700.156,24 | 
Running Balance EUR 3.090.221,09
  - Date 03/10/2025 | Description Transfer out TRX-0001 | Amount EUR -898.241,40 | Running 
Balance EUR 2.191.979,69
  - Date 12/10/2025 | Description Payroll PAYRUN-0001 | Amount EUR -208.691,91 | Running 
Balance EUR 1.983.287,78
  - Date 01/11/2025 | Description Supplier settlement BILL-0001 | Amount EUR -71.809,43 | 
Running Balance EUR 1.911.478,35

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D029 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Beacon Retail Group
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D029
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-1899
Statement Currency: EUR
Opening Balance: EUR 0,00
Closing Balance: EUR 898.241,40

Statement Rows
--------------
Rows:
  - Date 03/10/2025 | Description Transfer in TRX-0001 | Amount EUR 898.241,40 | Running 
Balance EUR 898.241,40

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 766,334.58 | D002, D003 | 2025-02-11 | subscription_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 47,895.91 | D002, D003 | 2025-02-11 | subscription_invoice_tax |
| 3 | Unearned Revenue | Service Revenue | 766,334.58 | D004, D003 | 2025-12-31 | revenue_release |
| 4 | Cash | Accounts Receivable | 700,156.24 | D005, D003 | 2025-09-05 | customer_payment |
| 5 | Utilities Expense | Accounts Payable | 73,302.41 | D006 | 2025-04-03 | hosting_bill |
| 6 | Input Tax Receivable | Accounts Payable | 5,314.42 | D006 | 2025-04-03 | hosting_bill_tax |
| 7 | Accounts Payable | Cash | 71,809.43 | D007, D006 | 2025-11-01 | vendor_payment |
| 8 | Salaries Expense | Cash | 187,725.20 | D008 | 2025-10-12 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 20,966.71 | D008 | 2025-10-12 | payroll_tax |
| 10 | Cash | Loans Payable | 643,591.27 | D009 | 2025-05-28 | loan_draw |
| 11 | Accounts Receivable | Unearned Revenue | 2,167,896.95 | D010, D011, D012 | 2025-03-28 | bundled_contract_allocation_invoice |
| 12 | Unearned Revenue | Service Revenue | 645,373.81 | D011, D012, D013, D014 | 2025-04-11 | bundled_contract_allocation_implementation_release |
| 13 | Unearned Revenue | Service Revenue | 1,522,523.14 | D011, D012, D013, D014 | 2025-12-31 | bundled_contract_allocation_platform_release |
| 14 | Reserve Cash | Cash | 898,241.40 | D015 | 2025-10-03 | interbank_transfer |
| 15 | Utilities Expense | Accrued Expenses | 39,623.26 | D016 | 2025-12-31 | expense_accrual |
| 16 | Service Revenue | Accounts Receivable | 14,612.39 | D003, D017 | 2025-09-08 | credit_memo |
| 17 | Cash | Unearned Revenue | 721,360.08 | D018, D019 | 2025-02-01 | subscription_cash_invoice |
| 18 | Cash | Sales Tax Payable | 52,298.61 | D018, D019 | 2025-02-01 | subscription_cash_invoice_tax |
| 19 | Accounts Receivable | Unearned Revenue | 737,796.60 | D021, D020, D022 | 2025-02-11 | renewal_invoice |
| 20 | Accounts Receivable | Sales Tax Payable | 53,490.25 | D021, D020, D022 | 2025-02-11 | renewal_invoice_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 1,911,478.35
- Accounts Receivable: 3,188,671.87
- Prepaid Insurance: 25,479.50
- Equipment: 171,894.56
- Office Supplies: 8,934.27
- Input Tax Receivable: 5,314.42
- Reserve Cash: 898,241.40

**Liabilities**
- Accounts Payable: 87,075.48
- Accrued Expenses: 56,836.93
- Unearned Revenue: 1,745,662.41
- Loans Payable: 744,602.57
- Sales Tax Payable: 153,684.77

**Equity**
- Retained Earnings: 2,792,842.55
- Share Capital: 629,309.66

**Totals:** Assets = 6,210,014.37; Liabilities = 2,787,862.16; Equity = 3,422,152.21
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
