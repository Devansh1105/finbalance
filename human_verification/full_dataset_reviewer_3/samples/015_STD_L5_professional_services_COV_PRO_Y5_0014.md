# Verification Packet — COV_PRO_Y5_0014

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Pioneer Clinic
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 50
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 123,611.72
- Accounts Receivable: 16,163.13
- Prepaid Rent: 10,469.39
- Prepaid Insurance: 3,932.33
- Office Supplies: 2,526.41
- Equipment: 32,204.12
- Furniture: 11,200.90

**Liabilities**
- Accounts Payable: 14,674.90
- Accrued Expenses: 6,359.55
- Unearned Revenue: 10,408.76
- Loans Payable: 11,675.37
- Notes Payable: 9,035.30

**Equity**
- Retained Earnings: 35,821.87
- Owner's Equity: 112,132.25


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
  - Section assets | Account Cash | Amount GBP 123,611.72
  - Section assets | Account Accounts Receivable | Amount GBP 16,163.13
  - Section assets | Account Prepaid Rent | Amount GBP 10,469.39
  - Section assets | Account Prepaid Insurance | Amount GBP 3,932.33
  - Section assets | Account Office Supplies | Amount GBP 2,526.41
  - Section assets | Account Equipment | Amount GBP 32,204.12
  - Section assets | Account Furniture | Amount GBP 11,200.90
  - Section liabilities | Account Accounts Payable | Amount GBP 14,674.90
  - Section liabilities | Account Accrued Expenses | Amount GBP 6,359.55
  - Section liabilities | Account Unearned Revenue | Amount GBP 10,408.76
  - Section liabilities | Account Loans Payable | Amount GBP 11,675.37
  - Section liabilities | Account Notes Payable | Amount GBP 9,035.30
  - Section equity | Account Retained Earnings | Amount GBP 35,821.87
  - Section equity | Account Owner's Equity | Amount GBP 112,132.25

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-01-15

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Oakline Services
Property: Cedar Plaza
Service Start: 15/01/2025
Service End: 14/04/2025
Total: GBP 16,233.80
Monthly Amount: GBP 5,411.27

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2025-01-20

```
INSURANCE NOTICE
================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 20/01/2025

To
--
Marina Assurance
Vendor remittance address on file

Terms
-----
Service Start: 20/01/2025
Service End: 19/04/2025

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Marina Assurance
Covered Item: Marina Heights
Coverage Start: 20/01/2025
Coverage End: 19/04/2025
Total Premium: GBP 49,411.38
Monthly Amount: GBP 16,470.46

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-05

```
CUSTOMER INVOICE
================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 05/02/2025

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 25/02/2025

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 25/02/2025
Subtotal: GBP 43,821.80
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 8,764.36
Total: GBP 52,586.16

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 8,821.85
  - Description Follow-up support | Amount GBP 34,999.95

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-07

```
VENDOR INVOICE
==============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 07/03/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025

Terms
-----
Due Date: 18/03/2025

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 18/03/2025
Subtotal: GBP 41,966.23
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 8,393.25
Total: GBP 50,359.48

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 13,914.27
  - Description Support fee | Amount GBP 28,051.96

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D035 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
CUSTOMER INVOICE
================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/03/2025

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D035
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0003

Terms
-----
Due Date: 16/04/2025

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 16/04/2025
Total: GBP 59,611.73

Line Items
----------
Items:
  - Description Monthly retainer | Amount GBP 14,806.77
  - Description Draft billing copy | Amount GBP 44,804.96

Notes
-----
Billing office archive copy retained with the packet.

Footer
------
Internal document packet copy.
Page marker: D035
```

### Document D029 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-04-01

```
RETAINER AGREEMENT MEMO
=======================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 01/04/2025

Reference Box
-------------
Document ID: D029
Document Type: retainer_agreement_memo
Period: FY 2025
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
Total Contract Value: GBP 217,279.78

Explanation
-----------
Narrative: Customer Crescent Labs agreed to a service package spanning 12 months.

Footer
------
Internal document packet copy.
Page marker: D029
```

### Document D030 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-01

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 01/04/2025

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D030
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 14/04/2025

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 14/04/2025
Subtotal: GBP 197,527.07
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 19,752.71
Total: GBP 217,279.78

Line Items
----------
Items:
  - Description Business Suite | Amount GBP 49,741.33
  - Description Service coverage under contract | Amount GBP 147,785.74

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D042 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-04-01

```
CANCELLATION NOTE
=================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 01/04/2025

Reference Box
-------------
Document ID: D042
Document Type: cancellation_note
Period: FY 2025

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
Page marker: D042
```

### Document D022 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2025-04-02

```
LEASE AGREEMENT
===============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 02/04/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: FY 2025

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Vertex Supply Co.
Commencement Date: 02/04/2025
Term Months: 48
Monthly Payment Amount: GBP 18,438.82
Incremental Borrowing Rate: 0.09
ROU Asset Amount: GBP 740,959.96
Lease Liability Amount: GBP 740,959.96

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D036 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `support_doc`
- **Date:** 2025-04-03

```
CANCELLATION NOTE
=================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 03/04/2025

Reference Box
-------------
Document ID: D036
Document Type: cancellation_note
Period: FY 2025

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
Page marker: D036
```

### Document D037 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-03

```
CUSTOMER INVOICE
================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 03/04/2025

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D037
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0003

Terms
-----
Due Date: 16/04/2025

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0003

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 16/04/2025
Total: GBP 59,542.81

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 13,463.16
  - Description Reissued billing | Amount GBP 46,079.65

Footer
------
Generated for synthetic accounting research use.
Page marker: D037
```

### Document D043 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-04-03

```
SECONDARY COPY
==============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 03/04/2025

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D043
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0004
Counterparty: Oak Harbor Foods
Total: GBP 59,542.81
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Generated for synthetic accounting research use.
Page marker: D043
```

### Document D038 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-06

```
CUSTOMER INVOICE
================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 06/04/2025

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D038
Document Type: customer_invoice
Period: FY 2025
Contract Ref: FXCTR-0001

Terms
-----
Due Date: 18/04/2025

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: FXCTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: FXINV-0001
Due Date: 18/04/2025
Total: $65,442.08

Line Items
----------
Items:
  - Description Review pack | Amount $21,865.20
  - Description Foreign-currency support | Amount $43,576.88

Footer
------
Internal document packet copy.
Page marker: D038
```

### Document D039 — Exchange Rate Notice

- **Type:** `exchange_rate_notice`
- **Role:** `support_doc`
- **Date:** 2025-04-06

```
EXCHANGE RATE NOTICE
====================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 06/04/2025

Reference Box
-------------
Document ID: D039
Document Type: exchange_rate_notice
Period: FY 2025
Reference: FXINV-0001

Rate Summary
------------
Notice Number: RATE-0001
Reference: FXINV-0001
Rate Date: 06/04/2025
Rate Type: Spot rate at invoice date

Conversion Details
------------------
Source Currency: USD
Source Amount: $65,442.08
Functional Currency: GBP
Exchange Rate: 0.7692
Functional Amount: GBP 50,338.05

Footer
------
Internal document packet copy.
Page marker: D039
```

### Document D045 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-04-06

```
CANCELLATION NOTE
=================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 06/04/2025

Reference Box
-------------
Document ID: D045
Document Type: cancellation_note
Period: FY 2025

Cancellation Summary
--------------------
Note Number: CNCL-0003
Withdrawn Reference: FXINV-0001-OLD
Replacement Reference: FXINV-0001

Background
----------
Narrative: FXINV-0001-OLD is withdrawn and must not be posted. Use FXINV-0001 as the only 
valid invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D045
```

### Document D047 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-04-06

```
CANCELLATION NOTE
=================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 06/04/2025

Reference Box
-------------
Document ID: D047
Document Type: cancellation_note
Period: FY 2025

Cancellation Summary
--------------------
Note Number: CNCL-0004
Withdrawn Reference: FXINV-0001-OLD
Replacement Reference: FXINV-0001

Background
----------
Narrative: FXINV-0001-OLD is withdrawn and must not be posted. Use FXINV-0001 as the only 
valid invoice.

Footer
------
Internal document packet copy.
Page marker: D047
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-11

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Prime Utility Desk
Asset Name: CNC router
Asset Tag: TAG-0001
Useful Life Months: 36
Total: GBP 202,960.74
Paid Cash: GBP 79,428.28
Financed Amount: GBP 123,532.46
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-07-09

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: GBP 48,424.25
Draw Amount: GBP 136,185.03
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 184,609.28
Note: Scheduled lender activity for the selected period.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-07-28

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Pace Office Mart
Total: GBP 561.90
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount GBP 177.65
  - Description Travel Incidentals | Amount GBP 384.25
```

### Document D024 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2025-09-23

```
LEASE PAYMENT NOTICE / REFERENCE COPY
=====================================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 23/09/2025

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: FY 2025

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 23/09/2025
Payment Amount: GBP 55,316.46
Interest Amount: GBP 16,671.60
Principal Amount: GBP 38,644.86

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-09-24

```
TRANSFER ADVICE
===============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 24/09/2025

Reference Box
-------------
Document ID: D028
Document Type: transfer_advice
Period: FY 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: GBP 275,564.40
Transfer Date: 24/09/2025
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
- **Date:** 2025-10-02

```
PAYMENT ADVICE
==============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 02/10/2025

To
--
Aster Point Services

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: GBP 45,150.21
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-10-27

```
ASSET DISPOSAL NOTICE
=====================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 27/10/2025

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: FY 2025

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Original Cost: GBP 32,204.12
Accumulated Depreciation: 8,051.04
Net Book Value: GBP 24,153.08
Proceeds Amount: GBP 19,805.53
Gain Loss Amount: GBP 4,347.55
Gain Loss Type: Loss

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2025-10-27

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 27/10/2025

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: FY 2025

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Metro Edge Partners
Asset Tag: OPEN-EQU
Proceeds Amount: GBP 19,805.53
Settlement Date: 27/10/2025
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-03

```
PAYMENT ADVICE
==============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 03/11/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: GBP 35,483.76
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-06

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: GBP 31,590.20
Draw Amount: GBP 0.00
Principal Paid: GBP 25,680.05
Interest Paid: GBP 2,133.40
Ending Principal: GBP 5,910.15
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-09

```
UTILITY INVOICE
===============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 09/11/2025

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: FY 2025

Terms
-----
Due Date: 25/11/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: FY 2025
Due Date: 25/11/2025
Total: GBP 1,983.43

Charges
-------
Charges:
  - Description Electricity | Amount GBP 820.01
  - Description Water | Amount GBP 1,163.42

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-11-18

```
PAYROLL SUMMARY
===============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 18/11/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025
Headcount: 7
Gross Pay: GBP 24,951.26
Employer Tax: 2,449.11
Cash Outflow: GBP 27,400.37

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-11-26

```
LEASE MODIFICATION NOTICE
=========================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 26/11/2025

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: FY 2025

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 26/11/2025
Old Liability Balance: GBP 702,315.10
Remeasured Liability Balance: GBP 761,214.55
Liability Remeasurement Delta Amount: GBP 58,899.45
ROU Asset Adjustment Amount: GBP 58,899.45

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
- **Date:** 2025-11-26

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 26/11/2025

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: FY 2025

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: GBP 761,214.55
Payment Amount: GBP 0.00
Interest Amount: GBP 0.00
Principal Amount: GBP 0.00
Ending Liability Balance: GBP 761,214.55
ROU Amortization Amount: GBP 0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D026
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
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: FY 2025
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: GBP 5,411.27

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
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: FY 2025
Reference: PRE-0002

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0002
Subject: Insurance coverage release
Reference: PRE-0002
Recognized Amount: GBP 16,470.46

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
- **Date:** 2025-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D015
Document Type: fixed_asset_rollforward
Period: FY 2025

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: GBP 32,204.12
Useful Life: 48
Current Charge: GBP 8,051.04
Accumulated Depreciation: 8,051.04
Opening Balance: GBP 32,204.12
Additions: 0.00
Disposals: 0.00
Ending Balance: GBP 32,204.12

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D018 — Tax Depreciation Schedule

- **Type:** `tax_depreciation_schedule`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D018
Document Type: tax_depreciation_schedule
Period: FY 2025

Book Tax Difference
-------------------
Schedule ID: TAXDEP-0001
Asset Tag: OPEN-EQU
Book Depreciation Amount: GBP 8,051.04
Tax Depreciation Amount: GBP 14,084.92
Temporary Difference Amount: GBP 6,033.88
Tax Rate: 25.00%

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
DEFERRED TAX MEMO
=================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D019
Document Type: deferred_tax_memo
Period: FY 2025

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0001
Asset Tag: OPEN-EQU
Opening Deferred Tax Liability: GBP 0.00
Current Period Deferred Tax Movement: GBP 1,508.47
Deferred Tax Liability Ending: GBP 1,508.47
Deferred Tax Expense Amount: GBP 1,508.47

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
- **Date:** 2025-12-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: FY 2025

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: OPEN-EQU
Book Depreciation Amount: GBP 24,153.08
Tax Depreciation Amount: GBP 25,613.73
Temporary Difference Amount: GBP 1,460.65
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
DEFERRED TAX MEMO
=================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D021
Document Type: deferred_tax_memo
Period: FY 2025

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0002
Asset Tag: OPEN-EQU
Opening Deferred Tax Liability: GBP 0.00
Current Period Deferred Tax Movement: GBP 365.16
Deferred Tax Liability Ending: GBP 365.16
Deferred Tax Expense Amount: GBP 365.16

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
- **Date:** 2025-12-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D023
Document Type: lease_amortization_schedule
Period: FY 2025

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: GBP 740,959.96
Payment Amount: GBP 55,316.46
Interest Amount: GBP 16,671.60
Principal Amount: GBP 38,644.86
Ending Liability Balance: GBP 702,315.10
ROU Amortization Amount: GBP 185,239.99

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D031 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
REVENUE RECOGNITION SCHEDULE / REFERENCE COPY
=============================================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D031
Document Type: revenue_recognition_schedule
Period: FY 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: FY 2025
Opening Deferred: GBP 197,527.07
Added Deferred: GBP 0.00
Released This Period: 197,527.07
Ending Deferred: GBP 0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D031
```

### Document D032 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D032
Document Type: service_period_memo
Period: FY 2025
Reference: FY 2025

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2025
Recognized Amount: GBP 6,304.85

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
- **Date:** 2025-12-31

```
AR AGING SUMMARY
================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D033
Document Type: ar_aging_summary
Period: FY 2025

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2025
Total Open: GBP 7,435.95

Customer Lines
--------------
Lines:
  - Customer Aster Point Services | Reference INV-0001 | Current GBP 4,348.68 | Past Due 
3,087.27

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
- **Date:** 2025-12-31

```
CREDIT MEMO
===========

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 31/12/2025

To
--
Aster Point Services

Reference Box
-------------
Document ID: D034
Document Type: credit_memo
Period: FY 2025
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Aster Point Services
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: GBP 3,087.27

Footer
------
Generated for synthetic accounting research use.
Page marker: D034
```

### Document D040 — FX Remeasurement Memo

- **Type:** `fx_remeasurement_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
FX REMEASUREMENT MEMO
=====================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D040
Document Type: fx_remeasurement_memo
Period: FY 2025
Reference: FXINV-0001

Remeasurement Details
---------------------
Memo ID: FXREM-0001
Reference: FXINV-0001
Source Currency: USD
Functional Currency: GBP
Source Amount: $65,442.08
Booked Amount: GBP 50,338.05
Closing Rate: 0.7635
Remeasured Amount: GBP 49,965.03
Difference Amount: GBP 373.02
Narrative: Open foreign-currency balance remeasured at the closing rate.

Footer
------
Internal document packet copy.
Page marker: D040
```

### Document D041 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 31/12/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D041
Document Type: vendor_statement
Period: FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Vertex Supply Co.
Closing Balance: GBP 14,875.72

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount GBP 14,875.72 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D041
```

### Document D044 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D044
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0001
Subject: Scanning checklist for back-office staff
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

### Document D046 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D046
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Annual leave policy reminder
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
Page marker: D046
```

### Document D048 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D048
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0003
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
Internal document packet copy.
Page marker: D048
```

### Document D049 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D049
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0014
Statement Currency: GBP
Opening Balance: GBP 123,611.72
Closing Balance: GBP -242,461.31

Statement Rows
--------------
Rows:
  - Date 15/01/2025 | Description Rent prepayment PRE-0001 | Amount GBP -16,233.80 | Running
 Balance GBP 107,377.92
  - Date 20/01/2025 | Description Insurance coverage prepayment PRE-0002 | Amount GBP 
-49,411.38 | Running Balance GBP 57,966.54
  - Date 11/05/2025 | Description Asset purchase ASSET-0001 | Amount GBP -79,428.28 | 
Running Balance GBP -21,461.74
  - Date 09/07/2025 | Description Loan draw LOAN-0001 | Amount GBP 136,185.03 | Running 
Balance GBP 114,723.29
  - Date 28/07/2025 | Description Pace Office Mart receipt RCPT-0001 | Amount GBP -561.90 | 
Running Balance GBP 114,161.39
  - Date 23/09/2025 | Description Lease payment LEASE-0001 | Amount GBP -55,316.46 | Running
 Balance GBP 58,844.93
  - Date 24/09/2025 | Description Transfer out TRX-0001 | Amount GBP -275,564.40 | Running 
Balance GBP -216,719.47
  - Date 02/10/2025 | Description Customer settlement INV-0001 | Amount GBP 45,150.21 | 
Running Balance GBP -171,569.26
  - Date 27/10/2025 | Description Asset sale OPEN-EQU | Amount GBP 19,805.53 | Running 
Balance GBP -151,763.73
  - Date 03/11/2025 | Description Supplier settlement BILL-0001 | Amount GBP -35,483.76 | 
Running Balance GBP -187,247.49
  - Date 06/11/2025 | Description Loan payment LOAN-0002 | Amount GBP -27,813.45 | Running 
Balance GBP -215,060.94
  - Date 18/11/2025 | Description Payroll PAYRUN-0001 | Amount GBP -27,400.37 | Running 
Balance GBP -242,461.31

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D049
```

### Document D050 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Clinic
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D050
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-1499
Statement Currency: GBP
Opening Balance: GBP 0.00
Closing Balance: GBP 275,564.40

Statement Rows
--------------
Rows:
  - Date 24/09/2025 | Description Transfer in TRX-0001 | Amount GBP 275,564.40 | Running 
Balance GBP 275,564.40

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D050
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 43,821.80 | D002 | 2025-02-05 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 8,764.36 | D002 | 2025-02-05 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 41,966.23 | D003 | 2025-03-07 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 8,393.25 | D003 | 2025-03-07 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 561.90 | D004 | 2025-07-28 | expense_receipt |
| 6 | Cash | Accounts Receivable | 45,150.21 | D005, D002 | 2025-10-02 | customer_payment |
| 7 | Accounts Payable | Cash | 35,483.76 | D006, D003 | 2025-11-03 | supplier_payment |
| 8 | Salaries Expense | Cash | 24,951.26 | D007 | 2025-11-18 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 2,449.11 | D007 | 2025-11-18 | payroll_tax |
| 10 | Prepaid Rent | Cash | 16,233.80 | D008 | 2025-01-15 | prepaid_rent_purchase |
| 11 | Rent Expense | Prepaid Rent | 5,411.27 | D008, D009 | 2025-12-31 | prepaid_rent_release |
| 12 | Prepaid Insurance | Cash | 49,411.38 | D010 | 2025-01-20 | prepaid_insurance_purchase |
| 13 | Insurance Expense | Prepaid Insurance | 16,470.46 | D010, D011 | 2025-12-31 | prepaid_insurance_release |
| 14 | Utilities Expense | Accounts Payable | 1,983.43 | D012 | 2025-11-09 | utilities_bill |
| 15 | Cash | Loans Payable | 136,185.03 | D013 | 2025-07-09 | loan_draw |
| 16 | Equipment | Cash | 79,428.28 | D014 | 2025-05-11 | equipment_purchase_cash |
| 17 | Equipment | Notes Payable | 123,532.46 | D014 | 2025-05-11 | equipment_purchase_financed |
| 18 | Depreciation Expense | Accumulated Depreciation | 8,051.04 | D015 | 2025-12-31 | depreciation |
| 19 | Cash | Equipment | 19,805.53 | D016, D017 | 2025-10-27 | asset_disposal_proceeds |
| 20 | Accumulated Depreciation | Equipment | 8,051.04 | D016, D017 | 2025-10-27 | asset_disposal_remove_accumulated_depreciation |
| 21 | Loss on Disposal | Equipment | 4,347.55 | D016, D017 | 2025-10-27 | asset_disposal_loss |
| 22 | Deferred Tax Expense | Deferred Tax Liability | 1,508.47 | D018, D019 | 2025-12-31 | deferred_tax_depreciation |
| 23 | Deferred Tax Expense | Deferred Tax Liability | 365.16 | D016, D017, D020, D021 | 2025-12-31 | asset_disposal_with_deferred_tax |
| 24 | Right-of-Use Asset | Lease Liability | 740,959.96 | D022 | 2025-04-02 | baseline_lease_initial_recognition |
| 25 | Lease Liability | Cash | 38,644.86 | D022, D023, D024 | 2025-09-23 | baseline_lease_principal |
| 26 | Lease Interest Expense | Cash | 16,671.60 | D022, D023, D024 | 2025-09-23 | baseline_lease_interest |
| 27 | Lease Amortization Expense | Right-of-Use Asset | 185,239.99 | D022, D023 | 2025-12-31 | baseline_lease_amortization |
| 28 | Right-of-Use Asset | Lease Liability | 58,899.45 | D025, D026 | 2025-11-26 | lease_modification |
| 29 | Loans Payable | Cash | 25,680.05 | D027 | 2025-11-06 | loan_repayment_principal |
| 30 | Interest Expense | Cash | 2,133.40 | D027 | 2025-11-06 | loan_repayment_interest |
| 31 | Reserve Cash | Cash | 275,564.40 | D028 | 2025-09-24 | interbank_transfer |
| 32 | Accounts Receivable | Unearned Revenue | 197,527.07 | D029, D030 | 2025-04-01 | retainer_invoice |
| 33 | Accounts Receivable | Sales Tax Payable | 19,752.71 | D029, D030 | 2025-04-01 | retainer_invoice_tax |
| 34 | Unearned Revenue | Service Revenue | 197,527.07 | D031, D030 | 2025-12-31 | retainer_release |
| 35 | Utilities Expense | Accrued Expenses | 6,304.85 | D032 | 2025-12-31 | expense_accrual |
| 36 | Bad Debt Expense | Accounts Receivable | 3,087.27 | D033, D034, D002 | 2025-12-31 | bad_debt_review |
| 37 | Accounts Receivable | Service Revenue | 59,542.81 | D035, D036, D037 | 2025-04-03 | reissued_invoice |
| 38 | Accounts Receivable | Service Revenue | 50,338.05 | D038, D039 | 2025-04-06 | fx_service_invoice |
| 39 | Foreign Exchange Loss | Accounts Receivable | 373.02 | D040, D038 | 2025-12-31 | fx_remeasurement |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: -242,461.31
- Accounts Receivable: 347,299.43
- Prepaid Rent: 21,291.92
- Prepaid Insurance: 36,873.25
- Office Supplies: 2,526.41
- Equipment: 202,960.74
- Furniture: 11,200.90
- Input Tax Receivable: 8,393.25
- Right-of-Use Asset: 614,619.42
- Reserve Cash: 275,564.40

**Liabilities**
- Accounts Payable: 31,534.05
- Accrued Expenses: 12,664.40
- Unearned Revenue: 10,408.76
- Loans Payable: 122,180.35
- Notes Payable: 132,567.76
- Sales Tax Payable: 28,517.07
- Deferred Tax Liability: 1,873.63
- Lease Liability: 761,214.55

**Equity**
- Retained Earnings: 65,175.59
- Owner's Equity: 112,132.25

**Totals:** Assets = 1,278,268.41; Liabilities = 1,100,960.57; Equity = 177,307.84
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
