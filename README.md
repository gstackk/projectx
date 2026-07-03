# Day 1 – Load CSV to BigQuery

## Process

- Started with a CSV file (orders dataset)
- Used Python (pandas) to read the CSV
- Loaded the data into BigQuery as a table
- Verified data by running a SQL query

## Flow

CSV file → Python script to copy the data to the folder in Big query → SQL table

## Query

```sql
SELECT COUNT(*)*
FROM `your*project.dataset.olist*orders_dataset`
``*

## Tests & Sample Questions:
why did we do the copying process?
because if we have data from any other part of the data source and if we are copying the data from a different location to our location we use python or sql to copy those tables. here we used python to copy the files and paste it in our table.

**FINAL TAKE**

BigQuery = home
Project → organizes system
Dataset → organizes tables + controls access
Table → stores data

**# Day 2 – SQL: CTEs + Window Functions**
implement pair swapping logic using CASE and CROSS JOIN
- handled odd-even order_id swapping
- managed last row edge case
- learned CROSS JOIN usage"


