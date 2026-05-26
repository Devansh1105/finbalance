# Verification Packet — COV_PRO_M2_0001

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** December 2025
- **Period start → end:** 2025-12-01 → 2025-12-31
- **Entity:** Northwind Manufacturing
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 9
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-12-01_

**Assets**
- Cash: 37,030.83
- Accounts Receivable: 4,291.36
- Prepaid Rent: 1,894.49
- Office Supplies: 1,407.98

**Liabilities**
- Accounts Payable: 2,939.36
- Accrued Expenses: 699.52

**Equity**
- Retained Earnings: 9,417.94
- Owner's Equity: 31,567.84


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-12-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/12/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 37.030,83
  - Section assets | Account Accounts Receivable | Amount EUR 4.291,36
  - Section assets | Account Prepaid Rent | Amount EUR 1.894,49
  - Section assets | Account Office Supplies | Amount EUR 1.407,98
  - Section liabilities | Account Accounts Payable | Amount EUR 2.939,36
  - Section liabilities | Account Accrued Expenses | Amount EUR 699,52
  - Section equity | Account Retained Earnings | Amount EUR 9.417,94
  - Section equity | Account Owner's Equity | Amount EUR 31.567,84

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D008 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-01

```
MEMO
====

From
----
Northwind Manufacturing
18 Marina Avenue, Chennai
Document Date: 01/12/2025

Reference Box
-------------
Document ID: D008
Document Type: memo
Period: December 2025

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0001
Subject: Document retention reminder
Audience: Finance Team

Memo Body
---------
Narrative: Follow the internal document-retention checklist before the binder is archived.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-12-04

```
CUSTOMER INVOICE
================

From
----
Northwind Manufacturing
18 Marina Avenue, Chennai
Date: 04/12/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: December 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 27/12/2025

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 27/12/2025
Subtotal: EUR 2.827,94
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: EUR 268,65
Total: EUR 3.096,59

Line Items
----------
Items:
  - Description Review pack | Amount EUR 656,58
  - Description Follow-up support | Amount EUR 2.171,36

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-12-06

```
VENDOR INVOICE
==============

From
----
Northwind Manufacturing
18 Marina Avenue, Chennai
Date: 06/12/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: December 2025

Terms
-----
Due Date: 16/12/2025

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 16/12/2025
Subtotal: EUR 1.325,56
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 96,10
Total: EUR 1.421,66

Bill Lines
----------
Lines:
  - Description Monthly retainer | Amount EUR 281,32
  - Description Support fee | Amount EUR 1.044,24

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-12-07

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Northwind Manufacturing
18 Marina Avenue, Chennai
Date: 07/12/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: December 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 28/12/2025

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 28/12/2025
Subtotal: EUR 5.184,91
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 259,25
Total: EUR 5.444,16

Line Items
----------
Items:
  - Description Review pack | Amount EUR 1.253,22
  - Description Follow-up support | Amount EUR 3.931,69

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-12-12

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Prime Utility Desk
Total: EUR 36,95
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount EUR 13,15
  - Description Travel Incidentals | Amount EUR 23,80
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-21

```
PAYMENT ADVICE
==============

From
----
Northwind Manufacturing
18 Marina Avenue, Chennai
Date: 21/12/2025

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: December 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: EUR 3.096,59
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-28

```
PAYMENT ADVICE
==============

From
----
Northwind Manufacturing
18 Marina Avenue, Chennai
Date: 28/12/2025

To
--
Golden State Finance

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: December 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: EUR 1.421,66
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D009 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Northwind Manufacturing
18 Marina Avenue, Chennai
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D009
Document Type: bank_statement
Period: December 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0001
Statement Currency: EUR
Opening Balance: EUR 37.030,83
Closing Balance: EUR 38.668,81

Statement Rows
--------------
Rows:
  - Date 12/12/2025 | Description Prime Utility Desk receipt RCPT-0001 | Amount EUR -36,95 |
 Running Balance EUR 36.993,88
  - Date 21/12/2025 | Description Customer settlement INV-0001 | Amount EUR 3.096,59 | 
Running Balance EUR 40.090,47
  - Date 28/12/2025 | Description Supplier settlement BILL-0001 | Amount EUR -1.421,66 | 
Running Balance EUR 38.668,81

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 2,827.94 | D002 | 2025-12-04 | service_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 268.65 | D002 | 2025-12-04 | service_invoice_tax |
| 3 | Office Supplies Expense | Accounts Payable | 1,325.56 | D003 | 2025-12-06 | vendor_bill |
| 4 | Input Tax Receivable | Accounts Payable | 96.10 | D003 | 2025-12-06 | vendor_bill_tax |
| 5 | Travel Expense | Cash | 36.95 | D004 | 2025-12-12 | expense_receipt |
| 6 | Cash | Accounts Receivable | 3,096.59 | D005, D002 | 2025-12-21 | customer_payment |
| 7 | Accounts Payable | Cash | 1,421.66 | D006, D003 | 2025-12-28 | supplier_payment |
| 8 | Accounts Receivable | Service Revenue | 5,184.91 | D007 | 2025-12-07 | service_invoice |
| 9 | Accounts Receivable | Sales Tax Payable | 259.25 | D007 | 2025-12-07 | service_invoice_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 38,668.81
- Accounts Receivable: 9,735.52
- Prepaid Rent: 1,894.49
- Office Supplies: 1,407.98
- Input Tax Receivable: 96.10

**Liabilities**
- Accounts Payable: 2,939.36
- Accrued Expenses: 699.52
- Sales Tax Payable: 527.90

**Equity**
- Retained Earnings: 16,068.28
- Owner's Equity: 31,567.84

**Totals:** Assets = 51,802.90; Liabilities = 4,166.78; Equity = 47,636.12
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
- Notes: Ties out, accept.
