# Verification Packet — COV_PRO_M4_0003

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** August 2025
- **Period start → end:** 2025-08-01 → 2025-08-31
- **Entity:** Cedar Builders
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 21
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-08-01_

**Assets**
- Cash: 19,736.01
- Accounts Receivable: 3,219.25
- Prepaid Rent: 1,615.39
- Office Supplies: 346.48
- Equipment: 4,956.06

**Liabilities**
- Accounts Payable: 2,889.81
- Accrued Expenses: 1,841.73
- Loans Payable: 2,389.75

**Equity**
- Retained Earnings: 8,363.97
- Owner's Equity: 14,387.93


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-08-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-08-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $19,736.01
  - Section assets | Account Accounts Receivable | Amount $3,219.25
  - Section assets | Account Prepaid Rent | Amount $1,615.39
  - Section assets | Account Office Supplies | Amount $346.48
  - Section assets | Account Equipment | Amount $4,956.06
  - Section liabilities | Account Accounts Payable | Amount $2,889.81
  - Section liabilities | Account Accrued Expenses | Amount $1,841.73
  - Section liabilities | Account Loans Payable | Amount $2,389.75
  - Section equity | Account Retained Earnings | Amount $8,363.97
  - Section equity | Account Owner's Equity | Amount $14,387.93

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2025-08-02

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Pace Office Mart
Property: Marina Heights
Service Start: 2025-08-02
Service End: 2025-11-01
Total: $4,821.85
Monthly Amount: $1,607.28

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D016 — Lease Agreement

- **Type:** `lease_agreement`
- **Role:** `posting_doc`
- **Date:** 2025-08-06

```
LEASE AGREEMENT / REFERENCE COPY
================================

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-06

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D016
Document Type: lease_agreement
Period: August 2025

Lease Terms
-----------
Agreement Number: LEASE-0001
Lessor: Vertex Supply Co.
Commencement Date: 2025-08-06
Term Months: 36
Monthly Payment Amount: $3,405.70
Incremental Borrowing Rate: 0.06
ROU Asset Amount: $111,948.82
Lease Liability Amount: $111,948.82

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-07

```
CUSTOMER INVOICE
================

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-07

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: August 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-08-22

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-08-22
Subtotal: $8,695.66
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $434.78
Total: $9,130.44

Line Items
----------
Items:
  - Description Monthly retainer | Amount $2,633.47
  - Description Follow-up support | Amount $6,062.19

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-07

```
VENDOR INVOICE
==============

From
----
Cedar Builders
18 Marina Avenue, Chennai
Date: 2025-08-07

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: August 2025

Terms
-----
Due Date: 2025-08-27

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-08-27
Subtotal: $3,167.30
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $316.73
Total: $3,484.03

Bill Lines
----------
Lines:
  - Description Support package | Amount $1,156.63
  - Description Support fee | Amount $2,010.67

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-08-18

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $8,530.97
Draw Amount: $37,012.36
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $45,543.33
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-18

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Prime Utility Desk
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 48
Total: $36,757.18
Paid Cash: $13,091.62
Financed Amount: $23,665.56
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-08-21

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: $232.21
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $75.04
  - Description Travel Incidentals | Amount $157.17
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-21

```
PAYMENT ADVICE
==============

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-21

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: August 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: $2,898.21
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D018 — Lease Payment Notice

- **Type:** `lease_payment_notice`
- **Role:** `support_doc`
- **Date:** 2025-08-21

```
LEASE PAYMENT NOTICE
====================

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-21

Reference Box
-------------
Document ID: D018
Document Type: lease_payment_notice
Period: August 2025

Payment
-------
Notice Number: LEASEPAY-0001
Agreement Number: LEASE-0001
Payment Date: 2025-08-21
Payment Amount: $3,405.70
Interest Amount: $559.74
Principal Amount: $2,845.96

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D014 — Asset Disposal Notice

- **Type:** `asset_disposal_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-08-23

```
ASSET DISPOSAL NOTICE
=====================

From
----
Cedar Builders
18 Marina Avenue, Chennai
Date: 2025-08-23

Reference Box
-------------
Document ID: D014
Document Type: asset_disposal_notice
Period: August 2025

Disposal Computation
--------------------
Notice Number: DISP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Original Cost: $4,956.06
Accumulated Depreciation: 103.25
Net Book Value: $4,852.81
Proceeds Amount: $3,979.30
Gain Loss Amount: $873.51
Gain Loss Type: Loss

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D015 — Sale Proceeds Advice

- **Type:** `sale_proceeds_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-23

```
SALE PROCEEDS ADVICE / REFERENCE COPY
=====================================

From
----
Cedar Builders
18 Marina Avenue, Chennai
Date: 2025-08-23

To
--
Aster Point Services

Reference Box
-------------
Document ID: D015
Document Type: sale_proceeds_advice
Period: August 2025

Proceeds
--------
Advice Number: DSPPAY-0001
Buyer: Aster Point Services
Asset Tag: OPEN-EQU
Proceeds Amount: $3,979.30
Settlement Date: 2025-08-23
Payment Reference: BNK-0001

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-08-25

```
PAYROLL SUMMARY
===============

From
----
Cedar Builders
18 Marina Avenue, Chennai
Date: 2025-08-25

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: August 2025
Headcount: 6
Gross Pay: $9,004.17
Employer Tax: 1,057.11
Cash Outflow: $10,061.28

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-26

```
PAYMENT ADVICE
==============

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-26

To
--
Crescent Labs

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: August 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: $8,767.91
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D019 — Transfer Advice

- **Type:** `transfer_advice`
- **Role:** `support_doc`
- **Date:** 2025-08-26

```
TRANSFER ADVICE
===============

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-26

Reference Box
-------------
Document ID: D019
Document Type: transfer_advice
Period: August 2025
Reference: TRX-0001

Transfer Details
----------------
Transfer Number: TRF-0001
From Account: Cash
To Account: Reserve Cash
Amount: $35,363.07
Transfer Date: 2025-08-26
Reference: TRX-0001

Notes
-----
Treasury desk transfer between company-controlled bank accounts.

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D010 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-08-28

```
UTILITY INVOICE
===============

From
----
Cedar Builders
18 Marina Avenue, Chennai
Date: 2025-08-28

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: utilities_statement
Period: August 2025

Terms
-----
Due Date: 2025-09-10

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: August 2025
Due Date: 2025-09-10
Total: $350.27

Charges
-------
Charges:
  - Description Electricity | Amount $75.47
  - Description Water | Amount $274.80

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-08-31

```
SERVICE PERIOD MEMO
===================

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: August 2025
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: $1,607.28

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
- **Date:** 2025-08-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $4,956.06
Useful Life Months: 48
Current Period Charge: $103.25
Accumulated Depreciation: 103.25
```

### Document D017 — Lease Amortization Schedule

- **Type:** `lease_amortization_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-08-31

```
LEASE AMORTIZATION SCHEDULE
===========================

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-31

Reference Box
-------------
Document ID: D017
Document Type: lease_amortization_schedule
Period: August 2025

Lease Schedule
--------------
Schedule ID: LEASESCH-0001
Agreement Number: LEASE-0001
Opening Liability Balance: $111,948.82
Payment Amount: $3,405.70
Interest Amount: $559.74
Principal Amount: $2,845.96
Ending Liability Balance: $109,102.86
ROU Amortization Amount: $3,109.69

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-08-31

```
BANK STATEMENT
==============

From
----
Cedar Builders
18 Marina Avenue, Chennai
Document Date: 2025-08-31

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: August 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0003
Statement Currency: USD
Opening Balance: $19,736.01
Closing Balance: $-378.36

Statement Rows
--------------
Rows:
  - Date 2025-08-02 | Description Rent prepayment PRE-0001 | Amount $-4,821.85 | Running 
Balance $14,914.16
  - Date 2025-08-18 | Description Asset purchase ASSET-0001 | Amount $-13,091.62 | Running 
Balance $1,822.54
  - Date 2025-08-18 | Description Loan draw LOAN-0001 | Amount $37,012.36 | Running Balance 
$38,834.90
  - Date 2025-08-21 | Description Lease payment LEASE-0001 | Amount $-3,405.70 | Running 
Balance $35,429.20
  - Date 2025-08-21 | Description Meridian Support LLP receipt RCPT-0001 | Amount $-232.21 |
 Running Balance $35,196.99
  - Date 2025-08-21 | Description Supplier settlement BILL-0001 | Amount $-2,898.21 | 
Running Balance $32,298.78
  - Date 2025-08-23 | Description Asset sale OPEN-EQU | Amount $3,979.30 | Running Balance 
$36,278.08
  - Date 2025-08-25 | Description Payroll PAYRUN-0001 | Amount $-10,061.28 | Running Balance
 $26,216.80
  - Date 2025-08-26 | Description Customer settlement INV-0001 | Amount $8,767.91 | Running 
Balance $34,984.71
  - Date 2025-08-26 | Description Transfer out TRX-0001 | Amount $-35,363.07 | Running 
Balance $-378.36

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-08-31

```
BANK STATEMENT
==============

From
----
Cedar Builders
18 Marina Avenue, Chennai
Date: 2025-08-31

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: August 2025

Account Summary
---------------
Account Name: Reserve Account
Account Number: 1002-0399
Statement Currency: USD
Opening Balance: $0.00
Closing Balance: $35,363.07

Statement Rows
--------------
Rows:
  - Date 2025-08-26 | Description Transfer in TRX-0001 | Amount $35,363.07 | Running Balance
 $35,363.07

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D021
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 8,695.66 | D002 | 2025-08-07 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 434.78 | D002 | 2025-08-07 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 3,167.30 | D003 | 2025-08-07 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 316.73 | D003 | 2025-08-07 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 232.21 | D004 | 2025-08-21 | expense_receipt |
| 6 | Cash | Accounts Receivable | 8,767.91 | D005, D002 | 2025-08-26 | customer_payment |
| 7 | Accounts Payable | Cash | 2,898.21 | D006, D003 | 2025-08-21 | supplier_payment |
| 8 | Salaries Expense | Cash | 9,004.17 | D007 | 2025-08-25 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 1,057.11 | D007 | 2025-08-25 | payroll_tax |
| 10 | Prepaid Rent | Cash | 4,821.85 | D008 | 2025-08-02 | prepaid_rent_purchase |
| 11 | Rent Expense | Prepaid Rent | 1,607.28 | D008, D009 | 2025-08-31 | prepaid_rent_release |
| 12 | Utilities Expense | Accounts Payable | 350.27 | D010 | 2025-08-28 | utilities_bill |
| 13 | Cash | Loans Payable | 37,012.36 | D011 | 2025-08-18 | loan_draw |
| 14 | Equipment | Cash | 13,091.62 | D012 | 2025-08-18 | equipment_purchase_cash |
| 15 | Equipment | Notes Payable | 23,665.56 | D012 | 2025-08-18 | equipment_purchase_financed |
| 16 | Depreciation Expense | Accumulated Depreciation | 103.25 | D013 | 2025-08-31 | depreciation |
| 17 | Cash | Equipment | 3,979.30 | D014, D015 | 2025-08-23 | asset_disposal_proceeds |
| 18 | Accumulated Depreciation | Equipment | 103.25 | D014, D015 | 2025-08-23 | asset_disposal_remove_accumulated_depreciation |
| 19 | Loss on Disposal | Equipment | 873.51 | D014, D015 | 2025-08-23 | asset_disposal_loss |
| 20 | Right-of-Use Asset | Lease Liability | 111,948.82 | D016 | 2025-08-06 | baseline_lease_initial_recognition |
| 21 | Lease Liability | Cash | 2,845.96 | D016, D017, D018 | 2025-08-21 | baseline_lease_principal |
| 22 | Lease Interest Expense | Cash | 559.74 | D016, D017, D018 | 2025-08-21 | baseline_lease_interest |
| 23 | Lease Amortization Expense | Right-of-Use Asset | 3,109.69 | D016, D017 | 2025-08-31 | baseline_lease_amortization |
| 24 | Reserve Cash | Cash | 35,363.07 | D019 | 2025-08-26 | interbank_transfer |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: -378.36
- Accounts Receivable: 3,581.78
- Prepaid Rent: 4,829.96
- Office Supplies: 346.48
- Equipment: 36,757.18
- Input Tax Receivable: 316.73
- Right-of-Use Asset: 108,839.13
- Reserve Cash: 35,363.07

**Liabilities**
- Accounts Payable: 3,825.90
- Accrued Expenses: 1,841.73
- Loans Payable: 39,402.11
- Sales Tax Payable: 434.78
- Notes Payable: 23,665.56
- Lease Liability: 109,102.86

**Equity**
- Retained Earnings: -3,004.90
- Owner's Equity: 14,387.93

**Totals:** Assets = 189,655.97; Liabilities = 178,272.94; Equity = 11,383.03
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
- Notes:

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

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Support ties to postings. Acceptable.
