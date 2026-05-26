# Verification Packet — COV_NEG_00_DEFERRED_TAX_ROLLFORWARD_MISMATC

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** December 2024
- **Period start → end:** 2024-12-01 → 2024-12-31
- **Entity:** Beacon Clinic
- **Currency (display / functional):** USD / USD
- **Tax regime:** `vat`
- **Document count:** 31
- **Labeled as inconsistent:** True
- **Inconsistency codes:** deferred_tax_rollforward_mismatch
- **Inconsistency reasons:** Deferred tax rollforward does not reconcile the opening liability, current movement, and ending liability.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-12-01_

**Assets**
- Cash: 32,059.15
- Accounts Receivable: 5,080.28
- Prepaid Rent: 1,095.92
- Office Supplies: 1,055.05
- Equipment: 8,732.89

**Liabilities**
- Accounts Payable: 1,496.37
- Accrued Expenses: 756.08
- Loans Payable: 5,073.97

**Equity**
- Retained Earnings: 7,787.65
- Owner's Equity: 32,909.22


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-12-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-12-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $32,059.15
  - Section assets | Account Accounts Receivable | Amount $5,080.28
  - Section assets | Account Prepaid Rent | Amount $1,095.92
  - Section assets | Account Office Supplies | Amount $1,055.05
  - Section assets | Account Equipment | Amount $8,732.89
  - Section liabilities | Account Accounts Payable | Amount $1,496.37
  - Section liabilities | Account Accrued Expenses | Amount $756.08
  - Section liabilities | Account Loans Payable | Amount $5,073.97
  - Section equity | Account Retained Earnings | Amount $7,787.65
  - Section equity | Account Owner's Equity | Amount $32,909.22

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2024-12-01

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Oakline Services
Property: Cedar Plaza
Service Start: 2024-12-01
Service End: 2025-02-28
Total: $9,116.69
Monthly Amount: $3,038.90

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2024-12-02

```
INSURANCE NOTICE
================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-02

To
--
Marina Assurance
Vendor remittance address on file

Terms
-----
Service Start: 2024-12-02
Service End: 2025-03-01

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Marina Assurance
Covered Item: Harbor View Offices
Coverage Start: 2024-12-02
Coverage End: 2025-03-01
Total Premium: $5,036.02
Monthly Amount: $1,678.67

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
- **Date:** 2024-12-04

```
LEASE AGREEMENT / REFERENCE COPY
================================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-04

To
--
Golden State Finance

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: December 2024

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Golden State Finance
Commencement Date: 2024-12-04
Term Months: 24
Monthly Payment Amount: $2,030.11
Incremental Borrowing Rate: 0.06
ROU Asset Amount: $45,805.10
Lease Liability Amount: $45,805.10

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-05

```
CUSTOMER INVOICE
================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-05

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: December 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 2024-12-28

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-12-28
Subtotal: $7,086.94
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $1,417.39
Total: $8,504.33

Line Items
----------
Items:
  - Description Consulting sprint | Amount $1,649.41
  - Description Follow-up support | Amount $5,437.53

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-05

```
VENDOR INVOICE
==============

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-05

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: December 2024

Terms
-----
Due Date: 2024-12-26

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-12-26
Subtotal: $3,155.28
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: $394.41
Total: $3,549.69

Bill Lines
----------
Lines:
  - Description Review pack | Amount $1,314.34
  - Description Support fee | Amount $1,840.94

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D029 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-12-05

```
CANCELLATION NOTE
=================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-05

Reference Box
-------------
Document ID: D029
Document Type: cancellation_note
Period: December 2024

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D029
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-11

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: $5,637.36
Draw Amount: $22,139.58
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $27,776.94
Note: Scheduled lender activity for the selected period.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-12-14

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: $225.75
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $55.07
  - Description Travel Incidentals | Amount $170.68
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-15

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Vertex Supply Co.
Asset Name: Server rack
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $23,682.43
Paid Cash: $6,824.36
Financed Amount: $16,858.07
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-22

```
PAYMENT ADVICE
==============

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-22

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: December 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Meridian Support LLP
Amount: $2,829.96
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-23

```
TRANSFER ADVICE
===============

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-23

Reference Box
-------------
Document ID: D028
Document Type: transfer_advice
Period: December 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $22,405.11
Transfer Date: 2024-12-23
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
- **Date:** 2024-12-25

```
PAYMENT ADVICE
==============

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-25

To
--
Aster Point Services

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: December 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: $7,425.47
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-26

```
ASSET DISPOSAL NOTICE
=====================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-26

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: December 2024

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Original Cost: $8,732.89
Accumulated Depreciation: 181.94
Net Book Value: $8,550.95
Proceeds Amount: $7,011.78
Gain Loss Amount: $1,539.17
Gain Loss Type: Loss

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-26

```
SALE PROCEEDS ADVICE
====================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-26

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: December 2024

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Metro Edge Partners
Asset Tag: OPEN-EQU
Proceeds Amount: $7,011.78
Settlement Date: 2024-12-26
Payment Reference: BNK-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D024 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2024-12-26

```
LEASE PAYMENT NOTICE
====================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-26

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: December 2024

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 2024-12-26
Payment Amount: $2,030.11
Interest Amount: $229.03
Principal Amount: $1,801.08

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-26

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: $16,963.70
Draw Amount: $0.00
Principal Paid: $9,970.28
Interest Paid: $1,387.97
Ending Principal: $6,993.42
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-12-28

```
PAYROLL SUMMARY
===============

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-28

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: December 2024
Headcount: 4
Gross Pay: $12,240.67
Employer Tax: 1,332.76
Cash Outflow: $13,573.43

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-12-28

```
UTILITY INVOICE
===============

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-28

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: December 2024

Terms
-----
Due Date: 2025-01-05

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: December 2024
Due Date: 2025-01-05
Total: $548.00

Charges
-------
Charges:
  - Description Electricity | Amount $236.59
  - Description Water | Amount $311.41

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-28

```
LEASE MODIFICATION NOTICE / REFERENCE COPY
==========================================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-28

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: December 2024

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 2024-12-28
Old Liability Balance: $44,004.02
Remeasured Liability Balance: $49,236.35
Liability Remeasurement Delta Amount: $5,232.33
ROU Asset Adjustment Amount: $5,232.33

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
- **Date:** 2024-12-28

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-28

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: December 2024

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: $49,236.35
Payment Amount: $0.00
Interest Amount: $0.00
Principal Amount: $0.00
Ending Liability Balance: $49,236.35
ROU Amortization Amount: $0.00

Footer
------
Internal document packet copy.
Page marker: D026
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
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: December 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $3,038.90

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
- **Date:** 2024-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: December 2024
Reference: PRE-0002

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0002
Subject: Insurance coverage release
Reference: PRE-0002
Recognized Amount: $1,678.67

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
- **Date:** 2024-12-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $8,732.89
Useful Life Months: 48
Current Period Charge: $181.94
Accumulated Depreciation: 181.94
```

### Document D018 — Tax Depreciation Schedule

- **Type:** `tax_depreciation_schedule`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D018
Document Type: tax_depreciation_schedule
Period: December 2024

Book Tax Difference
-------------------
Schedule ID: TAXDEP-0001
Asset Tag: OPEN-EQU
Book Depreciation Amount: $181.94
Tax Depreciation Amount: $307.86
Temporary Difference Amount: $125.92
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
DEFERRED TAX MEMO
=================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D019
Document Type: deferred_tax_memo
Period: December 2024

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0001
Asset Tag: OPEN-EQU
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $31.48
Deferred Tax Liability Ending: $1,376.46
Deferred Tax Expense Amount: $31.48

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
- **Date:** 2024-12-31

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: December 2024

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: OPEN-EQU
Book Depreciation Amount: $8,550.95
Tax Depreciation Amount: $9,187.38
Temporary Difference Amount: $636.43
Tax Rate: 25.00%

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Deferred Tax Memo

- **Type:** `deferred_tax_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
DEFERRED TAX MEMO
=================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D021
Document Type: deferred_tax_memo
Period: December 2024

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0002
Asset Tag: OPEN-EQU
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $159.11
Deferred Tax Liability Ending: $159.11
Deferred Tax Expense Amount: $159.11

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
- **Date:** 2024-12-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D023
Document Type: lease_amortization_schedule
Period: December 2024

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: $45,805.10
Payment Amount: $2,030.11
Interest Amount: $229.03
Principal Amount: $1,801.08
Ending Liability Balance: $44,004.02
ROU Amortization Amount: $1,908.55

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D030 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D030
Document Type: bank_statement
Period: December 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-MATC
Statement Currency: USD
Opening Balance: $32,059.15
Closing Balance: $-4,763.70

Statement Rows
--------------
Rows:
  - Date 2024-12-01 | Description Rent prepayment PRE-0001 | Amount $-9,116.69 | Running 
Balance $22,942.46
  - Date 2024-12-02 | Description Insurance coverage prepayment PRE-0002 | Amount $-5,036.02
 | Running Balance $17,906.44
  - Date 2024-12-11 | Description Loan draw LOAN-0001 | Amount $22,139.58 | Running Balance 
$40,046.02
  - Date 2024-12-14 | Description Meridian Support LLP receipt RCPT-0001 | Amount $-225.75 |
 Running Balance $39,820.27
  - Date 2024-12-15 | Description Asset purchase ASSET-0001 | Amount $-6,824.36 | Running 
Balance $32,995.91
  - Date 2024-12-22 | Description Supplier settlement BILL-0001 | Amount $-2,829.96 | 
Running Balance $30,165.95
  - Date 2024-12-23 | Description Transfer out TRX-0001 | Amount $-22,405.11 | Running 
Balance $7,760.84
  - Date 2024-12-25 | Description Customer settlement INV-0001 | Amount $7,425.47 | Running 
Balance $15,186.31
  - Date 2024-12-26 | Description Asset sale OPEN-EQU | Amount $7,011.78 | Running Balance 
$22,198.09
  - Date 2024-12-26 | Description Lease payment LEASE-0001 | Amount $-2,030.11 | Running 
Balance $20,167.98
  - Date 2024-12-26 | Description Loan payment LOAN-0002 | Amount $-11,358.25 | Running 
Balance $8,809.73
  - Date 2024-12-28 | Description Payroll PAYRUN-0001 | Amount $-13,573.43 | Running Balance
 $-4,763.70

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D030
```

### Document D031 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Beacon Clinic
18 Marina Avenue, Chennai
Date: 2024-12-31

Reference Box
-------------
Document ID: D031
Document Type: bank_statement
Period: December 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-TC99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $22,405.11

Statement Rows
--------------
Rows:
  - Date 2024-12-23 | Description Transfer in TRX-0001 | Amount $22,405.11 | Running Balance
 $22,405.11

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D031
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
Is the labeled contradiction (codes: `deferred_tax_rollforward_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: DTL rollforward doesn't tie opening to closing.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
