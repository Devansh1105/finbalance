# Verification Packet — COV_PRO_M5_0004

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** January 2025
- **Period start → end:** 2025-01-01 → 2025-01-31
- **Entity:** Silverline Distribution
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 30
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 30,912.63
- Accounts Receivable: 1,951.95
- Prepaid Rent: 2,353.97
- Office Supplies: 340.13
- Equipment: 5,853.80

**Liabilities**
- Accounts Payable: 2,825.82
- Accrued Expenses: 1,076.54
- Loans Payable: 3,873.97

**Equity**
- Retained Earnings: 9,509.56
- Owner's Equity: 24,126.59


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
  - Section assets | Account Cash | Amount EUR 30.912,63
  - Section assets | Account Accounts Receivable | Amount EUR 1.951,95
  - Section assets | Account Prepaid Rent | Amount EUR 2.353,97
  - Section assets | Account Office Supplies | Amount EUR 340,13
  - Section assets | Account Equipment | Amount EUR 5.853,80
  - Section liabilities | Account Accounts Payable | Amount EUR 2.825,82
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.076,54
  - Section liabilities | Account Loans Payable | Amount EUR 3.873,97
  - Section equity | Account Retained Earnings | Amount EUR 9.509,56
  - Section equity | Account Owner's Equity | Amount EUR 24.126,59

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Vertex Supply Co.
Property: Park Lane Residences
Service Start: 01/01/2025
Service End: 31/03/2025
Total: EUR 3.364,42
Monthly Amount: EUR 1.121,47

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
INSURANCE NOTICE
================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 01/01/2025

To
--
Marina Assurance
Vendor remittance address on file

Terms
-----
Service Start: 01/01/2025
Service End: 31/03/2025

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Marina Assurance
Covered Item: Marina Heights
Coverage Start: 01/01/2025
Coverage End: 31/03/2025
Total Premium: EUR 7.088,98
Monthly Amount: EUR 2.362,99

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D022 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2025-01-06

```
LEASE AGREEMENT / REFERENCE COPY
================================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 06/01/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: January 2025

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Vertex Supply Co.
Commencement Date: 06/01/2025
Term Months: 24
Monthly Payment Amount: EUR 2.772,50
Incremental Borrowing Rate: 0,06
ROU Asset Amount: EUR 62.555,55
Lease Liability Amount: EUR 62.555,55

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-07

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 07/01/2025

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: January 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 28/01/2025

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 28/01/2025
Subtotal: EUR 7.426,11
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 612,65
Total: EUR 8.038,76

Line Items
----------
Items:
  - Description Consulting sprint | Amount EUR 1.769,86
  - Description Follow-up support | Amount EUR 5.656,25

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-07

```
VENDOR INVOICE
==============

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 07/01/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: January 2025

Terms
-----
Due Date: 22/01/2025

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 22/01/2025
Subtotal: EUR 7.618,85
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 552,37
Total: EUR 8.171,22

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 2.254,92
  - Description Support fee | Amount EUR 5.363,93

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-11

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: Delivery van
Asset Tag: TAG-0001
Useful Life Months: 60
Total: EUR 16.906,88
Paid Cash: EUR 5.616,57
Financed Amount: EUR 11.290,31
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-01-19

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: EUR 294,91
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount EUR 110,97
  - Description Travel Incidentals | Amount EUR 183,94
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-21

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: EUR 2.212,94
Draw Amount: EUR 24.317,53
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 26.530,47
Note: Scheduled lender activity for the selected period.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-23

```
PAYMENT ADVICE
==============

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 23/01/2025

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: January 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Pace Office Mart
Amount: EUR 5.850,54
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-01-23

```
PAYROLL SUMMARY
===============

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 23/01/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: January 2025
Headcount: 11
Gross Pay: EUR 11.044,89
Employer Tax: 1.322,33
Cash Outflow: EUR 12.367,22

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-25

```
PAYMENT ADVICE
==============

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 25/01/2025

To
--
Aster Point Services

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: January 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: EUR 4.654,97
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-25

```
UTILITY INVOICE
===============

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 25/01/2025

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: January 2025

Terms
-----
Due Date: 01/02/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: January 2025
Due Date: 01/02/2025
Total: EUR 1.133,87

Charges
-------
Charges:
  - Description Electricity | Amount EUR 373,34
  - Description Water | Amount EUR 760,53

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-26

```
TRANSFER ADVICE
===============

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 26/01/2025

Reference Box
-------------
Document ID: D028
Document Type: transfer_advice
Period: January 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: EUR 11.179,66
Transfer Date: 26/01/2025
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D028
```

### Document D024 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2025-01-27

```
LEASE PAYMENT NOTICE / REFERENCE COPY
=====================================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 27/01/2025

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: January 2025

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 27/01/2025
Payment Amount: EUR 2.772,50
Interest Amount: EUR 312,78
Principal Amount: EUR 2.459,72

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-27

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: EUR 14.894,16
Draw Amount: EUR 0,00
Principal Paid: EUR 8.534,53
Interest Paid: EUR 1.152,86
Ending Principal: EUR 6.359,63
Note: Scheduled lender activity for the selected period.
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-01-28

```
ASSET DISPOSAL NOTICE
=====================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 28/01/2025

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: January 2025

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Delivery van
Asset Tag: TAG-0001
Original Cost: EUR 16.906,88
Accumulated Depreciation: 281,78
Net Book Value: EUR 16.625,10
Proceeds Amount: EUR 19.617,62
Gain Loss Amount: EUR 2.992,52
Gain Loss Type: Gain

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-28

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 28/01/2025

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: January 2025

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Oak Harbor Foods
Asset Tag: TAG-0001
Proceeds Amount: EUR 19.617,62
Settlement Date: 28/01/2025
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-01-29

```
LEASE MODIFICATION NOTICE / REFERENCE COPY
==========================================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 29/01/2025

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: January 2025

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 29/01/2025
Old Liability Balance: EUR 60.095,83
Remeasured Liability Balance: EUR 70.767,82
Liability Remeasurement Delta Amount: EUR 10.671,99
ROU Asset Adjustment Amount: EUR 10.671,99

Narrative
---------
Details: Lease term extension remeasures the liability; the ROU asset is adjusted by the 
same amount.

Footer
------
Generated for synthetic accounting research use.
Page marker: D025
```

### Document D026 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `support_doc`
- **Date:** 2025-01-29

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 29/01/2025

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: January 2025

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: EUR 70.767,82
Payment Amount: EUR 0,00
Interest Amount: EUR 0,00
Principal Amount: EUR 0,00
Ending Liability Balance: EUR 70.767,82
ROU Amortization Amount: EUR 0,00

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-01-31

```
SERVICE PERIOD MEMO
===================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 31/01/2025

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: January 2025
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: EUR 1.121,47

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D011 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-01-31

```
SERVICE PERIOD MEMO
===================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 31/01/2025

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: January 2025
Reference: PRE-0002

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0002
Subject: Insurance coverage release
Reference: PRE-0002
Recognized Amount: EUR 2.362,99

Explanation
-----------
Narrative: One month of insurance coverage has expired and should be expensed this period.

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D015 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-01-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Delivery van
Asset Tag: TAG-0001
Cost: EUR 16.906,88
Useful Life Months: 60
Current Period Charge: EUR 281,78
Accumulated Depreciation: 281,78
```

### Document D018 — Tax Depreciation Schedule

- **Type:** `tax_depreciation_schedule`
- **Role:** `support_doc`
- **Date:** 2025-01-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 31/01/2025

Reference Box
-------------
Document ID: D018
Document Type: tax_depreciation_schedule
Period: January 2025

Book Tax Difference
-------------------
Schedule ID: TAXDEP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: EUR 281,78
Tax Depreciation Amount: EUR 533,97
Temporary Difference Amount: EUR 252,19
Tax Rate: 25.00%

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-01-31

```
DEFERRED TAX MEMO
=================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 31/01/2025

Reference Box
-------------
Document ID: D019
Document Type: deferred_tax_memo
Period: January 2025

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0001
Asset Tag: TAG-0001
Opening Deferred Tax Liability: EUR 0,00
Current Period Deferred Tax Movement: EUR 63,05
Deferred Tax Liability Ending: EUR 63,05
Deferred Tax Expense Amount: EUR 63,05

Narrative
---------
Details: Tax depreciation exceeds book depreciation, creating a taxable temporary 
difference.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D020 — Tax Depreciation Schedule

- **Type:** `tax_depreciation_schedule`
- **Role:** `support_doc`
- **Date:** 2025-01-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 31/01/2025

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: January 2025

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: EUR 16.625,10
Tax Depreciation Amount: EUR 17.814,66
Temporary Difference Amount: EUR 1.189,56
Tax Rate: 25.00%

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D021 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-01-31

```
DEFERRED TAX MEMO
=================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 31/01/2025

Reference Box
-------------
Document ID: D021
Document Type: deferred_tax_memo
Period: January 2025

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0002
Asset Tag: TAG-0001
Opening Deferred Tax Liability: EUR 0,00
Current Period Deferred Tax Movement: EUR 297,39
Deferred Tax Liability Ending: EUR 297,39
Deferred Tax Expense Amount: EUR 297,39

Narrative
---------
Details: Deferred tax movement recorded after combining disposal proceeds with the tax-basis
 difference.

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D023 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-01-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 31/01/2025

Reference Box
-------------
Document ID: D023
Document Type: lease_amortization_schedule
Period: January 2025

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: EUR 62.555,55
Payment Amount: EUR 2.772,50
Interest Amount: EUR 312,78
Principal Amount: EUR 2.459,72
Ending Liability Balance: EUR 60.095,83
ROU Amortization Amount: EUR 2.606,48

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D029 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-01-31

```
BANK STATEMENT
==============

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Document Date: 31/01/2025

Reference Box
-------------
Document ID: D029
Document Type: bank_statement
Period: January 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0004
Statement Currency: EUR
Opening Balance: EUR 30.912,63
Closing Balance: EUR 21.280,56

Statement Rows
--------------
Rows:
  - Date 01/01/2025 | Description Insurance coverage prepayment PRE-0002 | Amount EUR 
-7.088,98 | Running Balance EUR 23.823,65
  - Date 01/01/2025 | Description Rent prepayment PRE-0001 | Amount EUR -3.364,42 | Running 
Balance EUR 20.459,23
  - Date 11/01/2025 | Description Asset purchase ASSET-0001 | Amount EUR -5.616,57 | Running
 Balance EUR 14.842,66
  - Date 19/01/2025 | Description Oakline Services receipt RCPT-0001 | Amount EUR -294,91 | 
Running Balance EUR 14.547,75
  - Date 21/01/2025 | Description Loan draw LOAN-0001 | Amount EUR 24.317,53 | Running 
Balance EUR 38.865,28
  - Date 23/01/2025 | Description Payroll PAYRUN-0001 | Amount EUR -12.367,22 | Running 
Balance EUR 26.498,06
  - Date 23/01/2025 | Description Supplier settlement BILL-0001 | Amount EUR -5.850,54 | 
Running Balance EUR 20.647,52
  - Date 25/01/2025 | Description Customer settlement INV-0001 | Amount EUR 4.654,97 | 
Running Balance EUR 25.302,49
  - Date 26/01/2025 | Description Transfer out TRX-0001 | Amount EUR -11.179,66 | Running 
Balance EUR 14.122,83
  - Date 27/01/2025 | Description Lease payment LEASE-0001 | Amount EUR -2.772,50 | Running 
Balance EUR 11.350,33
  - Date 27/01/2025 | Description Loan payment LOAN-0002 | Amount EUR -9.687,39 | Running 
Balance EUR 1.662,94
  - Date 28/01/2025 | Description Asset sale TAG-0001 | Amount EUR 19.617,62 | Running 
Balance EUR 21.280,56

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D030 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-01-31

```
BANK STATEMENT
==============

From
----
Silverline Distribution
90 Hill Park, Hyderabad
Date: 31/01/2025

Reference Box
-------------
Document ID: D030
Document Type: bank_statement
Period: January 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-0499
Statement Currency: EUR
Opening Balance: EUR 0,00
Closing Balance: EUR 11.179,66

Statement Rows
--------------
Rows:
  - Date 26/01/2025 | Description Transfer in TRX-0001 | Amount EUR 11.179,66 | Running 
Balance EUR 11.179,66

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D030
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 7,426.11 | D002 | 2025-01-07 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 612.65 | D002 | 2025-01-07 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 7,618.85 | D003 | 2025-01-07 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 552.37 | D003 | 2025-01-07 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 294.91 | D004 | 2025-01-19 | expense_receipt |
| 6 | Cash | Accounts Receivable | 4,654.97 | D005, D002 | 2025-01-25 | customer_payment |
| 7 | Accounts Payable | Cash | 5,850.54 | D006, D003 | 2025-01-23 | supplier_payment |
| 8 | Salaries Expense | Cash | 11,044.89 | D007 | 2025-01-23 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 1,322.33 | D007 | 2025-01-23 | payroll_tax |
| 10 | Prepaid Rent | Cash | 3,364.42 | D008 | 2025-01-01 | prepaid_rent_purchase |
| 11 | Rent Expense | Prepaid Rent | 1,121.47 | D008, D009 | 2025-01-31 | prepaid_rent_release |
| 12 | Prepaid Insurance | Cash | 7,088.98 | D010 | 2025-01-01 | prepaid_insurance_purchase |
| 13 | Insurance Expense | Prepaid Insurance | 2,362.99 | D010, D011 | 2025-01-31 | prepaid_insurance_release |
| 14 | Utilities Expense | Accounts Payable | 1,133.87 | D012 | 2025-01-25 | utilities_bill |
| 15 | Cash | Loans Payable | 24,317.53 | D013 | 2025-01-21 | loan_draw |
| 16 | Equipment | Cash | 5,616.57 | D014 | 2025-01-11 | equipment_purchase_cash |
| 17 | Equipment | Notes Payable | 11,290.31 | D014 | 2025-01-11 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 281.78 | D015 | 2025-01-31 | depreciation |
| 19 | Cash | Equipment | 19,617.62 | D016, D017 | 2025-01-28 | asset_disposal_proceeds |
| 20 | Accumulated Depreciation | Equipment | 281.78 | D016, D017 | 2025-01-28 | asset_disposal_remove_accumulated_depreciation |
| 21 | Equipment | Gain on Disposal | 2,992.52 | D016, D017 | 2025-01-28 | asset_disposal_gain |
| 22 | Deferred Tax Expense | Deferred Tax Liability | 63.05 | D018, D019 | 2025-01-31 | deferred_tax_depreciation |
| 23 | Deferred Tax Expense | Deferred Tax Liability | 297.39 | D016, D017, D020, D021 | 2025-01-31 | asset_disposal_with_deferred_tax |
| 24 | Right-of-Use Asset | Lease Liability | 62,555.55 | D022 | 2025-01-06 | baseline_lease_initial_recognition |
| 25 | Lease Liability | Cash | 2,459.72 | D022, D023, D024 | 2025-01-27 | baseline_lease_principal |
| 26 | Lease Interest Expense | Cash | 312.78 | D022, D023, D024 | 2025-01-27 | baseline_lease_interest |
| 27 | Lease Amortization Expense | Right-of-Use Asset | 2,606.48 | D022, D023 | 2025-01-31 | baseline_lease_amortization |
| 28 | Right-of-Use Asset | Lease Liability | 10,671.99 | D025, D026 | 2025-01-29 | lease_modification |
| 29 | Loans Payable | Cash | 8,534.53 | D027 | 2025-01-27 | loan_repayment_principal |
| 30 | Interest Expense | Cash | 1,152.86 | D027 | 2025-01-27 | loan_repayment_interest |
| 31 | Reserve Cash | Cash | 11,179.66 | D028 | 2025-01-26 | interbank_transfer |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 21,280.56
- Accounts Receivable: 5,335.74
- Prepaid Rent: 4,596.92
- Office Supplies: 340.13
- Equipment: 5,853.80
- Input Tax Receivable: 552.37
- Prepaid Insurance: 4,725.99
- Right-of-Use Asset: 70,621.06
- Reserve Cash: 11,179.66

**Liabilities**
- Accounts Payable: 6,280.37
- Accrued Expenses: 1,076.54
- Loans Payable: 19,656.97
- Sales Tax Payable: 612.65
- Notes Payable: 11,290.31
- Deferred Tax Liability: 360.44
- Lease Liability: 70,767.82

**Equity**
- Retained Earnings: -9,685.46
- Owner's Equity: 24,126.59

**Totals:** Assets = 124,486.23; Liabilities = 110,045.10; Equity = 14,441.13
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
- Notes: Checks out.
