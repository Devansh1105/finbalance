# Verification Packet — COV_HEA_Q3_0067

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q4 FY 2025-26
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Willow Software
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 14
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 65,466.67
- Accounts Receivable: 10,472.43
- Prepaid Insurance: 4,672.96
- Office Supplies: 1,664.65

**Liabilities**
- Accounts Payable: 3,786.61
- Accrued Expenses: 3,787.45

**Equity**
- Retained Earnings: 15,761.52
- Owner's Equity: 58,941.13


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
  - Section assets | Account Cash | Amount EUR 65.466,67
  - Section assets | Account Accounts Receivable | Amount EUR 10.472,43
  - Section assets | Account Prepaid Insurance | Amount EUR 4.672,96
  - Section assets | Account Office Supplies | Amount EUR 1.664,65
  - Section liabilities | Account Accounts Payable | Amount EUR 3.786,61
  - Section liabilities | Account Accrued Expenses | Amount EUR 3.787,45
  - Section equity | Account Retained Earnings | Amount EUR 15.761,52
  - Section equity | Account Owner's Equity | Amount EUR 58.941,13

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D011 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-13

```
VENDOR INVOICE
==============

From
----
Willow Software
14 King Street, Pune
Date: 13/01/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 29/01/2025

Supplier Header
---------------
Vendor: Pace Office Mart
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0004
Due Date: 29/01/2025
Total: EUR 1.752,50

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 724,96
  - Description Support fee | Amount EUR 1.027,54

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-19

```
VENDOR INVOICE
==============

From
----
Willow Software
14 King Street, Pune
Document Date: 19/01/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 09/02/2025

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 09/02/2025
Total: EUR 8.728,78

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 2.147,91
  - Description Support fee | Amount EUR 6.580,87

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D010 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-20

```
VENDOR INVOICE
==============

From
----
Willow Software
14 King Street, Pune
Date: 20/01/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 05/02/2025

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0003
Due Date: 05/02/2025
Total: EUR 14.858,18

Bill Lines
----------
Lines:
  - Description Implementation work | Amount EUR 4.312,26
  - Description Support fee | Amount EUR 10.545,92

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-21

```
VENDOR INVOICE
==============

From
----
Willow Software
14 King Street, Pune
Date: 21/01/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: vendor_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 31/01/2025

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 31/01/2025
Total: EUR 12.594,43

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 4.611,58
  - Description Support fee | Amount EUR 7.982,85

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-10

```
PATIENT INVOICE
===============

From
----
Willow Software
14 King Street, Pune
Date: 10/02/2025

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: Q4 FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Marcus Lee
Payer: Unity Health Plan
Service Date: 10/02/2025
Gross Charge: EUR 8.206,03
Patient Due: 2.661,99
Insurer Due: 5.544,04

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D012 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-10

```
PATIENT INVOICE
===============

From
----
Willow Software
14 King Street, Pune
Date: 10/02/2025

To
--
Anaya Patel
Patient billing contact

Reference Box
-------------
Document ID: D012
Document Type: patient_invoice
Period: Q4 FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Anaya Patel
Payer: NorthCover
Service Date: 10/02/2025
Gross Charge: EUR 2.141,97
Patient Due: 569,09
Insurer Due: 1.572,88

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D009 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-20

```
PATIENT INVOICE
===============

From
----
Willow Software
14 King Street, Pune
Date: 20/02/2025

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D009
Document Type: patient_invoice
Period: Q4 FY 2025-26

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Noah Ferreira
Payer: CareSure
Service Date: 20/02/2025
Gross Charge: EUR 6.779,91
Patient Due: 1.584,41
Insurer Due: 5.195,50

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D006 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-03-10

```
PAYROLL SUMMARY
===============

From
----
Willow Software
14 King Street, Pune
Date: 10/03/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2025-26
Headcount: 6
Gross Pay: EUR 22.581,50
Employer Tax: 3.138,66
Cash Outflow: EUR 25.720,16

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-03-14

```
COPAY RECEIPT
=============

From
----
Willow Software
14 King Street, Pune
Document Date: 14/03/2025

To
--
Marcus Lee
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Marcus Lee
Amount: EUR 2.661,99
Reference Invoice: PTINV-0001
Payment Method: Cash

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2025-03-22

```
INSURER REMITTANCE
==================

From
----
Willow Software
14 King Street, Pune
Document Date: 22/03/2025

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
Approved Amount: EUR 5.544,04
Paid Amount: EUR 5.544,04
Payment Date: 22/03/2025

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D007 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Willow Software
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D007
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
Recognized Amount: EUR 5.032,62

Explanation
-----------
Narrative: Accrue unpaid office supplies expense incurred before period end.

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D013 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Willow Software
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D013
Document Type: memo
Period: Q4 FY 2025-26

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
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
Page marker: D013
```

### Document D014 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Willow Software
14 King Street, Pune
Date: 31/03/2025

Reference Box
-------------
Document ID: D014
Document Type: bank_statement
Period: Q4 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0067
Statement Currency: EUR
Opening Balance: EUR 65.466,67
Closing Balance: EUR 47.952,54

Statement Rows
--------------
Rows:
  - Date 10/03/2025 | Description Payroll PAYRUN-0001 | Amount EUR -25.720,16 | Running 
Balance EUR 39.746,51
  - Date 14/03/2025 | Description Copay receipt COPAY-0001 | Amount EUR 2.661,99 | Running 
Balance EUR 42.408,50
  - Date 22/03/2025 | Description Insurer remittance PTINV-0001 | Amount EUR 5.544,04 | 
Running Balance EUR 47.952,54

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D014
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 8,206.03 | D002 | 2025-02-10 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 8,728.78 | D003 | 2025-01-19 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 2,661.99 | D004, D002 | 2025-03-14 | copay_collection |
| 4 | Cash | Accounts Receivable | 5,544.04 | D005, D002 | 2025-03-22 | insurer_remittance |
| 5 | Salaries Expense | Cash | 22,581.50 | D006 | 2025-03-10 | payroll_gross |
| 6 | Payroll Tax Expense | Cash | 3,138.66 | D006 | 2025-03-10 | payroll_tax |
| 7 | Office Supplies Expense | Accrued Expenses | 5,032.62 | D007 | 2025-03-31 | expense_accrual |
| 8 | Office Supplies Expense | Accounts Payable | 12,594.43 | D008 | 2025-01-21 | clinic_supplies_bill |
| 9 | Accounts Receivable | Service Revenue | 6,779.91 | D009 | 2025-02-20 | patient_billing |
| 10 | Office Supplies Expense | Accounts Payable | 14,858.18 | D010 | 2025-01-20 | clinic_supplies_bill |
| 11 | Office Supplies Expense | Accounts Payable | 1,752.50 | D011 | 2025-01-13 | clinic_supplies_bill |
| 12 | Accounts Receivable | Service Revenue | 2,141.97 | D012 | 2025-02-10 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 47,952.54
- Accounts Receivable: 19,394.31
- Prepaid Insurance: 4,672.96
- Office Supplies: 1,664.65

**Liabilities**
- Accounts Payable: 41,720.50
- Accrued Expenses: 8,820.07

**Equity**
- Retained Earnings: -35,797.24
- Owner's Equity: 58,941.13

**Totals:** Assets = 73,684.46; Liabilities = 50,540.57; Equity = 23,143.89
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
- [ ] Yes, doc_refs are correct
- [x] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes: Bank statement (D014, support_doc) cited in a few entries where only the posting doc should appear.

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [x] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [x] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Minor doc_ref mismatch, acceptable overall.
