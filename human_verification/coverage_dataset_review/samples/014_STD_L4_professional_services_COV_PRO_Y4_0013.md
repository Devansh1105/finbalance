# Verification Packet — COV_PRO_Y4_0013

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 4
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Northwind Clinic
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 37
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 93,664.52
- Accounts Receivable: 20,068.55
- Prepaid Rent: 8,993.20
- Prepaid Insurance: 4,589.32
- Office Supplies: 4,581.20
- Equipment: 26,680.47
- Furniture: 20,167.89

**Liabilities**
- Accounts Payable: 5,649.04
- Accrued Expenses: 5,081.19
- Unearned Revenue: 3,981.59
- Loans Payable: 17,104.02
- Notes Payable: 9,573.12

**Equity**
- Retained Earnings: 21,560.75
- Owner's Equity: 115,795.44


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
  - Section assets | Account Cash | Amount EUR 93.664,52
  - Section assets | Account Accounts Receivable | Amount EUR 20.068,55
  - Section assets | Account Prepaid Rent | Amount EUR 8.993,20
  - Section assets | Account Prepaid Insurance | Amount EUR 4.589,32
  - Section assets | Account Office Supplies | Amount EUR 4.581,20
  - Section assets | Account Equipment | Amount EUR 26.680,47
  - Section assets | Account Furniture | Amount EUR 20.167,89
  - Section liabilities | Account Accounts Payable | Amount EUR 5.649,04
  - Section liabilities | Account Accrued Expenses | Amount EUR 5.081,19
  - Section liabilities | Account Unearned Revenue | Amount EUR 3.981,59
  - Section liabilities | Account Loans Payable | Amount EUR 17.104,02
  - Section liabilities | Account Notes Payable | Amount EUR 9.573,12
  - Section equity | Account Retained Earnings | Amount EUR 21.560,75
  - Section equity | Account Owner's Equity | Amount EUR 115.795,44

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2024-01-16

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Prime Utility Desk
Property: Cedar Plaza
Service Start: 16/01/2024
Service End: 15/04/2024
Total: EUR 22.319,48
Monthly Amount: EUR 7.439,83

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D020 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2024-02-14

```
RETAINER AGREEMENT MEMO
=======================

From
----
Northwind Clinic
14 King Street, Pune
Date: 14/02/2024

Reference Box
-------------
Document ID: D020
Document Type: retainer_agreement_memo
Period: FY 2024
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 12
Total Contract Value: EUR 229.636,25

Explanation
-----------
Narrative: Customer Oak Harbor Foods agreed to a service package spanning 12 months.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-14

```
CUSTOMER INVOICE
================

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 14/02/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D021
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0002

Terms
-----
Due Date: 23/02/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 23/02/2024
Subtotal: EUR 214.113,05
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 15.523,20
Total: EUR 229.636,25

Line Items
----------
Items:
  - Description Business Suite | Amount EUR 79.261,41
  - Description Service coverage under contract | Amount EUR 134.851,64

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D029 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-02-14

```
CANCELLATION NOTE
=================

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 14/02/2024

Reference Box
-------------
Document ID: D029
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0002
Withdrawn Reference: INV-0002-OLD
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0002-OLD is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D032 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-02-14

```
CANCELLATION NOTE
=================

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 14/02/2024

Reference Box
-------------
Document ID: D032
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0003
Withdrawn Reference: INV-0002-OLD
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0002-OLD is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D032
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-29

```
CUSTOMER INVOICE
================

From
----
Northwind Clinic
14 King Street, Pune
Date: 29/02/2024

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 13/03/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 13/03/2024
Subtotal: EUR 42.783,37
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 3.101,79
Total: EUR 45.885,16

Line Items
----------
Items:
  - Description Review pack | Amount EUR 10.430,35
  - Description Follow-up support | Amount EUR 32.353,02

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D016 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2024-02-29

```
LEASE AGREEMENT
===============

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 29/02/2024

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D016
Document Type: lease_agreement
Period: FY 2024

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Pace Office Mart
Commencement Date: 29/02/2024
Term Months: 48
Monthly Payment Amount: EUR 11.939,62
Incremental Borrowing Rate: 0,09
ROU Asset Amount: EUR 479.791,03
Lease Liability Amount: EUR 479.791,03

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D033 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-02-29

```
CANCELLATION NOTE
=================

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 29/02/2024

Reference Box
-------------
Document ID: D033
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0004
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D033
```

### Document D024 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2024-03-21

```
CUSTOMER INVOICE
================

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 21/03/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D024
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0003

Terms
-----
Due Date: 01/04/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 01/04/2024
Total: EUR 41.540,80

Line Items
----------
Items:
  - Description Support package | Amount EUR 13.550,24
  - Description Draft billing copy | Amount EUR 27.990,56

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

### Document D035 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-03-21

```
CANCELLATION NOTE
=================

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 21/03/2024

Reference Box
-------------
Document ID: D035
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0005
Withdrawn Reference: INV-0003-OLD
Replacement Reference: INV-0003

Background
----------
Narrative: INV-0003-OLD is withdrawn and must not be posted. Use INV-0003 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D035
```

### Document D025 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2024-03-23

```
CANCELLATION NOTE
=================

From
----
Northwind Clinic
14 King Street, Pune
Date: 23/03/2024

Reference Box
-------------
Document ID: D025
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0003
Replacement Reference: INV-0004

Background
----------
Narrative: INV-0003 is withdrawn and must not be posted. Use INV-0004 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D025
```

### Document D026 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-23

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Northwind Clinic
14 King Street, Pune
Date: 23/03/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D026
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0003

Terms
-----
Due Date: 04/04/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 04/04/2024
Total: EUR 39.328,36

Line Items
----------
Items:
  - Description Review pack | Amount EUR 9.942,75
  - Description Reissued billing | Amount EUR 29.385,61

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-29

```
VENDOR INVOICE
==============

From
----
Northwind Clinic
14 King Street, Pune
Date: 29/03/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2024

Terms
-----
Due Date: 19/04/2024

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 19/04/2024
Subtotal: EUR 19.396,48
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 1.842,67
Total: EUR 21.239,15

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount EUR 6.964,92
  - Description Support fee | Amount EUR 12.431,56

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-05-23

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Pace Office Mart
Total: EUR 1.666,53
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount EUR 439,26
  - Description Travel Incidentals | Amount EUR 1.227,27
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-09

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: EUR 14.386,26
Draw Amount: EUR 286.195,35
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 300.581,61
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-25

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Golden State Finance
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 24
Total: EUR 239.341,76
Paid Cash: EUR 71.057,37
Financed Amount: EUR 168.284,39
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-09-15

```
PAYMENT ADVICE
==============

From
----
Northwind Clinic
14 King Street, Pune
Date: 15/09/2024

To
--
Oakline Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: EUR 14.260,61
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D019 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-09

```
TRANSFER ADVICE
===============

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 09/10/2024

Reference Box
-------------
Document ID: D019
Document Type: transfer_advice
Period: FY 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: EUR 201.302,92
Transfer Date: 09/10/2024
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-10-10

```
UTILITY INVOICE
===============

From
----
Northwind Clinic
14 King Street, Pune
Date: 10/10/2024

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: FY 2024

Terms
-----
Due Date: 23/10/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: FY 2024
Due Date: 23/10/2024
Total: EUR 4.016,18

Charges
-------
Charges:
  - Description Electricity | Amount EUR 1.277,54
  - Description Water | Amount EUR 2.738,64

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-13

```
PAYMENT ADVICE
==============

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 13/10/2024

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
Amount: EUR 39.666,75
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D014 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-10-20

```
ASSET DISPOSAL NOTICE
=====================

From
----
Northwind Clinic
14 King Street, Pune
Date: 20/10/2024

Reference Box
-------------
Document ID: D014
Document Type: asset_disposal_notice
Period: FY 2024

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Original Cost: EUR 26.680,47
Accumulated Depreciation: 6.670,08
Net Book Value: EUR 20.010,39
Proceeds Amount: EUR 16.408,52
Gain Loss Amount: EUR 3.601,87
Gain Loss Type: Loss

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D015 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-20

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Northwind Clinic
14 King Street, Pune
Date: 20/10/2024

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D015
Document Type: sale_proceeds_advice
Period: FY 2024

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Maple Ridge Trading
Asset Tag: OPEN-EQU
Proceeds Amount: EUR 16.408,52
Settlement Date: 20/10/2024
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D018 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2024-11-04

```
LEASE PAYMENT NOTICE
====================

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 04/11/2024

Reference Box
-------------
Document ID: D018
Document Type: lease_payment_notice
Period: FY 2024

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 04/11/2024
Payment Amount: EUR 35.818,86
Interest Amount: EUR 10.795,30
Principal Amount: EUR 25.023,56

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-11-06

```
PAYROLL SUMMARY
===============

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 06/11/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024
Headcount: 4
Gross Pay: EUR 44.540,08
Employer Tax: 4.768,98
Cash Outflow: EUR 49.309,06

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Northwind Clinic
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: FY 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: EUR 7.439,83

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D013 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Northwind Clinic
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D013
Document Type: fixed_asset_rollforward
Period: FY 2024

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 26.680,47
Useful Life: 48
Current Charge: EUR 6.670,08
Accumulated Depreciation: 6.670,08
Opening Balance: EUR 26.680,47
Additions: 0,00
Disposals: 0,00
Ending Balance: EUR 26.680,47

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D017 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Northwind Clinic
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D017
Document Type: lease_amortization_schedule
Period: FY 2024

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: EUR 479.791,03
Payment Amount: EUR 35.818,86
Interest Amount: EUR 10.795,30
Principal Amount: EUR 25.023,56
Ending Liability Balance: EUR 454.767,47
ROU Amortization Amount: EUR 119.947,76

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D022 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D022
Document Type: revenue_recognition_schedule
Period: FY 2024

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: FY 2024
Opening Deferred: EUR 214.113,05
Added Deferred: EUR 0,00
Released This Period: 214.113,05
Ending Deferred: EUR 0,00

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D023 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Northwind Clinic
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D023
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
Recognized Amount: EUR 6.859,22

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D027 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
AR AGING SUMMARY
================

From
----
Northwind Clinic
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D027
Document Type: ar_aging_summary
Period: FY 2024

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2024
Total Open: EUR 6.218,41

Customer Lines
--------------
Lines:
  - Customer Riverfront Group | Reference INV-0001 | Current EUR 3.311,12 | Past Due 
2.907,29

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Internal document packet copy.
Page marker: D027
```

### Document D028 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
CREDIT MEMO
===========

From
----
Northwind Clinic
14 King Street, Pune
Date: 31/12/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D028
Document Type: credit_memo
Period: FY 2024
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Riverfront Group
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: EUR 2.907,29

Footer
------
Internal document packet copy.
Page marker: D028
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
Northwind Clinic
14 King Street, Pune
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D030
Document Type: memo
Period: FY 2024

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
Audience: Operations Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
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
Northwind Clinic
14 King Street, Pune
Date: 31/12/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D031
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Oakline Services
Closing Balance: EUR 6.978,54

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount EUR 6.978,54 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D031
```

### Document D034 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
MEMO
====

From
----
Northwind Clinic
14 King Street, Pune
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D034
Document Type: memo
Period: FY 2024

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0002
Subject: Scanning checklist for back-office staff
Audience: All Staff

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
Page marker: D034
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
Northwind Clinic
14 King Street, Pune
Document Date: 31/12/2024

Reference Box
-------------
Document ID: D036
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0013
Statement Currency: EUR
Opening Balance: EUR 93.664,52
Closing Balance: EUR 40.200,31

Statement Rows
--------------
Rows:
  - Date 16/01/2024 | Description Rent prepayment PRE-0001 | Amount EUR -22.319,48 | Running
 Balance EUR 71.345,04
  - Date 23/05/2024 | Description Pace Office Mart receipt RCPT-0001 | Amount EUR -1.666,53 
| Running Balance EUR 69.678,51
  - Date 09/06/2024 | Description Loan draw LOAN-0001 | Amount EUR 286.195,35 | Running 
Balance EUR 355.873,86
  - Date 25/07/2024 | Description Asset purchase ASSET-0001 | Amount EUR -71.057,37 | 
Running Balance EUR 284.816,49
  - Date 15/09/2024 | Description Supplier settlement BILL-0001 | Amount EUR -14.260,61 | 
Running Balance EUR 270.555,88
  - Date 09/10/2024 | Description Transfer out TRX-0001 | Amount EUR -201.302,92 | Running 
Balance EUR 69.252,96
  - Date 13/10/2024 | Description Customer settlement INV-0001 | Amount EUR 39.666,75 | 
Running Balance EUR 108.919,71
  - Date 20/10/2024 | Description Asset sale OPEN-EQU | Amount EUR 16.408,52 | Running 
Balance EUR 125.328,23
  - Date 04/11/2024 | Description Lease payment LEASE-0001 | Amount EUR -35.818,86 | Running
 Balance EUR 89.509,37
  - Date 06/11/2024 | Description Payroll PAYRUN-0001 | Amount EUR -49.309,06 | Running 
Balance EUR 40.200,31

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D036
```

### Document D037 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Northwind Clinic
14 King Street, Pune
Date: 31/12/2024

Reference Box
-------------
Document ID: D037
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-1399
Statement Currency: EUR
Opening Balance: EUR 0,00
Closing Balance: EUR 201.302,92

Statement Rows
--------------
Rows:
  - Date 09/10/2024 | Description Transfer in TRX-0001 | Amount EUR 201.302,92 | Running 
Balance EUR 201.302,92

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D037
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 42,783.37 | D002 | 2024-02-29 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 3,101.79 | D002 | 2024-02-29 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 19,396.48 | D003 | 2024-03-29 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 1,842.67 | D003 | 2024-03-29 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 1,666.53 | D004 | 2024-05-23 | expense_receipt |
| 6 | Cash | Accounts Receivable | 39,666.75 | D005, D002 | 2024-10-13 | customer_payment |
| 7 | Accounts Payable | Cash | 14,260.61 | D006, D003 | 2024-09-15 | supplier_payment |
| 8 | Salaries Expense | Cash | 44,540.08 | D007 | 2024-11-06 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 4,768.98 | D007 | 2024-11-06 | payroll_tax |
| 10 | Prepaid Rent | Cash | 22,319.48 | D008 | 2024-01-16 | prepaid_rent_purchase |
| 11 | Rent Expense | Prepaid Rent | 7,439.83 | D008, D009 | 2024-12-31 | prepaid_rent_release |
| 12 | Utilities Expense | Accounts Payable | 4,016.18 | D010 | 2024-10-10 | utilities_bill |
| 13 | Cash | Loans Payable | 286,195.35 | D011 | 2024-06-09 | loan_draw |
| 14 | Equipment | Cash | 71,057.37 | D012 | 2024-07-25 | equipment_purchase_cash |
| 15 | Equipment | Notes Payable | 168,284.39 | D012 | 2024-07-25 | equipment_purchase_financed |
| 16 | Depreciation Expense | Accumulated Depreciation | 6,670.08 | D013 | 2024-12-31 | depreciation |
| 17 | Cash | Equipment | 16,408.52 | D014, D015 | 2024-10-20 | asset_disposal_proceeds |
| 18 | Accumulated Depreciation | Equipment | 6,670.08 | D014, D015 | 2024-10-20 | asset_disposal_remove_accumulated_depreciation |
| 19 | Loss on Disposal | Equipment | 3,601.87 | D014, D015 | 2024-10-20 | asset_disposal_loss |
| 20 | Right-of-Use Asset | Lease Liability | 479,791.03 | D016 | 2024-02-29 | baseline_lease_initial_recognition |
| 21 | Lease Liability | Cash | 25,023.56 | D016, D017, D018 | 2024-11-04 | baseline_lease_principal |
| 22 | Lease Interest Expense | Cash | 10,795.30 | D016, D017, D018 | 2024-11-04 | baseline_lease_interest |
| 23 | Lease Amortization Expense | Right-of-Use Asset | 119,947.76 | D016, D017 | 2024-12-31 | baseline_lease_amortization |
| 24 | Reserve Cash | Cash | 201,302.92 | D019 | 2024-10-09 | interbank_transfer |
| 25 | Accounts Receivable | Unearned Revenue | 214,113.05 | D020, D021 | 2024-02-14 | retainer_invoice |
| 26 | Accounts Receivable | Sales Tax Payable | 15,523.20 | D020, D021 | 2024-02-14 | retainer_invoice_tax |
| 27 | Unearned Revenue | Service Revenue | 214,113.05 | D022, D021 | 2024-12-31 | retainer_release |
| 28 | Utilities Expense | Accrued Expenses | 6,859.22 | D023 | 2024-12-31 | expense_accrual |
| 29 | Accounts Receivable | Service Revenue | 39,328.36 | D024, D025, D026 | 2024-03-23 | reissued_invoice |
| 30 | Bad Debt Expense | Accounts Receivable | 2,907.29 | D027, D028, D002 | 2024-12-31 | bad_debt_review |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 40,200.31
- Accounts Receivable: 292,344.28
- Prepaid Rent: 23,872.85
- Prepaid Insurance: 4,589.32
- Office Supplies: 4,581.20
- Equipment: 239,341.76
- Furniture: 20,167.89
- Input Tax Receivable: 1,842.67
- Right-of-Use Asset: 359,843.27
- Reserve Cash: 201,302.92

**Liabilities**
- Accounts Payable: 16,643.76
- Accrued Expenses: 11,940.41
- Unearned Revenue: 3,981.59
- Loans Payable: 303,299.37
- Notes Payable: 177,857.51
- Sales Tax Payable: 18,624.99
- Lease Liability: 454,767.47

**Equity**
- Retained Earnings: 85,175.93
- Owner's Equity: 115,795.44

**Totals:** Assets = 1,188,086.47; Liabilities = 987,115.10; Equity = 200,971.37
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
