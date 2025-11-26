# Sales Trend Analysis Using Aggregations

## Improving Business Insights Through Time-Based Aggregations

### **Task Overview**

This task focuses on performing **sales trend analysis** using SQL aggregation techniques on an e-commerce dataset.
The objective is to extract **monthly revenue**, **order volume**, **top-performing months**, and **average revenue per order** by applying date-time functions, grouping logic, and feature engineering on transactional sales data.

The dataset used contains order-level records with fields such as **order_id**, **order_date**, **product_id**, and **total_amount**, which were cleaned and transformed into a structured analysis-ready format using MySQL.

------

## Key Insights

- Extracting **month and year** from order dates helps reveal seasonal buying patterns.
- Using **COUNT(DISTINCT order_id)** ensures accurate order volume by avoiding duplicate counting.
- Monthly **revenue and order trends** show clear seasonal peaks and slow periods.
- **Top 5 revenue months** highlight when customers purchase the most, useful for business planning.
- Calculating **average revenue per order** reveals customer spending behavior.
- Proper handling of missing or incorrect values in the raw dataset improves accuracy.
- SQL functions like `DATE_FORMAT()`, `GROUP BY`, and aggregate functions significantly boost analytical capabilities.

------

## Repository Contents

| File                      | Description                                           |
| ------------------------- | ----------------------------------------------------- |
| ecommerceSales.csv        | Original raw dataset                                  |
| task9.sql                 | SQL script for revenue, order volume & trend analysis |
| resultMonthlySales.csv    | results of monthly revenue & orders                   |
| resultTop5Month.csv       | Highest revenue-generating months                     |
| avg_revenue_per_order.csv | Calculated Average Revenue Per Order                  |
| README.md                 | readme file                                           |

------

## Tools & Technologies Used

- **MySQL / MySQL Workbench**
- SQL Functions:
   `YEAR()`, `MONTH()`, `DATE_FORMAT()`, `SUM()`, `COUNT(DISTINCT ...)`, `GROUP BY`, `ORDER BY`
- **Kaggle** e-commerce dataset

------

## Task Workflow

### **1. Data Import**

The raw CSV file was imported into MySQL using the Table Import Wizard to create the `ecommerce_raw` table.

### **2. Data Cleaning & Transformation**

A cleaned table `online_sales` was created containing only essential fields.

### **3. Feature Engineering (SQL-Based)**

- Extracted **Year** and **Month** from `order_date`
- Created a readable **month label** using `DATE_FORMAT()`
- Grouped by month for time-based analysis
- Used `COUNT(DISTINCT order_id)` to accurately compute order volume

### **4. Trend Analysis**

SQL aggregations were used to compute:

- Monthly Revenue
- Monthly Orders
- Average Revenue Per Order
- Top 5 Revenue Months