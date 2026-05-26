# Verification Packet — COV_NEG_00_TAX_TOTAL_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `professional_services`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** January 2025
- **Period start → end:** 2025-01-01 → 2025-01-31
- **Entity:** Silverline Property Services
- **Currency (display / functional):** USD / USD
- **Tax regime:** `sales_tax`
- **Document count:** 8
- **Labeled as inconsistent:** True
- **Inconsistency codes:** tax_total_mismatch
- **Inconsistency reasons:** Subtotal, indirect tax, and total do not reconcile on the document.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Reserve Cash`, `Accounts Receivable`, `Prepaid Rent`, `Prepaid Insurance`, `Office Supplies`, `Equipment`, `Furniture`, `Accumulated Depreciation`, `Right-of-Use Asset`, `Accounts Payable`, `Accrued Expenses`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Deferred Tax Liability`, `Lease Liability`, `Unearned Revenue`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Rent Expense`, `Insurance Expense`, `Office Supplies Expense`, `Travel Expense`, `Utilities Expense`, `Bad Debt Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Deferred Tax Expense`, `Interest Expense`, `Lease Interest Expense`, `Lease Amortization Expense`, `Gain on Disposal`, `Loss on Disposal`, `Foreign Exchange Gain`, `Foreign Exchange Loss`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 28,864.47
- Accounts Receivable: 6,562.17
- Prepaid Rent: 1,952.89
- Office Supplies: 462.71

**Liabilities**
- Accounts Payable: 2,167.84
- Accrued Expenses: 1,163.65

**Equity**
- Retained Earnings: 10,305.24
- Owner's Equity: 24,205.51


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
Statement Date: 2025-01-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $28,864.47
  - Section assets | Account Accounts Receivable | Amount $6,562.17
  - Section assets | Account Prepaid Rent | Amount $1,952.89
  - Section assets | Account Office Supplies | Amount $462.71
  - Section liabilities | Account Accounts Payable | Amount $2,167.84
  - Section liabilities | Account Accrued Expenses | Amount $1,163.65
  - Section equity | Account Retained Earnings | Amount $10,305.24
  - Section equity | Account Owner's Equity | Amount $24,205.51

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-02

```
CUSTOMER INVOICE
================

From
----
Silverline Property Services
220 Lake View Road, Bengaluru
Date: 2025-01-02

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: January 2025
Contract Ref: CTR-0002

Terms
-----
Due Date: 2025-01-19

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-01-19
Subtotal: $6,159.97
Tax Label: Sales Tax
Tax Rate: 9.50%
Tax Amount: $585.20
Total: $3,957.48

Line Items
----------
Items:
  - Description Support package | Amount $1,333.02
  - Description Follow-up support | Amount $4,826.95

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D002 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-06

```
CUSTOMER INVOICE
================

From
----
Silverline Property Services
220 Lake View Road, Bengaluru
Date: 2025-01-06

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D002
Document Type: customer_invoice
Period: January 2025
Contract Ref: CTR-0001

Terms
-----
Due Date: 2025-01-28

Parties
-------
Customer: Maple Ridge Trading
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-01-28
Subtotal: $7,547.78
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: $377.39
Total: $7,925.17

Line Items
----------
Items:
  - Description Monthly retainer | Amount $2,259.06
  - Description Follow-up support | Amount $5,288.72

Footer
------
Internal document packet copy.
Page marker: D002
```

### Document D003 — Vendor Invoice

- **Type:** `vendor_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-09

```
VENDOR INVOICE
==============

From
----
Silverline Property Services
220 Lake View Road, Bengaluru
Document Date: 2025-01-09

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: vendor_invoice
Period: January 2025

Terms
-----
Due Date: 2025-01-20

Supplier Header
---------------
Vendor: Prime Utility Desk
Expense Label: Office Supplies Expense
Currency: USD

Bill Details
------------
Invoice Number: BILL-0001
Due Date: 2025-01-20
Subtotal: $2,337.51
Tax Label: Sales Tax
Tax Rate: 8.25%
Tax Amount: $192.84
Total: $2,530.35

Bill Lines
----------
Lines:
  - Description Implementation work | Amount $781.17
  - Description Support fee | Amount $1,556.34

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-01-11

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Beacon Industrial Supply
Total: $8.66
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Travel Expense | Amount $3.72
  - Description Travel Incidentals | Amount $4.94
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-25

```
PAYMENT ADVICE
==============

From
----
Silverline Property Services
220 Lake View Road, Bengaluru
Date: 2025-01-25

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: January 2025
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: $2,530.35
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D005 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-26

```
PAYMENT ADVICE
==============

From
----
Silverline Property Services
220 Lake View Road, Bengaluru
Date: 2025-01-26

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D005
Document Type: payment_advice
Period: January 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Maple Ridge Trading
Amount: $7,925.17
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D008 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-01-31

```
BANK STATEMENT
==============

From
----
Silverline Property Services
220 Lake View Road, Bengaluru
Date: 2025-01-31

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: January 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $28,864.47
Closing Balance: $34,250.63

Statement Rows
--------------
Rows:
  - Date 2025-01-11 | Description Beacon Industrial Supply receipt RCPT-0001 | Amount $-8.66
 | Running Balance $28,855.81
  - Date 2025-01-25 | Description Supplier settlement BILL-0001 | Amount $-2,530.35 | 
Running Balance $26,325.46
  - Date 2025-01-26 | Description Customer settlement INV-0001 | Amount $7,925.17 | Running 
Balance $34,250.63

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D008
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

### Q6 — Inconsistency validity (inconsistency packets only)
Is the labeled contradiction (codes: `tax_total_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Subtotal + tax doesn't equal the stated total.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
