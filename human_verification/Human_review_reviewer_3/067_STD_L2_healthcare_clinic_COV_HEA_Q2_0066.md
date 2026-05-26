# Verification Packet — COV_HEA_Q2_0066

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 2
- **Period type:** quarter
- **Period label:** Q4 FY 2024
- **Period start → end:** 2024-10-01 → 2024-12-31
- **Entity:** Cedar Operations
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-10-01_

**Assets**
- Cash: 48,576.60
- Accounts Receivable: 10,514.00
- Prepaid Insurance: 1,736.25
- Office Supplies: 2,176.61

**Liabilities**
- Accounts Payable: 5,280.86
- Accrued Expenses: 3,242.81

**Equity**
- Retained Earnings: 19,193.39
- Owner's Equity: 35,286.40


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-10-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $48,576.60
  - Section assets | Account Accounts Receivable | Amount $10,514.00
  - Section assets | Account Prepaid Insurance | Amount $1,736.25
  - Section assets | Account Office Supplies | Amount $2,176.61
  - Section liabilities | Account Accounts Payable | Amount $5,280.86
  - Section liabilities | Account Accrued Expenses | Amount $3,242.81
  - Section equity | Account Retained Earnings | Amount $19,193.39
  - Section equity | Account Owner's Equity | Amount $35,286.40

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-10-20

```
VENDOR INVOICE
==============

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Document Date: 2024-10-20

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: Q4 FY 2024

Terms
-----
Due Date: 2024-11-08

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-11-08
Total: $16,006.56

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount $5,137.94
  - Description Support fee | Amount $10,868.62

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D009 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-02

```
PATIENT INVOICE
===============

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Date: 2024-11-02

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D009
Document Type: patient_invoice
Period: Q4 FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0005
Patient: Marcus Lee
Payer: Unity Health Plan
Service Date: 2024-11-02
Gross Charge: $3,242.73
Patient Due: 506.59
Insurer Due: 2,736.14

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D007 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-10

```
PATIENT INVOICE
===============

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Document Date: 2024-11-10

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D007
Document Type: patient_invoice
Period: Q4 FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0003
Patient: Marcus Lee
Payer: NorthCover
Service Date: 2024-11-10
Gross Charge: $4,510.44
Patient Due: 701.00
Insurer Due: 3,809.44

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D006 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-14

```
PATIENT INVOICE
===============

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Date: 2024-11-14

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D006
Document Type: patient_invoice
Period: Q4 FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Noah Ferreira
Payer: CareSure
Service Date: 2024-11-14
Gross Charge: $3,315.66
Patient Due: 1,017.99
Insurer Due: 2,297.67

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-21

```
PATIENT INVOICE
===============

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Date: 2024-11-21

To
--
Ella Santos
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: Q4 FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Ella Santos
Payer: Unity Health Plan
Service Date: 2024-11-21
Gross Charge: $2,409.36
Patient Due: 727.19
Insurer Due: 1,682.17

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D008 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-29

```
PATIENT INVOICE
===============

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Date: 2024-11-29

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D008
Document Type: patient_invoice
Period: Q4 FY 2024

Invoice Summary
---------------
Invoice Number: PTINV-0004
Patient: Noah Ferreira
Payer: Unity Health Plan
Service Date: 2024-11-29
Gross Charge: $1,846.17
Patient Due: 514.00
Insurer Due: 1,332.17

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D005 — Insurer Remittance

- **Type:** `insurer_remittance`
- **Role:** `posting_doc`
- **Date:** 2024-12-11

```
INSURER REMITTANCE
==================

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Date: 2024-12-11

Reference Box
-------------
Document ID: D005
Document Type: insurer_remittance
Period: Q4 FY 2024

Remittance Summary
------------------
Remittance Number: REM-0001
Payer: Unity Health Plan
Claim Reference: PTINV-0001
Approved Amount: $1,682.17
Paid Amount: $1,682.17
Payment Date: 2024-12-11

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D004 — Copay Receipt

- **Type:** `copay_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-12-13

```
COPAY RECEIPT
=============

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Date: 2024-12-13

To
--
Ella Santos
Patient billing contact

Copay Receipt
-------------
Receipt Number: COPAY-0001
Patient: Ella Santos
Amount: $727.19
Reference Invoice: PTINV-0001
Payment Method: Card

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Cedar Operations
220 Lake View Road, Bengaluru
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: Q4 FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0066
Statement Currency: USD
Opening Balance: $48,576.60
Closing Balance: $50,985.96

Statement Rows
--------------
Rows:
  - Date 2024-12-11 | Description Insurer remittance PTINV-0001 | Amount $1,682.17 | Running
 Balance $50,258.77
  - Date 2024-12-13 | Description Copay receipt COPAY-0001 | Amount $727.19 | Running 
Balance $50,985.96

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 2,409.36 | D002 | 2024-11-21 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 16,006.56 | D003 | 2024-10-20 | clinic_supplies_bill |
| 3 | Cash | Accounts Receivable | 727.19 | D004, D002 | 2024-12-13 | copay_collection |
| 4 | Cash | Accounts Receivable | 1,682.17 | D005, D002 | 2024-12-11 | insurer_remittance |
| 5 | Accounts Receivable | Service Revenue | 3,315.66 | D006 | 2024-11-14 | patient_billing |
| 6 | Accounts Receivable | Service Revenue | 4,510.44 | D007 | 2024-11-10 | patient_billing |
| 7 | Accounts Receivable | Service Revenue | 1,846.17 | D008 | 2024-11-29 | patient_billing |
| 8 | Accounts Receivable | Service Revenue | 3,242.73 | D009 | 2024-11-02 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 50,985.96
- Accounts Receivable: 23,429.00
- Prepaid Insurance: 1,736.25
- Office Supplies: 2,176.61

**Liabilities**
- Accounts Payable: 21,287.42
- Accrued Expenses: 3,242.81

**Equity**
- Retained Earnings: 18,511.19
- Owner's Equity: 35,286.40

**Totals:** Assets = 78,327.82; Liabilities = 24,530.23; Equity = 53,797.59
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
- Notes: Fine as ground truth.
