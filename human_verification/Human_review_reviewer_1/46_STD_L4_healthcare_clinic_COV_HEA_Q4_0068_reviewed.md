# Verification Packet — COV_HEA_Q4_0068

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q4 FY 2025-26
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Willow Clinic
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 18
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 79,659.18
- Accounts Receivable: 14,659.34
- Prepaid Insurance: 4,229.81
- Office Supplies: 2,540.51
- Equipment: 60,585.63

**Liabilities**
- Accounts Payable: 9,043.17
- Accrued Expenses: 2,417.08
- Loans Payable: 14,813.88

**Equity**
- Retained Earnings: 19,453.24
- Owner's Equity: 115,947.10


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
  - Section assets | Account Cash | Amount GBP 79,659.18
  - Section assets | Account Accounts Receivable | Amount GBP 14,659.34
  - Section assets | Account Prepaid Insurance | Amount GBP 4,229.81
  - Section assets | Account Office Supplies | Amount GBP 2,540.51
  - Section assets | Account Equipment | Amount GBP 60,585.63
  - Section liabilities | Account Accounts Payable | Amount GBP 9,043.17
  - Section liabilities | Account Accrued Expenses | Amount GBP 2,417.08
  - Section liabilities | Account Loans Payable | Amount GBP 14,813.88
  - Section equity | Account Retained Earnings | Amount GBP 19,453.24
  - Section equity | Account Owner's Equity | Amount GBP 115,947.10

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D013 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-05

```
VENDOR INVOICE
==============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 05/01/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 16/01/2025

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 16/01/2025
Total: GBP 17,707.77

Bill Lines
----------
Lines:
  - Description Implementation work | Amount GBP 6,425.45
  - Description Support fee | Amount GBP 11,282.32

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D016 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-06

```
VENDOR INVOICE
==============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 06/01/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 16/01/2025

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 16/01/2025
Total: GBP 4,455.28

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 983.36
  - Description Support fee | Amount GBP 3,471.92

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-07

```
VENDOR INVOICE
==============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 07/01/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 19/01/2025

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 19/01/2025
Total: GBP 8,383.82

Bill Lines
----------
Lines:
  - Description Implementation work | Amount GBP 2,022.01
  - Description Support fee | Amount GBP 6,361.81

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D012 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-07

```
VENDOR INVOICE
==============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 07/01/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 18/01/2025

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 18/01/2025
Total: GBP 12,333.22

Bill Lines
----------
Lines:
  - Description Implementation work | Amount GBP 5,328.18
  - Description Support fee | Amount GBP 7,005.04

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D015 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-02

```
PATIENT INVOICE
===============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 02/02/2025

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D015
Document Type: patient_invoice
Period: Q4 FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Anaya Patel
Payer: CareSure
Service Date: 02/02/2025
Gross Charge: GBP 7,525.26
Patient Due: 2,213.49
Insurer Due: 5,311.77

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D014 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-16

```
PATIENT INVOICE
===============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Document Date: 16/02/2025

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D014
Document Type: patient_invoice
Period: Q4 FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Anaya Patel
Payer: CareSure
Service Date: 16/02/2025
Gross Charge: GBP 8,484.87
Patient Due: 2,128.11
Insurer Due: 6,356.76

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D008 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-18

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Prime Utility Desk
Asset Name: CNC router
Asset Tag: TAG-0001
Useful Life Months: 24
Total: GBP 107,158.38
Paid Cash: GBP 37,973.74
Financed Amount: GBP 69,184.64
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D007 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-02-23

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 5,999.31
Draw Amount: GBP 96,126.12
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 102,125.43
Note: Scheduled lender activity for the selected period.
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-24

```
PATIENT INVOICE
===============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Document Date: 24/02/2025

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: Q4 FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Noah Ferreira
Payer: Unity Health Plan
Service Date: 24/02/2025
Gross Charge: GBP 3,053.98
Patient Due: 595.77
Insurer Due: 2,458.21

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D011 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-25

```
PATIENT INVOICE
===============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 25/02/2025

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D011
Document Type: patient_invoice
Period: Q4 FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Anaya Patel
Payer: NorthCover
Service Date: 25/02/2025
Gross Charge: GBP 5,082.63
Patient Due: 845.62
Insurer Due: 4,237.01

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2025-03-02

```
INSURER REMITTANCE
==================

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 02/03/2025

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: Q4 FY 2025-26

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: Unity Health Plan
Claim Reference: PTINV-0001
Approved Amount: GBP 2,458.21
Paid Amount: GBP 2,458.21
Payment Date: 02/03/2025

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-03-02

```
PAYROLL SUMMARY
===============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 02/03/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2025-26
Headcount: 10
Gross Pay: GBP 30,074.32
Employer Tax: 3,746.21
Cash Outflow: GBP 33,820.53

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-03-10

```
COPAY RECEIPT
=============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Document Date: 10/03/2025

To
--
Noah Ferreira
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Noah Ferreira
Amount: GBP 595.77
Reference Invoice: PTINV-0001
Payment Method: Card

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D009 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: CNC router
Asset Tag: TAG-0001
Cost: GBP 107,158.38
Useful Life Months: 24
Current Period Charge: GBP 13,394.79
Accumulated Depreciation: 13,394.79
```

### Document D010 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 31/03/2025

Reference Box
-------------
Document ID: D010
Document Type: service_period_memo
Period: Q4 FY 2025-26
Reference: Q4 FY 2025-26

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q4 FY 2025-26
Recognized Amount: GBP 6,922.79

Explanation
-----------
Narrative: Accrue unpaid office supplies expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D017 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Willow Clinic
90 Hill Park, Hyderabad
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D017
Document Type: memo
Period: Q4 FY 2025-26

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
Audience: Back Office

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
Page marker: D017
```

### Document D018 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Willow Clinic
90 Hill Park, Hyderabad
Date: 31/03/2025

Reference Box
-------------
Document ID: D018
Document Type: bank_statement
Period: Q4 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0068
Statement Currency: GBP
Opening Balance: GBP 79,659.18
Closing Balance: GBP 107,045.01

Statement Rows
--------------
Rows:
  - Date 18/02/2025 | Description Asset purchase ASSET-0001 | Amount GBP -37,973.74 | 
Running Balance GBP 41,685.44
  - Date 23/02/2025 | Description Loan draw LOAN-0001 | Amount GBP 96,126.12 | Running 
Balance GBP 137,811.56
  - Date 02/03/2025 | Description Insurer remittance PTINV-0001 | Amount GBP 2,458.21 | 
Running Balance GBP 140,269.77
  - Date 02/03/2025 | Description Payroll PAYRUN-0001 | Amount GBP -33,820.53 | Running 
Balance GBP 106,449.24
  - Date 10/03/2025 | Description Copay receipt COPAY-0001 | Amount GBP 595.77 | Running 
Balance GBP 107,045.01

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D018
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 3,053.98 | D002 | 2025-02-24 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 8,383.82 | D003 | 2025-01-07 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 595.77 | D004, D002 | 2025-03-10 | copay_collection |
| 4 | Cash | Accounts Receivable | 2,458.21 | D005, D002 | 2025-03-02 | insurer_remittance |
| 5 | Salaries Expense | Cash | 30,074.32 | D006 | 2025-03-02 | payroll_gross |
| 6 | Payroll Tax Expense | Cash | 3,746.21 | D006 | 2025-03-02 | payroll_tax |
| 7 | Cash | Loans Payable | 96,126.12 | D007 | 2025-02-23 | loan_draw |
| 8 | Equipment | Cash | 37,973.74 | D008 | 2025-02-18 | equipment_purchase_cash |
| 9 | Equipment | Notes Payable | 69,184.64 | D008 | 2025-02-18 | equipment_purchase_financed |
| 10 | Depreciation Expense | Accumulated Depreciation | 13,394.79 | D009 | 2025-03-31 | depreciation |
| 11 | Office Supplies Expense | Accrued Expenses | 6,922.79 | D010 | 2025-03-31 | expense_accrual |
| 12 | Accounts Receivable | Service Revenue | 5,082.63 | D011 | 2025-02-25 | patient_billing |
| 13 | Office Supplies Expense | Accounts Payable | 12,333.22 | D012 | 2025-01-07 | clinic_supplies_bill |
| 14 | Office Supplies Expense | Accounts Payable | 17,707.77 | D013 | 2025-01-05 | clinic_supplies_bill |
| 15 | Accounts Receivable | Service Revenue | 8,484.87 | D014 | 2025-02-16 | patient_billing |
| 16 | Accounts Receivable | Service Revenue | 7,525.26 | D015 | 2025-02-02 | patient_billing |
| 17 | Office Supplies Expense | Accounts Payable | 4,455.28 | D016 | 2025-01-06 | clinic_supplies_bill |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 107,045.01
- Accounts Receivable: 35,752.10
- Prepaid Insurance: 4,229.81
- Office Supplies: 2,540.51
- Equipment: 167,744.01
- Accumulated Depreciation: -13,394.79

**Liabilities**
- Accounts Payable: 51,923.26
- Accrued Expenses: 9,339.87
- Loans Payable: 110,940.00
- Notes Payable: 69,184.64

**Equity**
- Retained Earnings: -53,418.22
- Owner's Equity: 115,947.10

**Totals:** Assets = 303,916.65; Liabilities = 241,387.77; Equity = 62,528.88
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
- Notes: Clean. No issues noted.
