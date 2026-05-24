# Verification Packet — COV_NEG_00_LEASE_SCHEDULE_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** November 2024
- **Period start → end:** 2024-11-01 → 2024-11-30
- **Entity:** Harbor Advisors
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 21
- **Labeled as inconsistent:** True
- **Inconsistency codes:** lease_schedule_mismatch
- **Inconsistency reasons:** Lease amortization schedule does not reconcile payment, interest, principal, and ending liability.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-11-01_

**Assets**
- Cash: 40,845.31
- Accounts Receivable: 3,279.75
- Prepaid Rent: 1,446.79
- Office Supplies: 602.86
- Equipment: 4,490.12

**Liabilities**
- Accounts Payable: 2,337.43
- Accrued Expenses: 2,025.91
- Loans Payable: 2,504.76

**Equity**
- Retained Earnings: 7,304.74
- Owner's Equity: 36,491.99


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-11-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/11/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 40,845.31
  - Section assets | Account Accounts Receivable | Amount GBP 3,279.75
  - Section assets | Account Prepaid Rent | Amount GBP 1,446.79
  - Section assets | Account Office Supplies | Amount GBP 602.86
  - Section assets | Account Equipment | Amount GBP 4,490.12
  - Section liabilities | Account Accounts Payable | Amount GBP 2,337.43
  - Section liabilities | Account Accrued Expenses | Amount GBP 2,025.91
  - Section liabilities | Account Loans Payable | Amount GBP 2,504.76
  - Section equity | Account Retained Earnings | Amount GBP 7,304.74
  - Section equity | Account Owner's Equity | Amount GBP 36,491.99

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2024-11-03

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Beacon Industrial Supply
Property: Park Lane Residences
Service Start: 03/11/2024
Service End: 02/02/2025
Total: GBP 6,427.19
Monthly Amount: GBP 2,142.40

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D016 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2024-11-04

```
LEASE AGREEMENT
===============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Document Date: 04/11/2024

To
--
Meridian Support LLP

Reference Box
-------------
Document ID: D016
Document Type: lease_agreement
Period: November 2024

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Meridian Support LLP
Commencement Date: 04/11/2024
Term Months: 24
Monthly Payment Amount: GBP 2,775.88
Incremental Borrowing Rate: 0.09
ROU Asset Amount: GBP 60,761.64
Lease Liability Amount: GBP 60,761.64

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-05

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 05/11/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: November 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 29/11/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 29/11/2024
Subtotal: GBP 2,849.30
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 284.93
Total: GBP 3,134.23

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 1,119.11
  - Description Follow-up support | Amount GBP 1,730.19

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-08

```
VENDOR INVOICE
==============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 08/11/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: November 2024

Terms
-----
Due Date: 22/11/2024

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 22/11/2024
Subtotal: GBP 5,557.95
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: GBP 694.74
Total: GBP 6,252.69

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount GBP 1,459.39
  - Description Support fee | Amount GBP 4,098.56

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-12

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Prime Utility Desk
Asset Name: Server rack
Asset Tag: TAG-0001
Useful Life Months: 24
Total: GBP 35,871.39
Paid Cash: GBP 16,628.82
Financed Amount: GBP 19,242.57
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-11-15

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: GBP 306.50
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount GBP 112.85
  - Description Travel Incidentals | Amount GBP 193.65
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-18

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 4,728.25
Draw Amount: GBP 30,392.49
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 35,120.74
Note: Scheduled lender activity for the selected period.
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-20

```
PAYMENT ADVICE
==============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 20/11/2024

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: November 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: GBP 2,914.31
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D018 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2024-11-20

```
LEASE PAYMENT NOTICE
====================

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Document Date: 20/11/2024

Reference Box
-------------
Document ID: D018
Document Type: lease_payment_notice
Period: November 2024

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 20/11/2024
Payment Amount: GBP 2,775.88
Interest Amount: GBP 455.71
Principal Amount: GBP 2,320.17

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-11-21

```
PAYROLL SUMMARY
===============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 21/11/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: November 2024
Headcount: 5
Gross Pay: GBP 12,202.94
Employer Tax: 1,045.69
Cash Outflow: GBP 13,248.63

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-21

```
UTILITY INVOICE
===============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Document Date: 21/11/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: November 2024

Terms
-----
Due Date: 29/11/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: November 2024
Due Date: 29/11/2024
Total: GBP 376.62

Charges
-------
Charges:
  - Description Electricity | Amount GBP 129.60
  - Description Water | Amount GBP 247.02

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D014 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2024-11-21

```
ASSET DISPOSAL NOTICE
=====================

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 21/11/2024

Reference Box
-------------
Document ID: D014
Document Type: asset_disposal_notice
Period: November 2024

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Server rack
Asset Tag: TAG-0001
Original Cost: GBP 35,871.39
Accumulated Depreciation: 1,494.64
Net Book Value: GBP 34,376.75
Proceeds Amount: GBP 40,564.56
Gain Loss Amount: GBP 6,187.81
Gain Loss Type: Gain

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D015 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-21

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 21/11/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D015
Document Type: sale_proceeds_advice
Period: November 2024

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Riverfront Group
Asset Tag: TAG-0001
Proceeds Amount: GBP 40,564.56
Settlement Date: 21/11/2024
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-26

```
PAYMENT ADVICE
==============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 26/11/2024

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: November 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: GBP 5,135.72
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D019 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-27

```
TRANSFER ADVICE
===============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 27/11/2024

Reference Box
-------------
Document ID: D019
Document Type: transfer_advice
Period: November 2024
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: GBP 35,219.66
Transfer Date: 27/11/2024
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
- **Date:** 2024-11-30

```
SERVICE PERIOD MEMO
===================

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 30/11/2024

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: November 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: GBP 2,142.40

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D013 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-11-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Server rack
Asset Tag: TAG-0001
Cost: GBP 35,871.39
Useful Life Months: 24
Current Period Charge: GBP 1,494.64
Accumulated Depreciation: 1,494.64
```

### Document D017 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-11-30

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 30/11/2024

Reference Box
-------------
Document ID: D017
Document Type: lease_amortization_schedule
Period: November 2024

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: GBP 60,761.64
Payment Amount: GBP 2,775.88
Interest Amount: GBP 455.71
Principal Amount: GBP 2,320.17
Ending Liability Balance: GBP 55,753.54
ROU Amortization Amount: GBP 2,531.74

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-11-30

```
BANK STATEMENT
==============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 30/11/2024

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: November 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: GBP
Opening Balance: GBP 40,845.31
Closing Balance: GBP 34,974.27

Statement Rows
--------------
Rows:
  - Date 03/11/2024 | Description Rent prepayment PRE-0001 | Amount GBP -6,427.19 | Running 
Balance GBP 34,418.12
  - Date 12/11/2024 | Description Asset purchase ASSET-0001 | Amount GBP -16,628.82 | 
Running Balance GBP 17,789.30
  - Date 15/11/2024 | Description Meridian Support LLP receipt RCPT-0001 | Amount GBP 
-306.50 | Running Balance GBP 17,482.80
  - Date 18/11/2024 | Description Loan draw LOAN-0001 | Amount GBP 30,392.49 | Running 
Balance GBP 47,875.29
  - Date 20/11/2024 | Description Customer settlement INV-0001 | Amount GBP 2,914.31 | 
Running Balance GBP 50,789.60
  - Date 20/11/2024 | Description Lease payment LEASE-0001 | Amount GBP -2,775.88 | Running 
Balance GBP 48,013.72
  - Date 21/11/2024 | Description Asset sale TAG-0001 | Amount GBP 40,564.56 | Running 
Balance GBP 88,578.28
  - Date 21/11/2024 | Description Payroll PAYRUN-0001 | Amount GBP -13,248.63 | Running 
Balance GBP 75,329.65
  - Date 26/11/2024 | Description Supplier settlement BILL-0001 | Amount GBP -5,135.72 | 
Running Balance GBP 70,193.93
  - Date 27/11/2024 | Description Transfer out TRX-0001 | Amount GBP -35,219.66 | Running 
Balance GBP 34,974.27

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
- **Date:** 2024-11-30

```
BANK STATEMENT
==============

From
----
Harbor Advisors
18 Marina Avenue, Chennai
Date: 30/11/2024

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: November 2024

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-CH99
Statement Currency: GBP
Opening Balance: GBP 0.00
Closing Balance: GBP 35,219.66

Statement Rows
--------------
Rows:
  - Date 27/11/2024 | Description Transfer in TRX-0001 | Amount GBP 35,219.66 | Running 
Balance GBP 35,219.66

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
- [x] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [x] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:  Missing from section 5: DR Office Supplies Expense / CR Accounts Payable 6252.69

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
Is the labeled contradiction (codes: `lease_schedule_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes:

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
