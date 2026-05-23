# Verification Packet — COV_HEA_Q1_0065

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 1
- **Period type:** quarter
- **Period label:** Q4 FY 2025
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Cedar Retail Group
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `none`
- **Document count:** 7
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 60,913.67
- Accounts Receivable: 8,485.11

**Liabilities**
- Accounts Payable: 6,566.95

**Equity**
- Owner's Equity: 62,831.83


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
Statement Date: 01/10/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 60,913.67
  - Section assets | Account Accounts Receivable | Amount GBP 8,485.11
  - Section liabilities | Account Accounts Payable | Amount GBP 6,566.95
  - Section equity | Account Owner's Equity | Amount GBP 62,831.83

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-09

```
VENDOR INVOICE
==============

From
----
Cedar Retail Group
75 Market Road, Mumbai
Document Date: 09/10/2025

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q4 FY 2025

Terms
-----
Due Date: 20/10/2025

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 20/10/2025
Total: GBP 6,137.13

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount GBP 2,694.19
  - Description Support fee | Amount GBP 3,442.94

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-08

```
PATIENT INVOICE
===============

From
----
Cedar Retail Group
75 Market Road, Mumbai
Document Date: 08/11/2025

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D004
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Noah Ferreira
Payer: NorthCover
Service Date: 08/11/2025
Gross Charge: GBP 1,557.25
Patient Due: 318.60
Insurer Due: 1,238.65

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-11

```
PATIENT INVOICE
===============

From
----
Cedar Retail Group
75 Market Road, Mumbai
Document Date: 11/11/2025

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
Payer: Unity Health Plan
Service Date: 11/11/2025
Gross Charge: GBP 6,058.69
Patient Due: 1,798.86
Insurer Due: 4,259.83

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D006 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-17

```
PATIENT INVOICE
===============

From
----
Cedar Retail Group
75 Market Road, Mumbai
Document Date: 17/11/2025

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D006
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Ella Santos
Payer: CareSure
Service Date: 17/11/2025
Gross Charge: GBP 5,630.58
Patient Due: 1,669.37
Insurer Due: 3,961.21

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D005 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-26

```
PATIENT INVOICE
===============

From
----
Cedar Retail Group
75 Market Road, Mumbai
Date: 26/11/2025

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D005
Document Type: patient_invoice
Period: Q4 FY 2025

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Marcus Lee
Payer: CareSure
Service Date: 26/11/2025
Gross Charge: GBP 4,390.34
Patient Due: 1,009.82
Insurer Due: 3,380.52

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D007 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Cedar Retail Group
75 Market Road, Mumbai
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D007
Document Type: bank_statement
Period: Q4 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0065
Statement Currency: GBP
Opening Balance: GBP 60,913.67
Closing Balance: GBP 60,913.67

Statement Rows
--------------
Rows: None

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 6,058.69 | D002 | 2025-11-11 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 6,137.13 | D003 | 2025-10-09 | clinic_supplies_bill |
| 3 | Accounts Receivable | Service Revenue | 1,557.25 | D004 | 2025-11-08 | patient_billing |
| 4 | Accounts Receivable | Service Revenue | 4,390.34 | D005 | 2025-11-26 | patient_billing |
| 5 | Accounts Receivable | Service Revenue | 5,630.58 | D006 | 2025-11-17 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 60,913.67
- Accounts Receivable: 26,121.97

**Liabilities**
- Accounts Payable: 12,704.08

**Equity**
- Owner's Equity: 62,831.83
- Retained Earnings: 11,499.73

**Totals:** Assets = 87,035.64; Liabilities = 12,704.08; Equity = 74,331.56
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
- Notes: Reviewed, no material concerns.
