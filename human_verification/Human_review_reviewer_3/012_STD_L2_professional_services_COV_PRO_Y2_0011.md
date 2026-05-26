# Verification Packet — COV_PRO_Y2_0011

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 2
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Pioneer Manufacturing
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 16
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 79,506.38
- Accounts Receivable: 17,724.92
- Prepaid Rent: 8,657.97
- Prepaid Insurance: 2,066.61
- Office Supplies: 1,025.48

**Liabilities**
- Accounts Payable: 4,176.14
- Accrued Expenses: 1,691.53

**Equity**
- Retained Earnings: 24,571.49
- Owner's Equity: 78,542.20


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
  - Section assets | Account Cash | Amount GBP 79,506.38
  - Section assets | Account Accounts Receivable | Amount GBP 17,724.92
  - Section assets | Account Prepaid Rent | Amount GBP 8,657.97
  - Section assets | Account Prepaid Insurance | Amount GBP 2,066.61
  - Section assets | Account Office Supplies | Amount GBP 1,025.48
  - Section liabilities | Account Accounts Payable | Amount GBP 4,176.14
  - Section liabilities | Account Accrued Expenses | Amount GBP 1,691.53
  - Section equity | Account Retained Earnings | Amount GBP 24,571.49
  - Section equity | Account Owner's Equity | Amount GBP 78,542.20

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-07

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Document Date: 07/02/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: FY 2025

Terms
-----
Due Date: 22/02/2025

Supplier Header
---------------
Vendor: Beacon Industrial Supply
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 22/02/2025
Subtotal: GBP 3,728.61
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 671.15
Total: GBP 4,399.76

Bill Lines
----------
Lines:
  - Description Review pack | Amount GBP 961.19
  - Description Support fee | Amount GBP 2,767.42

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D011 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-13

```
VENDOR INVOICE
==============

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Document Date: 13/02/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: vendor_invoice
Period: FY 2025

Terms
-----
Due Date: 01/03/2025

Supplier Header
---------------
Vendor: Golden State Finance
Expense Label: Office Supplies Expense
Currency: GBP

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 01/03/2025
Subtotal: GBP 10,585.24
Tax Label: India GST
Tax Rate: 5.00%
Tax Amount: GBP 529.26
Total: GBP 11,114.50

Bill Lines
----------
Lines:
  - Description Review pack | Amount GBP 2,291.75
  - Description Support fee | Amount GBP 8,293.49

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D007 — Retainer Agreement Memo

- **Type:** `retainer_agreement_memo`
- **Role:** `support_doc`
- **Date:** 2025-02-20

```
RETAINER AGREEMENT MEMO
=======================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 20/02/2025

Reference Box
-------------
Document ID: D007
Document Type: retainer_agreement_memo
Period: FY 2025
Reference: RET-CTR-0001

Approval / Context
------------------
Subject: Retainer engagement

Memo Summary
------------
Memo ID: RET-0001
Subject: Retainer engagement
Reference: RET-CTR-0001
Contract Months: 12
Total Contract Value: GBP 37,008.87

Explanation
-----------
Narrative: Customer Metro Edge Partners agreed to a service package spanning 12 months.

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-20

```
CUSTOMER INVOICE
================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 20/02/2025

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D008
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 01/03/2025

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0002
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 01/03/2025
Subtotal: GBP 33,043.63
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 3,965.24
CGST Amount: GBP 1,982.62
SGST Amount: GBP 1,982.62
Total: GBP 37,008.87

Line Items
----------
Items:
  - Description Business Suite | Amount GBP 8,253.95
  - Description Service coverage under contract | Amount GBP 24,789.68

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D014 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-02-20

```
CANCELLATION NOTE
=================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 20/02/2025

Reference Box
-------------
Document ID: D014
Document Type: cancellation_note
Period: FY 2025

Cancellation Summary
--------------------
Note Number: CNCL-0002
Withdrawn Reference: INV-0002-OLD
Replacement Reference: INV-0002

Background
----------
Narrative: INV-0002-OLD is withdrawn and must not be posted. Use INV-0002 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-02

```
CUSTOMER INVOICE / REFERENCE COPY
=================================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 02/03/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 24/03/2025

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 24/03/2025
Subtotal: GBP 15,293.36
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 1,835.20
CGST Amount: GBP 917.60
SGST Amount: GBP 917.60
Total: GBP 17,128.56

Line Items
----------
Items:
  - Description Support package | Amount GBP 4,636.16
  - Description Follow-up support | Amount GBP 10,657.20

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D009 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-11

```
CUSTOMER INVOICE
================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 11/04/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D009
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0003

Terms
-----
Due Date: 28/04/2025

Parties
-------
Customer: Riverfront Group
Contract Ref: CTR-0003
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 28/04/2025
Subtotal: GBP 33,041.53
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 3,964.98
CGST Amount: GBP 1,982.49
SGST Amount: GBP 1,982.49
Total: GBP 37,006.51

Line Items
----------
Items:
  - Description Implementation work | Amount GBP 10,929.35
  - Description Follow-up support | Amount GBP 22,112.18

Footer
------
Internal document packet copy.
Page marker: D009
```

### Document D012 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-04-12

```
CUSTOMER INVOICE
================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Document Date: 12/04/2025

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D012
Document Type: customer_invoice
Period: FY 2025
Contract Ref: CTR-0004

Terms
-----
Due Date: 29/04/2025

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0004
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0004
Due Date: 29/04/2025
Subtotal: GBP 17,957.39
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 2,154.89
CGST Amount: GBP 1,077.44
SGST Amount: GBP 1,077.45
Total: GBP 20,112.28

Line Items
----------
Items:
  - Description Support package | Amount GBP 4,658.55
  - Description Follow-up support | Amount GBP 13,298.84

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D013 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2025-04-12

```
CANCELLATION NOTE
=================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Document Date: 12/04/2025

Reference Box
-------------
Document ID: D013
Document Type: cancellation_note
Period: FY 2025

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0004-OLD
Replacement Reference: INV-0004

Background
----------
Narrative: INV-0004-OLD is withdrawn and must not be posted. Use INV-0004 as the only valid 
invoice.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-06-24

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: GBP 40.56
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount GBP 9.08
  - Description Travel Incidentals | Amount GBP 31.48
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-05

```
PAYMENT ADVICE
==============

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 05/11/2025

To
--
Riverfront Group

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: GBP 17,128.56
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
- **Date:** 2025-11-14

```
PAYMENT ADVICE
==============

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Document Date: 14/11/2025

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: GBP 4,399.76
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D010 — Revenue Recognition Schedule

- **Type:** `revenue_recognition_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
REVENUE RECOGNITION SCHEDULE / REFERENCE COPY
=============================================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D010
Document Type: revenue_recognition_schedule
Period: FY 2025

Recognition Summary
-------------------
Schedule ID: REVREC-0001
Contract Reference: INV-0002
Period: FY 2025
Opening Deferred: GBP 33,043.63
Added Deferred: GBP 0.00
Released This Period: 33,043.63
Ending Deferred: GBP 0.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D015 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 31/12/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: vendor_statement
Period: FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Golden State Finance
Closing Balance: GBP 11,114.50

Statement Lines
---------------
Lines:
  - Reference BILL-0002 | Document Type Open invoice | Amount GBP 11,114.50 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D016 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Pioneer Manufacturing
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D016
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0011
Statement Currency: GBP
Opening Balance: GBP 79,506.38
Closing Balance: GBP 92,194.62

Statement Rows
--------------
Rows:
  - Date 24/06/2025 | Description Oakline Services receipt RCPT-0001 | Amount GBP -40.56 | 
Running Balance GBP 79,465.82
  - Date 05/11/2025 | Description Customer settlement INV-0001 | Amount GBP 17,128.56 | 
Running Balance GBP 96,594.38
  - Date 14/11/2025 | Description Supplier settlement BILL-0001 | Amount GBP -4,399.76 | 
Running Balance GBP 92,194.62

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D016
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 15,293.36 | D002 | 2025-03-02 | service_invoice |
| 2 | Accounts Receivable | CGST Payable | 917.60 | D002 | 2025-03-02 | service_invoice_tax_cgst |
| 3 | Accounts Receivable | SGST Payable | 917.60 | D002 | 2025-03-02 | service_invoice_tax_sgst |
| 4 | Office Supplies Expense | Accounts Payable | 3,728.61 | D003 | 2025-02-07 | vendor_bill |
| 5 | Input CGST Receivable | Accounts Payable | 335.57 | D003 | 2025-02-07 | vendor_bill_tax_cgst |
| 6 | Input SGST Receivable | Accounts Payable | 335.58 | D003 | 2025-02-07 | vendor_bill_tax_sgst |
| 7 | Travel Expense | Cash | 40.56 | D004 | 2025-06-24 | expense_receipt |
| 8 | Cash | Accounts Receivable | 17,128.56 | D005, D002 | 2025-11-05 | customer_payment |
| 9 | Accounts Payable | Cash | 4,399.76 | D006, D003 | 2025-11-14 | supplier_payment |
| 10 | Accounts Receivable | Unearned Revenue | 33,043.63 | D007, D008 | 2025-02-20 | retainer_invoice |
| 11 | Accounts Receivable | CGST Payable | 1,982.62 | D007, D008 | 2025-02-20 | retainer_invoice_tax_cgst |
| 12 | Accounts Receivable | SGST Payable | 1,982.62 | D007, D008 | 2025-02-20 | retainer_invoice_tax_sgst |
| 13 | Accounts Receivable | Service Revenue | 33,041.53 | D009 | 2025-04-11 | service_invoice |
| 14 | Accounts Receivable | CGST Payable | 1,982.49 | D009 | 2025-04-11 | service_invoice_tax_cgst |
| 15 | Accounts Receivable | SGST Payable | 1,982.49 | D009 | 2025-04-11 | service_invoice_tax_sgst |
| 16 | Unearned Revenue | Service Revenue | 33,043.63 | D010, D008 | 2025-12-31 | retainer_release |
| 17 | Office Supplies Expense | Accounts Payable | 10,585.24 | D011 | 2025-02-13 | vendor_bill |
| 18 | Input CGST Receivable | Accounts Payable | 264.63 | D011 | 2025-02-13 | vendor_bill_tax_cgst |
| 19 | Input SGST Receivable | Accounts Payable | 264.63 | D011 | 2025-02-13 | vendor_bill_tax_sgst |
| 20 | Accounts Receivable | Service Revenue | 17,957.39 | D012 | 2025-04-12 | service_invoice |
| 21 | Accounts Receivable | CGST Payable | 1,077.44 | D012 | 2025-04-12 | service_invoice_tax_cgst |
| 22 | Accounts Receivable | SGST Payable | 1,077.45 | D012 | 2025-04-12 | service_invoice_tax_sgst |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 92,194.62
- Accounts Receivable: 111,852.58
- Prepaid Rent: 8,657.97
- Prepaid Insurance: 2,066.61
- Office Supplies: 1,025.48
- Input CGST Receivable: 600.20
- Input SGST Receivable: 600.21

**Liabilities**
- Accounts Payable: 15,290.64
- Accrued Expenses: 1,691.53
- CGST Payable: 5,960.15
- SGST Payable: 5,960.16

**Equity**
- Retained Earnings: 109,552.99
- Owner's Equity: 78,542.20

**Totals:** Assets = 216,997.67; Liabilities = 28,902.48; Equity = 188,095.19
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [x] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes: Date formats hop between styles across the docs. Cosmetic.

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
