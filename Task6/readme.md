# **Sales Summary Analysis – Python + SQLite**

## **Overview**

This task demonstrates how to build a simple **Sales Analysis Dashboard** using **Python, SQLite, Pandas, and Matplotlib**.
 A small SQLite database (`sales_data.db`) is used, containing product-level sales transactions.

The task showcases how to:

- Connect Python to an SQLite database
- Run SQL queries to aggregate sales
- Generate a clean sales summary table
- Visualize revenue using a bar chart

## **Repository Contents**

| File            | Description                                     |
| --------------- | ----------------------------------------------- |
| `sales_data.db` | SQLite database file containing the sales table |
| `Task6.ipynb`   | Notebook for the analysis                       |
| `README.md`     | Project description and instructions            |

## **Dataset Structure**

The dataset is stored in an SQLite file (`sales_data.db`) with one table:

### **Table: sales**

| Column   | Type    | Description    |
| -------- | ------- | -------------- |
| id       | INTEGER | Primary key    |
| product  | TEXT    | Product name   |
| quantity | INTEGER | Quantity sold  |
| price    | REAL    | Price per unit |

Products included:
 Laptop, Mouse, USB Cable, Monitor, Keyboard, Printer, Tablet, Headset, SSD, HDD etc.

## **Output Produced**

- A clean **Sales Summary Table**
- A bar chart showing **Revenue by Product**

- Auto-created **SQLite database file**


