# Verification Packet — COV_WHO_Y5_0059

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 5
- **Period type:** year
- **Period label:** FY 2025
- **Period start → end:** 2025-01-01 → 2025-12-31
- **Entity:** Willow Advisors
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 34
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 231,071.24
- Inventory: 231,220.34
- Accounts Receivable: 56,059.01
- Office Supplies: 5,108.65
- Equipment: 89,806.76

**Liabilities**
- Accounts Payable: 49,010.59
- Accrued Expenses: 12,995.56
- Loans Payable: 28,953.54
- Notes Payable: 26,547.36

**Equity**
- Retained Earnings: 82,710.25
- Owner's Equity: 413,048.70


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
  - Section assets | Account Cash | Amount GBP 231,071.24
  - Section assets | Account Inventory | Amount GBP 231,220.34
  - Section assets | Account Accounts Receivable | Amount GBP 56,059.01
  - Section assets | Account Office Supplies | Amount GBP 5,108.65
  - Section assets | Account Equipment | Amount GBP 89,806.76
  - Section liabilities | Account Accounts Payable | Amount GBP 49,010.59
  - Section liabilities | Account Accrued Expenses | Amount GBP 12,995.56
  - Section liabilities | Account Loans Payable | Amount GBP 28,953.54
  - Section liabilities | Account Notes Payable | Amount GBP 26,547.36
  - Section equity | Account Retained Earnings | Amount GBP 82,710.25
  - Section equity | Account Owner's Equity | Amount GBP 413,048.70

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2025-02-10

```
TAX REGIME NOTICE
=================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 10/02/2025

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: FY 2025

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: india_gst
Company Jurisdiction: Karnataka
Counterparty Jurisdiction: Karnataka
Tax Rate: 12.00%
Jurisdiction Tax Amount: GBP 21,174.47
Treatment: India GST same-state CGST+SGST input credit

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-10

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 10/02/2025

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 22/02/2025

Supplier Header
---------------
Supplier: Meridian Support LLP
Goods Receipt Ref: GRN-TAX-0001
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 22/02/2025
Subtotal: GBP 176,453.92
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 21,174.47
CGST Amount: GBP 10,587.24
SGST Amount: GBP 10,587.23
Total: GBP 197,628.39

Supplier Bill Lines
-------------------
Lines:
  - Description Premium Kit | Quantity 1 | Unit Cost GBP 176,453.92 | Amount GBP 176,453.92

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-02-22

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Pace Office Mart
Purchase Ref: PO-0001
Total Quantity: GBP 140.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Filter Pack | Quantity 140 | Unit Cost GBP 235.56
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-24

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 24/02/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 07/03/2025

Supplier Header
---------------
Supplier: Pace Office Mart
Goods Receipt Ref: GRN-0001
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 07/03/2025
Subtotal: GBP 32,978.40
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 3,957.41
CGST Amount: GBP 1,978.70
SGST Amount: GBP 1,978.71
Total: GBP 36,935.81

Supplier Bill Lines
-------------------
Lines:
  - Description Filter Pack | Quantity 140 | Unit Cost GBP 235.56 | Amount GBP 32,978.40

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D025 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-03-27

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0002
Supplier: Beacon Industrial Supply
Purchase Ref: PO-0002
Total Quantity: GBP 155.00

Received Items
--------------
Items:
  - Sku SKU-0005 | Description Widget B | Quantity 155 | Unit Cost GBP 427.24
```

### Document D026 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-29

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 29/03/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D026
Document Type: supplier_invoice
Period: FY 2025

Terms
-----
Due Date: 09/04/2025

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Goods Receipt Ref: GRN-0002
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: SUP-0002
Due Date: 09/04/2025
Subtotal: GBP 66,222.20
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 7,946.66
CGST Amount: GBP 3,973.33
SGST Amount: GBP 3,973.33
Total: GBP 74,168.86

Supplier Bill Lines
-------------------
Lines:
  - Description Widget B | Quantity 155 | Unit Cost GBP 427.24 | Amount GBP 66,222.20

Footer
------
Internal document packet copy.
Page marker: D026
```

### Document D033 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2025-03-29

```
SECONDARY COPY
==============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 29/03/2025

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D033
Document Type: secondary_copy
Period: FY 2025

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: SUP-0002
Counterparty: Beacon Industrial Supply
Total: GBP 74,168.86
Copy Context: Scanned from the archive packet after the month-end close.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D033
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-04-28

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 6,278.25
Draw Amount: GBP 352,147.08
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 358,425.33
Note: Scheduled lender activity for the selected period.
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2025-06-17

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 17/06/2025

To
--
Aster Point Services

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: FY 2025

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Aster Point Services
Tax Regime: india_gst
Effective Date: 01/01/2025
Expiration Date: 31/12/2025
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
- **Date:** 2025-06-17

```
CUSTOMER TAX PROFILE
====================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 17/06/2025

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: FY 2025

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Aster Point Services
Customer Jurisdiction: Karnataka
Company Jurisdiction: Karnataka
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
- **Date:** 2025-06-17

```
CUSTOMER INVOICE
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 17/06/2025

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: FY 2025
Shipment Ref: SHP-0002

Terms
-----
Due Date: 28/06/2025

Parties
-------
Customer: Aster Point Services
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 28/06/2025
Subtotal: GBP 220,790.96
Tax Label: India GST
Tax Rate: 0.00%
Tax Amount: GBP 0.00
Exemption Certificate: EXEMPT-0001
Total: GBP 220,790.96

Line Items
----------
Items:
  - Description Widget A | Amount GBP 220,790.96

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D023 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-07-19

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0002
Customer: Blue Finch Holdings
Shipment Ref: SHP-0003
Billed Amount: GBP 44,159.90
Cost Basis Amount: GBP 24,178.49
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0004 | Description Filter Pack | Quantity 32 | Unit Price GBP 1,232.14 | Unit 
Cost GBP 755.58 | Extended Cost GBP 24,178.49
```

### Document D024 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-07-19

```
CUSTOMER INVOICE
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 19/07/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D024
Document Type: customer_invoice
Period: FY 2025
Shipment Ref: SHP-0003

Terms
-----
Due Date: 30/07/2025

Parties
-------
Customer: Blue Finch Holdings
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0003
Due Date: 30/07/2025
Subtotal: GBP 39,428.48
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 4,731.42
CGST Amount: GBP 2,365.71
SGST Amount: GBP 2,365.71
Total: GBP 44,159.90

Line Items
----------
Items:
  - Description Filter Pack | Amount GBP 39,428.48

Shipment Link
-------------
Shipment Ref: SHP-0003

Footer
------
Internal document packet copy.
Page marker: D024
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-08-12

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Blue Finch Holdings
Shipment Ref: SHP-0001
Billed Amount: GBP 68,775.24
Cost Basis Amount: GBP 31,411.63
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 70 | Unit Price GBP 832.63 | Unit Cost 
GBP 448.74 | Extended Cost GBP 31,411.63
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-12

```
CUSTOMER INVOICE
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 12/08/2025

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: FY 2025
Shipment Ref: SHP-0001

Terms
-----
Due Date: 27/08/2025

Parties
-------
Customer: Blue Finch Holdings
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 27/08/2025
Subtotal: GBP 58,284.10
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 10,491.14
CGST Amount: GBP 5,245.57
SGST Amount: GBP 5,245.57
Total: GBP 68,775.24

Line Items
----------
Items:
  - Description Widget A | Amount GBP 58,284.10

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-08-18

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Golden State Finance
Asset Name: Server rack
Asset Tag: TAG-0001
Useful Life Months: 60
Total: GBP 440,412.34
Paid Cash: GBP 103,788.29
Financed Amount: GBP 336,624.05
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-09-06

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 06/09/2025

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: GBP 59,632.81
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
- **Date:** 2025-09-24

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 24/09/2025

To
--
Pace Office Mart

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2025
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Pace Office Mart
Amount: GBP 29,695.83
Reference: SUP-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-09-26

```
PAYROLL SUMMARY
===============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 26/09/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2025
Headcount: 10
Gross Pay: GBP 132,871.65
Employer Tax: 15,166.52
Cash Outflow: GBP 148,038.17

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-09

```
UTILITY INVOICE
===============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 09/11/2025

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: FY 2025

Terms
-----
Due Date: 18/11/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: FY 2025
Due Date: 18/11/2025
Total: GBP 13,311.54

Charges
-------
Charges:
  - Description Electricity | Amount GBP 4,962.14
  - Description Water | Amount GBP 8,349.40

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D020 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-11-14

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Aurora Capital
Opening Principal: GBP 314,939.50
Draw Amount: GBP 0.00
Principal Paid: GBP 54,479.91
Interest Paid: GBP 3,550.70
Ending Principal: GBP 260,459.59
Note: Scheduled lender activity for the selected period.
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-12-31

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
  - Sku SKU-0003 | Description Widget B | System Qty 100 | Counted Qty 94 | Unit Cost GBP 
94.96
```

### Document D009 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D009
Document Type: inventory_rollforward
Period: FY 2025

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0001
Opening Balance: GBP 7,324.89
Additions: 13,601.59
Usage Or Sales: GBP 9,178.47
Write Down: 569.76
Ending Balance: GBP 11,178.25

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D014 — Fixed Asset Rollforward

- **Type:** `fixed_asset_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
FIXED ASSET ROLLFORWARD
=======================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D014
Document Type: fixed_asset_rollforward
Period: FY 2025

Asset Rollforward
-----------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: GBP 89,806.76
Useful Life: 48
Current Charge: GBP 22,451.64
Accumulated Depreciation: 22,451.64
Opening Balance: GBP 89,806.76
Additions: 0.00
Disposals: 0.00
Ending Balance: GBP 89,806.76

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D021 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
AR AGING SUMMARY
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D021
Document Type: ar_aging_summary
Period: FY 2025

Aging Summary
-------------
Summary ID: AGING-0001
Period: FY 2025
Total Open: GBP 9,142.43

Customer Lines
--------------
Lines:
  - Customer Blue Finch Holdings | Reference INV-0001 | Current GBP 6,294.85 | Past Due 
2,847.58

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Generated for synthetic accounting research use.
Page marker: D021
```

### Document D022 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
CREDIT MEMO
===========

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 31/12/2025

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D022
Document Type: credit_memo
Period: FY 2025
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Blue Finch Holdings
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: GBP 2,847.58

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D027 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0002
Location: Front store

Counted Items
-------------
Items:
  - Sku SKU-0006 | Description Widget A | System Qty 100 | Counted Qty 96 | Unit Cost GBP 
125.82
```

### Document D028 — Inventory Rollforward

- **Type:** `inventory_rollforward`
- **Role:** `adjustment_doc`
- **Date:** 2025-12-31

```
INVENTORY ROLLFORWARD
=====================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D028
Document Type: inventory_rollforward
Period: FY 2025

Inventory Rollforward
---------------------
Rollforward ID: INVROLL-0002
Opening Balance: GBP 7,849.43
Additions: 11,069.17
Usage Or Sales: GBP 6,063.02
Write Down: 503.28
Ending Balance: GBP 12,352.30

Footer
------
Generated for synthetic accounting research use.
Page marker: D028
```

### Document D029 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 31/12/2025

Reference Box
-------------
Document ID: D029
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Quarter-end packet routing note

Memo Summary
------------
Memo ID: INFO-0001
Subject: Quarter-end packet routing note
Audience: All Staff

Memo Body
---------
Narrative: The packet may include supporting correspondence gathered during the close 
review.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D029
```

### Document D030 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
VENDOR STATEMENT
================

From
----
Willow Advisors
90 Hill Park, Hyderabad
Document Date: 31/12/2025

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D030
Document Type: vendor_statement
Period: FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Metro Water
Closing Balance: GBP 13,311.54

Statement Lines
---------------
Lines:
  - Reference UTIL-0001 | Document Type Open invoice | Amount GBP 13,311.54 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D030
```

### Document D031 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D031
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Annual leave policy reminder

Memo Summary
------------
Memo ID: INFO-0002
Subject: Annual leave policy reminder
Audience: Finance Team

Memo Body
---------
Narrative: The packet may include supporting correspondence gathered during the close 
review.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D031
```

### Document D032 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-12-31

```
MEMO
====

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D032
Document Type: memo
Period: FY 2025

Approval / Context
------------------
Subject: Document retention reminder

Memo Summary
------------
Memo ID: INFO-0003
Subject: Document retention reminder
Audience: Back Office

Memo Body
---------
Narrative: The packet may include supporting correspondence gathered during the close 
review.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Internal document packet copy.
Page marker: D032
```

### Document D034 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Willow Advisors
90 Hill Park, Hyderabad
Date: 31/12/2025

Reference Box
-------------
Document ID: D034
Document Type: bank_statement
Period: FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0059
Statement Currency: GBP
Opening Balance: GBP 231,071.24
Closing Balance: GBP 303,298.23

Statement Rows
--------------
Rows:
  - Date 28/04/2025 | Description Loan draw LOAN-0001 | Amount GBP 352,147.08 | Running 
Balance GBP 583,218.32
  - Date 18/08/2025 | Description Asset purchase ASSET-0001 | Amount GBP -103,788.29 | 
Running Balance GBP 479,430.03
  - Date 06/09/2025 | Description Customer settlement INV-0001 | Amount GBP 59,632.81 | 
Running Balance GBP 539,062.84
  - Date 24/09/2025 | Description Supplier settlement SUP-0001 | Amount GBP -29,695.83 | 
Running Balance GBP 509,367.01
  - Date 26/09/2025 | Description Payroll PAYRUN-0001 | Amount GBP -148,038.17 | Running 
Balance GBP 361,328.84
  - Date 14/11/2025 | Description Loan payment LOAN-0002 | Amount GBP -58,030.61 | Running 
Balance GBP 303,298.23

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D034
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 32,978.40 | D002, D003 | 2025-02-24 | goods_receipt_purchase |
| 2 | Input CGST Receivable | Accounts Payable | 1,978.70 | D002, D003 | 2025-02-24 | goods_receipt_purchase_tax_cgst |
| 3 | Input SGST Receivable | Accounts Payable | 1,978.71 | D002, D003 | 2025-02-24 | goods_receipt_purchase_tax_sgst |
| 4 | Accounts Receivable | Sales Revenue | 58,284.10 | D004, D005 | 2025-08-12 | delivery_sale_sale |
| 5 | Cost of Goods Sold | Inventory | 31,411.63 | D004, D005 | 2025-08-12 | delivery_sale_cogs |
| 6 | Accounts Receivable | CGST Payable | 5,245.57 | D004, D005 | 2025-08-12 | delivery_sale_tax_cgst |
| 7 | Accounts Receivable | SGST Payable | 5,245.57 | D004, D005 | 2025-08-12 | delivery_sale_tax_sgst |
| 8 | Cash | Accounts Receivable | 59,632.81 | D006, D005 | 2025-09-06 | customer_payment |
| 9 | Accounts Payable | Cash | 29,695.83 | D007, D003 | 2025-09-24 | supplier_payment |
| 10 | Inventory Shrinkage Expense | Inventory | 569.76 | D008, D009 | 2025-12-31 | inventory_adjustment |
| 11 | Salaries Expense | Cash | 132,871.65 | D010 | 2025-09-26 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 15,166.52 | D010 | 2025-09-26 | payroll_tax |
| 13 | Utilities Expense | Accounts Payable | 13,311.54 | D011 | 2025-11-09 | utilities_bill |
| 14 | Cash | Loans Payable | 352,147.08 | D012 | 2025-04-28 | loan_draw |
| 15 | Equipment | Cash | 103,788.29 | D013 | 2025-08-18 | equipment_purchase_cash |
| 16 | Equipment | Notes Payable | 336,624.05 | D013 | 2025-08-18 | equipment_purchase_financed |
| 17 | Depreciation Expense | Accumulated Depreciation | 22,451.64 | D014 | 2025-12-31 | depreciation |
| 18 | Inventory | Accounts Payable | 176,453.92 | D015, D016 | 2025-02-10 | jurisdictional_tax_invoice_purchase_inventory |
| 19 | Input CGST Receivable | Accounts Payable | 10,587.24 | D015, D016 | 2025-02-10 | jurisdictional_tax_invoice_input_cgst |
| 20 | Input SGST Receivable | Accounts Payable | 10,587.23 | D015, D016 | 2025-02-10 | jurisdictional_tax_invoice_input_sgst |
| 21 | Accounts Receivable | Sales Revenue | 220,790.96 | D017, D018, D019 | 2025-06-17 | jurisdictional_tax_invoice_exempt_sale |
| 22 | Loans Payable | Cash | 54,479.91 | D020 | 2025-11-14 | loan_repayment_principal |
| 23 | Interest Expense | Cash | 3,550.70 | D020 | 2025-11-14 | loan_repayment_interest |
| 24 | Bad Debt Expense | Accounts Receivable | 2,847.58 | D021, D022, D005 | 2025-12-31 | bad_debt_review |
| 25 | Accounts Receivable | Sales Revenue | 39,428.48 | D023, D024 | 2025-07-19 | delivery_sale_sale |
| 26 | Cost of Goods Sold | Inventory | 24,178.49 | D023, D024 | 2025-07-19 | delivery_sale_cogs |
| 27 | Accounts Receivable | CGST Payable | 2,365.71 | D023, D024 | 2025-07-19 | delivery_sale_tax_cgst |
| 28 | Accounts Receivable | SGST Payable | 2,365.71 | D023, D024 | 2025-07-19 | delivery_sale_tax_sgst |
| 29 | Inventory | Accounts Payable | 66,222.20 | D025, D026 | 2025-03-29 | goods_receipt_purchase |
| 30 | Input CGST Receivable | Accounts Payable | 3,973.33 | D025, D026 | 2025-03-29 | goods_receipt_purchase_tax_cgst |
| 31 | Input SGST Receivable | Accounts Payable | 3,973.33 | D025, D026 | 2025-03-29 | goods_receipt_purchase_tax_sgst |
| 32 | Inventory Shrinkage Expense | Inventory | 503.28 | D027, D028 | 2025-12-31 | inventory_adjustment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 303,298.23
- Inventory: 450,211.70
- Accounts Receivable: 327,304.72
- Office Supplies: 5,108.65
- Equipment: 530,219.10
- Input CGST Receivable: 16,539.27
- Input SGST Receivable: 16,539.27
- Accumulated Depreciation: -22,451.64

**Liabilities**
- Accounts Payable: 341,359.36
- Accrued Expenses: 12,995.56
- Loans Payable: 326,620.71
- Notes Payable: 363,171.41
- CGST Payable: 7,611.28
- SGST Payable: 7,611.28

**Equity**
- Retained Earnings: 154,351.00
- Owner's Equity: 413,048.70

**Totals:** Assets = 1,626,769.30; Liabilities = 1,059,369.60; Equity = 567,399.70
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
