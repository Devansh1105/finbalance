# Verification Packet — COV_NEG_00_LEASE_REMEASUREMENT_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** June 2024
- **Period start → end:** 2024-06-01 → 2024-06-30
- **Entity:** Summit Software
- **Currency (display / functional):** USD / USD
- **Tax regime:** `sales_tax`
- **Document count:** 30
- **Labeled as inconsistent:** True
- **Inconsistency codes:** lease_remeasurement_mismatch
- **Inconsistency reasons:** Lease modification support does not reconcile liability remeasurement and equal ROU asset adjustment.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-06-01_

**Assets**
- Cash: 29,583.28
- Accounts Receivable: 4,292.72
- Prepaid Rent: 2,045.85
- Office Supplies: 1,431.71
- Equipment: 5,744.71

**Liabilities**
- Accounts Payable: 1,876.98
- Accrued Expenses: 518.87
- Loans Payable: 3,506.29

**Equity**
- Retained Earnings: 6,598.20
- Owner's Equity: 30,597.93


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-06-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-06-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $29,583.28
  - Section assets | Account Accounts Receivable | Amount $4,292.72
  - Section assets | Account Prepaid Rent | Amount $2,045.85
  - Section assets | Account Office Supplies | Amount $1,431.71
  - Section assets | Account Equipment | Amount $5,744.71
  - Section liabilities | Account Accounts Payable | Amount $1,876.98
  - Section liabilities | Account Accrued Expenses | Amount $518.87
  - Section liabilities | Account Loans Payable | Amount $3,506.29
  - Section equity | Account Retained Earnings | Amount $6,598.20
  - Section equity | Account Owner's Equity | Amount $30,597.93

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2024-06-01

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Beacon Industrial Supply
Property: Park Lane Residences
Service Start: 2024-06-01
Service End: 2024-08-31
Total: $9,972.83
Monthly Amount: $3,324.28

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-02

```
VENDOR INVOICE
==============

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-02

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: June 2024

Terms
-----
Due Date: 2024-06-19

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-06-19
Subtotal: $6,076.64
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: $501.32
Total: $6,577.96

Bill Lines
----------
Lines:
  - Description Support package | Amount $1,926.46
  - Description Support fee | Amount $4,150.18

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D010 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2024-06-02

```
INSURANCE NOTICE
================

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-02

To
--
Shield Mutual
Vendor remittance address on file

Terms
-----
Service Start: 2024-06-02
Service End: 2024-09-01

Coverage Notice
---------------
Notice Number: PRE-0002
Carrier: Shield Mutual
Covered Item: Marina Heights
Coverage Start: 2024-06-02
Coverage End: 2024-09-01
Total Premium: $6,574.96
Monthly Amount: $2,191.65

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
- **Date:** 2024-06-02

```
LEASE AGREEMENT
===============

From
----
Summit Software
75 Market Road, Mumbai
Document Date: 2024-06-02

To
--
Oakline Services

Reference Box
-------------
Document ID: D022
Document Type: lease_agreement
Period: June 2024

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Oakline Services
Commencement Date: 2024-06-02
Term Months: 36
Monthly Payment Amount: $2,709.50
Incremental Borrowing Rate: 0.07
ROU Asset Amount: $87,104.77
Lease Liability Amount: $87,104.77

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-07

```
CUSTOMER INVOICE
================

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-07

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: June 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 2024-06-27

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-06-27
Subtotal: $11,509.90
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: $1,093.44
Total: $12,603.34

Line Items
----------
Items:
  - Description Review pack | Amount $3,760.59
  - Description Follow-up support | Amount $7,749.31

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D014 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-10

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Pace Office Mart
Asset Name: Server rack
Asset Tag: TAG-0001
Useful Life Months: 48
Total: $36,705.63
Paid Cash: $17,260.31
Financed Amount: $19,445.32
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-06-12

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: $44.47
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $12.07
  - Description Travel Incidentals | Amount $32.40
```

### Document D013 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-13

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $1,979.98
Draw Amount: $38,012.04
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $39,992.02
Note: Scheduled lender activity for the selected period.
```

### Document D027 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-20

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: First City Bank
Opening Principal: $33,026.52
Draw Amount: $0.00
Principal Paid: $7,869.88
Interest Paid: $810.91
Ending Principal: $25,156.64
Note: Scheduled lender activity for the selected period.
```

### Document D016 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-23

```
ASSET DISPOSAL NOTICE
=====================

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-23

Reference Box
-------------
Document ID: D016
Document Type: asset_disposal_notice
Period: June 2024

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Server rack
Asset Tag: TAG-0001
Original Cost: $36,705.63
Accumulated Depreciation: 764.70
Net Book Value: $35,940.93
Proceeds Amount: $29,471.56
Gain Loss Amount: $6,469.37
Gain Loss Type: Loss

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D017 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-23

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-23

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D017
Document Type: sale_proceeds_advice
Period: June 2024

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Blue Finch Holdings
Asset Tag: TAG-0001
Proceeds Amount: $29,471.56
Settlement Date: 2024-06-23
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-06-24

```
PAYROLL SUMMARY
===============

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-24

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: June 2024
Headcount: 11
Gross Pay: $16,693.62
Employer Tax: 1,644.53
Cash Outflow: $18,338.15

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D028 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-24

```
TRANSFER ADVICE
===============

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-24

Reference Box
-------------
Document ID: D028
Document Type: transfer_advice
Period: June 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $59,055.99
Transfer Date: 2024-06-24
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D028
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-25

```
PAYMENT ADVICE
==============

From
----
Summit Software
75 Market Road, Mumbai
Document Date: 2024-06-25

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: June 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: $5,878.32
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D012 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-06-26

```
UTILITY INVOICE
===============

From
----
Summit Software
75 Market Road, Mumbai
Document Date: 2024-06-26

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: utilities_statement
Period: June 2024

Terms
-----
Due Date: 2024-07-08

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: June 2024
Due Date: 2024-07-08
Total: $721.39

Charges
-------
Charges:
  - Description Electricity | Amount $182.53
  - Description Water | Amount $538.86

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-27

```
PAYMENT ADVICE
==============

From
----
Summit Software
75 Market Road, Mumbai
Document Date: 2024-06-27

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: June 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Metro Edge Partners
Amount: $9,727.04
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D024 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2024-06-27

```
LEASE PAYMENT NOTICE
====================

From
----
Summit Software
75 Market Road, Mumbai
Document Date: 2024-06-27

Reference Box
-------------
Document ID: D024
Document Type: lease_payment_notice
Period: June 2024

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 2024-06-27
Payment Amount: $2,709.50
Interest Amount: $544.40
Principal Amount: $2,165.10

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
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
75 Market Road, Mumbai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: June 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $3,324.28

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
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: June 2024
Reference: PRE-0002

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0002
Subject: Insurance coverage release
Reference: PRE-0002
Recognized Amount: $2,191.65

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
- **Date:** 2024-06-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Server rack
Asset Tag: TAG-0001
Cost: $36,705.63
Useful Life Months: 48
Current Period Charge: $764.70
Accumulated Depreciation: 764.70
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
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D018
Document Type: tax_depreciation_schedule
Period: June 2024

Book Tax Difference
-------------------
Schedule ID: TAXDEP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: $764.70
Tax Depreciation Amount: $1,426.33
Temporary Difference Amount: $661.63
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
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D019
Document Type: deferred_tax_memo
Period: June 2024

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0001
Asset Tag: TAG-0001
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $165.41
Deferred Tax Liability Ending: $165.41
Deferred Tax Expense Amount: $165.41

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
- **Date:** 2024-06-30

```
TAX DEPRECIATION SCHEDULE
=========================

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D020
Document Type: tax_depreciation_schedule
Period: June 2024

Book Tax Difference
-------------------
Schedule ID: TAXDSP-0001
Asset Tag: TAG-0001
Book Depreciation Amount: $35,940.93
Tax Depreciation Amount: $38,110.65
Temporary Difference Amount: $2,169.72
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
75 Market Road, Mumbai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D021
Document Type: deferred_tax_memo
Period: June 2024

Deferred Tax Rollforward
------------------------
Memo ID: DTAX-0002
Asset Tag: TAG-0001
Opening Deferred Tax Liability: $0.00
Current Period Deferred Tax Movement: $542.43
Deferred Tax Liability Ending: $542.43
Deferred Tax Expense Amount: $542.43

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
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D023
Document Type: lease_amortization_schedule
Period: June 2024

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: $87,104.77
Payment Amount: $2,709.50
Interest Amount: $544.40
Principal Amount: $2,165.10
Ending Liability Balance: $84,939.67
ROU Amortization Amount: $2,419.58

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D025 — Lease Modification Notice

- **Type:** `lease_modification_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-06-30

```
LEASE MODIFICATION NOTICE
=========================

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D025
Document Type: lease_modification_notice
Period: June 2024

Remeasurement
-------------
Modification Number: LEASEMOD-0001
Agreement Number: LEASE-0001
Modification Date: 2024-06-30
Old Liability Balance: $84,939.67
Remeasured Liability Balance: $97,446.57
Liability Remeasurement Delta Amount: $11,801.48
ROU Asset Adjustment Amount: $12,506.90

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
- **Date:** 2024-06-30

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D026
Document Type: lease_amortization_schedule
Period: June 2024

Lease Schedule
--------------
Schedule ID: LEASESCH-0002
Agreement Number: LEASE-0001
Opening Liability Balance: $97,446.57
Payment Amount: $0.00
Interest Amount: $0.00
Principal Amount: $0.00
Ending Liability Balance: $97,446.57
ROU Amortization Amount: $0.00

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D029 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Summit Software
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D029
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $29,583.28
Closing Balance: $-21,721.40

Statement Rows
--------------
Rows:
  - Date 2024-06-01 | Description Rent prepayment PRE-0001 | Amount $-9,972.83 | Running 
Balance $19,610.45
  - Date 2024-06-02 | Description Insurance coverage prepayment PRE-0002 | Amount $-6,574.96
 | Running Balance $13,035.49
  - Date 2024-06-10 | Description Asset purchase ASSET-0001 | Amount $-17,260.31 | Running 
Balance $-4,224.82
  - Date 2024-06-12 | Description Meridian Support LLP receipt RCPT-0001 | Amount $-44.47 | 
Running Balance $-4,269.29
  - Date 2024-06-13 | Description Loan draw LOAN-0001 | Amount $38,012.04 | Running Balance 
$33,742.75
  - Date 2024-06-20 | Description Loan payment LOAN-0002 | Amount $-8,680.79 | Running 
Balance $25,061.96
  - Date 2024-06-23 | Description Asset sale TAG-0001 | Amount $29,471.56 | Running Balance 
$54,533.52
  - Date 2024-06-24 | Description Payroll PAYRUN-0001 | Amount $-18,338.15 | Running Balance
 $36,195.37
  - Date 2024-06-24 | Description Transfer out TRX-0001 | Amount $-59,055.99 | Running 
Balance $-22,860.62
  - Date 2024-06-25 | Description Supplier settlement BILL-0001 | Amount $-5,878.32 | 
Running Balance $-28,738.94
  - Date 2024-06-27 | Description Customer settlement INV-0001 | Amount $9,727.04 | Running 
Balance $-19,011.90
  - Date 2024-06-27 | Description Lease payment LEASE-0001 | Amount $-2,709.50 | Running 
Balance $-21,721.40

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D029
```

### Document D030 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Summit Software
75 Market Road, Mumbai
Document Date: 2024-06-30

Reference Box
-------------
Document ID: D030
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $59,055.99

Statement Rows
--------------
Rows:
  - Date 2024-06-24 | Description Transfer in TRX-0001 | Amount $59,055.99 | Running Balance
 $59,055.99

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D030
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
- Notes: No entries is right given the lease remeasurement conflict.

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
- Notes: N/A.

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [x] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `lease_remeasurement_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: ROU asset and liability remeasurement amounts conflict with modification schedule.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Acceptable.
