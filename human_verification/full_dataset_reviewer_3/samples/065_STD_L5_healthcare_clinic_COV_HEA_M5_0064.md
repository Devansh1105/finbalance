# Verification Packet — COV_HEA_M5_0064

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** September 2024
- **Period start → end:** 2024-09-01 → 2024-09-30
- **Entity:** Pioneer Manufacturing
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 19
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-09-01_

**Assets**
- Cash: 35,008.60
- Accounts Receivable: 8,534.66
- Prepaid Insurance: 2,133.11
- Office Supplies: 1,098.60
- Equipment: 23,926.01

**Liabilities**
- Accounts Payable: 4,406.28
- Accrued Expenses: 1,478.55
- Loans Payable: 10,590.72

**Equity**
- Retained Earnings: 14,168.07
- Owner's Equity: 40,057.36


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-09-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/09/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 35.008,60
  - Section assets | Account Accounts Receivable | Amount EUR 8.534,66
  - Section assets | Account Prepaid Insurance | Amount EUR 2.133,11
  - Section assets | Account Office Supplies | Amount EUR 1.098,60
  - Section assets | Account Equipment | Amount EUR 23.926,01
  - Section liabilities | Account Accounts Payable | Amount EUR 4.406,28
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.478,55
  - Section liabilities | Account Loans Payable | Amount EUR 10.590,72
  - Section equity | Account Retained Earnings | Amount EUR 14.168,07
  - Section equity | Account Owner's Equity | Amount EUR 40.057,36

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D014 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-05

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 05/09/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D014
Document Type: vendor_invoice
Period: September 2024

Terms
-----
Due Date: 18/09/2024

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 18/09/2024
Total: EUR 1.993,60

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 455,66
  - Description Support fee | Amount EUR 1.537,94

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D015 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-05

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
14 King Street, Pune
Date: 05/09/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: vendor_invoice
Period: September 2024

Terms
-----
Due Date: 26/09/2024

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 26/09/2024
Total: EUR 2.352,27

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 510,40
  - Description Support fee | Amount EUR 1.841,87

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-06

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
14 King Street, Pune
Date: 06/09/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: September 2024

Terms
-----
Due Date: 18/09/2024

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 18/09/2024
Total: EUR 5.928,09

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 1.413,04
  - Description Support fee | Amount EUR 4.515,05

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D016 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-06

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 06/09/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: vendor_invoice
Period: September 2024

Terms
-----
Due Date: 24/09/2024

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0005
Due Date: 24/09/2024
Total: EUR 12.021,30

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 2.411,76
  - Description Support fee | Amount EUR 9.609,54

Footer
------
Generated for synthetic accounting research use.
Page marker: D016
```

### Document D011 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-08

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
14 King Street, Pune
Date: 08/09/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: vendor_invoice
Period: September 2024

Terms
-----
Due Date: 18/09/2024

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 18/09/2024
Total: EUR 11.752,79

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 2.826,08
  - Description Support fee | Amount EUR 8.926,71

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-11

```
PATIENT INVOICE
===============

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 11/09/2024

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: September 2024

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Marcus Lee
Payer: NorthCover
Service Date: 11/09/2024
Gross Charge: EUR 2.877,37
Patient Due: 749,91
Insurer Due: 2.127,46

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D017 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-11

```
PATIENT INVOICE
===============

From
----
Pioneer Manufacturing
14 King Street, Pune
Date: 11/09/2024

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D017
Document Type: patient_invoice
Period: September 2024

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Ella Santos
Payer: NorthCover
Service Date: 11/09/2024
Gross Charge: EUR 4.651,18
Patient Due: 968,06
Insurer Due: 3.683,12

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D007 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-15

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: EUR 14.773,95
Draw Amount: EUR 59.064,55
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 73.838,50
Note: Scheduled lender activity for the selected period.
```

### Document D013 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-17

```
PATIENT INVOICE
===============

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 17/09/2024

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D013
Document Type: patient_invoice
Period: September 2024

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Noah Ferreira
Payer: Unity Health Plan
Service Date: 17/09/2024
Gross Charge: EUR 3.357,83
Patient Due: 1.056,64
Insurer Due: 2.301,19

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D012 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-18

```
PATIENT INVOICE
===============

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 18/09/2024

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D012
Document Type: patient_invoice
Period: September 2024

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Anaya Patel
Payer: CareSure
Service Date: 18/09/2024
Gross Charge: EUR 4.336,06
Patient Due: 1.268,31
Insurer Due: 3.067,75

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D008 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-09-20

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Golden State Finance
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 60
Total: EUR 79.901,70
Paid Cash: EUR 29.159,71
Financed Amount: EUR 50.741,99
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-09-22

```
COPAY RECEIPT
=============

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 22/09/2024

To
--
Marcus Lee
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Marcus Lee
Amount: EUR 749,91
Reference Invoice: PTINV-0001
Payment Method: Card

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2024-09-23

```
INSURER REMITTANCE
==================

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 23/09/2024

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: September 2024

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: NorthCover
Claim Reference: PTINV-0001
Approved Amount: EUR 2.127,46
Paid Amount: EUR 2.127,46
Payment Date: 23/09/2024

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D006 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-23

```
PAYROLL SUMMARY
===============

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 23/09/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: September 2024
Headcount: 5
Gross Pay: EUR 11.811,78
Employer Tax: 1.576,98
Cash Outflow: EUR 13.388,76

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-09-26

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: First City Bank
Opening Principal: EUR 47.365,08
Draw Amount: EUR 0,00
Principal Paid: EUR 9.169,16
Interest Paid: EUR 1.171,01
Ending Principal: EUR 38.195,92
Note: Scheduled lender activity for the selected period.
```

### Document D009 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-09-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 23.926,01
Useful Life Months: 48
Current Period Charge: EUR 498,46
Accumulated Depreciation: 498,46
```

### Document D018 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-09-30

```
VENDOR STATEMENT
================

From
----
Pioneer Manufacturing
14 King Street, Pune
Document Date: 30/09/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D018
Document Type: vendor_statement
Period: September 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Pace Office Mart
Closing Balance: EUR 5.928,09

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount EUR 5.928,09 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-09-30

```
BANK STATEMENT
==============

From
----
Pioneer Manufacturing
14 King Street, Pune
Date: 30/09/2024

Reference Box
-------------
Document ID: D019
Document Type: bank_statement
Period: September 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0064
Statement Currency: EUR
Opening Balance: EUR 35.008,60
Closing Balance: EUR 44.061,88

Statement Rows
--------------
Rows:
  - Date 15/09/2024 | Description Loan draw LOAN-0001 | Amount EUR 59.064,55 | Running 
Balance EUR 94.073,15
  - Date 20/09/2024 | Description Asset purchase ASSET-0001 | Amount EUR -29.159,71 | 
Running Balance EUR 64.913,44
  - Date 22/09/2024 | Description Copay receipt COPAY-0001 | Amount EUR 749,91 | Running 
Balance EUR 65.663,35
  - Date 23/09/2024 | Description Insurer remittance PTINV-0001 | Amount EUR 2.127,46 | 
Running Balance EUR 67.790,81
  - Date 23/09/2024 | Description Payroll PAYRUN-0001 | Amount EUR -13.388,76 | Running 
Balance EUR 54.402,05
  - Date 26/09/2024 | Description Loan payment LOAN-0002 | Amount EUR -10.340,17 | Running 
Balance EUR 44.061,88

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D019
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 2,877.37 | D002 | 2024-09-11 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 5,928.09 | D003 | 2024-09-06 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 749.91 | D004, D002 | 2024-09-22 | copay_collection |
| 4 | Cash | Accounts Receivable | 2,127.46 | D005, D002 | 2024-09-23 | insurer_remittance |
| 5 | Salaries Expense | Cash | 11,811.78 | D006 | 2024-09-23 | payroll_gross |
| 6 | Payroll Tax Expense | Cash | 1,576.98 | D006 | 2024-09-23 | payroll_tax |
| 7 | Cash | Loans Payable | 59,064.55 | D007 | 2024-09-15 | loan_draw |
| 8 | Equipment | Cash | 29,159.71 | D008 | 2024-09-20 | equipment_purchase_cash |
| 9 | Equipment | Notes Payable | 50,741.99 | D008 | 2024-09-20 | equipment_purchase_financed |
| 10 | Depreciation Expense | Accumulated Depreciation | 498.46 | D009 | 2024-09-30 | depreciation |
| 11 | Loans Payable | Cash | 9,169.16 | D010 | 2024-09-26 | loan_repayment_principal |
| 12 | Interest Expense | Cash | 1,171.01 | D010 | 2024-09-26 | loan_repayment_interest |
| 13 | Office Supplies Expense | Accounts Payable | 11,752.79 | D011 | 2024-09-08 | clinic_supplies_bill |
| 14 | Accounts Receivable | Service Revenue | 4,336.06 | D012 | 2024-09-18 | patient_billing |
| 15 | Accounts Receivable | Service Revenue | 3,357.83 | D013 | 2024-09-17 | patient_billing |
| 16 | Office Supplies Expense | Accounts Payable | 1,993.60 | D014 | 2024-09-05 | clinic_supplies_bill |
| 17 | Office Supplies Expense | Accounts Payable | 2,352.27 | D015 | 2024-09-05 | clinic_supplies_bill |
| 18 | Office Supplies Expense | Accounts Payable | 12,021.30 | D016 | 2024-09-06 | clinic_supplies_bill |
| 19 | Accounts Receivable | Service Revenue | 4,651.18 | D017 | 2024-09-11 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 44,061.88
- Accounts Receivable: 20,879.73
- Prepaid Insurance: 2,133.11
- Office Supplies: 1,098.60
- Equipment: 103,827.71
- Accumulated Depreciation: -498.46

**Liabilities**
- Accounts Payable: 38,454.33
- Accrued Expenses: 1,478.55
- Loans Payable: 60,486.11
- Notes Payable: 50,741.99

**Equity**
- Retained Earnings: -19,715.77
- Owner's Equity: 40,057.36

**Totals:** Assets = 171,502.57; Liabilities = 151,160.98; Equity = 20,341.59
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
