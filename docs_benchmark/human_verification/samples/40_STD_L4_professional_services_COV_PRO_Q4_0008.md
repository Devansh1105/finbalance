# Verification Packet — COV_PRO_Q4_0008

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q3 FY 2025-26
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Summit Manufacturing
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 28
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 38,169.47
- Accounts Receivable: 3,317.05
- Prepaid Rent: 4,169.21
- Prepaid Insurance: 1,649.05
- Office Supplies: 2,330.49
- Equipment: 11,295.98
- Furniture: 8,117.44

**Liabilities**
- Accounts Payable: 5,212.95
- Accrued Expenses: 2,685.48
- Unearned Revenue: 4,503.24
- Loans Payable: 4,740.51
- Notes Payable: 8,224.90

**Equity**
- Retained Earnings: 4,665.19
- Owner's Equity: 39,016.42


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/10/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 38,169.47
  - Section assets | Account Accounts Receivable | Amount GBP 3,317.05
  - Section assets | Account Prepaid Rent | Amount GBP 4,169.21
  - Section assets | Account Prepaid Insurance | Amount GBP 1,649.05
  - Section assets | Account Office Supplies | Amount GBP 2,330.49
  - Section assets | Account Equipment | Amount GBP 11,295.98
  - Section assets | Account Furniture | Amount GBP 8,117.44
  - Section liabilities | Account Accounts Payable | Amount GBP 5,212.95
  - Section liabilities | Account Accrued Expenses | Amount GBP 2,685.48
  - Section liabilities | Account Unearned Revenue | Amount GBP 4,503.24
  - Section liabilities | Account Loans Payable | Amount GBP 4,740.51
  - Section liabilities | Account Notes Payable | Amount GBP 8,224.90
  - Section equity | Account Retained Earnings | Amount GBP 4,665.19
  - Section equity | Account Owner's Equity | Amount GBP 39,016.42

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-10-04

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Golden State Finance
Property: Cedar Plaza
Service Start: 04/10/2025
Service End: 03/01/2026
Total: GBP 7,562.99
Monthly Amount: GBP 2,521.00

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-08

```
VENDOR INVOICE
==============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 08/10/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q3 FY 2025-26

Terms
-----
Due Date: 26/10/2025

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 26/10/2025
Subtotal: GBP 15,875.69
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 3,175.14
Total: GBP 19,050.83

Bill Lines
----------
Lines:
  - Description Support package | Amount GBP 5,144.14
  - Description Support fee | Amount GBP 10,731.55

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D020 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-10-15

```
RETAINER AGREEMENT MEMO
=======================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 15/10/2025

Reference Box
-------------
Document ID: D020
Document Type: retainer_agreement_memo
Period: Q3 FY 2025-26
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 6
Total Contract Value: GBP 65,937.44

Explanation
-----------
Narrative: Customer Crescent Labs agreed to a service package spanning 6 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D021 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-15

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 15/10/2025

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D021
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0002

Terms
-----
Due Date: 30/10/2025

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 30/10/2025
Subtotal: GBP 54,947.87
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 10,989.57
Total: GBP 65,937.44

Line Items
----------
Items:
  - Description Team Support Plan | Amount GBP 12,209.69
  - Description Service coverage under contract | Amount GBP 42,738.18

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D016 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2025-10-16

```
LEASE AGREEMENT / REFERENCE COPY
================================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 16/10/2025

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D016
Document Type: lease_agreement
Period: Q3 FY 2025-26

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Meridian Support LLP
Commencement Date: 16/10/2025
Term Months: 24
Monthly Payment Amount: GBP 3,844.81
Incremental Borrowing Rate: 0.09
ROU Asset Amount: GBP 84,159.61
Lease Liability Amount: GBP 84,159.61

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-24

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 24/10/2025

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0001

Terms
-----
Due Date: 04/11/2025

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 04/11/2025
Subtotal: GBP 15,498.44
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 3,099.69
Total: GBP 18,598.13

Line Items
----------
Items:
  - Description Review pack | Amount GBP 5,743.50
  - Description Follow-up support | Amount GBP 9,754.94

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D024 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2025-10-26

```
CUSTOMER INVOICE
================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 26/10/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D024
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0003

Terms
-----
Due Date: 07/11/2025

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 07/11/2025
Total: GBP 5,526.04

Line Items
----------
Items:
  - Description Monthly retainer | Amount GBP 1,534.83
  - Description Draft billing copy | Amount GBP 3,991.21

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D025 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2025-10-29

```
CANCELLATION NOTE
=================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 29/10/2025

Reference Box
-------------
Document ID: D025
Document Type: cancellation_note
Period: Q3 FY 2025-26

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
- **Date:** 2025-10-29

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 29/10/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D026
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0003

Terms
-----
Due Date: 19/11/2025

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 19/11/2025
Total: GBP 5,296.74

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 1,080.30
  - Description Reissued billing | Amount GBP 4,216.44

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-02

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 13,471.67
Draw Amount: GBP 86,831.93
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 100,303.60
Note: Scheduled lender activity for the selected period.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-07

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Pace Office Mart
Total: GBP 410.53
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount GBP 91.67
  - Description Travel Incidentals | Amount GBP 318.86
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-15

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Beacon Industrial Supply
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 60
Total: GBP 69,825.77
Paid Cash: GBP 23,707.26
Financed Amount: GBP 46,118.51
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D018 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2025-12-02

```
LEASE PAYMENT NOTICE / REFERENCE COPY
=====================================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 02/12/2025

Reference Box
-------------
Document ID: D018
Document Type: lease_payment_notice
Period: Q3 FY 2025-26

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 02/12/2025
Payment Amount: GBP 11,534.43
Interest Amount: GBP 1,893.59
Principal Amount: GBP 9,640.84

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D014 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-03

```
ASSET DISPOSAL NOTICE
=====================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 03/12/2025

Reference Box
-------------
Document ID: D014
Document Type: asset_disposal_notice
Period: Q3 FY 2025-26

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Furniture
Asset Tag: OPEN-FUR
Original Cost: GBP 8,117.44
Accumulated Depreciation: 405.87
Net Book Value: GBP 7,711.57
Proceeds Amount: GBP 9,099.65
Gain Loss Amount: GBP 1,388.08
Gain Loss Type: Gain

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D015 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-03

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 03/12/2025

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D015
Document Type: sale_proceeds_advice
Period: Q3 FY 2025-26

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Blue Finch Holdings
Asset Tag: OPEN-FUR
Proceeds Amount: GBP 9,099.65
Settlement Date: 03/12/2025
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-05

```
PAYMENT ADVICE
==============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 05/12/2025

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Metro Edge Partners
Amount: GBP 16,574.26
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-05

```
UTILITY INVOICE
===============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 05/12/2025

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: Q3 FY 2025-26

Terms
-----
Due Date: 15/12/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: Q3 FY 2025-26
Due Date: 15/12/2025
Total: GBP 1,562.19

Charges
-------
Charges:
  - Description Electricity | Amount GBP 443.64
  - Description Water | Amount GBP 1,118.55

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-19

```
PAYMENT ADVICE
==============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 19/12/2025

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: GBP 13,550.45
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D019 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-19

```
TRANSFER ADVICE
===============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 19/12/2025

Reference Box
-------------
Document ID: D019
Document Type: transfer_advice
Period: Q3 FY 2025-26
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: GBP 15,865.18
Transfer Date: 19/12/2025
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-12-21

```
PAYROLL SUMMARY
===============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 21/12/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q3 FY 2025-26
Headcount: 11
Gross Pay: GBP 17,741.68
Employer Tax: 2,460.79
Cash Outflow: GBP 20,202.47

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 31/12/2025

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q3 FY 2025-26
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: GBP 2,521.00

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Furniture
Asset Tag: OPEN-FUR
Cost: GBP 8,117.44
Useful Life Months: 60
Current Period Charge: GBP 405.87
Accumulated Depreciation: 405.87
```

### Document D017 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D017
Document Type: lease_amortization_schedule
Period: Q3 FY 2025-26

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: GBP 84,159.61
Payment Amount: GBP 11,534.43
Interest Amount: GBP 1,893.59
Principal Amount: GBP 9,640.84
Ending Liability Balance: GBP 74,518.77
ROU Amortization Amount: GBP 10,519.95

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D022 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D022
Document Type: revenue_recognition_schedule
Period: Q3 FY 2025-26

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: Q3 FY 2025-26
Opening Deferred: GBP 54,947.87
Added Deferred: GBP 0.00
Released This Period: 27,473.94
Ending Deferred: GBP 27,473.93

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D023 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 31/12/2025

Reference Box
-------------
Document ID: D023
Document Type: service_period_memo
Period: Q3 FY 2025-26
Reference: Q3 FY 2025-26

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q3 FY 2025-26
Recognized Amount: GBP 1,574.66

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D027 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 31/12/2025

Reference Box
-------------
Document ID: D027
Document Type: bank_statement
Period: Q3 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0008
Statement Currency: GBP
Opening Balance: GBP 38,169.47
Closing Balance: GBP 57,842.00

Statement Rows
--------------
Rows:
  - Date 04/10/2025 | Description Rent prepayment PRE-0001 | Amount GBP -7,562.99 | Running 
Balance GBP 30,606.48
  - Date 02/11/2025 | Description Loan draw LOAN-0001 | Amount GBP 86,831.93 | Running 
Balance GBP 117,438.41
  - Date 07/11/2025 | Description Pace Office Mart receipt RCPT-0001 | Amount GBP -410.53 | 
Running Balance GBP 117,027.88
  - Date 15/11/2025 | Description Asset purchase ASSET-0001 | Amount GBP -23,707.26 | 
Running Balance GBP 93,320.62
  - Date 02/12/2025 | Description Lease payment LEASE-0001 | Amount GBP -11,534.43 | Running
 Balance GBP 81,786.19
  - Date 03/12/2025 | Description Asset sale OPEN-FUR | Amount GBP 9,099.65 | Running 
Balance GBP 90,885.84
  - Date 05/12/2025 | Description Customer settlement INV-0001 | Amount GBP 16,574.26 | 
Running Balance GBP 107,460.10
  - Date 19/12/2025 | Description Supplier settlement BILL-0001 | Amount GBP -13,550.45 | 
Running Balance GBP 93,909.65
  - Date 19/12/2025 | Description Transfer out TRX-0001 | Amount GBP -15,865.18 | Running 
Balance GBP 78,044.47
  - Date 21/12/2025 | Description Payroll PAYRUN-0001 | Amount GBP -20,202.47 | Running 
Balance GBP 57,842.00

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D027
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
Summit Manufacturing
18 Marina Avenue, Chennai
Date: 31/12/2025

Reference Box
-------------
Document ID: D028
Document Type: bank_statement
Period: Q3 FY 2025-26

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-0899
Statement Currency: GBP
Opening Balance: GBP 0.00
Closing Balance: GBP 15,865.18

Statement Rows
--------------
Rows:
  - Date 19/12/2025 | Description Transfer in TRX-0001 | Amount GBP 15,865.18 | Running 
Balance GBP 15,865.18

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D028
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 15,498.44 | D002 | 2025-10-24 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 3,099.69 | D002 | 2025-10-24 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 15,875.69 | D003 | 2025-10-08 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 3,175.14 | D003 | 2025-10-08 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 410.53 | D004 | 2025-11-07 | expense_receipt |
| 6 | Cash | Accounts Receivable | 16,574.26 | D005, D002 | 2025-12-05 | customer_payment |
| 7 | Accounts Payable | Cash | 13,550.45 | D006, D003 | 2025-12-19 | supplier_payment |
| 8 | Salaries Expense | Cash | 17,741.68 | D007 | 2025-12-21 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 2,460.79 | D007 | 2025-12-21 | payroll_tax |
| 10 | Prepaid Rent | Cash | 7,562.99 | D008 | 2025-10-04 | prepaid_rent_purchase |
| 11 | Rent Expense | Prepaid Rent | 2,521.00 | D008, D009 | 2025-12-31 | prepaid_rent_release |
| 12 | Utilities Expense | Accounts Payable | 1,562.19 | D010 | 2025-12-05 | utilities_bill |
| 13 | Cash | Loans Payable | 86,831.93 | D011 | 2025-11-02 | loan_draw |
| 14 | Equipment | Cash | 23,707.26 | D012 | 2025-11-15 | equipment_purchase_cash |
| 15 | Equipment | Notes Payable | 46,118.51 | D012 | 2025-11-15 | equipment_purchase_financed |
| 16 | Depreciation Expense | Accumulated Depreciation | 405.87 | D013 | 2025-12-31 | depreciation |
| 17 | Cash | Furniture | 9,099.65 | D014, D015 | 2025-12-03 | asset_disposal_proceeds |
| 18 | Accumulated Depreciation | Furniture | 405.87 | D014, D015 | 2025-12-03 | asset_disposal_remove_accumulated_depreciation |
| 19 | Furniture | Gain on Disposal | 1,388.08 | D014, D015 | 2025-12-03 | asset_disposal_gain |
| 20 | Right-of-Use Asset | Lease Liability | 84,159.61 | D016 | 2025-10-16 | baseline_lease_initial_recognition |
| 21 | Lease Liability | Cash | 9,640.84 | D016, D017, D018 | 2025-12-02 | baseline_lease_principal |
| 22 | Lease Interest Expense | Cash | 1,893.59 | D016, D017, D018 | 2025-12-02 | baseline_lease_interest |
| 23 | Lease Amortization Expense | Right-of-Use Asset | 10,519.95 | D016, D017 | 2025-12-31 | baseline_lease_amortization |
| 24 | Reserve Cash | Cash | 15,865.18 | D019 | 2025-12-19 | interbank_transfer |
| 25 | Accounts Receivable | Unearned Revenue | 54,947.87 | D020, D021 | 2025-10-15 | retainer_invoice |
| 26 | Accounts Receivable | Sales Tax Payable | 10,989.57 | D020, D021 | 2025-10-15 | retainer_invoice_tax |
| 27 | Unearned Revenue | Service Revenue | 27,473.94 | D022, D021 | 2025-12-31 | retainer_release |
| 28 | Utilities Expense | Accrued Expenses | 1,574.66 | D023 | 2025-12-31 | expense_accrual |
| 29 | Accounts Receivable | Service Revenue | 5,296.74 | D024, D025, D026 | 2025-10-29 | reissued_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 57,842.00
- Accounts Receivable: 76,575.10
- Prepaid Rent: 9,211.20
- Prepaid Insurance: 1,649.05
- Office Supplies: 2,330.49
- Equipment: 81,121.75
- Input Tax Receivable: 3,175.14
- Right-of-Use Asset: 73,639.66
- Reserve Cash: 15,865.18

**Liabilities**
- Accounts Payable: 12,275.52
- Accrued Expenses: 4,260.14
- Unearned Revenue: 31,977.17
- Loans Payable: 91,572.44
- Notes Payable: 54,343.41
- Sales Tax Payable: 14,089.26
- Lease Liability: 74,518.77

**Equity**
- Retained Earnings: -643.56
- Owner's Equity: 39,016.42

**Totals:** Assets = 321,409.57; Liabilities = 283,036.71; Equity = 38,372.86
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
