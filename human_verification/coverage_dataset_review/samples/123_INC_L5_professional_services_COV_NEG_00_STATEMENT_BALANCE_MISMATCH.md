# Verification Packet — COV_NEG_00_STATEMENT_BALANCE_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2025-26
- **Period start → end:** 2025-04-01 → 2026-03-31
- **Entity:** Pioneer Builders
- **Currency (display / functional):** USD / USD
- **Tax regime:** `vat`
- **Document count:** 50
- **Labeled as inconsistent:** True
- **Inconsistency codes:** statement_balance_mismatch
- **Inconsistency reasons:** Statement closing balance does not reconcile with the listed open lines.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 140,913.91
- Accounts Receivable: 8,825.64
- Prepaid Rent: 11,778.02
- Prepaid Insurance: 8,028.89
- Office Supplies: 5,825.23
- Equipment: 18,661.83
- Furniture: 16,603.88

**Liabilities**
- Accounts Payable: 11,971.98
- Accrued Expenses: 5,545.68
- Unearned Revenue: 8,079.20
- Loans Payable: 17,435.18
- Notes Payable: 22,326.44

**Equity**
- Retained Earnings: 46,272.66
- Owner's Equity: 99,006.26


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-04-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $140,913.91
  - Section assets | Account Accounts Receivable | Amount $8,825.64
  - Section assets | Account Prepaid Rent | Amount $11,778.02
  - Section assets | Account Prepaid Insurance | Amount $8,028.89
  - Section assets | Account Office Supplies | Amount $5,825.23
  - Section assets | Account Equipment | Amount $18,661.83
  - Section assets | Account Furniture | Amount $16,603.88
  - Section liabilities | Account Accounts Payable | Amount $11,971.98
  - Section liabilities | Account Accrued Expenses | Amount $5,545.68
  - Section liabilities | Account Unearned Revenue | Amount $8,079.20
  - Section liabilities | Account Loans Payable | Amount $17,435.18
  - Section liabilities | Account Notes Payable | Amount $22,326.44
  - Section equity | Account Retained Earnings | Amount $46,272.66
  - Section equity | Account Owner's Equity | Amount $99,006.26

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-16

```
INSURANCE NOTICE
================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-04-16

To
--
Beacon General
Vendor remittance address on file

Terms
-----
Service Start: 2025-04-16
Service End: 2025-07-15

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Beacon General
Covered Item: Cedar Plaza
Coverage Start: 2025-04-16
Coverage End: 2025-07-15
Total Premium: $41,843.56
Monthly Amount: $13,947.85

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-23

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Prime Utility Desk
Property: Cedar Plaza
Service Start: 2025-04-23
Service End: 2025-07-22
Total: $44,320.41
Monthly Amount: $14,773.47

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D035 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2025-04-24

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-04-24

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D035
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: CTR-0003

Terms
-----
Due Date: 2025-05-04

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2025-05-04
Total: $56,863.84

Line Items
----------
Items:
  - Description Monthly retainer | Amount $19,042.57
  - Description Draft billing copy | Amount $37,821.27

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Internal document packet copy.
Page marker: D035
```

### Document D041 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-04-24

```
CANCELLATION NOTE
=================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2025-04-24

Reference Box
-------------
Document ID: D041
Document Type: cancellation_note
Period: FY 2025-26

Cancellation Summary
--------------------
Note Number: CNCL-0002
Withdrawn Reference: INV-0003-OLD
Replacement Reference: INV-0003

Background
----------
Narrative: INV-0003-OLD is withdrawn and must not be posted. Use INV-0003 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D041
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-30

```
VENDOR INVOICE
==============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-04-30

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 2025-05-19

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-05-19
Subtotal: $16,250.96
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $3,250.19
Total: $19,501.15

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $6,393.37
  - Description Support fee | Amount $9,857.59

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D036 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2025-04-30

```
CANCELLATION NOTE
=================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2025-04-30

Reference Box
-------------
Document ID: D036
Document Type: cancellation_note
Period: FY 2025-26

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
- **Date:** 2025-04-30

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-04-30

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D037
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: CTR-0003

Terms
-----
Due Date: 2025-05-11

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2025-05-11
Total: $56,648.63

Line Items
----------
Items:
  - Description Review pack | Amount $16,037.47
  - Description Reissued billing | Amount $40,611.16

Footer
------
Internal document packet copy.
Page marker: D037
```

### Document D043 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-04-30

```
CANCELLATION NOTE
=================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-04-30

Reference Box
-------------
Document ID: D043
Document Type: cancellation_note
Period: FY 2025-26

Cancellation Summary
--------------------
Note Number: CNCL-0003
Withdrawn Reference: INV-0004-OLD
Replacement Reference: INV-0004

Background
----------
Narrative: INV-0004-OLD is withdrawn and must not be posted. Use INV-0004 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D043
```

### Document D038 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-11

```
CUSTOMER INVOICE
================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-05-11

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D038
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: FXCTR-0001

Terms
-----
Due Date: 2025-06-03

Parties
-------
Customer: Crescent Labs
Contract Ref: FXCTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: FXINV-0001
Due Date: 2025-06-03
Total: EUR 17.797,82

Line Items
----------
Items:
  - Description Implementation work | Amount EUR 6.015,44
  - Description Foreign-currency support | Amount EUR 11.782,38

Footer
------
Internal document packet copy.
Page marker: D038
```

### Document D039 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2025-05-11

```
EXCHANGE RATE NOTICE
====================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-05-11

Reference Box
-------------
Document ID: D039
Document Type: exchange_rate_notice
Period: FY 2025-26
Reference: FXINV-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXINV-0001
Rate Date: 2025-05-11
Rate Type: Spot rate at invoice date

Conversion Details
------------------
Source Currency: EUR
Source Amount: EUR 17.797,82
Functional Currency: USD
Exchange Rate: 1.0441
Functional Amount: $18,582.70

Footer
------
Internal document packet copy.
Page marker: D039
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-13

```
CUSTOMER INVOICE
================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2025-05-13

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-05-28

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-05-28
Subtotal: $39,969.78
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: $4,996.22
Total: $44,966.00

Line Items
----------
Items:
  - Description Review pack | Amount $8,169.22
  - Description Follow-up support | Amount $31,800.56

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D045 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-05-13

```
CANCELLATION NOTE
=================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-05-13

Reference Box
-------------
Document ID: D045
Document Type: cancellation_note
Period: FY 2025-26

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
Internal document packet copy.
Page marker: D045
```

### Document D046 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-05-13

```
CANCELLATION NOTE
=================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2025-05-13

Reference Box
-------------
Document ID: D046
Document Type: cancellation_note
Period: FY 2025-26

Cancellation Summary
--------------------
Note Number: CNCL-0005
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D046
```

### Document D047 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-05-13

```
SECONDARY COPY
==============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-05-13

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D047
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0001
Counterparty: Oak Harbor Foods
Total: $44,966.00
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D047
```

### Document D029 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-05-19

```
RETAINER AGREEMENT MEMO
=======================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2025-05-19

Reference Box
-------------
Document ID: D029
Document Type: retainer_agreement_memo
Period: FY 2025-26
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
Total Contract Value: $106,916.64

Explanation
-----------
Narrative: Customer Maple Ridge Trading agreed to a service package spanning 12 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D030 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-19

```
CUSTOMER INVOICE
================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-05-19

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D030
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-05-31

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-05-31
Subtotal: $89,097.20
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $17,819.44
Total: $106,916.64

Line Items
----------
Items:
  - Description Annual Growth Plan | Amount $20,361.26
  - Description Service coverage under contract | Amount $68,735.94

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D022 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2025-06-19

```
LEASE AGREEMENT
===============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2025-06-19

To
--
Oakline Services

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: FY 2025-26

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Oakline Services
Commencement Date: 2025-06-19
Term Months: 48
Monthly Payment Amount: $12,597.55
Incremental Borrowing Rate: 0.09
ROU Asset Amount: $506,229.80
Lease Liability Amount: $506,229.80

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-13

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
Total: $216,345.89
Paid Cash: $97,026.49
Financed Amount: $119,319.40
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-01

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: $6,871.36
Draw Amount: $224,701.52
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $231,572.88
Note: Scheduled lender activity for the selected period.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-12-04

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Prime Utility Desk
Total: $265.89
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $115.64
  - Description Travel Incidentals | Amount $150.25
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-13

```
TRANSFER ADVICE
===============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-12-13

Reference Box
-------------
Document ID: D028
Document Type: transfer_advice
Period: FY 2025-26
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $97,035.77
Transfer Date: 2025-12-13
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-12-19

```
PAYROLL SUMMARY
===============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-12-19

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025-26
Headcount: 10
Gross Pay: $69,775.88
Employer Tax: 6,896.15
Cash Outflow: $76,672.03

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-21

```
UTILITY INVOICE
===============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2025-12-21

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: FY 2025-26

Terms
-----
Due Date: 2026-01-02

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: FY 2025-26
Due Date: 2026-01-02
Total: $2,255.88

Charges
-------
Charges:
  - Description Electricity | Amount $701.39
  - Description Water | Amount $1,554.49

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2026-01-05

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: $8,201.42
Draw Amount: $0.00
Principal Paid: $33,467.77
Interest Paid: $3,361.64
Ending Principal: $-25,266.35
Note: Scheduled lender activity for the selected period.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-18

```
PAYMENT ADVICE
==============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-01-18

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: $12,052.48
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D024 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2026-01-18

```
LEASE PAYMENT NOTICE / REFERENCE COPY
=====================================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-01-18

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: FY 2025-26

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 2026-01-18
Payment Amount: $37,792.65
Interest Amount: $11,390.17
Principal Amount: $26,402.48

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2026-01-22

```
ASSET DISPOSAL NOTICE
=====================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-01-22

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: FY 2025-26

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Delivery van
Asset Tag: TAG-0001
Original Cost: $216,345.89
Accumulated Depreciation: 43,269.12
Net Book Value: $173,076.77
Proceeds Amount: $204,230.59
Gain Loss Amount: $31,153.82
Gain Loss Type: Gain

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-22

```
SALE PROCEEDS ADVICE
====================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-01-22

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: FY 2025-26

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Blue Finch Holdings
Asset Tag: TAG-0001
Proceeds Amount: $204,230.59
Settlement Date: 2026-01-22
Payment Reference: BNK-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-29

```
PAYMENT ADVICE
==============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-01-29

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: $26,129.23
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-03

```
LEASE MODIFICATION NOTICE / REFERENCE COPY
==========================================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-03

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: FY 2025-26

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 2026-03-03
Old Liability Balance: $479,827.32
Remeasured Liability Balance: $527,599.04
Liability Remeasurement Delta Amount: $47,771.72
ROU Asset Adjustment Amount: $47,771.72

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
- **Date:** 2026-03-03

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-03

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: FY 2025-26

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: $527,599.04
Payment Amount: $0.00
Interest Amount: $0.00
Principal Amount: $0.00
Ending Liability Balance: $527,599.04
ROU Amortization Amount: $0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
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
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: FY 2025-26
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $14,773.47

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
- **Date:** 2026-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: FY 2025-26
Reference: PRE-0002

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0002
Subject: Insurance coverage release
Reference: PRE-0002
Recognized Amount: $13,947.85

Explanation
-----------
Narrative: One month of insurance coverage has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D015 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D015
Document Type: fixed_asset_rollforward
Period: FY 2025-26

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Delivery van
Asset Tag: TAG-0001
Cost: $216,345.89
Useful Life: 60
Current Charge: $43,269.12
Accumulated Depreciation: 43,269.12
Opening Balance: $216,345.89
Additions: 0.00
Disposals: 0.00
Ending Balance: $216,345.89

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
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
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D018
Document Type: tax_depreciation_schedule
Period: FY 2025-26

Book Tax Difference
-------------------
Schedule ID: TAXDEP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: $43,269.12
Tax Depreciation Amount: $76,136.78
Temporary Difference Amount: $32,867.66
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
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D019
Document Type: deferred_tax_memo
Period: FY 2025-26

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0001
Asset Tag: TAG-0001
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $8,216.92
Deferred Tax Liability Ending: $8,216.92
Deferred Tax Expense Amount: $8,216.92

Narrative
---------
Details: Tax depreciation exceeds book depreciation, creating a taxable temporary 
difference.

Footer
------
Internal document packet copy.
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
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: FY 2025-26

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: $173,076.77
Tax Depreciation Amount: $179,475.75
Temporary Difference Amount: $6,398.98
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
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D021
Document Type: deferred_tax_memo
Period: FY 2025-26

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0002
Asset Tag: TAG-0001
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $1,599.74
Deferred Tax Liability Ending: $1,599.74
Deferred Tax Expense Amount: $1,599.74

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
- **Date:** 2026-03-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D023
Document Type: lease_amortization_schedule
Period: FY 2025-26

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: $506,229.80
Payment Amount: $37,792.65
Interest Amount: $11,390.17
Principal Amount: $26,402.48
Ending Liability Balance: $479,827.32
ROU Amortization Amount: $126,557.45

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D031 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D031
Document Type: revenue_recognition_schedule
Period: FY 2025-26

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: FY 2025-26
Opening Deferred: $89,097.20
Added Deferred: $0.00
Released This Period: 89,097.20
Ending Deferred: $0.00

Footer
------
Internal document packet copy.
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
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D032
Document Type: service_period_memo
Period: FY 2025-26
Reference: FY 2025-26

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2025-26
Recognized Amount: $4,718.82

Explanation
-----------
Narrative: Accrue unpaid utilities expense incurred before period end.

Footer
------
Generated for synthetic accounting research use.
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
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D033
Document Type: ar_aging_summary
Period: FY 2025-26

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2025-26
Total Open: $18,836.77

Customer Lines
--------------
Lines:
  - Customer Oak Harbor Foods | Reference INV-0001 | Current $13,551.93 | Past Due 5,284.84

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
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D034
Document Type: credit_memo
Period: FY 2025-26
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
Amount: $5,284.84

Footer
------
Generated for synthetic accounting research use.
Page marker: D034
```

### Document D040 — FX Remeasurement Memo

- **Type:** `fx_remeasurement_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
FX REMEASUREMENT MEMO
=====================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D040
Document Type: fx_remeasurement_memo
Period: FY 2025-26
Reference: FXINV-0001

Remeasurement Details
---------------------
Memo ID: FXREM-0001
Reference: FXINV-0001
Source Currency: EUR
Functional Currency: USD
Source Amount: EUR 17.797,82
Booked Amount: $18,582.70
Closing Rate: 1.0318
Remeasured Amount: $18,363.79
Difference Amount: $218.91
Narrative: Open foreign-currency balance remeasured at the closing rate.

Footer
------
Generated for synthetic accounting research use.
Page marker: D040
```

### Document D042 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
MEMO
====

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D042
Document Type: memo
Period: FY 2025-26

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
Narrative: Please route scanned paperwork to the shared archive after the period binder is 
complete.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D042
```

### Document D044 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
MEMO
====

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D044
Document Type: memo
Period: FY 2025-26

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0002
Subject: Quarter-end packet routing note
Audience: Operations Team

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
Page marker: D044
```

### Document D048 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
VENDOR STATEMENT
================

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Date: 2026-03-31

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D048
Document Type: vendor_statement
Period: FY 2025-26

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Metro Water
Closing Balance: $120.70

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount $2,255.88 | Status Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D048
```

### Document D049 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D049
Document Type: bank_statement
Period: FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $140,913.91
Closing Balance: $152,136.56

Statement Rows
--------------
Rows:
  - Date 2025-04-16 | Description Insurance coverage prepayment PRE-0002 | Amount 
$-41,843.56 | Running Balance $99,070.35
  - Date 2025-04-23 | Description Rent prepayment PRE-0001 | Amount $-44,320.41 | Running 
Balance $54,749.94
  - Date 2025-11-13 | Description Asset purchase ASSET-0001 | Amount $-97,026.49 | Running 
Balance $-42,276.55
  - Date 2025-12-01 | Description Loan draw LOAN-0001 | Amount $224,701.52 | Running Balance
 $182,424.97
  - Date 2025-12-04 | Description Prime Utility Desk receipt RCPT-0001 | Amount $-265.89 | 
Running Balance $182,159.08
  - Date 2025-12-13 | Description Transfer out TRX-0001 | Amount $-97,035.77 | Running 
Balance $85,123.31
  - Date 2025-12-19 | Description Payroll PAYRUN-0001 | Amount $-76,672.03 | Running Balance
 $8,451.28
  - Date 2026-01-05 | Description Loan payment LOAN-0002 | Amount $-36,829.41 | Running 
Balance $-28,378.13
  - Date 2026-01-18 | Description Lease payment LEASE-0001 | Amount $-37,792.65 | Running 
Balance $-66,170.78
  - Date 2026-01-18 | Description Supplier settlement BILL-0001 | Amount $-12,052.48 | 
Running Balance $-78,223.26
  - Date 2026-01-22 | Description Asset sale TAG-0001 | Amount $204,230.59 | Running Balance
 $126,007.33
  - Date 2026-01-29 | Description Customer settlement INV-0001 | Amount $26,129.23 | Running
 Balance $152,136.56

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D049
```

### Document D050 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Pioneer Builders
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D050
Document Type: bank_statement
Period: FY 2025-26

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $97,035.77

Statement Rows
--------------
Rows:
  - Date 2025-12-13 | Description Transfer in TRX-0001 | Amount $97,035.77 | Running Balance
 $97,035.77

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D050
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
Is the labeled contradiction (codes: `statement_balance_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
