# Verification Packet — COV_NEG_00_JURISDICTION_TAX_MISMATCH

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** November 2025
- **Period start → end:** 2025-11-01 → 2025-11-30
- **Entity:** Northwind Operations
- **Currency (display / functional):** USD / USD
- **Tax regime:** `us_sales_tax`
- **Document count:** 20
- **Labeled as inconsistent:** True
- **Inconsistency codes:** jurisdiction_tax_mismatch
- **Inconsistency reasons:** Jurisdiction-specific tax treatment does not reconcile with the applicable support documents.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-11-01_

**Assets**
- Cash: 56,052.72
- Inventory: 34,054.11
- Accounts Receivable: 8,279.35
- Office Supplies: 1,370.61
- Equipment: 14,005.47

**Liabilities**
- Accounts Payable: 6,348.42
- Accrued Expenses: 825.14
- Loans Payable: 10,545.91

**Equity**
- Retained Earnings: 4,853.64
- Owner's Equity: 91,189.15


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-11-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-11-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $56,052.72
  - Section assets | Account Inventory | Amount $34,054.11
  - Section assets | Account Accounts Receivable | Amount $8,279.35
  - Section assets | Account Office Supplies | Amount $1,370.61
  - Section assets | Account Equipment | Amount $14,005.47
  - Section liabilities | Account Accounts Payable | Amount $6,348.42
  - Section liabilities | Account Accrued Expenses | Amount $825.14
  - Section liabilities | Account Loans Payable | Amount $10,545.91
  - Section equity | Account Retained Earnings | Amount $4,853.64
  - Section equity | Account Owner's Equity | Amount $91,189.15

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2025-11-02

```
TAX REGIME NOTICE
=================

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Date: 2025-11-02

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: November 2025

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: us_sales_tax
Company Jurisdiction: New York
Counterparty Jurisdiction: New York
Tax Rate: 7.25%
Jurisdiction Tax Amount: $0.01
Treatment: US purchase sales tax capitalized into inventory cost

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-02

```
SUPPLIER INVOICE
================

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Date: 2025-11-02

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: November 2025

Terms
-----
Due Date: 2025-11-17

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Goods Receipt Ref: GRN-TAX-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 2025-11-17
Subtotal: $16,347.68
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: $1,185.21
Total: $17,532.89

Supplier Bill Lines
-------------------
Lines:
  - Description Service Bundle | Quantity 1 | Unit Cost $16,347.68 | Amount $16,347.68

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-11-08

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Vertex Supply Co.
Purchase Ref: PO-0001
Total Quantity: $133.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Widget B | Quantity 133 | Unit Cost $53.63
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-10

```
SUPPLIER INVOICE
================

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Date: 2025-11-10

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: November 2025

Terms
-----
Due Date: 2025-12-01

Supplier Header
---------------
Supplier: Vertex Supply Co.
Goods Receipt Ref: GRN-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 2025-12-01
Subtotal: $7,132.79
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: $588.46
Total: $7,721.25

Supplier Bill Lines
-------------------
Lines:
  - Description Widget B | Quantity 133 | Unit Cost $53.63 | Amount $7,132.79

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2025-11-13

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Date: 2025-11-13

To
--
Maple Ridge Trading

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: November 2025

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Maple Ridge Trading
Tax Regime: us_sales_tax
Effective Date: 2025-11-01
Expiration Date: 2025-11-30
Exemption Status: Valid
Exempt Reason: Resale exemption certificate overrides default invoice tax treatment.

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D018 — Customer Tax Profile

- **Type:** `customer_tax_profile`
- **Role:** `support_doc`
- **Date:** 2025-11-13

```
CUSTOMER TAX PROFILE
====================

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Document Date: 2025-11-13

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: November 2025

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Maple Ridge Trading
Customer Jurisdiction: New York
Company Jurisdiction: New York
Same State: True
Exemption Certificate: EXEMPT-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-13

```
CUSTOMER INVOICE
================

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Document Date: 2025-11-13

To
--
Maple Ridge Trading
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: November 2025
Shipment Ref: SHP-0002

Terms
-----
Due Date: 2025-11-26

Parties
-------
Customer: Maple Ridge Trading
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2025-11-26
Subtotal: $21,168.53
Tax Label: US Sales Tax
Tax Rate: 0.00%
Tax Amount: $0.00
Exemption Certificate: EXEMPT-0001
Total: $21,168.53

Line Items
----------
Items:
  - Description Refill Pack | Amount $21,168.53

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-11-14

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Riverfront Group
Shipment Ref: SHP-0001
Billed Amount: $5,917.75
Cost Basis Amount: $3,294.74
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget B | Quantity 54 | Unit Price $102.18 | Unit Cost 
$61.01 | Extended Cost $3,294.74
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-14

```
CUSTOMER INVOICE
================

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Date: 2025-11-14

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: November 2025
Shipment Ref: SHP-0001

Terms
-----
Due Date: 2025-12-02

Parties
-------
Customer: Riverfront Group
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-12-02
Subtotal: $5,517.72
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: $400.03
Total: $5,917.75

Line Items
----------
Items:
  - Description Widget B | Amount $5,517.72

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-16

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $1,010.62
Draw Amount: $32,020.17
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $33,030.79
Note: Scheduled lender activity for the selected period.
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-11-16

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Golden State Finance
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 60
Total: $49,681.12
Paid Cash: $17,484.69
Financed Amount: $32,196.43
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-22

```
PAYMENT ADVICE
==============

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Date: 2025-11-22

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: November 2025
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $5,617.67
Reference: SUP-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-22

```
UTILITY INVOICE
===============

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Document Date: 2025-11-22

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: November 2025

Terms
-----
Due Date: 2025-12-08

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: November 2025
Due Date: 2025-12-08
Total: $410.77

Charges
-------
Charges:
  - Description Electricity | Amount $134.85
  - Description Water | Amount $275.92

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-11-25

```
PAYMENT ADVICE
==============

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Date: 2025-11-25

To
--
Riverfront Group

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: November 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: $5,817.44
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-11-27

```
PAYROLL SUMMARY
===============

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Document Date: 2025-11-27

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: November 2025
Headcount: 3
Gross Pay: $10,062.51
Employer Tax: 1,105.13
Cash Outflow: $11,167.64

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-11-30

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Warehouse A

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Widget A | System Qty 100 | Counted Qty 89 | Unit Cost $23.36
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2025-11-30

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: $256.96
Reference Sheet: COUNT-0001
```

### Document D014 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-11-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Display fixtures
Asset Tag: TAG-0001
Cost: $49,681.12
Useful Life Months: 60
Current Period Charge: $828.02
Accumulated Depreciation: 828.02
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-11-30

```
BANK STATEMENT
==============

From
----
Northwind Operations
220 Lake View Road, Bengaluru
Date: 2025-11-30

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: November 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-ATCH
Statement Currency: USD
Opening Balance: $56,052.72
Closing Balance: $59,620.33

Statement Rows
--------------
Rows:
  - Date 2025-11-16 | Description Asset purchase ASSET-0001 | Amount $-17,484.69 | Running 
Balance $38,568.03
  - Date 2025-11-16 | Description Loan draw LOAN-0001 | Amount $32,020.17 | Running Balance 
$70,588.20
  - Date 2025-11-22 | Description Supplier settlement SUP-0001 | Amount $-5,617.67 | Running
 Balance $64,970.53
  - Date 2025-11-25 | Description Customer settlement INV-0001 | Amount $5,817.44 | Running 
Balance $70,787.97
  - Date 2025-11-27 | Description Payroll PAYRUN-0001 | Amount $-11,167.64 | Running Balance
 $59,620.33

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
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
Is the labeled contradiction (codes: `jurisdiction_tax_mismatch`) actually present in the documents and would prevent a clean reconciliation?
- [ ] Yes, the contradiction is real and would block reconciliation
- [x] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Contradiction's there, but the labeled code is a loose fit.

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [x] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes: Real break — just relabel the inconsistency code.
