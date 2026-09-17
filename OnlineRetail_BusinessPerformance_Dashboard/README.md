# Online Retail Business Performance Dashboard

### Power BI | Python | Pandas | Data Cleaning & ETL | Business Intelligence

An executive Power BI dashboard built from a large transactional retail dataset, with a focus on **sales performance, product performance, customer behavior, geographic distribution, and revenue trends over time**.

The project combines a reproducible Python/Pandas data preparation pipeline with a structured Power BI reporting layer, turning raw transactional data into a business-ready analytical dataset and interactive dashboard.

---

## Project Overview

The objective of this project is to transform raw online retail transaction data into a reliable analytical dataset and an executive-facing Business Intelligence dashboard.

The workflow separates **data preparation** from **business reporting**, allowing the cleaning and transformation process to be reproduced independently from the Power BI analysis.

### Workflow

```text
Raw Excel Dataset
       ↓
Python / Pandas
       ↓
Data Cleaning & Transformation
       ↓
Cleaned CSV Dataset
       ↓
Power BI Data Model
       ↓
Executive Dashboard
```

---

## Data Preparation

The raw dataset is provided as an Excel workbook containing multiple sheets. The Python pipeline loads and combines the available sheets before applying the cleaning and transformation rules required for analysis.

### Cleaning & Transformation Steps

* Load all sheets from `online_retail_II.xlsx`.
* Combine the sheets into a single transactional dataset.
* Remove records with missing `Customer ID`.
* Exclude cancelled transactions identified by invoice numbers beginning with `C`.
* Keep only records with positive `Quantity` and `Price`.
* Convert `Customer ID` to integer format.
* Standardize unit prices to two decimal places.
* Calculate transaction-level revenue using:

```text
Revenue = Quantity × Price
```

* Export the resulting dataset as `online_retail_cleaned.csv`.
* Preserve two-decimal numeric formatting in the exported revenue and price fields.

### Pipeline Result

The cleaning pipeline processed **805,549 records** and generated the cleaned analytical dataset used for reporting.

---

## Power BI Dashboard

The dashboard provides an executive view of several dimensions of business performance.

### 1. Financial & Sales Performance

Key metrics include:

* **Total Revenue:** Revenue generated from valid sales transactions.
* **Average Order Value (AOV):** Average revenue generated per unique invoice.
* **Average Unit Price:** Average selling price across the analyzed products.

### 2. Operational & Sales Volume

The dashboard measures the scale of transactional activity through:

* **Total Quantity:** Total number of units sold.
* **Total Orders / Transactions:** Number of unique invoices.
* **Total SKUs / Unique Products:** Number of distinct products represented in the dataset.

Cancelled transactions are excluded during the data preparation stage to keep the primary sales analysis focused on valid transactions.

### 3. Customer & Market Performance

The dashboard provides customer and geographic analysis through:

* **Unique Customers:** Number of distinct customers represented in the cleaned dataset.
* **Revenue by Country:** Geographic distribution of revenue across markets.
* **Top Customers:** Identification of customers contributing the highest revenue.
* **Top Products:** Identification of products generating the highest revenue and sales volume.

### 4. Revenue Trends

Temporal analysis is used to examine:

* **Revenue by Month / Year:** Evolution of revenue over time.
* **Monthly Revenue Changes:** Identification of increases and decreases in revenue between periods.
* **Sales Trends:** Detection of peaks, declines, and changes in business performance over the analyzed period.

---

## Dashboard Screenshots

The `Dashboard/` directory contains screenshots of the Power BI report.

The dashboard focuses on three main analytical areas:

* **Revenue Performance Over Time**
* **Product Performance**
* **Customer & Market Performance**

---

## Repository Structure

```text
OnlineRetail_BusinessPerformance_Dashboard/
│
├── Dashboard/
│   └── Power BI dashboard screenshots
│
├── Script/
│   └── Data cleaning and transformation script
│
└── README.md
```

---

## Tools & Technologies

* **Python**
* **Pandas**
* **Power BI**
* **DAX**
* **Microsoft Excel**
* **CSV**

---

## Key Skills Demonstrated

* Data Cleaning
* Data Transformation
* ETL
* Exploratory Data Analysis
* Business Intelligence
* Power BI Dashboard Development
* KPI Design
* Revenue Analysis
* Customer Analytics
* Product Performance Analysis
* Geographic Analysis
* Time-Series Analysis
* Python / Pandas Data Processing

---

## Project Purpose

This project demonstrates the ability to take a large, raw transactional dataset through a reproducible data preparation process and transform it into a structured analytical foundation for business reporting.

The emphasis is not only on visualization, but on **data quality, reproducibility, metric definition, and business-oriented analysis**.
