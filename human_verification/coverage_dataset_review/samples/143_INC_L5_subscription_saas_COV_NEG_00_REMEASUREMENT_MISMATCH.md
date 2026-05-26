# Verification Packet — COV_NEG_00_REMEASUREMENT_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `subscription_saas`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Beacon Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 33
- **Labeled as inconsistent:** True
- **Inconsistency codes:** remeasurement_mismatch
- **Inconsistency reasons:** Closing-rate remeasurement does not reconcile the open foreign balance to the stated functional amount.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Unearned Revenue`, `Share Capital`, `Retained Earnings`, `Service Revenue`, `Utilities Expense`, `Insurance Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Interest Expense`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 785,166.40
- Accounts Receivable: 90,546.50
- Prepaid Insurance: 22,183.74
- Equipment: 160,325.72
- Office Supplies: 13,649.26

**Liabilities**
- Accounts Payable: 89,248.37
- Accrued Expenses: 17,454.27
- Unearned Revenue: 244,330.75
- Loans Payable: 128,924.29

**Equity**
- Retained Earnings: 216,136.85
- Share Capital: 375,777.09


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
Statement Date: 2024-01-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $785,166.40
  - Section assets | Account Accounts Receivable | Amount $90,546.50
  - Section assets | Account Prepaid Insurance | Amount $22,183.74
  - Section assets | Account Equipment | Amount $160,325.72
  - Section assets | Account Office Supplies | Amount $13,649.26
  - Section liabilities | Account Accounts Payable | Amount $89,248.37
  - Section liabilities | Account Accrued Expenses | Amount $17,454.27
  - Section liabilities | Account Unearned Revenue | Amount $244,330.75
  - Section liabilities | Account Loans Payable | Amount $128,924.29
  - Section equity | Account Retained Earnings | Amount $216,136.85
  - Section equity | Account Share Capital | Amount $375,777.09

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D025 — Renewal Notice

- **Type:** `renewal_notice`
- **Role:** `support_doc`
- **Date:** 2024-02-07

```
RENEWAL NOTICE / REFERENCE COPY
===============================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-07

To
--
Aster Point Services
Customer account on file

Terms
-----
Renewal Start: 2024-02-22

Renewal Summary
---------------
Notice Number: RENEW-0001
Customer: Aster Point Services
Contract Reference: SOF-0002
Renewal Start: 2024-02-22
Renewal Amount: $1,040,802.35

Footer
------
Generated for synthetic accounting research use.
Page marker: D025
```

### Document D027 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-02-10

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-02-10

To
--
Crescent Labs
Customer account on file

Terms
-----
Contract Start: 2024-02-10

Approval / Context
------------------
Plan Name: Annual Growth Plan

Order Summary
-------------
Form Number: SOF-0003
Customer: Crescent Labs
Plan Name: Annual Growth Plan
Term Months: 12
Contract Start: 2024-02-10
Contract Value: $1,178,875.31

Footer
------
Internal document packet copy.
Page marker: D027
```

### Document D028 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-10

```
CUSTOMER INVOICE
================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-02-10

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D028
Document Type: customer_invoice
Period: FY 2024
Contract Ref: SOF-0003

Terms
-----
Due Date: 2024-02-27

Parties
-------
Customer: Crescent Labs
Contract Ref: SOF-0003
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2024-02-27
Subtotal: $1,122,738.39
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $56,136.92
Total: $1,178,875.31

Line Items
----------
Items:
  - Description Enterprise License | Amount $342,163.66
  - Description Service coverage under contract | Amount $780,574.73

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D012 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-02-13

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-13

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Contract Start: 2024-02-13

Approval / Context
------------------
Plan Name: Team Support Plan

Order Summary
-------------
Form Number: ASC606-0001
Customer: Oak Harbor Foods
Plan Name: Team Support Plan
Term Months: 12
Contract Start: 2024-02-13
Contract Value: $3,881,251.25

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D013 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-13

```
CUSTOMER INVOICE
================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-13

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
Due Date: 2024-02-26

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: ASC606-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-02-26
Total: $3,881,251.25

Line Items
----------
Items:
  - Description Implementation invoice line | Amount $582,187.69
  - Description Platform access invoice line | Amount $3,299,063.56

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D014 — SSP Rate Card

- **Type:** `ssp_rate_card`
- **Role:** `support_doc`
- **Date:** 2024-02-13

```
SSP RATE CARD / REFERENCE COPY
==============================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-13

Reference Box
-------------
Document ID: D014
Document Type: ssp_rate_card
Period: FY 2024

Rate Card
---------
Rate Card ID: SSP-0001
Contract Reference: ASC606-0001
Effective Date: 2024-02-13
Total SSP: $4,221,017.62

Standalone Selling Prices
-------------------------
Obligations:
  - Obligation Implementation | Ssp Amount $1,263,168.15
  - Obligation Platform access | Ssp Amount $2,957,849.47

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D024 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-02-22

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-02-22

To
--
Aster Point Services
Customer account on file

Terms
-----
Contract Start: 2024-02-22

Approval / Context
------------------
Plan Name: Enterprise License

Order Summary
-------------
Form Number: SOF-0002
Customer: Aster Point Services
Plan Name: Enterprise License
Term Months: 12
Contract Start: 2024-02-22
Contract Value: $1,040,802.35

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D026 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-22

```
CUSTOMER INVOICE
================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-22

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D026
Document Type: customer_invoice
Period: FY 2024
Contract Ref: SOF-0002

Terms
-----
Due Date: 2024-02-29

Parties
-------
Customer: Aster Point Services
Contract Ref: SOF-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2024-02-29
Subtotal: $946,183.95
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $94,618.40
Total: $1,040,802.35

Line Items
----------
Items:
  - Description Enterprise License | Amount $294,499.72
  - Description Service coverage under contract | Amount $651,684.23

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D006 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-23

```
VENDOR INVOICE
==============

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-23

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D006
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-03-12

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Utilities Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-03-12
Subtotal: $181,434.62
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $9,071.73
Total: $190,506.35

Bill Lines
----------
Lines:
  - Description Review pack | Amount $64,571.86
  - Description Support fee | Amount $116,862.76

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D002 — Subscription Order Form

- **Type:** `subscription_order_form`
- **Role:** `support_doc`
- **Date:** 2024-02-27

```
SUBSCRIPTION ORDER FORM
=======================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-27

To
--
Oak Harbor Foods
Customer account on file

Terms
-----
Contract Start: 2024-02-27

Approval / Context
------------------
Plan Name: Team Support Plan

Order Summary
-------------
Form Number: SOF-0001
Customer: Oak Harbor Foods
Plan Name: Team Support Plan
Term Months: 12
Contract Start: 2024-02-27
Contract Value: $665,187.41

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-27

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-02-27

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2024
Contract Ref: SOF-0001

Terms
-----
Due Date: 2024-03-09

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: SOF-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-03-09
Subtotal: $604,715.83
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $60,471.58
Total: $665,187.41

Line Items
----------
Items:
  - Description Business Suite | Amount $134,602.87
  - Description Service coverage under contract | Amount $470,112.96

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D015 — Implementation Acceptance Memo

- **Type:** `implementation_acceptance_memo`
- **Role:** `support_doc`
- **Date:** 2024-02-27

```
IMPLEMENTATION ACCEPTANCE MEMO / REFERENCE COPY
===============================================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-27

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
Acceptance Date: 2024-02-27
Accepted Obligation: Implementation
Accepted Amount: $1,161,490.76

Narrative
---------
Details: Customer accepted implementation. Only the implementation performance obligation is
 released on acceptance.

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D021 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-28

```
VENDOR INVOICE
==============

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-02-28

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D021
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-03-13

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Utilities Expense
Currency: GBP

Bill Details
------------
Invoice Number: FXBILL-0001
Due Date: 2024-03-13
Total: GBP 104,322.82

Bill Lines
----------
Lines:
  - Description Support package | Amount GBP 32,993.73
  - Description Foreign-currency support | Amount GBP 71,329.09

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D022 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2024-02-28

```
EXCHANGE RATE NOTICE
====================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-02-28

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
Rate Date: 2024-02-28
Rate Type: Spot rate at bill date

Conversion Details
------------------
Source Currency: GBP
Source Amount: GBP 104,322.82
Functional Currency: USD
Exchange Rate: 1.2242
Functional Amount: $127,712.00

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D009 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-03

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: $53,738.50
Draw Amount: $1,324,409.86
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $1,378,148.36
Note: Scheduled lender activity for the selected period.
```

### Document D011 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-04

```
TRANSFER ADVICE
===============

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-10-04

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
Amount: $551,931.34
Transfer Date: 2024-10-04
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-10-13

```
PAYROLL SUMMARY
===============

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-10-13

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024
Headcount: 7
Gross Pay: $215,408.06
Employer Tax: 17,520.64
Cash Outflow: $232,928.70

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-02

```
PAYMENT ADVICE
==============

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-11-02

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: $492,251.45
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-09

```
PAYMENT ADVICE
==============

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-11-09

To
--
Golden State Finance

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: $136,145.69
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-14

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: $534,987.26
Draw Amount: $0.00
Principal Paid: $191,424.31
Interest Paid: $18,368.63
Ending Principal: $343,562.95
Note: Scheduled lender activity for the selected period.
```

### Document D018 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `posting_doc`
- **Date:** 2024-11-16

```
CREDIT MEMO
===========

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-11-16

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D018
Document Type: credit_memo
Period: FY 2024
Reference: INV-0001

Approval / Context
------------------
Reason: Pricing adjustment

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Oak Harbor Foods
Currency: USD
Reference: INV-0001
Reason: Pricing adjustment
Amount: $53,441.17

Footer
------
Internal document packet copy.
Page marker: D018
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
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-12-31

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
Opening Deferred: $604,715.83
Added Deferred: $0.00
Released This Period: 604,715.83
Ending Deferred: $0.00

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
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D016
Document Type: performance_obligation_schedule
Period: FY 2024

Allocation Summary
------------------
Schedule ID: POB-0001
Contract Reference: ASC606-0001
Transaction Price: $3,881,251.25
Total SSP: $4,221,017.62
Allocation Total: $3,881,251.25
Released This Period: 3,881,251.25
Ending Deferred: $0.00

Performance Obligations
-----------------------
Obligations:
  - Obligation Implementation | Ssp Amount $1,263,168.15 | Invoice Line Amount $582,187.69 |
 Allocated Transaction Price $1,161,490.76 | Release Pattern On acceptance | Released This 
Period 1,161,490.76
  - Obligation Platform access | Ssp Amount $2,957,849.47 | Invoice Line Amount 
$3,299,063.56 | Allocated Transaction Price $2,719,760.49 | Release Pattern Ratable over 12 
months | Released This Period 2,719,760.49

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
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-12-31

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
Recognized Amount: $33,775.49

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
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D019
Document Type: ar_aging_summary
Period: FY 2024

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2024
Total Open: $119,494.79

Customer Lines
--------------
Lines:
  - Customer Oak Harbor Foods | Reference INV-0001 | Current $51,737.17 | Past Due 67,757.62

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
- **Date:** 2024-12-31

```
CREDIT MEMO
===========

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-12-31

To
--
Oak Harbor Foods

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
Counterparty: Oak Harbor Foods
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: $67,757.62

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
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-12-31

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
Source Currency: GBP
Functional Currency: USD
Source Amount: GBP 104,322.82
Booked Amount: $127,712.00
Closing Rate: 1.3305
Remeasured Amount: $137,437.33
Difference Amount: $11,089.51
Narrative: Open foreign-currency balance remeasured at the closing rate.

Footer
------
Generated for synthetic accounting research use.
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
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-12-31

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
Audience: Finance Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D030 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D030
Document Type: memo
Period: FY 2024

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Document retention reminder
Audience: Finance Team

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
Page marker: D030
```

### Document D031 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-12-31

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D031
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Golden State Finance
Closing Balance: $54,360.66

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount $54,360.66 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D031
```

### Document D032 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D032
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $785,166.40
Closing Balance: $2,649,904.35

Statement Rows
--------------
Rows:
  - Date 2024-02-10 | Description Advance collection INV-0004 | Amount $1,178,875.31 | 
Running Balance $1,964,041.71
  - Date 2024-06-03 | Description Loan draw LOAN-0001 | Amount $1,324,409.86 | Running 
Balance $3,288,451.57
  - Date 2024-10-04 | Description Transfer out TRX-0001 | Amount $-551,931.34 | Running 
Balance $2,736,520.23
  - Date 2024-10-13 | Description Payroll PAYRUN-0001 | Amount $-232,928.70 | Running 
Balance $2,503,591.53
  - Date 2024-11-02 | Description Customer settlement INV-0001 | Amount $492,251.45 | 
Running Balance $2,995,842.98
  - Date 2024-11-09 | Description Supplier settlement BILL-0001 | Amount $-136,145.69 | 
Running Balance $2,859,697.29
  - Date 2024-11-14 | Description Loan payment LOAN-0002 | Amount $-209,792.94 | Running 
Balance $2,649,904.35

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D032
```

### Document D033 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Beacon Manufacturing
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D033
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $551,931.34

Statement Rows
--------------
Rows:
  - Date 2024-10-04 | Description Transfer in TRX-0001 | Amount $551,931.34 | Running 
Balance $551,931.34

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D033
```

## 5. Expected Journal Entries (ground truth)

_(no expected entries — packet is labeled inconsistent)_

## 6. Expected Final Balance Sheet (ground truth)

_Packet is labeled inconsistent — the expected balance sheet should be empty._

**Totals:** Assets = 0.00; Liabilities = 0.00; Equity = 0.00
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

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `remeasurement_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
