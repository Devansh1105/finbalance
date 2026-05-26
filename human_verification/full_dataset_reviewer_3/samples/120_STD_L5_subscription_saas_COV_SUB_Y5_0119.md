# Verification Packet — COV_SUB_Y5_0119

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Summit Manufacturing
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 36
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 1,022,130.02
- Accounts Receivable: 104,116.72
- Prepaid Insurance: 39,927.04
- Equipment: 173,749.00
- Office Supplies: 15,770.36

**Liabilities**
- Accounts Payable: 92,760.50
- Accrued Expenses: 35,501.34
- Unearned Revenue: 341,881.91
- Loans Payable: 136,035.56

**Equity**
- Retained Earnings: 108,938.90
- Share Capital: 640,574.93


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
  - Section assets | Account Cash | Amount GBP 1,022,130.02
  - Section assets | Account Accounts Receivable | Amount GBP 104,116.72
  - Section assets | Account Prepaid Insurance | Amount GBP 39,927.04
  - Section assets | Account Equipment | Amount GBP 173,749.00
  - Section assets | Account Office Supplies | Amount GBP 15,770.36
  - Section liabilities | Account Accounts Payable | Amount GBP 92,760.50
  - Section liabilities | Account Accrued Expenses | Amount GBP 35,501.34
  - Section liabilities | Account Unearned Revenue | Amount GBP 341,881.91
  - Section liabilities | Account Loans Payable | Amount GBP 136,035.56
  - Section equity | Account Retained Earnings | Amount GBP 108,938.90
  - Section equity | Account Share Capital | Amount GBP 640,574.93

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-01-21

```
VENDOR INVOICE
==============

From
----
Summit Manufacturing
14 King Street, Pune
Date: 21/01/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 03/02/2024

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Utilities Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 03/02/2024
Subtotal: GBP 118,273.92
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 14,192.87
Total: GBP 132,466.79

Bill Lines
----------
Lines:
  - Description Review pack | Amount GBP 41,350.66
  - Description Support fee | Amount GBP 76,923.26

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D021 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-19

```
VENDOR INVOICE
==============

From
----
Summit Manufacturing
14 King Street, Pune
Date: 19/02/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D021
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 03/03/2024

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Utilities Expense
Currency: USD

Bill Details
------------
Invoice Number: FXBILL-0001
Due Date: 03/03/2024
Total: $80,386.18

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $23,738.59
  - Description Foreign-currency support | Amount $56,647.59

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D022 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2024-02-19

```
EXCHANGE RATE NOTICE
====================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 19/02/2024

Reference Box
-------------
Document ID: D022
Document Type: exchange_rate_notice
Period: FY 2024
Reference: FXBILL-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXBILL-0001
Rate Date: 19/02/2024
Rate Type: Spot rate at bill date

Conversion Details
------------------
Source Currency: USD
Source Amount: $80,386.18
Functional Currency: GBP
Exchange Rate: 0.7501
Functional Amount: GBP 60,297.67

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D025 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2024-02-24

```
RENEWAL NOTICE / REFERENCE COPY
===============================

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 24/02/2024

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Renewal Start: 10/03/2024

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Blue Finch Holdings
Contract Reference: SOF-0002
Renewal Start: 10/03/2024
Renewal Amount: GBP 625,086.25

Footer
------
Generated for synthetic accounting research use.
Page marker: D025
```

### Document D012 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-03-05

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 05/03/2024

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Contract Start: 05/03/2024

Approval / Context
------------------
Plan Name: Team Support Plan

Order Summary
-------------
Form Number: ASC606-0001
Customer: Oak Harbor Foods
Plan Name: Team Support Plan
Term Months: 12
Contract Start: 05/03/2024
Contract Value: GBP 3,495,519.55

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D013 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-05

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 05/03/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D013
Document Type: customer_invoice
Period: FY 2024
Contract Ref: ASC606-0001

Terms
-----
Due Date: 15/03/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: ASC606-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 15/03/2024
Total: GBP 3,495,519.55

Line Items
----------
Items:
  - Description Implementation invoice line | Amount GBP 524,327.93
  - Description Platform access invoice line | Amount GBP 2,971,191.62

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D014 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2024-03-05

```
SSP RATE CARD
=============

From
----
Summit Manufacturing
14 King Street, Pune
Date: 05/03/2024

Reference Box
-------------
Document ID: D014
Document Type: ssp_rate_card
Period: FY 2024

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 05/03/2024
Total SSP: GBP 3,872,452.69

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount GBP 1,015,568.91
  - Obligation Platform access | Ssp Amount GBP 2,856,883.78

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D031 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-03-05

```
SECONDARY COPY
==============

From
----
Summit Manufacturing
14 King Street, Pune
Date: 05/03/2024

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D031
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0002
Counterparty: Oak Harbor Foods
Total: GBP 3,495,519.55
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D031
```

### Document D033 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-03-05

```
CANCELLATION NOTE
=================

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 05/03/2024

Reference Box
-------------
Document ID: D033
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0002-OLD
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0002-OLD is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D033
```

### Document D024 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-03-10

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 10/03/2024

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Contract Start: 10/03/2024

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0002
Customer: Blue Finch Holdings
Plan Name: Enterprise License
Term Months: 12
Contract Start: 10/03/2024
Contract Value: GBP 625,086.25

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D026 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-10

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 10/03/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D026
Document Type: customer_invoice
Period: FY 2024
Contract Ref: SOF-0002

Terms
-----
Due Date: 19/03/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: SOF-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 19/03/2024
Subtotal: GBP 529,734.11
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 95,352.14
CGST Amount: GBP 47,676.07
SGST Amount: GBP 47,676.07
Total: GBP 625,086.25

Line Items
----------
Items:
  - Description Business Suite | Amount GBP 149,437.78
  - Description Service coverage under contract | Amount GBP 380,296.33

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D015 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2024-03-19

```
IMPLEMENTATION ACCEPTANCE MEMO
==============================

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 19/03/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D015
Document Type: implementation_acceptance_memo
Period: FY 2024

Acceptance
----------
Memo ID: ACCEPT-0001
Contract Reference: ASC606-0001
Customer: Oak Harbor Foods
Acceptance Date: 19/03/2024
Accepted Obligation: Implementation
Accepted Amount: GBP 916,716.42

Narrative
---------
Details: Customer accepted implementation. Only the implementation performance obligation is
 released on acceptance.

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D027 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-03-22

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 22/03/2024

To
--
Blue Finch Holdings
Customer account on file

Terms
-----
Contract Start: 22/03/2024

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0003
Customer: Blue Finch Holdings
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 22/03/2024
Contract Value: GBP 1,292,477.88

Footer
------
Internal document packet copy.
Page marker: D027
```

### Document D028 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-22

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 22/03/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D028
Document Type: customer_invoice
Period: FY 2024
Contract Ref: SOF-0003

Terms
-----
Due Date: 04/04/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: SOF-0003
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 04/04/2024
Subtotal: GBP 1,153,998.11
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 138,479.77
CGST Amount: GBP 69,239.88
SGST Amount: GBP 69,239.89
Total: GBP 1,292,477.88

Line Items
----------
Items:
  - Description Team Support Plan | Amount GBP 244,325.84
  - Description Service coverage under contract | Amount GBP 909,672.27

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-03-27

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 27/03/2024

To
--
Riverfront Group
Customer account on file

Terms
-----
Contract Start: 27/03/2024

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Riverfront Group
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 27/03/2024
Contract Value: GBP 658,742.18

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-27

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 27/03/2024

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
Due Date: 10/04/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: SOF-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 10/04/2024
Subtotal: GBP 588,162.66
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 70,579.52
CGST Amount: GBP 35,289.76
SGST Amount: GBP 35,289.76
Total: GBP 658,742.18

Line Items
----------
Items:
  - Description Business Suite | Amount GBP 151,881.85
  - Description Service coverage under contract | Amount GBP 436,280.81

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D034 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-03-27

```
CANCELLATION NOTE
=================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 27/03/2024

Reference Box
-------------
Document ID: D034
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0002
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D034
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
Lender: First City Bank
Opening Principal: GBP 106,377.06
Draw Amount: GBP 554,745.14
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 661,122.20
Note: Scheduled lender activity for the selected period.
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-10

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: GBP 1,086,587.44
Draw Amount: GBP 0.00
Principal Paid: GBP 179,688.50
Interest Paid: GBP 19,754.71
Ending Principal: GBP 906,898.94
Note: Scheduled lender activity for the selected period.
```

### Document D011 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-27

```
TRANSFER ADVICE
===============

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 27/09/2024

Reference Box
-------------
Document ID: D011
Document Type: transfer_advice
Period: FY 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: GBP 497,744.49
Transfer Date: 27/09/2024
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-09

```
PAYMENT ADVICE
==============

From
----
Summit Manufacturing
14 King Street, Pune
Date: 09/10/2024

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: GBP 122,877.56
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-27

```
PAYMENT ADVICE
==============

From
----
Summit Manufacturing
14 King Street, Pune
Date: 27/10/2024

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
Amount: GBP 523,774.89
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D018 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `posting_doc`
- **Date:** 2024-10-28

```
CREDIT MEMO
===========

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 28/10/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D018
Document Type: credit_memo
Period: FY 2024
Reference: INV-0001

Approval / Context
------------------
Reason: Service issue

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Riverfront Group
Currency: GBP
Reference: INV-0001
Reason: Service issue
Amount: GBP 20,939.27

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-11-11

```
PAYROLL SUMMARY
===============

From
----
Summit Manufacturing
14 King Street, Pune
Date: 11/11/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024
Headcount: 8
Gross Pay: GBP 129,007.70
Employer Tax: 13,102.18
Cash Outflow: GBP 142,109.88

Footer
------
Internal document packet copy.
Page marker: D008
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
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

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
Opening Deferred: GBP 588,162.66
Added Deferred: GBP 0.00
Released This Period: 588,162.66
Ending Deferred: GBP 0.00

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D016 — Performance Obligation Schedule

- **Type:** `performance_obligation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
PERFORMANCE OBLIGATION SCHEDULE
===============================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D016
Document Type: performance_obligation_schedule
Period: FY 2024

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: GBP 3,495,519.55
Total SSP: GBP 3,872,452.69
Allocation Total: GBP 3,495,519.55
Released This Period: 3,495,519.55
Ending Deferred: GBP 0.00

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount GBP 1,015,568.91 | Invoice Line Amount GBP 
524,327.93 | Allocated Transaction Price GBP 916,716.42 | Release Pattern On acceptance | 
Released This Period 916,716.42
  - Obligation Platform access | Ssp Amount GBP 2,856,883.78 | Invoice Line Amount GBP 
2,971,191.62 | Allocated Transaction Price GBP 2,578,803.13 | Release Pattern Ratable over 
12 months | Released This Period 2,578,803.13

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D017
Document Type: service_period_memo
Period: FY 2024
Reference: FY 2024

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2024
Recognized Amount: GBP 58,553.47

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D019 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
AR AGING SUMMARY
================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D019
Document Type: ar_aging_summary
Period: FY 2024

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2024
Total Open: GBP 114,028.02

Customer Lines
--------------
Lines:
  - Customer Riverfront Group | Reference INV-0001 | Current GBP 66,098.39 | Past Due 
47,929.63

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D020 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
CREDIT MEMO
===========

From
----
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D020
Document Type: credit_memo
Period: FY 2024
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
Amount: GBP 47,929.63

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D023 — FX Remeasurement Memo

- **Type:** `fx_remeasurement_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
FX REMEASUREMENT MEMO
=====================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D023
Document Type: fx_remeasurement_memo
Period: FY 2024
Reference: FXBILL-0001

Remeasurement Details
---------------------
Memo ID: FXREM-0001
Reference: FXBILL-0001
Source Currency: USD
Functional Currency: GBP
Source Amount: $80,386.18
Booked Amount: GBP 60,297.67
Closing Rate: 0.7374
Remeasured Amount: GBP 59,276.77
Difference Amount: GBP 1,020.90
Narrative: Open foreign-currency balance remeasured at the closing rate.

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D029 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D029
Document Type: memo
Period: FY 2024

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0001
Subject: Scanning checklist for back-office staff
Audience: All Staff

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
Page marker: D029
```

### Document D030 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D030
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Prime Utility Desk
Closing Balance: GBP 9,589.23

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount GBP 9,589.23 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D032 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D032
Document Type: memo
Period: FY 2024

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0002
Subject: Scanning checklist for back-office staff
Audience: Back Office

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D032
```

### Document D035 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Summit Manufacturing
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D035
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0119
Statement Currency: GBP
Opening Balance: GBP 1,022,130.02
Closing Balance: GBP 2,430,952.79

Statement Rows
--------------
Rows:
  - Date 22/03/2024 | Description Advance collection INV-0004 | Amount GBP 1,292,477.88 | 
Running Balance GBP 2,314,607.90
  - Date 17/06/2024 | Description Loan draw LOAN-0001 | Amount GBP 554,745.14 | Running 
Balance GBP 2,869,353.04
  - Date 10/09/2024 | Description Loan payment LOAN-0002 | Amount GBP -199,443.21 | Running 
Balance GBP 2,669,909.83
  - Date 27/09/2024 | Description Transfer out TRX-0001 | Amount GBP -497,744.49 | Running 
Balance GBP 2,172,165.34
  - Date 09/10/2024 | Description Supplier settlement BILL-0001 | Amount GBP -122,877.56 | 
Running Balance GBP 2,049,287.78
  - Date 27/10/2024 | Description Customer settlement INV-0001 | Amount GBP 523,774.89 | 
Running Balance GBP 2,573,062.67
  - Date 11/11/2024 | Description Payroll PAYRUN-0001 | Amount GBP -142,109.88 | Running 
Balance GBP 2,430,952.79

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D035
```

### Document D036 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Summit Manufacturing
14 King Street, Pune
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D036
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-1999
Statement Currency: GBP
Opening Balance: GBP 0.00
Closing Balance: GBP 497,744.49

Statement Rows
--------------
Rows:
  - Date 27/09/2024 | Description Transfer in TRX-0001 | Amount GBP 497,744.49 | Running 
Balance GBP 497,744.49

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D036
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Unearned Revenue | 588,162.66 | D002, D003 | 2024-03-27 | subscription_invoice |
| 2 | Accounts Receivable | CGST Payable | 35,289.76 | D002, D003 | 2024-03-27 | subscription_invoice_tax_cgst |
| 3 | Accounts Receivable | SGST Payable | 35,289.76 | D002, D003 | 2024-03-27 | subscription_invoice_tax_sgst |
| 4 | Unearned Revenue | Service Revenue | 588,162.66 | D004, D003 | 2024-12-31 | revenue_release |
| 5 | Cash | Accounts Receivable | 523,774.89 | D005, D003 | 2024-10-27 | customer_payment |
| 6 | Utilities Expense | Accounts Payable | 118,273.92 | D006 | 2024-01-21 | hosting_bill |
| 7 | Input CGST Receivable | Accounts Payable | 7,096.44 | D006 | 2024-01-21 | hosting_bill_tax_cgst |
| 8 | Input SGST Receivable | Accounts Payable | 7,096.43 | D006 | 2024-01-21 | hosting_bill_tax_sgst |
| 9 | Accounts Payable | Cash | 122,877.56 | D007, D006 | 2024-10-09 | vendor_payment |
| 10 | Salaries Expense | Cash | 129,007.70 | D008 | 2024-11-11 | payroll_gross |
| 11 | Payroll Tax Expense | Cash | 13,102.18 | D008 | 2024-11-11 | payroll_tax |
| 12 | Cash | Loans Payable | 554,745.14 | D009 | 2024-06-17 | loan_draw |
| 13 | Loans Payable | Cash | 179,688.50 | D010 | 2024-09-10 | loan_repayment_principal |
| 14 | Interest Expense | Cash | 19,754.71 | D010 | 2024-09-10 | loan_repayment_interest |
| 15 | Reserve Cash | Cash | 497,744.49 | D011 | 2024-09-27 | interbank_transfer |
| 16 | Accounts Receivable | Unearned Revenue | 3,495,519.55 | D012, D013, D014 | 2024-03-05 | bundled_contract_allocation_invoice |
| 17 | Unearned Revenue | Service Revenue | 916,716.42 | D013, D014, D015, D016 | 2024-03-19 | bundled_contract_allocation_implementation_release |
| 18 | Unearned Revenue | Service Revenue | 2,578,803.13 | D013, D014, D015, D016 | 2024-12-31 | bundled_contract_allocation_platform_release |
| 19 | Utilities Expense | Accrued Expenses | 58,553.47 | D017 | 2024-12-31 | expense_accrual |
| 20 | Service Revenue | Accounts Receivable | 20,939.27 | D003, D018 | 2024-10-28 | credit_memo |
| 21 | Bad Debt Expense | Accounts Receivable | 47,929.63 | D019, D020, D003 | 2024-12-31 | bad_debt_review |
| 22 | Utilities Expense | Accounts Payable | 60,297.67 | D021, D022 | 2024-02-19 | fx_hosting_bill |
| 23 | Accounts Payable | Foreign Exchange Gain | 1,020.90 | D023, D021 | 2024-12-31 | fx_remeasurement |
| 24 | Accounts Receivable | Unearned Revenue | 529,734.11 | D025, D024, D026 | 2024-03-10 | renewal_invoice |
| 25 | Accounts Receivable | CGST Payable | 47,676.07 | D025, D024, D026 | 2024-03-10 | renewal_invoice_tax_cgst |
| 26 | Accounts Receivable | SGST Payable | 47,676.07 | D025, D024, D026 | 2024-03-10 | renewal_invoice_tax_sgst |
| 27 | Cash | Unearned Revenue | 1,153,998.11 | D027, D028 | 2024-03-22 | subscription_cash_invoice |
| 28 | Cash | CGST Payable | 69,239.88 | D027, D028 | 2024-03-22 | subscription_cash_invoice_tax_cgst |
| 29 | Cash | SGST Payable | 69,239.89 | D027, D028 | 2024-03-22 | subscription_cash_invoice_tax_sgst |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 2,430,952.79
- Accounts Receivable: 4,290,820.91
- Prepaid Insurance: 39,927.04
- Equipment: 173,749.00
- Office Supplies: 15,770.36
- Input CGST Receivable: 7,096.44
- Input SGST Receivable: 7,096.43
- Reserve Cash: 497,744.49

**Liabilities**
- Accounts Payable: 161,626.50
- Accrued Expenses: 94,054.81
- Unearned Revenue: 2,025,614.13
- Loans Payable: 511,092.20
- CGST Payable: 152,205.71
- SGST Payable: 152,205.72

**Equity**
- Retained Earnings: 3,725,783.46
- Share Capital: 640,574.93

**Totals:** Assets = 7,463,157.46; Liabilities = 3,096,799.07; Equity = 4,366,358.39
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
