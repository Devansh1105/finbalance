# Verification Packet — COV_NEG_00_ASSET_DISPOSAL_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** July 2025
- **Period start → end:** 2025-07-01 → 2025-07-31
- **Entity:** Silverline Distribution
- **Currency (display / functional):** USD / USD
- **Tax regime:** `vat`
- **Document count:** 21
- **Labeled as inconsistent:** True
- **Inconsistency codes:** asset_disposal_mismatch
- **Inconsistency reasons:** Fixed asset disposal support does not reconcile cost, accumulated depreciation, NBV, proceeds, and gain or loss.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-07-01_

**Assets**
- Cash: 22,258.17
- Accounts Receivable: 2,506.47
- Prepaid Rent: 2,956.79
- Office Supplies: 594.99
- Equipment: 6,486.22

**Liabilities**
- Accounts Payable: 1,679.64
- Accrued Expenses: 2,003.27
- Loans Payable: 5,383.26

**Equity**
- Retained Earnings: 4,158.80
- Owner's Equity: 21,577.67


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-07-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-07-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $22,258.17
  - Section assets | Account Accounts Receivable | Amount $2,506.47
  - Section assets | Account Prepaid Rent | Amount $2,956.79
  - Section assets | Account Office Supplies | Amount $594.99
  - Section assets | Account Equipment | Amount $6,486.22
  - Section liabilities | Account Accounts Payable | Amount $1,679.64
  - Section liabilities | Account Accrued Expenses | Amount $2,003.27
  - Section liabilities | Account Loans Payable | Amount $5,383.26
  - Section equity | Account Retained Earnings | Amount $4,158.80
  - Section equity | Account Owner's Equity | Amount $21,577.67

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-07-02

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Beacon Industrial Supply
Property: Cedar Plaza
Service Start: 2025-07-02
Service End: 2025-10-01
Total: $2,593.71
Monthly Amount: $864.57

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-07

```
CUSTOMER INVOICE
================

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-07

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: July 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-07-24

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-07-24
Subtotal: $2,941.24
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $588.25
Total: $3,529.49

Line Items
----------
Items:
  - Description Implementation work | Amount $938.29
  - Description Follow-up support | Amount $2,002.95

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D016 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2025-07-07

```
LEASE AGREEMENT
===============

From
----
Silverline Distribution
14 King Street, Pune
Document Date: 2025-07-07

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D016
Document Type: lease_agreement
Period: July 2025

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Prime Utility Desk
Commencement Date: 2025-07-07
Term Months: 36
Monthly Payment Amount: $2,500.05
Incremental Borrowing Rate: 0.09
ROU Asset Amount: $78,618.59
Lease Liability Amount: $78,618.59

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-08

```
VENDOR INVOICE
==============

From
----
Silverline Distribution
14 King Street, Pune
Document Date: 2025-07-08

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: July 2025

Terms
-----
Due Date: 2025-07-24

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-07-24
Subtotal: $4,058.78
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $811.76
Total: $4,870.54

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $920.08
  - Description Support fee | Amount $3,138.70

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-07-10

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Vertex Supply Co.
Total: $2.72
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $0.58
  - Description Travel Incidentals | Amount $2.14
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-16

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Pace Office Mart
Asset Name: Delivery van
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $32,897.34
Paid Cash: $13,930.25
Financed Amount: $18,967.09
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-07-20

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $3,967.45
Draw Amount: $16,842.05
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $20,809.50
Note: Scheduled lender activity for the selected period.
```

### Document D014 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-07-21

```
ASSET DISPOSAL NOTICE
=====================

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-21

Reference Box
-------------
Document ID: D014
Document Type: asset_disposal_notice
Period: July 2025

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Original Cost: $6,486.22
Accumulated Depreciation: 135.13
Net Book Value: $4,175.74
Proceeds Amount: $7,494.29
Gain Loss Amount: $1,143.20
Gain Loss Type: Gain

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D015 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2025-07-21

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-21

To
--
Aster Point Services

Reference Box
-------------
Document ID: D015
Document Type: sale_proceeds_advice
Period: July 2025

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Aster Point Services
Asset Tag: OPEN-EQU
Proceeds Amount: $7,494.29
Settlement Date: 2025-07-21
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-07-22

```
PAYMENT ADVICE
==============

From
----
Silverline Distribution
14 King Street, Pune
Document Date: 2025-07-22

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: July 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Maple Ridge Trading
Amount: $2,947.43
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-07-23

```
PAYMENT ADVICE
==============

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-23

To
--
Oakline Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: July 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: $2,911.39
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D018 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2025-07-24

```
LEASE PAYMENT NOTICE / REFERENCE COPY
=====================================

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-24

Reference Box
-------------
Document ID: D018
Document Type: lease_payment_notice
Period: July 2025

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 2025-07-24
Payment Amount: $2,500.05
Interest Amount: $589.64
Principal Amount: $1,910.41

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-07-25

```
UTILITY INVOICE
===============

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-25

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: July 2025

Terms
-----
Due Date: 2025-08-09

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: July 2025
Due Date: 2025-08-09
Total: $420.05

Charges
-------
Charges:
  - Description Electricity | Amount $133.85
  - Description Water | Amount $286.20

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-07-28

```
PAYROLL SUMMARY
===============

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-28

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: July 2025
Headcount: 8
Gross Pay: $11,119.50
Employer Tax: 1,271.93
Cash Outflow: $12,391.43

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D019 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-07-28

```
TRANSFER ADVICE
===============

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-28

Reference Box
-------------
Document ID: D019
Document Type: transfer_advice
Period: July 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $49,830.08
Transfer Date: 2025-07-28
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-07-31

```
SERVICE PERIOD MEMO
===================

From
----
Silverline Distribution
14 King Street, Pune
Document Date: 2025-07-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: July 2025
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $864.57

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-07-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $6,486.22
Useful Life Months: 48
Current Period Charge: $135.13
Accumulated Depreciation: 135.13
```

### Document D017 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-07-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-31

Reference Box
-------------
Document ID: D017
Document Type: lease_amortization_schedule
Period: July 2025

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: $78,618.59
Payment Amount: $2,500.05
Interest Amount: $589.64
Principal Amount: $1,910.41
Ending Liability Balance: $76,708.18
ROU Amortization Amount: $2,183.85

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-07-31

```
BANK STATEMENT
==============

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-31

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: July 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $22,258.17
Closing Balance: $-34,617.69

Statement Rows
--------------
Rows:
  - Date 2025-07-02 | Description Rent prepayment PRE-0001 | Amount $-2,593.71 | Running 
Balance $19,664.46
  - Date 2025-07-10 | Description Vertex Supply Co. receipt RCPT-0001 | Amount $-2.72 | 
Running Balance $19,661.74
  - Date 2025-07-16 | Description Asset purchase ASSET-0001 | Amount $-13,930.25 | Running 
Balance $5,731.49
  - Date 2025-07-20 | Description Loan draw LOAN-0001 | Amount $16,842.05 | Running Balance 
$22,573.54
  - Date 2025-07-21 | Description Asset sale OPEN-EQU | Amount $7,494.29 | Running Balance 
$30,067.83
  - Date 2025-07-22 | Description Customer settlement INV-0001 | Amount $2,947.43 | Running 
Balance $33,015.26
  - Date 2025-07-23 | Description Supplier settlement BILL-0001 | Amount $-2,911.39 | 
Running Balance $30,103.87
  - Date 2025-07-24 | Description Lease payment LEASE-0001 | Amount $-2,500.05 | Running 
Balance $27,603.82
  - Date 2025-07-28 | Description Payroll PAYRUN-0001 | Amount $-12,391.43 | Running Balance
 $15,212.39
  - Date 2025-07-28 | Description Transfer out TRX-0001 | Amount $-49,830.08 | Running 
Balance $-34,617.69

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-07-31

```
BANK STATEMENT
==============

From
----
Silverline Distribution
14 King Street, Pune
Date: 2025-07-31

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: July 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $49,830.08

Statement Rows
--------------
Rows:
  - Date 2025-07-28 | Description Transfer in TRX-0001 | Amount $49,830.08 | Running Balance
 $49,830.08

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D021
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
Is the labeled contradiction (codes: `asset_disposal_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
