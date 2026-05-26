# Verification Packet — COV_PRO_Q5_0009

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q2 FY 2024
- **Period start → end:** 2024-04-01 → 2024-06-30
- **Entity:** Summit Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 42
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 48,465.28
- Accounts Receivable: 9,604.95
- Prepaid Rent: 4,129.88
- Prepaid Insurance: 2,084.58
- Office Supplies: 1,452.11
- Equipment: 15,794.96
- Furniture: 6,405.29

**Liabilities**
- Accounts Payable: 5,454.96
- Accrued Expenses: 2,546.60
- Unearned Revenue: 6,147.22
- Loans Payable: 10,494.90
- Notes Payable: 8,520.43

**Equity**
- Retained Earnings: 16,838.90
- Owner's Equity: 37,934.04


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-04-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $48,465.28
  - Section assets | Account Accounts Receivable | Amount $9,604.95
  - Section assets | Account Prepaid Rent | Amount $4,129.88
  - Section assets | Account Prepaid Insurance | Amount $2,084.58
  - Section assets | Account Office Supplies | Amount $1,452.11
  - Section assets | Account Equipment | Amount $15,794.96
  - Section assets | Account Furniture | Amount $6,405.29
  - Section liabilities | Account Accounts Payable | Amount $5,454.96
  - Section liabilities | Account Accrued Expenses | Amount $2,546.60
  - Section liabilities | Account Unearned Revenue | Amount $6,147.22
  - Section liabilities | Account Loans Payable | Amount $10,494.90
  - Section liabilities | Account Notes Payable | Amount $8,520.43
  - Section equity | Account Retained Earnings | Amount $16,838.90
  - Section equity | Account Owner's Equity | Amount $37,934.04

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Golden State Finance
Property: Cedar Plaza
Service Start: 2024-04-01
Service End: 2024-06-30
Total: $11,639.94
Monthly Amount: $3,879.98

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-05

```
CUSTOMER INVOICE
================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-04-05

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: Q2 FY 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 2024-04-21

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-04-21
Subtotal: $16,123.50
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $1,128.65
Total: $17,252.15

Line Items
----------
Items:
  - Description Implementation work | Amount $7,166.21
  - Description Follow-up support | Amount $8,957.29

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D022 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2024-04-05

```
LEASE AGREEMENT
===============

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-04-05

To
--
Golden State Finance

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: Q2 FY 2024

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Golden State Finance
Commencement Date: 2024-04-05
Term Months: 48
Monthly Payment Amount: $6,300.20
Incremental Borrowing Rate: 0.06
ROU Asset Amount: $268,264.52
Lease Liability Amount: $268,264.52

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2024-04-07

```
INSURANCE NOTICE / REFERENCE COPY
=================================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-04-07

To
--
Beacon General
Vendor remittance address on file

Terms
-----
Service Start: 2024-04-07
Service End: 2024-07-06

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Beacon General
Covered Item: Marina Heights
Coverage Start: 2024-04-07
Coverage End: 2024-07-06
Total Premium: $15,415.38
Monthly Amount: $5,138.46

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D038 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-09

```
CUSTOMER INVOICE
================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-04-09

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D038
Document Type: customer_invoice
Period: Q2 FY 2024
Contract Ref: FXCTR-0001

Terms
-----
Due Date: 2024-04-27

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: FXCTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: FXINV-0001
Due Date: 2024-04-27
Total: EUR 23.398,60

Line Items
----------
Items:
  - Description Support package | Amount EUR 6.600,99
  - Description Foreign-currency support | Amount EUR 16.797,61

Footer
------
Internal document packet copy.
Page marker: D038
```

### Document D039 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2024-04-09

```
EXCHANGE RATE NOTICE
====================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-04-09

Reference Box
-------------
Document ID: D039
Document Type: exchange_rate_notice
Period: Q2 FY 2024
Reference: FXINV-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXINV-0001
Rate Date: 2024-04-09
Rate Type: Spot rate at invoice date

Conversion Details
------------------
Source Currency: EUR
Source Amount: EUR 23.398,60
Functional Currency: USD
Exchange Rate: 1.0765
Functional Amount: $25,188.59

Footer
------
Internal document packet copy.
Page marker: D039
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-22

```
VENDOR INVOICE
==============

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-04-22

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q2 FY 2024

Terms
-----
Due Date: 2024-05-09

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-05-09
Subtotal: $4,609.40
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $230.47
Total: $4,839.87

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $2,062.55
  - Description Support fee | Amount $2,546.85

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D029 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2024-04-25

```
RETAINER AGREEMENT MEMO
=======================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-04-25

Reference Box
-------------
Document ID: D029
Document Type: retainer_agreement_memo
Period: Q2 FY 2024
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
Total Contract Value: $45,597.52

Explanation
-----------
Narrative: Customer Crescent Labs agreed to a service package spanning 12 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D030 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-25

```
CUSTOMER INVOICE
================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-04-25

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D030
Document Type: customer_invoice
Period: Q2 FY 2024
Contract Ref: CTR-0002

Terms
-----
Due Date: 2024-05-08

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-05-08
Subtotal: $41,452.29
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $4,145.23
Total: $45,597.52

Line Items
----------
Items:
  - Description Team Support Plan | Amount $17,661.41
  - Description Service coverage under contract | Amount $23,790.88

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D035 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2024-04-26

```
CUSTOMER INVOICE
================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-04-26

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D035
Document Type: customer_invoice
Period: Q2 FY 2024
Contract Ref: CTR-0003

Terms
-----
Due Date: 2024-05-17

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2024-05-17
Total: $16,840.31

Line Items
----------
Items:
  - Description Support package | Amount $4,733.96
  - Description Draft billing copy | Amount $12,106.35

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Internal document packet copy.
Page marker: D035
```

### Document D036 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2024-05-03

```
CANCELLATION NOTE
=================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-05-03

Reference Box
-------------
Document ID: D036
Document Type: cancellation_note
Period: Q2 FY 2024

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
- **Date:** 2024-05-03

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-05-03

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D037
Document Type: customer_invoice
Period: Q2 FY 2024
Contract Ref: CTR-0003

Terms
-----
Due Date: 2024-05-22

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2024-05-22
Total: $16,793.54

Line Items
----------
Items:
  - Description Monthly retainer | Amount $3,381.63
  - Description Reissued billing | Amount $13,411.91

Footer
------
Internal document packet copy.
Page marker: D037
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-11

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Prime Utility Desk
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $85,086.43
Paid Cash: $39,649.21
Financed Amount: $45,437.22
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-05-27

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: $15.87
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $5.32
  - Description Travel Incidentals | Amount $10.55
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-05-28

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $13,196.49
Draw Amount: $93,337.90
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $106,534.39
Note: Scheduled lender activity for the selected period.
```

### Document D040 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `posting_doc`
- **Date:** 2024-06-02

```
PAYMENT ADVICE
==============

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-02

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D040
Document Type: payment_advice
Period: Q2 FY 2024
Reference: FXINV-0001

Payment Details
---------------
Advice Number: FXPAY-0001
Counterparty: Maple Ridge Trading
Currency: USD
Amount: $25,544.25
Reference: FXINV-0001
Payment Method: Wire
Payment For: Foreign-currency receivable settlement

Foreign Currency Details
------------------------
Source Amount: EUR 23.398,60
Source Currency: EUR
Functional Currency: USD
Functional Amount: $25,544.25
Exchange Rate: 1.0917
FX Difference: 355.66

Footer
------
Internal document packet copy.
Page marker: D040
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-04

```
PAYMENT ADVICE
==============

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-04

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q2 FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: $4,509.67
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D024 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2024-06-06

```
LEASE PAYMENT NOTICE
====================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-06

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: Q2 FY 2024

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 2024-06-06
Payment Amount: $18,900.60
Interest Amount: $4,023.97
Principal Amount: $14,876.63

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-10

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: $83,230.77
Draw Amount: $0.00
Principal Paid: $19,743.83
Interest Paid: $2,478.82
Ending Principal: $63,486.94
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-16

```
UTILITY INVOICE
===============

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-16

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: Q2 FY 2024

Terms
-----
Due Date: 2024-07-01

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: Q2 FY 2024
Due Date: 2024-07-01
Total: $2,201.69

Charges
-------
Charges:
  - Description Electricity | Amount $469.82
  - Description Water | Amount $1,731.87

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-16

```
TRANSFER ADVICE
===============

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-16

Reference Box
-------------
Document ID: D028
Document Type: transfer_advice
Period: Q2 FY 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $63,605.50
Transfer Date: 2024-06-16
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D028
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-17

```
PAYMENT ADVICE
==============

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-17

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: Q2 FY 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: $17,228.14
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-06-18

```
PAYROLL SUMMARY
===============

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-18

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q2 FY 2024
Headcount: 10
Gross Pay: $31,979.56
Employer Tax: 3,147.42
Cash Outflow: $35,126.98

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-18

```
ASSET DISPOSAL NOTICE
=====================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-18

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: Q2 FY 2024

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Original Cost: $15,794.96
Accumulated Depreciation: 987.18
Net Book Value: $14,807.78
Proceeds Amount: $17,473.18
Gain Loss Amount: $2,665.40
Gain Loss Type: Gain

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-18

```
SALE PROCEEDS ADVICE
====================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-18

To
--
Crescent Labs

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: Q2 FY 2024

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Crescent Labs
Asset Tag: OPEN-EQU
Proceeds Amount: $17,473.18
Settlement Date: 2024-06-18
Payment Reference: BNK-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-29

```
LEASE MODIFICATION NOTICE
=========================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-29

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: Q2 FY 2024

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 2024-06-29
Old Liability Balance: $253,387.89
Remeasured Liability Balance: $286,347.22
Liability Remeasurement Delta Amount: $32,959.33
ROU Asset Adjustment Amount: $32,959.33

Narrative
---------
Details: Lease term extension remeasures the liability; the ROU asset is adjusted by the 
same amount.

Footer
------
Internal document packet copy.
Page marker: D025
```

### Document D026 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `support_doc`
- **Date:** 2024-06-29

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-29

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: Q2 FY 2024

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: $286,347.22
Payment Amount: $0.00
Interest Amount: $0.00
Principal Amount: $0.00
Ending Liability Balance: $286,347.22
ROU Amortization Amount: $0.00

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
SERVICE PERIOD MEMO
===================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q2 FY 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $3,879.98

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D011 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
SERVICE PERIOD MEMO
===================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: Q2 FY 2024
Reference: PRE-0002

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0002
Subject: Insurance coverage release
Reference: PRE-0002
Recognized Amount: $5,138.46

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
- **Date:** 2024-06-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $15,794.96
Useful Life Months: 48
Current Period Charge: $987.18
Accumulated Depreciation: 987.18
```

### Document D018 — Tax Depreciation Schedule

- **Type:** `tax_depreciation_schedule`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-30

Reference Box
-------------
Document ID: D018
Document Type: tax_depreciation_schedule
Period: Q2 FY 2024

Book Tax Difference
-------------------
Schedule ID: TAXDEP-0001
Asset Tag: OPEN-EQU
Book Depreciation Amount: $987.18
Tax Depreciation Amount: $1,510.72
Temporary Difference Amount: $523.54
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
DEFERRED TAX MEMO
=================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D019
Document Type: deferred_tax_memo
Period: Q2 FY 2024

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0001
Asset Tag: OPEN-EQU
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $130.88
Deferred Tax Liability Ending: $130.88
Deferred Tax Expense Amount: $130.88

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
- **Date:** 2024-06-30

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-30

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: Q2 FY 2024

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: OPEN-EQU
Book Depreciation Amount: $14,807.78
Tax Depreciation Amount: $15,539.50
Temporary Difference Amount: $731.72
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
DEFERRED TAX MEMO
=================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D021
Document Type: deferred_tax_memo
Period: Q2 FY 2024

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0002
Asset Tag: OPEN-EQU
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $182.93
Deferred Tax Liability Ending: $182.93
Deferred Tax Expense Amount: $182.93

Narrative
---------
Details: Deferred tax movement recorded after combining disposal proceeds with the tax-basis
 difference.

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D023 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-30

Reference Box
-------------
Document ID: D023
Document Type: lease_amortization_schedule
Period: Q2 FY 2024

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: $268,264.52
Payment Amount: $18,900.60
Interest Amount: $4,023.97
Principal Amount: $14,876.63
Ending Liability Balance: $253,387.89
ROU Amortization Amount: $16,766.53

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D031 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-30

Reference Box
-------------
Document ID: D031
Document Type: revenue_recognition_schedule
Period: Q2 FY 2024

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: Q2 FY 2024
Opening Deferred: $41,452.29
Added Deferred: $0.00
Released This Period: 10,363.07
Ending Deferred: $31,089.22

Footer
------
Internal document packet copy.
Page marker: D031
```

### Document D032 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
SERVICE PERIOD MEMO
===================

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-30

Reference Box
-------------
Document ID: D032
Document Type: service_period_memo
Period: Q2 FY 2024
Reference: Q2 FY 2024

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q2 FY 2024
Recognized Amount: $2,539.05

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
- **Date:** 2024-06-30

```
AR AGING SUMMARY
================

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D033
Document Type: ar_aging_summary
Period: Q2 FY 2024

Aging Summary
-------------
Summary ID: AGING-0001
Period: Q2 FY 2024
Total Open: $24.01

Customer Lines
--------------
Lines:
  - Customer Oak Harbor Foods | Reference INV-0001 | Current $15.35 | Past Due 8.66

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
- **Date:** 2024-06-30

```
CREDIT MEMO
===========

From
----
Summit Software
18 Marina Avenue, Chennai
Date: 2024-06-30

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D034
Document Type: credit_memo
Period: Q2 FY 2024
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
Amount: $8.66

Footer
------
Internal document packet copy.
Page marker: D034
```

### Document D041 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D041
Document Type: bank_statement
Period: Q2 FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0009
Statement Currency: USD
Opening Balance: $48,465.28
Closing Balance: $-9,037.05

Statement Rows
--------------
Rows:
  - Date 2024-04-01 | Description Rent prepayment PRE-0001 | Amount $-11,639.94 | Running 
Balance $36,825.34
  - Date 2024-04-07 | Description Insurance coverage prepayment PRE-0002 | Amount 
$-15,415.38 | Running Balance $21,409.96
  - Date 2024-05-11 | Description Asset purchase ASSET-0001 | Amount $-39,649.21 | Running 
Balance $-18,239.25
  - Date 2024-05-27 | Description Meridian Support LLP receipt RCPT-0001 | Amount $-15.87 | 
Running Balance $-18,255.12
  - Date 2024-05-28 | Description Loan draw LOAN-0001 | Amount $93,337.90 | Running Balance 
$75,082.78
  - Date 2024-06-02 | Description Foreign receipt FXINV-0001 | Amount $25,544.25 | Running 
Balance $100,627.03
  - Date 2024-06-04 | Description Supplier settlement BILL-0001 | Amount $-4,509.67 | 
Running Balance $96,117.36
  - Date 2024-06-06 | Description Lease payment LEASE-0001 | Amount $-18,900.60 | Running 
Balance $77,216.76
  - Date 2024-06-10 | Description Loan payment LOAN-0002 | Amount $-22,222.65 | Running 
Balance $54,994.11
  - Date 2024-06-16 | Description Transfer out TRX-0001 | Amount $-63,605.50 | Running 
Balance $-8,611.39
  - Date 2024-06-17 | Description Customer settlement INV-0001 | Amount $17,228.14 | Running
 Balance $8,616.75
  - Date 2024-06-18 | Description Asset sale OPEN-EQU | Amount $17,473.18 | Running Balance 
$26,089.93
  - Date 2024-06-18 | Description Payroll PAYRUN-0001 | Amount $-35,126.98 | Running Balance
 $-9,037.05

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D041
```

### Document D042 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Summit Software
18 Marina Avenue, Chennai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D042
Document Type: bank_statement
Period: Q2 FY 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-0999
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $63,605.50

Statement Rows
--------------
Rows:
  - Date 2024-06-16 | Description Transfer in TRX-0001 | Amount $63,605.50 | Running Balance
 $63,605.50

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D042
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 16,123.50 | D002 | 2024-04-05 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 1,128.65 | D002 | 2024-04-05 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 4,609.40 | D003 | 2024-04-22 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 230.47 | D003 | 2024-04-22 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 15.87 | D004 | 2024-05-27 | expense_receipt |
| 6 | Cash | Accounts Receivable | 17,228.14 | D005, D002 | 2024-06-17 | customer_payment |
| 7 | Accounts Payable | Cash | 4,509.67 | D006, D003 | 2024-06-04 | supplier_payment |
| 8 | Salaries Expense | Cash | 31,979.56 | D007 | 2024-06-18 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 3,147.42 | D007 | 2024-06-18 | payroll_tax |
| 10 | Prepaid Rent | Cash | 11,639.94 | D008 | 2024-04-01 | prepaid_rent_purchase |
| 11 | Rent Expense | Prepaid Rent | 3,879.98 | D008, D009 | 2024-06-30 | prepaid_rent_release |
| 12 | Prepaid Insurance | Cash | 15,415.38 | D010 | 2024-04-07 | prepaid_insurance_purchase |
| 13 | Insurance Expense | Prepaid Insurance | 5,138.46 | D010, D011 | 2024-06-30 | prepaid_insurance_release |
| 14 | Utilities Expense | Accounts Payable | 2,201.69 | D012 | 2024-06-16 | utilities_bill |
| 15 | Cash | Loans Payable | 93,337.90 | D013 | 2024-05-28 | loan_draw |
| 16 | Equipment | Cash | 39,649.21 | D014 | 2024-05-11 | equipment_purchase_cash |
| 17 | Equipment | Notes Payable | 45,437.22 | D014 | 2024-05-11 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 987.18 | D015 | 2024-06-30 | depreciation |
| 19 | Cash | Equipment | 17,473.18 | D016, D017 | 2024-06-18 | asset_disposal_proceeds |
| 20 | Accumulated Depreciation | Equipment | 987.18 | D016, D017 | 2024-06-18 | asset_disposal_remove_accumulated_depreciation |
| 21 | Equipment | Gain on Disposal | 2,665.40 | D016, D017 | 2024-06-18 | asset_disposal_gain |
| 22 | Deferred Tax Expense | Deferred Tax Liability | 130.88 | D018, D019 | 2024-06-30 | deferred_tax_depreciation |
| 23 | Deferred Tax Expense | Deferred Tax Liability | 182.93 | D016, D017, D020, D021 | 2024-06-30 | asset_disposal_with_deferred_tax |
| 24 | Right-of-Use Asset | Lease Liability | 268,264.52 | D022 | 2024-04-05 | baseline_lease_initial_recognition |
| 25 | Lease Liability | Cash | 14,876.63 | D022, D023, D024 | 2024-06-06 | baseline_lease_principal |
| 26 | Lease Interest Expense | Cash | 4,023.97 | D022, D023, D024 | 2024-06-06 | baseline_lease_interest |
| 27 | Lease Amortization Expense | Right-of-Use Asset | 16,766.53 | D022, D023 | 2024-06-30 | baseline_lease_amortization |
| 28 | Right-of-Use Asset | Lease Liability | 32,959.33 | D025, D026 | 2024-06-29 | lease_modification |
| 29 | Loans Payable | Cash | 19,743.83 | D027 | 2024-06-10 | loan_repayment_principal |
| 30 | Interest Expense | Cash | 2,478.82 | D027 | 2024-06-10 | loan_repayment_interest |
| 31 | Reserve Cash | Cash | 63,605.50 | D028 | 2024-06-16 | interbank_transfer |
| 32 | Accounts Receivable | Unearned Revenue | 41,452.29 | D029, D030 | 2024-04-25 | retainer_invoice |
| 33 | Accounts Receivable | Sales Tax Payable | 4,145.23 | D029, D030 | 2024-04-25 | retainer_invoice_tax |
| 34 | Unearned Revenue | Service Revenue | 10,363.07 | D031, D030 | 2024-06-30 | retainer_release |
| 35 | Utilities Expense | Accrued Expenses | 2,539.05 | D032 | 2024-06-30 | expense_accrual |
| 36 | Bad Debt Expense | Accounts Receivable | 8.66 | D033, D034, D002 | 2024-06-30 | bad_debt_review |
| 37 | Accounts Receivable | Service Revenue | 16,793.54 | D035, D036, D037 | 2024-05-03 | reissued_invoice |
| 38 | Accounts Receivable | Service Revenue | 25,188.59 | D038, D039 | 2024-04-09 | fx_service_invoice |
| 39 | Cash | Accounts Receivable | 25,188.59 | D040, D038 | 2024-06-02 | fx_customer_payment |
| 40 | Cash | Foreign Exchange Gain | 355.66 | D040, D038 | 2024-06-02 | fx_customer_payment_gain |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: -9,037.05
- Accounts Receivable: 72,011.36
- Prepaid Rent: 11,889.84
- Prepaid Insurance: 12,361.50
- Office Supplies: 1,452.11
- Equipment: 85,086.43
- Furniture: 6,405.29
- Input Tax Receivable: 230.47
- Right-of-Use Asset: 284,457.32
- Reserve Cash: 63,605.50

**Liabilities**
- Accounts Payable: 7,986.85
- Accrued Expenses: 5,085.65
- Unearned Revenue: 37,236.44
- Loans Payable: 84,088.97
- Notes Payable: 53,957.65
- Sales Tax Payable: 5,273.88
- Deferred Tax Liability: 313.81
- Lease Liability: 286,347.22

**Equity**
- Retained Earnings: 10,238.26
- Owner's Equity: 37,934.04

**Totals:** Assets = 528,462.77; Liabilities = 480,290.47; Equity = 48,172.30
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
