# Verification Packet — COV_HEA_M1_0060

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `healthcare_clinic`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** March 2025
- **Period start → end:** 2025-03-01 → 2025-03-31
- **Entity:** Pioneer Retail Group
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 5
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Office Supplies Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-03-01_

**Assets**
- Cash: 36,015.09
- Accounts Receivable: 7,090.65

**Liabilities**
- Accounts Payable: 4,286.87

**Equity**
- Owner's Equity: 38,818.87


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-03-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-03-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $36,015.09
  - Section assets | Account Accounts Receivable | Amount $7,090.65
  - Section liabilities | Account Accounts Payable | Amount $4,286.87
  - Section equity | Account Owner's Equity | Amount $38,818.87

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-02

```
VENDOR INVOICE
==============

From
----
Pioneer Retail Group
75 Market Road, Mumbai
Date: 2025-03-02

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: March 2025

Terms
-----
Due Date: 2025-03-20

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-03-20
Total: $1,682.26

Bill Lines
----------
Lines:
  - Description Support package | Amount $522.23
  - Description Support fee | Amount $1,160.03

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D002 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-12

```
PATIENT INVOICE
===============

From
----
Pioneer Retail Group
75 Market Road, Mumbai
Document Date: 2025-03-12

To
--
Noah Ferreira
Patient billing contact

Reference Box
-------------
Document ID: D002
Document Type: patient_invoice
Period: March 2025

Invoice Summary
---------------
Invoice Number: PTINV-0001
Patient: Noah Ferreira
Payer: Harbor Health Network
Service Date: 2025-03-12
Gross Charge: $1,075.64
Patient Due: 188.89
Insurer Due: 886.75

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D004 — Patient Invoice

- **Type:** `patient_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-21

```
PATIENT INVOICE
===============

From
----
Pioneer Retail Group
75 Market Road, Mumbai
Date: 2025-03-21

To
--
Marcus Lee
Patient billing contact

Reference Box
-------------
Document ID: D004
Document Type: patient_invoice
Period: March 2025

Invoice Summary
---------------
Invoice Number: PTINV-0002
Patient: Marcus Lee
Payer: Harbor Health Network
Service Date: 2025-03-21
Gross Charge: $2,069.17
Patient Due: 571.16
Insurer Due: 1,498.01

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D005 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Pioneer Retail Group
75 Market Road, Mumbai
Date: 2025-03-31

Reference Box
-------------
Document ID: D005
Document Type: bank_statement
Period: March 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0060
Statement Currency: USD
Opening Balance: $36,015.09
Closing Balance: $36,015.09

Statement Rows
--------------
Rows: None

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D005
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 1,075.64 | D002 | 2025-03-12 | patient_billing |
| 2 | Office Supplies Expense | Accounts Payable | 1,682.26 | D003 | 2025-03-02 | clinic_supplies_bill |
| 3 | Accounts Receivable | Service Revenue | 2,069.17 | D004 | 2025-03-21 | patient_billing |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 36,015.09
- Accounts Receivable: 10,235.46

**Liabilities**
- Accounts Payable: 5,969.13

**Equity**
- Owner's Equity: 38,818.87
- Retained Earnings: 1,462.55

**Totals:** Assets = 46,250.55; Liabilities = 5,969.13; Equity = 40,281.42
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
