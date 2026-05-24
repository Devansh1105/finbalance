# Verification Packet — COV_FIE_Q1_0020

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 1
- **Period type:** quarter
- **Period label:** Q2 FY 2024
- **Period start → end:** 2024-04-01 → 2024-06-30
- **Entity:** Willow Clinic
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `none`
- **Document count:** 9
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 38,286.82
- Accounts Receivable: 5,081.01

**Liabilities**
- Accounts Payable: 6,400.19

**Equity**
- Owner's Equity: 36,967.64


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/04/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 38,286.82
  - Section assets | Account Accounts Receivable | Amount GBP 5,081.01
  - Section liabilities | Account Accounts Payable | Amount GBP 6,400.19
  - Section equity | Account Owner's Equity | Amount GBP 36,967.64

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D006 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-04-12

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0002
Customer: Metro Edge Partners
Job Site: North Yard
Scope: Support package
Approved Amount: GBP 7,848.33

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-13

```
CUSTOMER INVOICE
================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Date: 13/04/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: Q2 FY 2024
Contract Ref: CTR-0002
Job Code: JOB-0002

Terms
-----
Due Date: 02/05/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 02/05/2024
Total: GBP 7,848.33

Line Items
----------
Items:
  - Description Support package | Amount GBP 1,961.89
  - Description Follow-up support | Amount GBP 5,886.44

Field Job
---------
Job Code: JOB-0002

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-04-13

```
CANCELLATION NOTE
=================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Document Date: 13/04/2024

Reference Box
-------------
Document ID: D008
Document Type: cancellation_note
Period: Q2 FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0002-OLD
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0002-OLD is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-15

```
SUPPLIER INVOICE
================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Date: 15/04/2024

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: Q2 FY 2024

Terms
-----
Due Date: 30/04/2024

Supplier Header
---------------
Supplier: Golden State Finance
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 30/04/2024
Total: GBP 7,156.19

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 14 | Unit Cost GBP 104.70 | 
Amount GBP 1,465.87
  - Description Preventive maintenance service parts | Quantity 11 | Unit Cost GBP 517.30 | 
Amount GBP 5,690.32

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-04-19

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Maple Ridge Trading
Job Site: Riverbank Plaza
Scope: Support package
Approved Amount: GBP 13,823.60

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-20

```
CUSTOMER INVOICE
================

From
----
Willow Clinic
18 Marina Avenue, Chennai
Date: 20/04/2024

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q2 FY 2024
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 10/05/2024

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 10/05/2024
Total: GBP 13,823.60

Line Items
----------
Items:
  - Description Implementation work | Amount GBP 5,154.71
  - Description Follow-up support | Amount GBP 8,668.89

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-04-29

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Prime Utility Desk
Total: GBP 429.74
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 111.34
  - Description Fuel Incidentals | Amount GBP 318.40
```

### Document D009 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-06-30

```
BANK STATEMENT
==============

From
----
Willow Clinic
18 Marina Avenue, Chennai
Date: 30/06/2024

Reference Box
-------------
Document ID: D009
Document Type: bank_statement
Period: Q2 FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0020
Statement Currency: GBP
Opening Balance: GBP 38,286.82
Closing Balance: GBP 37,857.08

Statement Rows
--------------
Rows:
  - Date 29/04/2024 | Description Prime Utility Desk receipt RCPT-0001 | Amount GBP -429.74 
| Running Balance GBP 37,857.08

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D009
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 13,823.60 | D002, D003 | 2024-04-20 | job_invoice |
| 2 | Repairs Expense | Accounts Payable | 7,156.19 | D004 | 2024-04-15 | supplier_bill |
| 3 | Fuel Expense | Cash | 429.74 | D005 | 2024-04-29 | fuel_receipt |
| 4 | Accounts Receivable | Service Revenue | 7,848.33 | D006, D007 | 2024-04-13 | job_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 37,857.08
- Accounts Receivable: 26,752.94

**Liabilities**
- Accounts Payable: 13,556.38

**Equity**
- Owner's Equity: 36,967.64
- Retained Earnings: 14,086.00

**Totals:** Assets = 64,610.02; Liabilities = 13,556.38; Equity = 51,053.64
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [] Yes — analogous to what an accountant would receive
- [x] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [x] Yes — entries match what I would book
- [] Mostly — minor account / amount issues (please describe)
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
