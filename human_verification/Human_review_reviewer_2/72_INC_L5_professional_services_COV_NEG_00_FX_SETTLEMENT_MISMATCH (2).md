# Verification Packet — COV_NEG_00_FX_SETTLEMENT_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q4 FY 2026-27
- **Period start → end:** 2026-01-01 → 2026-03-31
- **Entity:** Beacon Retail Group
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `vat`
- **Document count:** 42
- **Labeled as inconsistent:** True
- **Inconsistency codes:** fx_settlement_mismatch
- **Inconsistency reasons:** Foreign-currency settlement support does not reconcile booked amount, paid amount, and FX difference.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2026-01-01_

**Assets**
- Cash: 43,142.09
- Accounts Receivable: 8,380.81
- Prepaid Rent: 4,509.63
- Prepaid Insurance: 3,450.40
- Office Supplies: 1,449.37
- Equipment: 13,256.03
- Furniture: 4,249.90

**Liabilities**
- Accounts Payable: 3,053.50
- Accrued Expenses: 2,512.18
- Unearned Revenue: 2,587.34
- Loans Payable: 4,763.09
- Notes Payable: 8,896.03

**Equity**
- Retained Earnings: 9,264.36
- Owner's Equity: 47,361.73


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2026-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2026
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 43.142,09
  - Section assets | Account Accounts Receivable | Amount EUR 8.380,81
  - Section assets | Account Prepaid Rent | Amount EUR 4.509,63
  - Section assets | Account Prepaid Insurance | Amount EUR 3.450,40
  - Section assets | Account Office Supplies | Amount EUR 1.449,37
  - Section assets | Account Equipment | Amount EUR 13.256,03
  - Section assets | Account Furniture | Amount EUR 4.249,90
  - Section liabilities | Account Accounts Payable | Amount EUR 3.053,50
  - Section liabilities | Account Accrued Expenses | Amount EUR 2.512,18
  - Section liabilities | Account Unearned Revenue | Amount EUR 2.587,34
  - Section liabilities | Account Loans Payable | Amount EUR 4.763,09
  - Section liabilities | Account Notes Payable | Amount EUR 8.896,03
  - Section equity | Account Retained Earnings | Amount EUR 9.264,36
  - Section equity | Account Owner's Equity | Amount EUR 47.361,73

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-06

```
CUSTOMER INVOICE
================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 06/01/2026

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q4 FY 2026-27
Contract Ref: CTR-0001

Terms
-----
Due Date: 25/01/2026

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 25/01/2026
Subtotal: EUR 18.079,07
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: EUR 1.807,91
Total: EUR 19.886,98

Line Items
----------
Items:
  - Description Consulting sprint | Amount EUR 6.505,73
  - Description Follow-up support | Amount EUR 11.573,34

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2026-01-06

```
INSURANCE NOTICE
================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 06/01/2026

To
--
Shield Mutual
Vendor remittance address on file

Terms
-----
Service Start: 06/01/2026
Service End: 05/04/2026

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Shield Mutual
Covered Item: Harbor View Offices
Coverage Start: 06/01/2026
Coverage End: 05/04/2026
Total Premium: EUR 17.976,60
Monthly Amount: EUR 5.992,20

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D029 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2026-01-07

```
RETAINER AGREEMENT MEMO
=======================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 07/01/2026

Reference Box
-------------
Document ID: D029
Document Type: retainer_agreement_memo
Period: Q4 FY 2026-27
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 3
Total Contract Value: EUR 91.304,29

Explanation
-----------
Narrative: Customer Aster Point Services agreed to a service package spanning 3 months.

Footer
------
Internal document packet copy.
Page marker: D029
```

### Document D030 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-07

```
CUSTOMER INVOICE
================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 07/01/2026

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D030
Document Type: customer_invoice
Period: Q4 FY 2026-27
Contract Ref: CTR-0002

Terms
-----
Due Date: 19/01/2026

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 19/01/2026
Subtotal: EUR 83.003,90
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: EUR 8.300,39
Total: EUR 91.304,29

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount EUR 24.503,83
  - Description Service coverage under contract | Amount EUR 58.500,07

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2026-01-08

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Oakline Services
Property: Marina Heights
Service Start: 08/01/2026
Service End: 07/04/2026
Total: EUR 13.475,26
Monthly Amount: EUR 4.491,75

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D022 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2026-01-10

```
LEASE AGREEMENT / REFERENCE COPY
================================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 10/01/2026

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: Q4 FY 2026-27

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Prime Utility Desk
Commencement Date: 10/01/2026
Term Months: 36
Monthly Payment Amount: EUR 8.127,61
Incremental Borrowing Rate: 0,09
ROU Asset Amount: EUR 255.587,37
Lease Liability Amount: EUR 255.587,37

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D038 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-11

```
CUSTOMER INVOICE
================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 11/01/2026

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D038
Document Type: customer_invoice
Period: Q4 FY 2026-27
Contract Ref: FXCTR-0001

Terms
-----
Due Date: 29/01/2026

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: FXCTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: FXINV-0001
Due Date: 29/01/2026
Total: GBP 16,509.22

Line Items
----------
Items:
  - Description Review pack | Amount GBP 3,679.38
  - Description Foreign-currency support | Amount GBP 12,829.84

Footer
------
Generated for synthetic accounting research use.
Page marker: D038
```

### Document D039 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2026-01-11

```
EXCHANGE RATE NOTICE
====================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 11/01/2026

Reference Box
-------------
Document ID: D039
Document Type: exchange_rate_notice
Period: Q4 FY 2026-27
Reference: FXINV-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXINV-0001
Rate Date: 11/01/2026
Rate Type: Spot rate at invoice date

Conversion Details
------------------
Source Currency: GBP
Source Amount: GBP 16,509.22
Functional Currency: EUR
Exchange Rate: 0.8978
Functional Amount: EUR 14.821,98

Footer
------
Internal document packet copy.
Page marker: D039
```

### Document D035 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2026-01-19

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 19/01/2026

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D035
Document Type: customer_invoice
Period: Q4 FY 2026-27
Contract Ref: CTR-0003

Terms
-----
Due Date: 09/02/2026

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 09/02/2026
Total: EUR 24.271,74

Line Items
----------
Items:
  - Description Implementation work | Amount EUR 10.413,41
  - Description Draft billing copy | Amount EUR 13.858,33

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Internal document packet copy.
Page marker: D035
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-22

```
VENDOR INVOICE
==============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 22/01/2026

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q4 FY 2026-27

Terms
-----
Due Date: 11/02/2026

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 11/02/2026
Subtotal: EUR 7.039,44
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: EUR 1.407,89
Total: EUR 8.447,33

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 2.264,90
  - Description Support fee | Amount EUR 4.774,54

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D036 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2026-01-23

```
CANCELLATION NOTE
=================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 23/01/2026

Reference Box
-------------
Document ID: D036
Document Type: cancellation_note
Period: Q4 FY 2026-27

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
Generated for synthetic accounting research use.
Page marker: D036
```

### Document D037 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-01-23

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 23/01/2026

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D037
Document Type: customer_invoice
Period: Q4 FY 2026-27
Contract Ref: CTR-0003

Terms
-----
Due Date: 08/02/2026

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 08/02/2026
Total: EUR 23.754,05

Line Items
----------
Items:
  - Description Support package | Amount EUR 10.220,26
  - Description Reissued billing | Amount EUR 13.533,79

Footer
------
Internal document packet copy.
Page marker: D037
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2026-02-05

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: EUR 718,38
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount EUR 234,70
  - Description Travel Incidentals | Amount EUR 483,68
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2026-02-26

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Beacon Industrial Supply
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 36
Total: EUR 29.638,96
Paid Cash: EUR 9.305,11
Financed Amount: EUR 20.333,85
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-02-27

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: EUR 2.701,73
Draw Amount: EUR 56.062,21
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 58.763,94
Note: Scheduled lender activity for the selected period.
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-03

```
ASSET DISPOSAL NOTICE
=====================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 03/03/2026

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: Q4 FY 2026-27

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Original Cost: EUR 13.256,03
Accumulated Depreciation: 828,51
Net Book Value: EUR 12.427,52
Proceeds Amount: EUR 14.664,47
Gain Loss Amount: EUR 2.236,95
Gain Loss Type: Gain

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-03

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 03/03/2026

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: Q4 FY 2026-27

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Oak Harbor Foods
Asset Tag: OPEN-EQU
Proceeds Amount: EUR 14.664,47
Settlement Date: 03/03/2026
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2026-03-05

```
UTILITY INVOICE
===============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 05/03/2026

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: Q4 FY 2026-27

Terms
-----
Due Date: 12/03/2026

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: Q4 FY 2026-27
Due Date: 12/03/2026
Total: EUR 898,66

Charges
-------
Charges:
  - Description Electricity | Amount EUR 376,47
  - Description Water | Amount EUR 522,19

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-06

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 06/03/2026

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: EUR 4.827,82
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D040 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `posting_doc`
- **Date:** 2026-03-06

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 06/03/2026

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D040
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: FXINV-0001

Payment Details
---------------
Advice Number: FXPAY-0001
Counterparty: Oak Harbor Foods
Currency: EUR
Amount: EUR 15.023,39
Reference: FXINV-0001
Payment Method: Bank transfer
Payment For: Foreign-currency receivable settlement

Foreign Currency Details
------------------------
Source Amount: GBP 16,509.22
Source Currency: GBP
Functional Currency: EUR
Functional Amount: EUR 12.347,69
Exchange Rate: 0.9100
FX Difference: 201,41

Footer
------
Generated for synthetic accounting research use.
Page marker: D040
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-08

```
TRANSFER ADVICE
===============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 08/03/2026

Reference Box
-------------
Document ID: D028
Document Type: transfer_advice
Period: Q4 FY 2026-27
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: EUR 30.652,06
Transfer Date: 08/03/2026
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-03-12

```
PAYMENT ADVICE
==============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 12/03/2026

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q4 FY 2026-27
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: EUR 16.159,84
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D024 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2026-03-15

```
LEASE PAYMENT NOTICE / REFERENCE COPY
=====================================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 15/03/2026

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: Q4 FY 2026-27

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 15/03/2026
Payment Amount: EUR 24.382,83
Interest Amount: EUR 5.750,72
Principal Amount: EUR 18.632,11

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-03-15

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: First City Bank
Opening Principal: EUR 46.794,02
Draw Amount: EUR 0,00
Principal Paid: EUR 14.032,87
Interest Paid: EUR 1.811,05
Ending Principal: EUR 32.761,15
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-03-21

```
PAYROLL SUMMARY
===============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 21/03/2026

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2026-27
Headcount: 9
Gross Pay: EUR 22.820,52
Employer Tax: 2.883,17
Cash Outflow: EUR 25.703,69

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 31/03/2026

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q4 FY 2026-27
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: EUR 4.491,75

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
- **Date:** 2026-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 31/03/2026

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: Q4 FY 2026-27
Reference: PRE-0002

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0002
Subject: Insurance coverage release
Reference: PRE-0002
Recognized Amount: EUR 5.992,20

Explanation
-----------
Narrative: One month of insurance coverage has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D015 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 13.256,03
Useful Life Months: 48
Current Period Charge: EUR 828,51
Accumulated Depreciation: 828,51
```

### Document D018 — Tax Depreciation Schedule

- **Type:** `tax_depreciation_schedule`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 31/03/2026

Reference Box
-------------
Document ID: D018
Document Type: tax_depreciation_schedule
Period: Q4 FY 2026-27

Book Tax Difference
-------------------
Schedule ID: TAXDEP-0001
Asset Tag: OPEN-EQU
Book Depreciation Amount: EUR 828,51
Tax Depreciation Amount: EUR 1.295,22
Temporary Difference Amount: EUR 466,71
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
DEFERRED TAX MEMO
=================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D019
Document Type: deferred_tax_memo
Period: Q4 FY 2026-27

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0001
Asset Tag: OPEN-EQU
Opening Deferred Tax Liability: EUR 0,00
Current Period Deferred Tax Movement: EUR 116,68
Deferred Tax Liability Ending: EUR 116,68
Deferred Tax Expense Amount: EUR 116,68

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
- **Date:** 2026-03-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 31/03/2026

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: Q4 FY 2026-27

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: OPEN-EQU
Book Depreciation Amount: EUR 12.427,52
Tax Depreciation Amount: EUR 13.190,83
Temporary Difference Amount: EUR 763,31
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
DEFERRED TAX MEMO
=================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 31/03/2026

Reference Box
-------------
Document ID: D021
Document Type: deferred_tax_memo
Period: Q4 FY 2026-27

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0002
Asset Tag: OPEN-EQU
Opening Deferred Tax Liability: EUR 0,00
Current Period Deferred Tax Movement: EUR 190,83
Deferred Tax Liability Ending: EUR 190,83
Deferred Tax Expense Amount: EUR 190,83

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
- **Date:** 2026-03-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D023
Document Type: lease_amortization_schedule
Period: Q4 FY 2026-27

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: EUR 255.587,37
Payment Amount: EUR 24.382,83
Interest Amount: EUR 5.750,72
Principal Amount: EUR 18.632,11
Ending Liability Balance: EUR 236.955,26
ROU Amortization Amount: EUR 21.298,95

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
LEASE MODIFICATION NOTICE
=========================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: Q4 FY 2026-27

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 31/03/2026
Old Liability Balance: EUR 236.955,26
Remeasured Liability Balance: EUR 275.436,86
Liability Remeasurement Delta Amount: EUR 38.481,60
ROU Asset Adjustment Amount: EUR 38.481,60

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
- **Date:** 2026-03-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: Q4 FY 2026-27

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: EUR 275.436,86
Payment Amount: EUR 0,00
Interest Amount: EUR 0,00
Principal Amount: EUR 0,00
Ending Liability Balance: EUR 275.436,86
ROU Amortization Amount: EUR 0,00

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D031 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
REVENUE RECOGNITION SCHEDULE / REFERENCE COPY
=============================================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D031
Document Type: revenue_recognition_schedule
Period: Q4 FY 2026-27

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: Q4 FY 2026-27
Opening Deferred: EUR 83.003,90
Added Deferred: EUR 0,00
Released This Period: 83.003,90
Ending Deferred: EUR 0,00

Footer
------
Generated for synthetic accounting research use.
Page marker: D031
```

### Document D032 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 31/03/2026

Reference Box
-------------
Document ID: D032
Document Type: service_period_memo
Period: Q4 FY 2026-27
Reference: Q4 FY 2026-27

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q4 FY 2026-27
Recognized Amount: EUR 2.037,20

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D032
```

### Document D033 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
AR AGING SUMMARY
================

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D033
Document Type: ar_aging_summary
Period: Q4 FY 2026-27

Aging Summary
-------------
Summary ID: AGING-0001
Period: Q4 FY 2026-27
Total Open: EUR 3.727,14

Customer Lines
--------------
Lines:
  - Customer Oak Harbor Foods | Reference INV-0001 | Current EUR 2.446,35 | Past Due 
1.280,79

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Generated for synthetic accounting research use.
Page marker: D033
```

### Document D034 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
CREDIT MEMO
===========

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 31/03/2026

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D034
Document Type: credit_memo
Period: Q4 FY 2026-27
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Oak Harbor Foods
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: EUR 1.280,79

Footer
------
Internal document packet copy.
Page marker: D034
```

### Document D041 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Date: 31/03/2026

Reference Box
-------------
Document ID: D041
Document Type: bank_statement
Period: Q4 FY 2026-27

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: EUR
Opening Balance: EUR 43.142,09
Closing Balance: EUR 2.166,33

Statement Rows
--------------
Rows:
  - Date 06/01/2026 | Description Insurance coverage prepayment PRE-0002 | Amount EUR 
-17.976,60 | Running Balance EUR 25.165,49
  - Date 08/01/2026 | Description Rent prepayment PRE-0001 | Amount EUR -13.475,26 | Running
 Balance EUR 11.690,23
  - Date 05/02/2026 | Description Oakline Services receipt RCPT-0001 | Amount EUR -718,38 | 
Running Balance EUR 10.971,85
  - Date 26/02/2026 | Description Asset purchase ASSET-0001 | Amount EUR -9.305,11 | Running
 Balance EUR 1.666,74
  - Date 27/02/2026 | Description Loan draw LOAN-0001 | Amount EUR 56.062,21 | Running 
Balance EUR 57.728,95
  - Date 03/03/2026 | Description Asset sale OPEN-EQU | Amount EUR 14.664,47 | Running 
Balance EUR 72.393,42
  - Date 06/03/2026 | Description Foreign receipt FXINV-0001 | Amount EUR 15.023,39 | 
Running Balance EUR 87.416,81
  - Date 06/03/2026 | Description Supplier settlement BILL-0001 | Amount EUR -4.827,82 | 
Running Balance EUR 82.588,99
  - Date 08/03/2026 | Description Transfer out TRX-0001 | Amount EUR -30.652,06 | Running 
Balance EUR 51.936,93
  - Date 12/03/2026 | Description Customer settlement INV-0001 | Amount EUR 16.159,84 | 
Running Balance EUR 68.096,77
  - Date 15/03/2026 | Description Lease payment LEASE-0001 | Amount EUR -24.382,83 | Running
 Balance EUR 43.713,94
  - Date 15/03/2026 | Description Loan payment LOAN-0002 | Amount EUR -15.843,92 | Running 
Balance EUR 27.870,02
  - Date 21/03/2026 | Description Payroll PAYRUN-0001 | Amount EUR -25.703,69 | Running 
Balance EUR 2.166,33

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D041
```

### Document D042 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Beacon Retail Group
18 Marina Avenue, Chennai
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D042
Document Type: bank_statement
Period: Q4 FY 2026-27

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: EUR
Opening Balance: EUR 0,00
Closing Balance: EUR 30.652,06

Statement Rows
--------------
Rows:
  - Date 08/03/2026 | Description Transfer in TRX-0001 | Amount EUR 30.652,06 | Running 
Balance EUR 30.652,06

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D042
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
- [x] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [x] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:  Missing from section 5: DR Office Supplies Expense / CR Accounts Payable 8.45

### Q3 — Are entries complete?
Are there any entries you would book that are MISSING from section 5? Or any entries in section 5 that should NOT be there?
- [ ] Complete and exact
- [x] Missing entries (list them in notes)
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

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `fx_settlement_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
