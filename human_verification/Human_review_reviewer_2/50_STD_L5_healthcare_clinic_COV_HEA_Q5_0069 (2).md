# Verification Packet — COV_HEA_Q5_0069

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 5
- **Period type:** quarter
- **Period label:** Q4 FY 2025
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Summit Operations
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 24
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 68,999.10
- Accounts Receivable: 12,514.08
- Prepaid Insurance: 5,860.77
- Office Supplies: 2,764.82
- Equipment: 39,397.85

**Liabilities**
- Accounts Payable: 11,638.05
- Accrued Expenses: 4,960.49
- Loans Payable: 36,299.81

**Equity**
- Retained Earnings: 23,249.07
- Owner's Equity: 53,389.20


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-10-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $68,999.10
  - Section assets | Account Accounts Receivable | Amount $12,514.08
  - Section assets | Account Prepaid Insurance | Amount $5,860.77
  - Section assets | Account Office Supplies | Amount $2,764.82
  - Section assets | Account Equipment | Amount $39,397.85
  - Section liabilities | Account Accounts Payable | Amount $11,638.05
  - Section liabilities | Account Accrued Expenses | Amount $4,960.49
  - Section liabilities | Account Loans Payable | Amount $36,299.81
  - Section equity | Account Retained Earnings | Amount $23,249.07
  - Section equity | Account Owner's Equity | Amount $53,389.20

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D017 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-07

```
VENDOR INVOICE
==============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-10-07

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D017
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-10-20

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 2025-10-20
Total: $13,459.39

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $2,863.06
  - Description Support fee | Amount $10,596.33

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D019 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-13

```
VENDOR INVOICE
==============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-10-13

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D019
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-10-27

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0005
Due Date: 2025-10-27
Total: $24,165.36

Bill Lines
----------
Lines:
  - Description Support package | Amount $9,495.23
  - Description Support fee | Amount $14,670.13

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D013 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-16

```
VENDOR INVOICE
==============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-10-16

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-10-27

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 2025-10-27
Total: $22,912.42

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $9,535.76
  - Description Support fee | Amount $13,376.66

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D020 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-18

```
VENDOR INVOICE
==============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-10-18

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D020
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-11-05

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0006
Due Date: 2025-11-05
Total: $8,436.10

Bill Lines
----------
Lines:
  - Description Support package | Amount $2,062.50
  - Description Support fee | Amount $6,373.60

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D015 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-20

```
VENDOR INVOICE
==============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-10-20

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-11-09

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 2025-11-09
Total: $25,476.24

Bill Lines
----------
Lines:
  - Description Review pack | Amount $7,621.38
  - Description Support fee | Amount $17,854.86

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-21

```
VENDOR INVOICE
==============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-10-21

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 2025-11-07

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-11-07
Total: $23,254.13

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $8,949.95
  - Description Support fee | Amount $14,304.18

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D012 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-08

```
PATIENT INVOICE
===============

From
----
Summit Operations
75 Market Road, Mumbai
Document Date: 2025-11-08

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D012
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Ella Santos
Payer: NorthCover
Service Date: 2025-11-08
Gross Charge: $2,374.56
Patient Due: 383.49
Insurer Due: 1,991.07

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D018 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-13

```
PATIENT INVOICE
===============

From
----
Summit Operations
75 Market Road, Mumbai
Document Date: 2025-11-13

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D018
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0005
Patient: Noah Ferreira
Payer: CareSure
Service Date: 2025-11-13
Gross Charge: $2,474.83
Patient Due: 634.73
Insurer Due: 1,840.10

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D016 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-15

```
PATIENT INVOICE
===============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-11-15

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D016
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Anaya Patel
Payer: Harbor Health Network
Service Date: 2025-11-15
Gross Charge: $10,953.22
Patient Due: 1,934.63
Insurer Due: 9,018.59

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D021 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-19

```
PATIENT INVOICE
===============

From
----
Summit Operations
75 Market Road, Mumbai
Document Date: 2025-11-19

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D021
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0006
Patient: Noah Ferreira
Payer: CareSure
Service Date: 2025-11-19
Gross Charge: $5,711.95
Patient Due: 1,710.68
Insurer Due: 4,001.27

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-20

```
PATIENT INVOICE
===============

From
----
Summit Operations
75 Market Road, Mumbai
Document Date: 2025-11-20

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Marcus Lee
Payer: CareSure
Service Date: 2025-11-20
Gross Charge: $8,654.64
Patient Due: 2,026.22
Insurer Due: 6,628.42

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D008 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-22

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: Delivery van
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $135,399.26
Paid Cash: $45,093.36
Financed Amount: $90,305.90
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D014 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-22

```
PATIENT INVOICE
===============

From
----
Summit Operations
75 Market Road, Mumbai
Document Date: 2025-11-22

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D014
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Marcus Lee
Payer: Unity Health Plan
Service Date: 2025-11-22
Gross Charge: $7,617.65
Patient Due: 2,302.69
Insurer Due: 5,314.96

Footer
------
Generated for synthetic accounting research use.
Page marker: D014
```

### Document D007 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-28

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $19,621.32
Draw Amount: $184,231.76
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $203,853.08
Note: Scheduled lender activity for the selected period.
```

### Document D010 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-12-01

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: $96,849.04
Draw Amount: $0.00
Principal Paid: $27,455.50
Interest Paid: $2,177.41
Ending Principal: $69,393.54
Note: Scheduled lender activity for the selected period.
```

### Document D006 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-12-06

```
PAYROLL SUMMARY
===============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-12-06

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2025
Headcount: 10
Gross Pay: $19,094.45
Employer Tax: 2,410.20
Cash Outflow: $21,504.65

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-12-18

```
COPAY RECEIPT
=============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-12-18

To
--
Marcus Lee
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Marcus Lee
Amount: $2,026.22
Reference Invoice: PTINV-0001
Payment Method: Card

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2025-12-20

```
INSURER REMITTANCE
==================

From
----
Summit Operations
75 Market Road, Mumbai
Document Date: 2025-12-20

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: Q4 FY 2025

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: CareSure
Claim Reference: PTINV-0001
Approved Amount: $6,628.42
Paid Amount: $6,628.42
Payment Date: 2025-12-20

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D009 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Delivery van
Asset Tag: TAG-0001
Cost: $135,399.26
Useful Life Months: 60
Current Period Charge: $6,769.95
Accumulated Depreciation: 6,769.95
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
Summit Operations
75 Market Road, Mumbai
Date: 2025-12-31

Reference Box
-------------
Document ID: D011
Document Type: service_period_memo
Period: Q4 FY 2025
Reference: Q4 FY 2025

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q4 FY 2025
Recognized Amount: $6,817.30

Explanation
-----------
Narrative: Accrue unpaid office supplies expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D022 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-12-31

Reference Box
-------------
Document ID: D022
Document Type: memo
Period: Q4 FY 2025

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Annual leave policy reminder
Audience: Operations Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D023 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-12-31

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D023
Document Type: vendor_statement
Period: Q4 FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Vertex Supply Co.
Closing Balance: $25,476.24

Statement Lines
---------------
Lines:
  - Reference BILL-0003 | Document Type Open invoice | Amount $25,476.24 | Status 
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
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Summit Operations
75 Market Road, Mumbai
Date: 2025-12-31

Reference Box
-------------
Document ID: D024
Document Type: bank_statement
Period: Q4 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0069
Statement Currency: USD
Opening Balance: $68,999.10
Closing Balance: $165,654.58

Statement Rows
--------------
Rows:
  - Date 2025-11-22 | Description Asset purchase ASSET-0001 | Amount $-45,093.36 | Running 
Balance $23,905.74
  - Date 2025-11-28 | Description Loan draw LOAN-0001 | Amount $184,231.76 | Running Balance
 $208,137.50
  - Date 2025-12-01 | Description Loan payment LOAN-0002 | Amount $-29,632.91 | Running 
Balance $178,504.59
  - Date 2025-12-06 | Description Payroll PAYRUN-0001 | Amount $-21,504.65 | Running Balance
 $156,999.94
  - Date 2025-12-18 | Description Copay receipt COPAY-0001 | Amount $2,026.22 | Running 
Balance $159,026.16
  - Date 2025-12-20 | Description Insurer remittance PTINV-0001 | Amount $6,628.42 | Running
 Balance $165,654.58

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
| 1 | Accounts Receivable | Service Revenue | 8,654.64 | D002 | 2025-11-20 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 23,254.13 | D003 | 2025-10-21 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 2,026.22 | D004, D002 | 2025-12-18 | copay_collection |
| 4 | Cash | Accounts Receivable | 6,628.42 | D005, D002 | 2025-12-20 | insurer_remittance |
| 5 | Salaries Expense | Cash | 19,094.45 | D006 | 2025-12-06 | payroll_gross |
| 6 | Payroll Tax Expense | Cash | 2,410.20 | D006 | 2025-12-06 | payroll_tax |
| 7 | Cash | Loans Payable | 184,231.76 | D007 | 2025-11-28 | loan_draw |
| 8 | Equipment | Cash | 45,093.36 | D008 | 2025-11-22 | equipment_purchase_cash |
| 9 | Equipment | Notes Payable | 90,305.90 | D008 | 2025-11-22 | equipment_purchase_financed |
| 10 | Depreciation Expense | Accumulated Depreciation | 6,769.95 | D009 | 2025-12-31 | depreciation |
| 11 | Loans Payable | Cash | 27,455.50 | D010 | 2025-12-01 | loan_repayment_principal |
| 12 | Interest Expense | Cash | 2,177.41 | D010 | 2025-12-01 | loan_repayment_interest |
| 13 | Office Supplies Expense | Accrued Expenses | 6,817.30 | D011 | 2025-12-31 | expense_accrual |
| 14 | Accounts Receivable | Service Revenue | 2,374.56 | D012 | 2025-11-08 | patient_billing |
| 15 | Office Supplies Expense | Accounts Payable | 22,912.42 | D013 | 2025-10-16 | clinic_supplies_bill |
| 16 | Accounts Receivable | Service Revenue | 7,617.65 | D014 | 2025-11-22 | patient_billing |
| 17 | Office Supplies Expense | Accounts Payable | 25,476.24 | D015 | 2025-10-20 | clinic_supplies_bill |
| 18 | Accounts Receivable | Service Revenue | 10,953.22 | D016 | 2025-11-15 | patient_billing |
| 19 | Office Supplies Expense | Accounts Payable | 13,459.39 | D017 | 2025-10-07 | clinic_supplies_bill |
| 20 | Accounts Receivable | Service Revenue | 2,474.83 | D018 | 2025-11-13 | patient_billing |
| 21 | Office Supplies Expense | Accounts Payable | 24,165.36 | D019 | 2025-10-13 | clinic_supplies_bill |
| 22 | Office Supplies Expense | Accounts Payable | 8,436.10 | D020 | 2025-10-18 | clinic_supplies_bill |
| 23 | Accounts Receivable | Service Revenue | 5,711.95 | D021 | 2025-11-19 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 165,654.58
- Accounts Receivable: 41,646.29
- Prepaid Insurance: 5,860.77
- Office Supplies: 2,764.82
- Equipment: 174,797.11
- Accumulated Depreciation: -6,769.95

**Liabilities**
- Accounts Payable: 129,341.69
- Accrued Expenses: 11,777.79
- Loans Payable: 193,076.07
- Notes Payable: 90,305.90

**Equity**
- Retained Earnings: -93,937.03
- Owner's Equity: 53,389.20

**Totals:** Assets = 383,953.62; Liabilities = 424,501.45; Equity = -40,547.83
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
- [ ] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [x] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:  Extra / unsupported in section 5: DR Accounts Receivable / CR Service Revenue 8654.64; Extra / unsupported in section 5: DR Office Supplies Expense / CR Accounts Payable 23254.13; Extra / unsupported in section 5: DR Cash / CR Accounts Receivable 2026.22; Extra / unsupported in section 5: DR Cash / CR Accounts Receivable 6628.42; Extra / unsupported in section 5: DR Salaries Expense / CR Cash 19094.45; Extra / unsupported in section 5: DR Payroll Tax Expense / CR Cash 2410.2; Extra / unsupported in section 5: DR Cash / CR Loans Payable 184231.76; Extra / unsupported in section 5: DR Equipment / CR Cash 45093.36; Extra / unsupported in section 5: DR Equipment / CR Notes Payable 90305.9; Extra / unsupported in section 5: DR Depreciation Expense / CR Accumulated Depreciation 6769.95; Extra / unsupported in section 5: DR Loans Payable / CR Cash 27455.5; Extra / unsupported in section 5: DR Interest Expense / CR Cash 2177.41; Extra / unsupported in section 5: DR Office Supplies Expense / CR Accrued Expenses 6817.3; Extra / unsupported in section 5: DR Accounts Receivable / CR Service Revenue 2374.56; Extra / unsupported in section 5: DR Office Supplies Expense / CR Accounts Payable 22912.42; Extra / unsupported in section 5: DR Accounts Receivable / CR Service Revenue 7617.65; Extra / unsupported in section 5: DR Office Supplies Expense / CR Accounts Payable 25476.24; Extra / unsupported in section 5: DR Accounts Receivable / CR Service Revenue 10953.22; Extra / unsupported in section 5: DR Office Supplies Expense / CR Accounts Payable 13459.39; Extra / unsupported in section 5: DR Accounts Receivable / CR Service Revenue 2474.83; Extra / unsupported in section 5: DR Office Supplies Expense / CR Accounts Payable 24165.36; Extra / unsupported in section 5: DR Office Supplies Expense / CR Accounts Payable 8436.1; Extra / unsupported in section 5: DR Accounts Receivable / CR Service Revenue 5711.95

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

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [x] Not acceptable as ground truth
- Notes:  BS: Accounts Receivable: computed 12514.08 vs expected 41646.29; BS: Loans Payable: computed 36299.81 vs expected 193076.07; BS: Retained Earnings: computed 23249.07 vs expected 0.00; BS: Notes Payable: computed 0.00 vs expected 90305.90; BS: Accrued Expenses: computed 4960.49 vs expected 11777.79; BS: Equipment: computed 39397.85 vs expected 174797.11; BS: Accounts Payable: computed 11638.05 vs expected 129341.69; BS: Cash: computed 68999.10 vs expected 165654.58
