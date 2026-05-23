# Verification Packet — COV_NEG_00_INVOICE_TOTAL_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** June 2024
- **Period start → end:** 2024-06-01 → 2024-06-30
- **Entity:** Cedar Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `vat`
- **Document count:** 9
- **Labeled as inconsistent:** True
- **Inconsistency codes:** invoice_total_mismatch
- **Inconsistency reasons:** Invoice total does not match the visible line items.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2024-06-01_

**Assets**
- Cash: 36,224.01
- Accounts Receivable: 2,656.99
- Prepaid Rent: 2,596.49
- Office Supplies: 664.83

**Liabilities**
- Accounts Payable: 1,865.23
- Accrued Expenses: 1,843.20

**Equity**
- Retained Earnings: 10,494.61
- Owner's Equity: 27,939.28


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-06-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-06-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $36,224.01
  - Section assets | Account Accounts Receivable | Amount $2,656.99
  - Section assets | Account Prepaid Rent | Amount $2,596.49
  - Section assets | Account Office Supplies | Amount $664.83
  - Section liabilities | Account Accounts Payable | Amount $1,865.23
  - Section liabilities | Account Accrued Expenses | Amount $1,843.20
  - Section equity | Account Retained Earnings | Amount $10,494.61
  - Section equity | Account Owner's Equity | Amount $27,939.28

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-03

```
VENDOR INVOICE
==============

From
----
Cedar Manufacturing
75 Market Road, Mumbai
Date: 2024-06-03

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: June 2024

Terms
-----
Due Date: 2024-06-19

Supplier Header
---------------
Vendor: Oakline Services
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2024-06-19
Subtotal: $4,717.53
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: $471.75
Total: $6,955.88

Bill Lines
----------
Lines:
  - Description Consulting sprint | Amount $2,033.43
  - Description Support fee | Amount $2,684.10

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-05

```
CUSTOMER INVOICE
================

From
----
Cedar Manufacturing
75 Market Road, Mumbai
Document Date: 2024-06-05

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: June 2024
Contract Ref: CTR-0001

Terms
-----
Due Date: 2024-06-17

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-06-17
Subtotal: $4,689.37
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $937.87
Total: $5,627.24

Line Items
----------
Items:
  - Description Monthly retainer | Amount $1,312.96
  - Description Follow-up support | Amount $3,376.41

Footer
------
Generated for synthetic accounting research use.
Page marker: D002
```

### Document D007 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-05

```
VENDOR INVOICE
==============

From
----
Cedar Manufacturing
75 Market Road, Mumbai
Document Date: 2024-06-05

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D007
Document Type: vendor_invoice
Period: June 2024

Terms
-----
Due Date: 2024-06-20

Supplier Header
---------------
Vendor: Vertex Supply Co.
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0002
Due Date: 2024-06-20
Subtotal: $2,929.63
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: $585.93
Total: $3,515.56

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $1,026.47
  - Description Support fee | Amount $1,903.16

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-06-18

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Meridian Support LLP
Total: $229.53
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $75.44
  - Description Travel Incidentals | Amount $154.09
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-20

```
PAYMENT ADVICE
==============

From
----
Cedar Manufacturing
75 Market Road, Mumbai
Date: 2024-06-20

To
--
Oakline Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: June 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: $5,189.28
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-06-21

```
PAYMENT ADVICE
==============

From
----
Cedar Manufacturing
75 Market Road, Mumbai
Document Date: 2024-06-21

To
--
Metro Edge Partners

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: June 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Metro Edge Partners
Amount: $5,627.24
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D008 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-06-30

```
VENDOR STATEMENT
================

From
----
Cedar Manufacturing
75 Market Road, Mumbai
Document Date: 2024-06-30

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: vendor_statement
Period: June 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Vertex Supply Co.
Closing Balance: $3,515.56

Statement Lines
---------------
Lines:
  - Reference BILL-0002 | Document Type Open invoice | Amount $3,515.56 | Status Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D008
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
Cedar Manufacturing
75 Market Road, Mumbai
Date: 2024-06-30

Reference Box
-------------
Document ID: D009
Document Type: bank_statement
Period: June 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $36,224.01
Closing Balance: $36,432.44

Statement Rows
--------------
Rows:
  - Date 2024-06-18 | Description Meridian Support LLP receipt RCPT-0001 | Amount $-229.53 |
 Running Balance $35,994.48
  - Date 2024-06-20 | Description Supplier settlement BILL-0001 | Amount $-5,189.28 | 
Running Balance $30,805.20
  - Date 2024-06-21 | Description Customer settlement INV-0001 | Amount $5,627.24 | Running 
Balance $36,432.44

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D009
```

## 5. Expected Journal Entries (ground truth)

_(no expected entries — packet is labeled inconsistent)_

## 6. Expected Final Balance Sheet (ground truth)

_Packet is labeled inconsistent — the expected balance sheet should be empty._

**Totals:** Assets = 0.00; Liabilities = 0.00; Equity = 0.00
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
- Notes: Correct — invoice total inconsistency prevents clean entries.

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
- Notes: N/A.

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [x] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `invoice_total_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Line item sum doesn't match stated invoice total. Real mismatch.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Acceptable.
