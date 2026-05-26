# Verification Packet — COV_NEG_00_EXCHANGE_RATE_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Beacon Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `sales_tax`
- **Document count:** 50
- **Labeled as inconsistent:** True
- **Inconsistency codes:** exchange_rate_mismatch
- **Inconsistency reasons:** Exchange-rate support does not reconcile the foreign amount into the stated functional amount.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 168,827.90
- Accounts Receivable: 27,230.40
- Prepaid Rent: 6,743.38
- Prepaid Insurance: 9,522.95
- Office Supplies: 6,381.83
- Equipment: 29,917.23
- Furniture: 12,589.74

**Liabilities**
- Accounts Payable: 9,628.76
- Accrued Expenses: 3,232.64
- Unearned Revenue: 4,461.87
- Loans Payable: 24,478.45
- Notes Payable: 22,427.83

**Equity**
- Retained Earnings: 29,489.48
- Owner's Equity: 167,494.40


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
  - Section assets | Account Cash | Amount $168,827.90
  - Section assets | Account Accounts Receivable | Amount $27,230.40
  - Section assets | Account Prepaid Rent | Amount $6,743.38
  - Section assets | Account Prepaid Insurance | Amount $9,522.95
  - Section assets | Account Office Supplies | Amount $6,381.83
  - Section assets | Account Equipment | Amount $29,917.23
  - Section assets | Account Furniture | Amount $12,589.74
  - Section liabilities | Account Accounts Payable | Amount $9,628.76
  - Section liabilities | Account Accrued Expenses | Amount $3,232.64
  - Section liabilities | Account Unearned Revenue | Amount $4,461.87
  - Section liabilities | Account Loans Payable | Amount $24,478.45
  - Section liabilities | Account Notes Payable | Amount $22,427.83
  - Section equity | Account Retained Earnings | Amount $29,489.48
  - Section equity | Account Owner's Equity | Amount $167,494.40

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2024-04-14

```
INSURANCE NOTICE / REFERENCE COPY
=================================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2024-04-14

To
--
Beacon General
Vendor remittance address on file

Terms
-----
Service Start: 2024-04-14
Service End: 2024-07-13

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Beacon General
Covered Item: Park Lane Residences
Coverage Start: 2024-04-14
Coverage End: 2024-07-13
Total Premium: $49,392.29
Monthly Amount: $16,464.10

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-20

```
VENDOR INVOICE
==============

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-04-20

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 2024-05-07

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-05-07
Subtotal: $30,158.04
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: $2,488.04
Total: $32,646.08

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $12,975.12
  - Description Support fee | Amount $17,182.92

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2024-04-24

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Oakline Services
Property: Harbor View Offices
Service Start: 2024-04-24
Service End: 2024-07-23
Total: $51,654.59
Monthly Amount: $17,218.20

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D035 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2024-04-25

```
CUSTOMER INVOICE
================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2024-04-25

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D035
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0003

Terms
-----
Due Date: 2024-05-05

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2024-05-05
Total: $26,177.27

Line Items
----------
Items:
  - Description Support package | Amount $7,204.06
  - Description Draft billing copy | Amount $18,973.21

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D035
```

### Document D041 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-04-25

```
SECONDARY COPY
==============

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-04-25

To
--
Riverfront Group

Reference Box
-------------
Document ID: D041
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0003
Counterparty: Riverfront Group
Total: $26,177.27
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D041
```

### Document D042 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-04-25

```
SECONDARY COPY
==============

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2024-04-25

To
--
Riverfront Group

Reference Box
-------------
Document ID: D042
Document Type: secondary_copy
Period: FY 2024-25

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: INV-0003
Counterparty: Riverfront Group
Total: $26,177.27
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D042
```

### Document D048 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-04-25

```
CANCELLATION NOTE
=================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2024-04-25

Reference Box
-------------
Document ID: D048
Document Type: cancellation_note
Period: FY 2024-25

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
Page marker: D048
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
Beacon Software
75 Market Road, Mumbai
Document Date: 2024-05-03

Reference Box
-------------
Document ID: D036
Document Type: cancellation_note
Period: FY 2024-25

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
Beacon Software
75 Market Road, Mumbai
Date: 2024-05-03

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D037
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0003

Terms
-----
Due Date: 2024-05-17

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2024-05-17
Total: $27,060.10

Line Items
----------
Items:
  - Description Review pack | Amount $10,152.32
  - Description Reissued billing | Amount $16,907.78

Footer
------
Internal document packet copy.
Page marker: D037
```

### Document D022 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2024-05-31

```
LEASE AGREEMENT / REFERENCE COPY
================================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2024-05-31

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: FY 2024-25

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Pace Office Mart
Commencement Date: 2024-05-31
Term Months: 24
Monthly Payment Amount: $16,181.44
Incremental Borrowing Rate: 0.07
ROU Asset Amount: $359,590.81
Lease Liability Amount: $359,590.81

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-19

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-06-19

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0001

Terms
-----
Due Date: 2024-07-05

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-07-05
Subtotal: $35,958.38
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: $3,416.05
Total: $39,374.43

Line Items
----------
Items:
  - Description Review pack | Amount $12,152.34
  - Description Follow-up support | Amount $23,806.04

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D038 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-22

```
CUSTOMER INVOICE
================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-06-22

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D038
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: FXCTR-0001

Terms
-----
Due Date: 2024-07-06

Parties
-------
Customer: Aster Point Services
Contract Ref: FXCTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: FXINV-0001
Due Date: 2024-07-06
Total: GBP 59,242.48

Line Items
----------
Items:
  - Description Implementation work | Amount GBP 20,281.20
  - Description Foreign-currency support | Amount GBP 38,961.28

Footer
------
Internal document packet copy.
Page marker: D038
```

### Document D039 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2024-06-22

```
EXCHANGE RATE NOTICE
====================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2024-06-22

Reference Box
-------------
Document ID: D039
Document Type: exchange_rate_notice
Period: FY 2024-25
Reference: FXINV-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXINV-0001
Rate Date: 2024-06-22
Rate Type: Spot rate at invoice date

Conversion Details
------------------
Source Currency: GBP
Source Amount: GBP 59,242.48
Functional Currency: USD
Exchange Rate: 1.2740
Functional Amount: $73,893.35

Footer
------
Generated for synthetic accounting research use.
Page marker: D039
```

### Document D029 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
RETAINER AGREEMENT MEMO
=======================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D029
Document Type: retainer_agreement_memo
Period: FY 2024-25
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
Total Contract Value: $247,420.75

Explanation
-----------
Narrative: Customer Riverfront Group agreed to a service package spanning 12 months.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D030 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-30

```
CUSTOMER INVOICE
================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-06-30

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D030
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0002

Terms
-----
Due Date: 2024-07-17

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-07-17
Subtotal: $235,638.81
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: $11,781.94
Total: $247,420.75

Line Items
----------
Items:
  - Description Enterprise License | Amount $94,806.41
  - Description Service coverage under contract | Amount $140,832.40

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-07-28

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Meridian Support LLP
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 24
Total: $112,034.91
Paid Cash: $52,760.28
Financed Amount: $59,274.63
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-27

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $45,558.13
Draw Amount: $298,511.63
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $344,069.76
Note: Scheduled lender activity for the selected period.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-10-07

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: $16.98
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $4.07
  - Description Travel Incidentals | Amount $12.91
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-09

```
ASSET DISPOSAL NOTICE
=====================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-12-09

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: FY 2024-25

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Display fixtures
Asset Tag: TAG-0001
Original Cost: $112,034.91
Accumulated Depreciation: 56,017.44
Net Book Value: $56,017.47
Proceeds Amount: $45,934.33
Gain Loss Amount: $10,083.14
Gain Loss Type: Loss

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-09

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-12-09

To
--
Riverfront Group

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: FY 2024-25

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Riverfront Group
Asset Tag: TAG-0001
Proceeds Amount: $45,934.33
Settlement Date: 2024-12-09
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-15

```
PAYMENT ADVICE
==============

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-12-15

To
--
Crescent Labs

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2024-25
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: $33,429.67
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-12-20

```
PAYROLL SUMMARY
===============

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-12-20

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024-25
Headcount: 5
Gross Pay: $81,463.57
Employer Tax: 10,857.91
Cash Outflow: $92,321.48

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-23

```
UTILITY INVOICE
===============

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-12-23

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: FY 2024-25

Terms
-----
Due Date: 2025-01-03

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: FY 2024-25
Due Date: 2025-01-03
Total: $6,164.93

Charges
-------
Charges:
  - Description Electricity | Amount $1,767.21
  - Description Water | Amount $4,397.72

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-30

```
TRANSFER ADVICE
===============

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2024-12-30

Reference Box
-------------
Document ID: D028
Document Type: transfer_advice
Period: FY 2024-25
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $341,022.53
Transfer Date: 2024-12-30
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-01-03

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: $261,287.73
Draw Amount: $0.00
Principal Paid: $36,775.94
Interest Paid: $4,115.66
Ending Principal: $224,511.79
Note: Scheduled lender activity for the selected period.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-30

```
PAYMENT ADVICE
==============

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-01-30

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: $29,739.96
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
- **Date:** 2025-02-06

```
LEASE PAYMENT NOTICE
====================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-02-06

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: FY 2024-25

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 2025-02-06
Payment Amount: $48,544.32
Interest Amount: $6,742.33
Principal Amount: $41,801.99

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-24

```
LEASE MODIFICATION NOTICE / REFERENCE COPY
==========================================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-24

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: FY 2024-25

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 2025-03-24
Old Liability Balance: $317,788.82
Remeasured Liability Balance: $351,408.06
Liability Remeasurement Delta Amount: $33,619.24
ROU Asset Adjustment Amount: $33,619.24

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
- **Date:** 2025-03-24

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-24

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: FY 2024-25

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: $351,408.06
Payment Amount: $0.00
Interest Amount: $0.00
Principal Amount: $0.00
Ending Liability Balance: $351,408.06
ROU Amortization Amount: $0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: FY 2024-25
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $17,218.20

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
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: FY 2024-25
Reference: PRE-0002

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0002
Subject: Insurance coverage release
Reference: PRE-0002
Recognized Amount: $16,464.10

Explanation
-----------
Narrative: One month of insurance coverage has expired and should be expensed this period.

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D015 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D015
Document Type: fixed_asset_rollforward
Period: FY 2024-25

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Display fixtures
Asset Tag: TAG-0001
Cost: $112,034.91
Useful Life: 24
Current Charge: $56,017.44
Accumulated Depreciation: 56,017.44
Opening Balance: $112,034.91
Additions: 0.00
Disposals: 0.00
Ending Balance: $112,034.91

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D018 — Tax Depreciation Schedule

- **Type:** `tax_depreciation_schedule`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D018
Document Type: tax_depreciation_schedule
Period: FY 2024-25

Book Tax Difference
-------------------
Schedule ID: TAXDEP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: $56,017.44
Tax Depreciation Amount: $97,238.07
Temporary Difference Amount: $41,220.63
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
DEFERRED TAX MEMO
=================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D019
Document Type: deferred_tax_memo
Period: FY 2024-25

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0001
Asset Tag: TAG-0001
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $10,305.16
Deferred Tax Liability Ending: $10,305.16
Deferred Tax Expense Amount: $10,305.16

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
- **Date:** 2025-03-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: FY 2024-25

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: $56,017.47
Tax Depreciation Amount: $59,309.72
Temporary Difference Amount: $3,292.25
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
DEFERRED TAX MEMO
=================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D021
Document Type: deferred_tax_memo
Period: FY 2024-25

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0002
Asset Tag: TAG-0001
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $823.06
Deferred Tax Liability Ending: $823.06
Deferred Tax Expense Amount: $823.06

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
- **Date:** 2025-03-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D023
Document Type: lease_amortization_schedule
Period: FY 2024-25

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: $359,590.81
Payment Amount: $48,544.32
Interest Amount: $6,742.33
Principal Amount: $41,801.99
Ending Liability Balance: $317,788.82
ROU Amortization Amount: $179,795.40

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D031 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
REVENUE RECOGNITION SCHEDULE
============================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D031
Document Type: revenue_recognition_schedule
Period: FY 2024-25

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: FY 2024-25
Opening Deferred: $235,638.81
Added Deferred: $0.00
Released This Period: 235,638.81
Ending Deferred: $0.00

Footer
------
Internal document packet copy.
Page marker: D031
```

### Document D032 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D032
Document Type: service_period_memo
Period: FY 2024-25
Reference: FY 2024-25

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2024-25
Recognized Amount: $6,726.98

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
- **Date:** 2025-03-31

```
AR AGING SUMMARY
================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D033
Document Type: ar_aging_summary
Period: FY 2024-25

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2024-25
Total Open: $5,944.76

Customer Lines
--------------
Lines:
  - Customer Crescent Labs | Reference INV-0001 | Current $3,769.78 | Past Due 2,174.98

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Internal document packet copy.
Page marker: D033
```

### Document D034 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
CREDIT MEMO
===========

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

To
--
Crescent Labs

Reference Box
-------------
Document ID: D034
Document Type: credit_memo
Period: FY 2024-25
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Crescent Labs
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: $2,174.98

Footer
------
Internal document packet copy.
Page marker: D034
```

### Document D040 — FX Remeasurement Memo

- **Type:** `fx_remeasurement_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
FX REMEASUREMENT MEMO
=====================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D040
Document Type: fx_remeasurement_memo
Period: FY 2024-25
Reference: FXINV-0001

Remeasurement Details
---------------------
Memo ID: FXREM-0001
Reference: FXINV-0001
Source Currency: GBP
Functional Currency: USD
Source Amount: GBP 59,242.48
Booked Amount: $75,474.92
Closing Rate: 1.3649
Remeasured Amount: $80,860.06
Difference Amount: $5,385.14
Narrative: Open foreign-currency balance remeasured at the closing rate.

Footer
------
Internal document packet copy.
Page marker: D040
```

### Document D043 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D043
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0001
Subject: Scanning checklist for back-office staff
Audience: Back Office

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
Page marker: D043
```

### Document D044 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D044
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Document retention reminder
Audience: Back Office

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
Page marker: D044
```

### Document D045 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Beacon Software
75 Market Road, Mumbai
Date: 2025-03-31

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D045
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Prime Utility Desk
Closing Balance: $2,906.12

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount $2,906.12 | Status Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D045
```

### Document D046 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D046
Document Type: memo
Period: FY 2024-25

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0003
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
Page marker: D046
```

### Document D047 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-31

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D047
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0002
Vendor: Harbor Utilities
Closing Balance: $6,164.93

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount $6,164.93 | Status Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D047
```

### Document D049 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D049
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $168,827.90
Closing Balance: $-159,640.50

Statement Rows
--------------
Rows:
  - Date 2024-04-14 | Description Insurance coverage prepayment PRE-0002 | Amount 
$-49,392.29 | Running Balance $119,435.61
  - Date 2024-04-24 | Description Rent prepayment PRE-0001 | Amount $-51,654.59 | Running 
Balance $67,781.02
  - Date 2024-07-28 | Description Asset purchase ASSET-0001 | Amount $-52,760.28 | Running 
Balance $15,020.74
  - Date 2024-09-27 | Description Loan draw LOAN-0001 | Amount $298,511.63 | Running Balance
 $313,532.37
  - Date 2024-10-07 | Description Oakline Services receipt RCPT-0001 | Amount $-16.98 | 
Running Balance $313,515.39
  - Date 2024-12-09 | Description Asset sale TAG-0001 | Amount $45,934.33 | Running Balance 
$359,449.72
  - Date 2024-12-15 | Description Customer settlement INV-0001 | Amount $33,429.67 | Running
 Balance $392,879.39
  - Date 2024-12-20 | Description Payroll PAYRUN-0001 | Amount $-92,321.48 | Running Balance
 $300,557.91
  - Date 2024-12-30 | Description Transfer out TRX-0001 | Amount $-341,022.53 | Running 
Balance $-40,464.62
  - Date 2025-01-03 | Description Loan payment LOAN-0002 | Amount $-40,891.60 | Running 
Balance $-81,356.22
  - Date 2025-01-30 | Description Supplier settlement BILL-0001 | Amount $-29,739.96 | 
Running Balance $-111,096.18
  - Date 2025-02-06 | Description Lease payment LEASE-0001 | Amount $-48,544.32 | Running 
Balance $-159,640.50

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
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Beacon Software
75 Market Road, Mumbai
Document Date: 2025-03-31

Reference Box
-------------
Document ID: D050
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $341,022.53

Statement Rows
--------------
Rows:
  - Date 2024-12-30 | Description Transfer in TRX-0001 | Amount $341,022.53 | Running 
Balance $341,022.53

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
- [x] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [x] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes: No entries expected on a flagged packet — correct.

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

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `exchange_rate_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: FX support doesn't translate to the stated functional amount.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
