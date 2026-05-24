# Verification Packet — COV_PRO_Y1_0010

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 1
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Pioneer Manufacturing
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `none`
- **Document count:** 11
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 99,353.34
- Accounts Receivable: 16,799.27

**Liabilities**
- Accounts Payable: 3,458.36

**Equity**
- Owner's Equity: 112,694.25


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
  - Section assets | Account Cash | Amount EUR 99.353,34
  - Section assets | Account Accounts Receivable | Amount EUR 16.799,27
  - Section liabilities | Account Accounts Payable | Amount EUR 3.458,36
  - Section equity | Account Owner's Equity | Amount EUR 112.694,25

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-23

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Pioneer Manufacturing
18 Marina Avenue, Chennai
Date: 23/04/2024

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0001

Terms
-----
Due Date: 03/05/2024

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 03/05/2024
Total: EUR 21.176,00

Line Items
----------
Items:
  - Description Implementation work | Amount EUR 4.602,44
  - Description Follow-up support | Amount EUR 16.573,56

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D010 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-04-23

```
CANCELLATION NOTE
=================

From
----
Pioneer Manufacturing
18 Marina Avenue, Chennai
Document Date: 23/04/2024

Reference Box
-------------
Document ID: D010
Document Type: cancellation_note
Period: FY 2024-25

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-05

```
CUSTOMER INVOICE
================

From
----
Pioneer Manufacturing
18 Marina Avenue, Chennai
Document Date: 05/05/2024

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0002

Terms
-----
Due Date: 25/05/2024

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 25/05/2024
Total: EUR 21.487,26

Line Items
----------
Items:
  - Description Support package | Amount EUR 8.076,84
  - Description Follow-up support | Amount EUR 13.410,42

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-18

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
18 Marina Avenue, Chennai
Date: 18/05/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2024-25

Terms
-----
Due Date: 28/05/2024

Supplier Header
---------------
Vendor: Meridian Support LLP
Expense Label: Office Supplies Expense
Currency: EUR

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 28/05/2024
Total: EUR 8.842,33

Bill Lines
----------
Lines:
  - Description Review pack | Amount EUR 2.688,07
  - Description Support fee | Amount EUR 6.154,26

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-19

```
CUSTOMER INVOICE
================

From
----
Pioneer Manufacturing
18 Marina Avenue, Chennai
Document Date: 19/06/2024

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0003

Terms
-----
Due Date: 10/07/2024

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0003
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 10/07/2024
Total: EUR 13.147,45

Line Items
----------
Items:
  - Description Monthly retainer | Amount EUR 5.134,40
  - Description Follow-up support | Amount EUR 8.013,05

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
```

### Document D006 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-10-16

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Oakline Services
Total: EUR 577,86
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount EUR 196,84
  - Description Travel Incidentals | Amount EUR 381,02
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-10-30

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Vertex Supply Co.
Total: EUR 860,51
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount EUR 361,74
  - Description Travel Incidentals | Amount EUR 498,77
```

### Document D007 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-11-12

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0003
Merchant: Golden State Finance
Total: EUR 3,16
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount EUR 1,15
  - Description Travel Incidentals | Amount EUR 2,01
```

### Document D009 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Pioneer Manufacturing
18 Marina Avenue, Chennai
Date: 31/03/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Meridian Support LLP
Closing Balance: EUR 8.842,33

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount EUR 8.842,33 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D011 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Pioneer Manufacturing
18 Marina Avenue, Chennai
Date: 31/03/2025

Reference Box
-------------
Document ID: D011
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0010
Statement Currency: EUR
Opening Balance: EUR 99.353,34
Closing Balance: EUR 97.911,81

Statement Rows
--------------
Rows:
  - Date 16/10/2024 | Description Oakline Services receipt RCPT-0002 | Amount EUR -577,86 | 
Running Balance EUR 98.775,48
  - Date 30/10/2024 | Description Vertex Supply Co. receipt RCPT-0001 | Amount EUR -860,51 |
 Running Balance EUR 97.914,97
  - Date 12/11/2024 | Description Golden State Finance receipt RCPT-0003 | Amount EUR -3,16 
| Running Balance EUR 97.911,81

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D011
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 21,176.00 | D002 | 2024-04-23 | service_invoice |
| 2 | Office Supplies Expense | Accounts Payable | 8,842.33 | D003 | 2024-05-18 | vendor_bill |
| 3 | Travel Expense | Cash | 860.51 | D004 | 2024-10-30 | expense_receipt |
| 4 | Accounts Receivable | Service Revenue | 21,487.26 | D005 | 2024-05-05 | service_invoice |
| 5 | Travel Expense | Cash | 577.86 | D006 | 2024-10-16 | expense_receipt |
| 6 | Travel Expense | Cash | 3.16 | D007 | 2024-11-12 | expense_receipt |
| 7 | Accounts Receivable | Service Revenue | 13,147.45 | D008 | 2024-06-19 | service_invoice |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 97,911.81
- Accounts Receivable: 72,609.98

**Liabilities**
- Accounts Payable: 12,300.69

**Equity**
- Owner's Equity: 112,694.25
- Retained Earnings: 45,526.85

**Totals:** Assets = 170,521.79; Liabilities = 12,300.69; Equity = 158,221.10
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [x] Mostly — captures the right information, with rough edges
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
- Notes:
