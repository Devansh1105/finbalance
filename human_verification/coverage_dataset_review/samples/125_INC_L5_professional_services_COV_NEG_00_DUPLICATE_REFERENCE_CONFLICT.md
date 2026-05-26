# Verification Packet — COV_NEG_00_DUPLICATE_REFERENCE_CONFLICT

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2025-26
- **Period start → end:** 2025-04-01 → 2026-03-31
- **Entity:** Willow Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `sales_tax`
- **Document count:** 50
- **Labeled as inconsistent:** True
- **Inconsistency codes:** duplicate_reference_conflict
- **Inconsistency reasons:** Two documents show the same reference with conflicting totals or status.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 157,414.07
- Accounts Receivable: 14,033.46
- Prepaid Rent: 11,502.35
- Prepaid Insurance: 7,108.20
- Office Supplies: 4,068.95
- Equipment: 33,356.02
- Furniture: 23,004.43

**Liabilities**
- Accounts Payable: 10,175.13
- Accrued Expenses: 3,880.12
- Unearned Revenue: 6,881.31
- Loans Payable: 30,442.55
- Notes Payable: 11,928.53

**Equity**
- Retained Earnings: 26,995.17
- Owner's Equity: 160,184.67


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
  - Section assets | Account Cash | Amount $157,414.07
  - Section assets | Account Accounts Receivable | Amount $14,033.46
  - Section assets | Account Prepaid Rent | Amount $11,502.35
  - Section assets | Account Prepaid Insurance | Amount $7,108.20
  - Section assets | Account Office Supplies | Amount $4,068.95
  - Section assets | Account Equipment | Amount $33,356.02
  - Section assets | Account Furniture | Amount $23,004.43
  - Section liabilities | Account Accounts Payable | Amount $10,175.13
  - Section liabilities | Account Accrued Expenses | Amount $3,880.12
  - Section liabilities | Account Unearned Revenue | Amount $6,881.31
  - Section liabilities | Account Loans Payable | Amount $30,442.55
  - Section liabilities | Account Notes Payable | Amount $11,928.53
  - Section equity | Account Retained Earnings | Amount $26,995.17
  - Section equity | Account Owner's Equity | Amount $160,184.67

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-06

```
INSURANCE NOTICE
================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2025-04-06

To
--
Shield Mutual
Vendor remittance address on file

Terms
-----
Service Start: 2025-04-06
Service End: 2025-07-05

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Shield Mutual
Covered Item: Park Lane Residences
Coverage Start: 2025-04-06
Coverage End: 2025-07-05
Total Premium: $25,338.28
Monthly Amount: $8,446.09

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-10

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Vertex Supply Co.
Property: Cedar Plaza
Service Start: 2025-04-10
Service End: 2025-07-09
Total: $52,000.61
Monthly Amount: $17,333.54

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D038 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-27

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-04-27

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D038
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: FXCTR-0001

Terms
-----
Due Date: 2025-05-11

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: FXCTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: FXINV-0001
Due Date: 2025-05-11
Total: EUR 57.554,46

Line Items
----------
Items:
  - Description Implementation work | Amount EUR 23.577,38
  - Description Foreign-currency support | Amount EUR 33.977,08

Footer
------
Internal document packet copy.
Page marker: D038
```

### Document D039 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2025-04-27

```
EXCHANGE RATE NOTICE
====================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-04-27

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
Rate Date: 2025-04-27
Rate Type: Spot rate at invoice date

Conversion Details
------------------
Source Currency: EUR
Source Amount: EUR 57.554,46
Functional Currency: USD
Exchange Rate: 1.0835
Functional Amount: $62,360.26

Footer
------
Internal document packet copy.
Page marker: D039
```

### Document D029 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-05-01

```
RETAINER AGREEMENT MEMO
=======================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-05-01

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
Total Contract Value: $103,877.29

Explanation
-----------
Narrative: Customer Metro Edge Partners agreed to a service package spanning 12 months.

Footer
------
Internal document packet copy.
Page marker: D029
```

### Document D030 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-01

```
CUSTOMER INVOICE
================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2025-05-01

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D030
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-05-16

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-05-16
Subtotal: $96,855.28
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: $7,022.01
Total: $103,877.29

Line Items
----------
Items:
  - Description Enterprise License | Amount $43,427.24
  - Description Service coverage under contract | Amount $53,428.04

Footer
------
Generated for synthetic accounting research use.
Page marker: D030
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-14

```
VENDOR INVOICE
==============

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-05-14

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
Due Date: 2025-05-31

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-05-31
Subtotal: $32,356.90
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: $2,345.88
Total: $34,702.78

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $13,099.11
  - Description Support fee | Amount $19,257.79

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D043 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-05-14

```
SECONDARY COPY
==============

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-05-14

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D043
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: BILL-0001
Counterparty: Meridian Support LLP
Total: $37,475.19
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D043
```

### Document D035 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2025-05-16

```
CUSTOMER INVOICE
================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2025-05-16

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D035
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: CTR-0003

Terms
-----
Due Date: 2025-05-28

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 2025-05-28
Total: $54,722.80

Line Items
----------
Items:
  - Description Implementation work | Amount $23,068.70
  - Description Draft billing copy | Amount $31,654.10

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
- **Date:** 2025-05-16

```
SECONDARY COPY
==============

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-05-16

To
--
Crescent Labs

Reference Box
-------------
Document ID: D041
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0003
Counterparty: Crescent Labs
Total: $54,722.80
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D041
```

### Document D036 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2025-05-21

```
CANCELLATION NOTE
=================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2025-05-21

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
- **Date:** 2025-05-21

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-05-21

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D037
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: CTR-0003

Terms
-----
Due Date: 2025-06-04

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 2025-06-04
Total: $56,582.13

Line Items
----------
Items:
  - Description Monthly retainer | Amount $13,369.08
  - Description Reissued billing | Amount $43,213.05

Footer
------
Internal document packet copy.
Page marker: D037
```

### Document D045 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-05-21

```
SECONDARY COPY
==============

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-05-21

To
--
Crescent Labs

Reference Box
-------------
Document ID: D045
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0003
Source Reference: INV-0004
Counterparty: Crescent Labs
Total: $56,582.13
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D045
```

### Document D046 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-05-21

```
SECONDARY COPY
==============

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2025-05-21

To
--
Crescent Labs

Reference Box
-------------
Document ID: D046
Document Type: secondary_copy
Period: FY 2025-26

Copy Summary
------------
Copy ID: COPY-0004
Source Reference: INV-0004
Counterparty: Crescent Labs
Total: $56,582.13
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D046
```

### Document D022 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2025-05-23

```
LEASE AGREEMENT
===============

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2025-05-23

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: FY 2025-26

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Meridian Support LLP
Commencement Date: 2025-05-23
Term Months: 36
Monthly Payment Amount: $20,938.19
Incremental Borrowing Rate: 0.07
ROU Asset Amount: $673,119.11
Lease Liability Amount: $673,119.11

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-24

```
CUSTOMER INVOICE
================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2025-06-24

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: FY 2025-26
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-07-05

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-07-05
Subtotal: $47,086.51
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: $4,473.22
Total: $51,559.73

Line Items
----------
Items:
  - Description Support package | Amount $19,078.83
  - Description Follow-up support | Amount $28,007.68

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-02

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Meridian Support LLP
Asset Name: Office laptops
Asset Tag: TAG-0001
Useful Life Months: 24
Total: $200,665.87
Paid Cash: $87,132.21
Financed Amount: $113,533.66
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-09-11

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Beacon Industrial Supply
Total: $63.71
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $26.95
  - Description Travel Incidentals | Amount $36.76
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-09-22

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $53,773.35
Draw Amount: $264,840.08
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $318,613.43
Note: Scheduled lender activity for the selected period.
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-16

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: First City Bank
Opening Principal: $275,944.59
Draw Amount: $0.00
Principal Paid: $32,422.79
Interest Paid: $4,653.19
Ending Principal: $243,521.80
Note: Scheduled lender activity for the selected period.
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-30

```
TRANSFER ADVICE
===============

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2025-12-30

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
Amount: $79,499.24
Transfer Date: 2025-12-30
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2026-01-07

```
UTILITY INVOICE
===============

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-01-07

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: FY 2025-26

Terms
-----
Due Date: 2026-01-17

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: FY 2025-26
Due Date: 2026-01-17
Total: $3,018.05

Charges
-------
Charges:
  - Description Electricity | Amount $723.12
  - Description Water | Amount $2,294.93

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-01-13

```
PAYROLL SUMMARY
===============

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-01-13

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025-26
Headcount: 9
Gross Pay: $79,464.16
Employer Tax: 7,930.01
Cash Outflow: $87,394.17

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2026-01-15

```
ASSET DISPOSAL NOTICE
=====================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-01-15

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: FY 2025-26

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Office laptops
Asset Tag: TAG-0001
Original Cost: $200,665.87
Accumulated Depreciation: 100,332.96
Net Book Value: $100,332.91
Proceeds Amount: $118,392.83
Gain Loss Amount: $18,059.92
Gain Loss Type: Gain

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-15

```
SALE PROCEEDS ADVICE
====================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-01-15

To
--
Riverfront Group

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: FY 2025-26

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Riverfront Group
Asset Tag: TAG-0001
Proceeds Amount: $118,392.83
Settlement Date: 2026-01-15
Payment Reference: BNK-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-25

```
PAYMENT ADVICE
==============

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-01-25

To
--
Riverfront Group

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: $43,396.76
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
- **Date:** 2026-01-27

```
LEASE PAYMENT NOTICE / REFERENCE COPY
=====================================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-01-27

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: FY 2025-26

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 2026-01-27
Payment Amount: $62,814.57
Interest Amount: $12,620.98
Principal Amount: $50,193.59

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-29

```
PAYMENT ADVICE
==============

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-01-29

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
Amount: $23,779.81
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-12

```
LEASE MODIFICATION NOTICE
=========================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-12

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: FY 2025-26

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 2026-03-12
Old Liability Balance: $622,925.52
Remeasured Liability Balance: $687,102.49
Liability Remeasurement Delta Amount: $64,176.97
ROU Asset Adjustment Amount: $64,176.97

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
- **Date:** 2026-03-12

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-03-12

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: FY 2025-26

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: $687,102.49
Payment Amount: $0.00
Interest Amount: $0.00
Principal Amount: $0.00
Ending Liability Balance: $687,102.49
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
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

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
Recognized Amount: $17,333.54

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
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-03-31

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
Recognized Amount: $8,446.09

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
- **Date:** 2026-03-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D015
Document Type: fixed_asset_rollforward
Period: FY 2025-26

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Office laptops
Asset Tag: TAG-0001
Cost: $200,665.87
Useful Life: 24
Current Charge: $100,332.96
Accumulated Depreciation: 100,332.96
Opening Balance: $200,665.87
Additions: 0.00
Disposals: 0.00
Ending Balance: $200,665.87

Footer
------
Internal document packet copy.
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
Willow Software
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
Book Depreciation Amount: $100,332.96
Tax Depreciation Amount: $158,016.50
Temporary Difference Amount: $57,683.54
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
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-03-31

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
Current Period Deferred Tax Movement: $14,420.89
Deferred Tax Liability Ending: $14,420.89
Deferred Tax Expense Amount: $14,420.89

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
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: FY 2025-26

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: $100,332.91
Tax Depreciation Amount: $106,201.73
Temporary Difference Amount: $5,868.82
Tax Rate: 25.00%

Footer
------
Generated for synthetic accounting research use.
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
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

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
Current Period Deferred Tax Movement: $1,467.20
Deferred Tax Liability Ending: $1,467.20
Deferred Tax Expense Amount: $1,467.20

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
Willow Software
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
Opening Liability Balance: $673,119.11
Payment Amount: $62,814.57
Interest Amount: $12,620.98
Principal Amount: $50,193.59
Ending Liability Balance: $622,925.52
ROU Amortization Amount: $224,373.04

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
REVENUE RECOGNITION SCHEDULE / REFERENCE COPY
=============================================

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-03-31

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
Opening Deferred: $96,855.28
Added Deferred: $0.00
Released This Period: 96,855.28
Ending Deferred: $0.00

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
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

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
Recognized Amount: $5,486.27

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
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D033
Document Type: ar_aging_summary
Period: FY 2025-26

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2025-26
Total Open: $8,162.97

Customer Lines
--------------
Lines:
  - Customer Riverfront Group | Reference INV-0001 | Current $6,275.53 | Past Due 1,887.44

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
- **Date:** 2026-03-31

```
CREDIT MEMO
===========

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

To
--
Riverfront Group

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
Counterparty: Riverfront Group
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: $1,887.44

Footer
------
Internal document packet copy.
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
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

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
Source Amount: EUR 57.554,46
Booked Amount: $62,360.26
Closing Rate: 1.1896
Remeasured Amount: $68,466.79
Difference Amount: $6,106.53
Narrative: Open foreign-currency balance remeasured at the closing rate.

Footer
------
Internal document packet copy.
Page marker: D040
```

### Document D042 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
VENDOR STATEMENT
================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D042
Document Type: vendor_statement
Period: FY 2025-26

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Meridian Support LLP
Closing Balance: $10,922.97

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount $10,922.97 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

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
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

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
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
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
Page marker: D044
```

### Document D047 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
VENDOR STATEMENT
================

From
----
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D047
Document Type: vendor_statement
Period: FY 2025-26

Statement Header
----------------
Statement Number: VSTMT-0002
Vendor: City Power
Closing Balance: $3,018.05

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount $3,018.05 | Status Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D047
```

### Document D048 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
MEMO
====

From
----
Willow Software
90 Hill Park, Hyderabad
Document Date: 2026-03-31

Reference Box
-------------
Document ID: D048
Document Type: memo
Period: FY 2025-26

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
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
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
Willow Software
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
Account Number: 1002-LICT
Statement Currency: USD
Opening Balance: $157,414.07
Closing Balance: $128,945.16

Statement Rows
--------------
Rows:
  - Date 2025-04-06 | Description Insurance coverage prepayment PRE-0002 | Amount 
$-25,338.28 | Running Balance $132,075.79
  - Date 2025-04-10 | Description Rent prepayment PRE-0001 | Amount $-52,000.61 | Running 
Balance $80,075.18
  - Date 2025-08-02 | Description Asset purchase ASSET-0001 | Amount $-87,132.21 | Running 
Balance $-7,057.03
  - Date 2025-09-11 | Description Beacon Industrial Supply receipt RCPT-0001 | Amount 
$-63.71 | Running Balance $-7,120.74
  - Date 2025-09-22 | Description Loan draw LOAN-0001 | Amount $264,840.08 | Running Balance
 $257,719.34
  - Date 2025-12-16 | Description Loan payment LOAN-0002 | Amount $-37,075.98 | Running 
Balance $220,643.36
  - Date 2025-12-30 | Description Transfer out TRX-0001 | Amount $-79,499.24 | Running 
Balance $141,144.12
  - Date 2026-01-13 | Description Payroll PAYRUN-0001 | Amount $-87,394.17 | Running Balance
 $53,749.95
  - Date 2026-01-15 | Description Asset sale TAG-0001 | Amount $118,392.83 | Running Balance
 $172,142.78
  - Date 2026-01-25 | Description Customer settlement INV-0001 | Amount $43,396.76 | Running
 Balance $215,539.54
  - Date 2026-01-27 | Description Lease payment LEASE-0001 | Amount $-62,814.57 | Running 
Balance $152,724.97
  - Date 2026-01-29 | Description Supplier settlement BILL-0001 | Amount $-23,779.81 | 
Running Balance $128,945.16

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
Willow Software
90 Hill Park, Hyderabad
Date: 2026-03-31

Reference Box
-------------
Document ID: D050
Document Type: bank_statement
Period: FY 2025-26

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CT99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $79,499.24

Statement Rows
--------------
Rows:
  - Date 2025-12-30 | Description Transfer in TRX-0001 | Amount $79,499.24 | Running Balance
 $79,499.24

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
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
Is the labeled contradiction (codes: `duplicate_reference_conflict`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
