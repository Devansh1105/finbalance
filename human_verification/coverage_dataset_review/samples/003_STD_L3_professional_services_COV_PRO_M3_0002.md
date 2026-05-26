# Verification Packet — COV_PRO_M3_0002

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 3
- **Period type:** month
- **Period label:** March 2024
- **Period start → end:** 2024-03-01 → 2024-03-31
- **Entity:** Beacon Distribution
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-03-01_

**Assets**
- Cash: 20,799.61
- Accounts Receivable: 2,583.45
- Prepaid Rent: 3,175.83
- Office Supplies: 791.95

**Liabilities**
- Accounts Payable: 2,766.54
- Accrued Expenses: 525.04

**Equity**
- Retained Earnings: 7,631.54
- Owner's Equity: 16,427.72


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-03-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/03/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 20,799.61
  - Section assets | Account Accounts Receivable | Amount GBP 2,583.45
  - Section assets | Account Prepaid Rent | Amount GBP 3,175.83
  - Section assets | Account Office Supplies | Amount GBP 791.95
  - Section liabilities | Account Accounts Payable | Amount GBP 2,766.54
  - Section liabilities | Account Accrued Expenses | Amount GBP 525.04
  - Section equity | Account Retained Earnings | Amount GBP 7,631.54
  - Section equity | Account Owner's Equity | Amount GBP 16,427.72

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Rent Notice

- **Type:** `rent_notice`
- **Role:** `posting_doc`
- **Date:** 2024-03-02

```
RENT NOTICE
===========

Rent Notice
-----------
Notice Number: PRE-0001
Vendor: Beacon Industrial Supply
Property: Park Lane Residences
Service Start: 02/03/2024
Service End: 01/06/2024
Total: GBP 4,479.97
Monthly Amount: GBP 1,493.32

Notes
-----
Rent paid in advance and tracked for later release.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-03

```
CUSTOMER INVOICE
================

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 03/03/2024

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: March 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 14/03/2024

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 14/03/2024
Subtotal: GBP 9,127.68
Tax Label: VAT
Tax Rate: 12.50%
Tax Amount: GBP 1,140.96
Total: GBP 10,268.64

Line Items
----------
Items:
  - Description Consulting sprint | Amount GBP 1,905.41
  - Description Follow-up support | Amount GBP 7,222.27

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-09

```
VENDOR INVOICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 09/03/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: March 2024

Terms
-----
Due Date: 19/03/2024

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 19/03/2024
Subtotal: GBP 1,563.07
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 156.31
Total: GBP 1,719.38

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount GBP 604.56
  - Description Support fee | Amount GBP 958.51

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-03-20

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Pace Office Mart
Total: GBP 217.78
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount GBP 81.38
  - Description Travel Incidentals | Amount GBP 136.40
```

### Document D007 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-03-23

```
PAYROLL SUMMARY
===============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Document Date: 23/03/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: March 2024
Headcount: 6
Gross Pay: GBP 7,253.49
Employer Tax: 929.30
Cash Outflow: GBP 8,182.79

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-03-26

```
PAYMENT ADVICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 26/03/2024

To
--
Riverfront Group

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: March 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: GBP 10,268.64
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-03-28

```
PAYMENT ADVICE
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 28/03/2024

To
--
Oakline Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: March 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: GBP 1,719.38
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 31/03/2024

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: March 2024
Reference: PRE-0001

Approval / Context
------------------
Subject: Rent release

Memo Summary
------------
Memo ID: MEMO-0001
Subject: Rent release
Reference: PRE-0001
Recognized Amount: GBP 1,493.32

Explanation
-----------
Narrative: One month of rent has expired and should be expensed this period.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-03-31

```
BANK STATEMENT
==============

From
----
Beacon Distribution
18 Marina Avenue, Chennai
Date: 31/03/2024

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: March 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0002
Statement Currency: GBP
Opening Balance: GBP 20,799.61
Closing Balance: GBP 16,468.33

Statement Rows
--------------
Rows:
  - Date 02/03/2024 | Description Rent prepayment PRE-0001 | Amount GBP -4,479.97 | Running 
Balance GBP 16,319.64
  - Date 20/03/2024 | Description Pace Office Mart receipt RCPT-0001 | Amount GBP -217.78 | 
Running Balance GBP 16,101.86
  - Date 23/03/2024 | Description Payroll PAYRUN-0001 | Amount GBP -8,182.79 | Running 
Balance GBP 7,919.07
  - Date 26/03/2024 | Description Customer settlement INV-0001 | Amount GBP 10,268.64 | 
Running Balance GBP 18,187.71
  - Date 28/03/2024 | Description Supplier settlement BILL-0001 | Amount GBP -1,719.38 | 
Running Balance GBP 16,468.33

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D010
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 9,127.68 | D002 | 2024-03-03 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 1,140.96 | D002 | 2024-03-03 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 1,563.07 | D003 | 2024-03-09 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 156.31 | D003 | 2024-03-09 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 217.78 | D004 | 2024-03-20 | expense_receipt |
| 6 | Cash | Accounts Receivable | 10,268.64 | D005, D002 | 2024-03-26 | customer_payment |
| 7 | Accounts Payable | Cash | 1,719.38 | D006, D003 | 2024-03-28 | supplier_payment |
| 8 | Salaries Expense | Cash | 7,253.49 | D007 | 2024-03-23 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 929.30 | D007 | 2024-03-23 | payroll_tax |
| 10 | Prepaid Rent | Cash | 4,479.97 | D008 | 2024-03-02 | prepaid_rent_purchase |
| 11 | Rent Expense | Prepaid Rent | 1,493.32 | D008, D009 | 2024-03-31 | prepaid_rent_release |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 16,468.33
- Accounts Receivable: 2,583.45
- Prepaid Rent: 6,162.48
- Office Supplies: 791.95
- Input Tax Receivable: 156.31

**Liabilities**
- Accounts Payable: 2,766.54
- Accrued Expenses: 525.04
- Sales Tax Payable: 1,140.96

**Equity**
- Retained Earnings: 5,302.26
- Owner's Equity: 16,427.72

**Totals:** Assets = 26,162.52; Liabilities = 4,432.54; Equity = 21,729.98
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
