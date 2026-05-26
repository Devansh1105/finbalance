# Verification Packet — COV_PRO_Y4_0088

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `property_management`
- **Difficulty level (1–5):** 4
- **Period type:** year
- **Period label:** FY 2025-26
- **Period start → end:** 2025-04-01 → 2026-03-31
- **Entity:** Willow Manufacturing
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 24
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Security Deposits Payable`, `Owner's Equity`, `Retained Earnings`, `Rental Revenue`, `Maintenance Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-04-01_

**Assets**
- Cash: 186,003.43
- Accounts Receivable: 19,587.39
- Prepaid Insurance: 14,252.55
- Equipment: 30,861.52

**Liabilities**
- Accounts Payable: 20,232.61
- Accrued Expenses: 2,583.22
- Security Deposits Payable: 21,185.07
- Loans Payable: 24,152.95

**Equity**
- Retained Earnings: 27,479.93
- Owner's Equity: 155,071.11


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
Statement Date: 01/04/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 186.003,43
  - Section assets | Account Accounts Receivable | Amount EUR 19.587,39
  - Section assets | Account Prepaid Insurance | Amount EUR 14.252,55
  - Section assets | Account Equipment | Amount EUR 30.861,52
  - Section liabilities | Account Accounts Payable | Amount EUR 20.232,61
  - Section liabilities | Account Accrued Expenses | Amount EUR 2.583,22
  - Section liabilities | Account Security Deposits Payable | Amount EUR 21.185,07
  - Section liabilities | Account Loans Payable | Amount EUR 24.152,95
  - Section equity | Account Retained Earnings | Amount EUR 27.479,93
  - Section equity | Account Owner's Equity | Amount EUR 155.071,11

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D019 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-03

```
RENT ROLL
=========

From
----
Willow Manufacturing
14 King Street, Pune
Date: 03/04/2025

Reference Box
-------------
Document ID: D019
Document Type: rent_roll
Period: FY 2025-26

Rent Roll Summary
-----------------
Roll Number: ROLL-0003
Property: Harbor View Offices
Period: FY 2025-26
Total Rent: EUR 36.962,24

Tenant Rows
-----------
Rows:
  - Unit B-202 | Tenant Unit B - Romero | Amount EUR 36.962,24

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D021 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-06

```
RENT ROLL
=========

From
----
Willow Manufacturing
14 King Street, Pune
Date: 06/04/2025

Reference Box
-------------
Document ID: D021
Document Type: rent_roll
Period: FY 2025-26

Rent Roll Summary
-----------------
Roll Number: ROLL-0004
Property: Cedar Plaza
Period: FY 2025-26
Total Rent: EUR 32.426,70

Tenant Rows
-----------
Rows:
  - Unit B-202 | Tenant Unit A - Ellis | Amount EUR 32.426,70

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D015 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-09

```
RENT ROLL
=========

From
----
Willow Manufacturing
14 King Street, Pune
Date: 09/04/2025

Reference Box
-------------
Document ID: D015
Document Type: rent_roll
Period: FY 2025-26

Rent Roll Summary
-----------------
Roll Number: ROLL-0002
Property: Marina Heights
Period: FY 2025-26
Total Rent: EUR 28.094,69

Tenant Rows
-----------
Rows:
  - Unit C-303 | Tenant Unit A - Ellis | Amount EUR 28.094,69

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D002 — Rent Roll

- **Type:** `rent_roll`
- **Role:** `posting_doc`
- **Date:** 2025-04-18

```
RENT ROLL
=========

From
----
Willow Manufacturing
14 King Street, Pune
Document Date: 18/04/2025

Reference Box
-------------
Document ID: D002
Document Type: rent_roll
Period: FY 2025-26

Rent Roll Summary
-----------------
Roll Number: ROLL-0001
Property: Park Lane Residences
Period: FY 2025-26
Total Rent: EUR 31.965,58

Tenant Rows
-----------
Rows:
  - Unit B-202 | Tenant Unit B - Romero | Amount EUR 31.965,58

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D009 — Insurance Notice

- **Type:** `insurance_notice`
- **Role:** `posting_doc`
- **Date:** 2025-04-25

```
INSURANCE NOTICE
================

From
----
Willow Manufacturing
14 King Street, Pune
Document Date: 25/04/2025

To
--
Beacon General
Vendor remittance address on file

Terms
-----
Service Start: 25/04/2025
Service End: 24/07/2025

Coverage Notice
---------------
Notice Number: PRE-0001
Carrier: Beacon General
Covered Item: Marina Heights
Coverage Start: 25/04/2025
Coverage End: 24/07/2025
Total Premium: EUR 41.919,93
Monthly Amount: EUR 13.973,31

Notes
-----
Insurance coverage paid in advance and tracked for later release.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-03

```
VENDOR INVOICE
==============

From
----
Willow Manufacturing
14 King Street, Pune
Document Date: 03/05/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 19/05/2025

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 19/05/2025
Total: EUR 44.911,65

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 18.101,34
  - Description Support fee | Amount EUR 26.810,31

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D006 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-05-08

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Willow Manufacturing
14 King Street, Pune
Document Date: 08/05/2025

To
--
Unit C - Shah

Reference Box
-------------
Document ID: D006
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0001
Tenant: Unit C - Shah
Unit: D-404
Amount: EUR 11.475,63
Due Date: 17/05/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D018 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-05-10

```
VENDOR INVOICE
==============

From
----
Willow Manufacturing
14 King Street, Pune
Date: 10/05/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D018
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 30/05/2025

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 30/05/2025
Total: EUR 18.139,08

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount EUR 7.631,06
  - Description Support fee | Amount EUR 10.508,02

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D020 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-05-25

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Willow Manufacturing
14 King Street, Pune
Date: 25/05/2025

To
--
Unit D - Khan

Reference Box
-------------
Document ID: D020
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0004
Tenant: Unit D - Khan
Unit: C-303
Amount: EUR 11.296,10
Due Date: 01/06/2025

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D017 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `posting_doc`
- **Date:** 2025-06-03

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Willow Manufacturing
14 King Street, Pune
Date: 03/06/2025

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D017
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEP-0003
Tenant: Unit B - Romero
Unit: A-101
Amount: EUR 26.228,93
Due Date: 12/06/2025

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D016 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-06-04

```
VENDOR INVOICE
==============

From
----
Willow Manufacturing
14 King Street, Pune
Date: 04/06/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: vendor_invoice
Period: FY 2025-26

Terms
-----
Due Date: 16/06/2025

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Maintenance Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 16/06/2025
Total: EUR 47.517,39

Bill Lines
----------
Lines:
  - Description Support package | Amount EUR 12.105,36
  - Description Support fee | Amount EUR 35.412,03

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D011 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-08-31

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: EUR 58.875,56
Draw Amount: EUR 88.335,79
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 147.211,35
Note: Scheduled lender activity for the selected period.
```

### Document D012 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-24

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Pace Office Mart
Asset Name: CNC router
Asset Tag: TAG-0001
Useful Life Months: 48
Total: EUR 221.135,64
Paid Cash: EUR 47.737,12
Financed Amount: EUR 173.398,52
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D014 — Security Deposit Notice

- **Type:** `security_deposit_notice`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-15

```
SECURITY DEPOSIT NOTICE
=======================

From
----
Willow Manufacturing
14 King Street, Pune
Document Date: 15/12/2025

To
--
Unit C - Shah

Reference Box
-------------
Document ID: D014
Document Type: security_deposit_notice
Period: FY 2025-26

Security Deposit
----------------
Notice Number: DEPREF-0001
Tenant: Unit C - Shah
Unit: A-101
Amount: EUR 9.630,19
Due Date: 15/12/2025

Notes
-----
Refund of previously collected security deposit DEP-0001.

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2026-01-07

```
PAYROLL SUMMARY
===============

From
----
Willow Manufacturing
14 King Street, Pune
Document Date: 07/01/2026

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025-26
Headcount: 9
Gross Pay: EUR 40.951,50
Employer Tax: 4.350,20
Cash Outflow: EUR 45.301,70

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D004 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-01-25

```
PAYMENT ADVICE
==============

From
----
Willow Manufacturing
14 King Street, Pune
Date: 25/01/2026

To
--
Unit B - Romero

Reference Box
-------------
Document ID: D004
Document Type: payment_advice
Period: FY 2025-26
Reference: ROLL-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Unit B - Romero
Amount: EUR 23.865,28
Reference: ROLL-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2026-02-08

```
PAYMENT ADVICE
==============

From
----
Willow Manufacturing
14 King Street, Pune
Document Date: 08/02/2026

To
--
Oakline Services

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: EUR 32.086,46
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D008 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2026-02-22

```
UTILITY INVOICE
===============

From
----
Willow Manufacturing
14 King Street, Pune
Date: 22/02/2026

To
--
City Power
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: utilities_statement
Period: FY 2025-26

Terms
-----
Due Date: 03/03/2026

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: City Power
Pay To: City Power
Service Period: FY 2025-26
Due Date: 03/03/2026
Total: EUR 3.690,78

Charges
-------
Charges:
  - Description Electricity | Amount EUR 1.201,91
  - Description Water | Amount EUR 2.488,87

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D010 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Willow Manufacturing
14 King Street, Pune
Date: 31/03/2026

Reference Box
-------------
Document ID: D010
Document Type: service_period_memo
Period: FY 2025-26
Reference: PRE-0001

Approval / Context
------------------
Subject: Insurance coverage release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Insurance coverage release
Reference: PRE-0001
Recognized Amount: EUR 13.973,31

Explanation
-----------
Narrative: One month of insurance coverage has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D013 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2026-03-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Willow Manufacturing
14 King Street, Pune
Date: 31/03/2026

Reference Box
-------------
Document ID: D013
Document Type: fixed_asset_rollforward
Period: FY 2025-26

Asset Rollforward
-----------------
Schedule ID: DEP-0002
Asset Name: CNC router
Asset Tag: TAG-0001
Cost: EUR 221.135,64
Useful Life: 48
Current Charge: EUR 55.283,88
Accumulated Depreciation: 55.283,88
Opening Balance: EUR 221.135,64
Additions: 0,00
Disposals: 0,00
Ending Balance: EUR 221.135,64

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D022 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
MEMO
====

From
----
Willow Manufacturing
14 King Street, Pune
Document Date: 31/03/2026

Reference Box
-------------
Document ID: D022
Document Type: memo
Period: FY 2025-26

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
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D022
```

### Document D023 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2026-03-31

```
VENDOR STATEMENT
================

From
----
Willow Manufacturing
14 King Street, Pune
Date: 31/03/2026

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D023
Document Type: vendor_statement
Period: FY 2025-26

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Pace Office Mart
Closing Balance: EUR 47.517,39

Statement Lines
---------------
Lines:
  - Reference BILL-0002 | Document Type Open invoice | Amount EUR 47.517,39 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D023
```

### Document D024 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2026-03-31

```
BANK STATEMENT
==============

From
----
Willow Manufacturing
14 King Street, Pune
Date: 31/03/2026

Reference Box
-------------
Document ID: D024
Document Type: bank_statement
Period: FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0088
Statement Currency: EUR
Opening Balance: EUR 186.003,43
Closing Balance: EUR 170.529,76

Statement Rows
--------------
Rows:
  - Date 25/04/2025 | Description Insurance coverage prepayment PRE-0001 | Amount EUR 
-41.919,93 | Running Balance EUR 144.083,50
  - Date 08/05/2025 | Description Security deposit DEP-0001 | Amount EUR 11.475,63 | Running
 Balance EUR 155.559,13
  - Date 25/05/2025 | Description Security deposit DEP-0004 | Amount EUR 11.296,10 | Running
 Balance EUR 166.855,23
  - Date 03/06/2025 | Description Security deposit DEP-0003 | Amount EUR 26.228,93 | Running
 Balance EUR 193.084,16
  - Date 31/08/2025 | Description Loan draw LOAN-0001 | Amount EUR 88.335,79 | Running 
Balance EUR 281.419,95
  - Date 24/10/2025 | Description Asset purchase ASSET-0001 | Amount EUR -47.737,12 | 
Running Balance EUR 233.682,83
  - Date 15/12/2025 | Description Security deposit refund DEP-0001 | Amount EUR -9.630,19 | 
Running Balance EUR 224.052,64
  - Date 07/01/2026 | Description Payroll PAYRUN-0001 | Amount EUR -45.301,70 | Running 
Balance EUR 178.750,94
  - Date 25/01/2026 | Description Customer settlement ROLL-0001 | Amount EUR 23.865,28 | 
Running Balance EUR 202.616,22
  - Date 08/02/2026 | Description Supplier settlement BILL-0001 | Amount EUR -32.086,46 | 
Running Balance EUR 170.529,76

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D024
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Rental Revenue | 31,965.58 | D002 | 2025-04-18 | rent_roll |
| 2 | Maintenance Expense | Accounts Payable | 44,911.65 | D003 | 2025-05-03 | maintenance_bill |
| 3 | Cash | Accounts Receivable | 23,865.28 | D004, D002 | 2026-01-25 | tenant_payment |
| 4 | Accounts Payable | Cash | 32,086.46 | D005, D003 | 2026-02-08 | vendor_payment |
| 5 | Cash | Security Deposits Payable | 11,475.63 | D006 | 2025-05-08 | security_deposit |
| 6 | Salaries Expense | Cash | 40,951.50 | D007 | 2026-01-07 | payroll_gross |
| 7 | Payroll Tax Expense | Cash | 4,350.20 | D007 | 2026-01-07 | payroll_tax |
| 8 | Utilities Expense | Accounts Payable | 3,690.78 | D008 | 2026-02-22 | utilities_bill |
| 9 | Prepaid Insurance | Cash | 41,919.93 | D009 | 2025-04-25 | prepaid_insurance_purchase |
| 10 | Insurance Expense | Prepaid Insurance | 13,973.31 | D009, D010 | 2026-03-31 | prepaid_insurance_release |
| 11 | Cash | Loans Payable | 88,335.79 | D011 | 2025-08-31 | loan_draw |
| 12 | Equipment | Cash | 47,737.12 | D012 | 2025-10-24 | equipment_purchase_cash |
| 13 | Equipment | Notes Payable | 173,398.52 | D012 | 2025-10-24 | equipment_purchase_financed |
| 14 | Depreciation Expense | Accumulated Depreciation | 55,283.88 | D013 | 2026-03-31 | depreciation |
| 15 | Security Deposits Payable | Cash | 9,630.19 | D014, D006 | 2025-12-15 | security_deposit_refund |
| 16 | Accounts Receivable | Rental Revenue | 28,094.69 | D015 | 2025-04-09 | rent_roll |
| 17 | Maintenance Expense | Accounts Payable | 47,517.39 | D016 | 2025-06-04 | maintenance_bill |
| 18 | Cash | Security Deposits Payable | 26,228.93 | D017 | 2025-06-03 | security_deposit |
| 19 | Maintenance Expense | Accounts Payable | 18,139.08 | D018 | 2025-05-10 | maintenance_bill |
| 20 | Accounts Receivable | Rental Revenue | 36,962.24 | D019 | 2025-04-03 | rent_roll |
| 21 | Cash | Security Deposits Payable | 11,296.10 | D020 | 2025-05-25 | security_deposit |
| 22 | Accounts Receivable | Rental Revenue | 32,426.70 | D021 | 2025-04-06 | rent_roll |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 170,529.76
- Accounts Receivable: 125,171.32
- Prepaid Insurance: 42,199.17
- Equipment: 251,997.16
- Accumulated Depreciation: -55,283.88

**Liabilities**
- Accounts Payable: 102,405.05
- Accrued Expenses: 2,583.22
- Security Deposits Payable: 60,555.54
- Loans Payable: 112,488.74
- Notes Payable: 173,398.52

**Equity**
- Retained Earnings: -71,888.65
- Owner's Equity: 155,071.11

**Totals:** Assets = 534,613.53; Liabilities = 451,431.07; Equity = 83,182.46
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
- Notes:
