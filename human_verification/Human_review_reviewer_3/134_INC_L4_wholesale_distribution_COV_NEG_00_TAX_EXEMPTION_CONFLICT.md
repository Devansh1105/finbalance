# Verification Packet — COV_NEG_00_TAX_EXEMPTION_CONFLICT

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** May 2024
- **Period start → end:** 2024-05-01 → 2024-05-31
- **Entity:** Cedar Retail Group
- **Currency (display / functional):** USD / USD
- **Tax regime:** `us_sales_tax`
- **Document count:** 20
- **Labeled as inconsistent:** True
- **Inconsistency codes:** tax_exemption_conflict
- **Inconsistency reasons:** Tax exemption certificate evidence conflicts with the invoice tax treatment.

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-05-01_

**Assets**
- Cash: 36,045.73
- Inventory: 31,056.65
- Accounts Receivable: 3,444.06
- Office Supplies: 1,161.62
- Equipment: 12,363.74

**Liabilities**
- Accounts Payable: 9,912.55
- Accrued Expenses: 1,796.62
- Loans Payable: 6,808.71

**Equity**
- Retained Earnings: 6,914.70
- Owner's Equity: 58,639.22


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-05-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-05-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $36,045.73
  - Section assets | Account Inventory | Amount $31,056.65
  - Section assets | Account Accounts Receivable | Amount $3,444.06
  - Section assets | Account Office Supplies | Amount $1,161.62
  - Section assets | Account Equipment | Amount $12,363.74
  - Section liabilities | Account Accounts Payable | Amount $9,912.55
  - Section liabilities | Account Accrued Expenses | Amount $1,796.62
  - Section liabilities | Account Loans Payable | Amount $6,808.71
  - Section equity | Account Retained Earnings | Amount $6,914.70
  - Section equity | Account Owner's Equity | Amount $58,639.22

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2024-05-03

```
TAX REGIME NOTICE
=================

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Document Date: 2024-05-03

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: May 2024

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: us_sales_tax
Company Jurisdiction: California
Counterparty Jurisdiction: California
Tax Rate: 8.25%
Jurisdiction Tax Amount: $1,224.97
Treatment: US purchase sales tax capitalized into inventory cost

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-03

```
SUPPLIER INVOICE
================

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Date: 2024-05-03

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: May 2024

Terms
-----
Due Date: 2024-05-14

Supplier Header
---------------
Supplier: Meridian Support LLP
Goods Receipt Ref: GRN-TAX-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 2024-05-14
Subtotal: $14,848.16
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: $1,224.97
Total: $16,073.13

Supplier Bill Lines
-------------------
Lines:
  - Description Refill Pack | Quantity 1 | Unit Cost $14,848.16 | Amount $14,848.16

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-05-09

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Prime Utility Desk
Purchase Ref: PO-0001
Total Quantity: $102.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Refill Pack | Quantity 102 | Unit Cost $40.21
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-11

```
SUPPLIER INVOICE
================

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Document Date: 2024-05-11

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: May 2024

Terms
-----
Due Date: 2024-05-29

Supplier Header
---------------
Supplier: Prime Utility Desk
Goods Receipt Ref: GRN-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 2024-05-29
Subtotal: $4,101.42
Tax Label: US Sales Tax
Tax Rate: 9.50%
Tax Amount: $389.63
Total: $4,491.05

Supplier Bill Lines
-------------------
Lines:
  - Description Refill Pack | Quantity 102 | Unit Cost $40.21 | Amount $4,101.42

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2024-05-11

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Blue Finch Holdings
Shipment Ref: SHP-0001
Billed Amount: $2,816.95
Cost Basis Amount: $1,570.94
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 25 | Unit Price $106.05 | Unit Cost 
$62.84 | Extended Cost $1,570.94
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-11

```
CUSTOMER INVOICE
================

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Date: 2024-05-11

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: May 2024
Shipment Ref: SHP-0001

Terms
-----
Due Date: 2024-05-21

Parties
-------
Customer: Blue Finch Holdings
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-05-21
Subtotal: $2,651.25
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: $165.70
Total: $2,816.95

Line Items
----------
Items:
  - Description Widget A | Amount $2,651.25

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
- **Date:** 2024-05-15

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $3,240.88
Draw Amount: $67,203.92
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $70,444.80
Note: Scheduled lender activity for the selected period.
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-16

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Prime Utility Desk
Asset Name: Ultrasound console
Asset Tag: TAG-0001
Useful Life Months: 48
Total: $68,803.47
Paid Cash: $24,858.67
Financed Amount: $43,944.80
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2024-05-18

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Document Date: 2024-05-18

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: May 2024

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Oak Harbor Foods
Tax Regime: us_sales_tax
Effective Date: 2024-05-01
Expiration Date: 2024-05-31
Exemption Status: Expired
Exempt Reason: Resale exemption certificate overrides default invoice tax treatment.

Footer
------
Generated for synthetic accounting research use.
Page marker: D017
```

### Document D018 — Customer Tax Profile

- **Type:** `customer_tax_profile`
- **Role:** `support_doc`
- **Date:** 2024-05-18

```
CUSTOMER TAX PROFILE
====================

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Date: 2024-05-18

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: May 2024

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Oak Harbor Foods
Customer Jurisdiction: California
Company Jurisdiction: California
Same State: True
Exemption Certificate: EXEMPT-0001

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-18

```
CUSTOMER INVOICE
================

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Date: 2024-05-18

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: May 2024
Shipment Ref: SHP-0002

Terms
-----
Due Date: 2024-06-08

Parties
-------
Customer: Oak Harbor Foods
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-06-08
Subtotal: $21,008.41
Tax Label: US Sales Tax
Tax Rate: 0.00%
Tax Amount: $0.00
Exemption Certificate: EXEMPT-0001
Total: $21,008.41

Line Items
----------
Items:
  - Description Filter Pack | Amount $21,008.41

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-05-23

```
PAYMENT ADVICE
==============

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Date: 2024-05-23

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: May 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: $1,952.15
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-05-26

```
PAYMENT ADVICE
==============

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Date: 2024-05-26

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: May 2024
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: $2,547.85
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
- **Date:** 2024-05-27

```
UTILITY INVOICE
===============

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Date: 2024-05-27

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: May 2024

Terms
-----
Due Date: 2024-06-05

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: May 2024
Due Date: 2024-06-05
Total: $531.96

Charges
-------
Charges:
  - Description Electricity | Amount $143.55
  - Description Water | Amount $388.41

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-05-28

```
PAYROLL SUMMARY
===============

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Date: 2024-05-28

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: May 2024
Headcount: 12
Gross Pay: $8,322.84
Employer Tax: 1,046.71
Cash Outflow: $9,369.55

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-05-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Front store

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Widget A | System Qty 100 | Counted Qty 88 | Unit Cost $17.10
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2024-05-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: $205.20
Reference Sheet: COUNT-0001
```

### Document D014 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-05-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $12,363.74
Useful Life Months: 48
Current Period Charge: $257.58
Accumulated Depreciation: 257.58
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-05-31

```
BANK STATEMENT
==============

From
----
Cedar Retail Group
90 Hill Park, Hyderabad
Document Date: 2024-05-31

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: May 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-LICT
Statement Currency: USD
Opening Balance: $36,045.73
Closing Balance: $68,425.73

Statement Rows
--------------
Rows:
  - Date 2024-05-15 | Description Loan draw LOAN-0001 | Amount $67,203.92 | Running Balance 
$103,249.65
  - Date 2024-05-16 | Description Asset purchase ASSET-0001 | Amount $-24,858.67 | Running 
Balance $78,390.98
  - Date 2024-05-23 | Description Customer settlement INV-0001 | Amount $1,952.15 | Running 
Balance $80,343.13
  - Date 2024-05-26 | Description Supplier settlement SUP-0001 | Amount $-2,547.85 | Running
 Balance $77,795.28
  - Date 2024-05-28 | Description Payroll PAYRUN-0001 | Amount $-9,369.55 | Running Balance 
$68,425.73

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
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
Is the labeled contradiction (codes: `tax_exemption_conflict`) actually present in the documents and would prevent a clean reconciliation?
- [x] Yes, the contradiction is real and would block reconciliation
- [ ] Contradiction is real but the code(s) don't quite fit
- [ ] No clear contradiction visible — this packet looks reconcilable
- Notes: Exemption cert conflicts with the invoice tax.

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
