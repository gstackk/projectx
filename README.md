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

--------------------------------------------------------------------------------------
**# Day 2 – SQL: CTEs + Window Functions**
implement pair swapping logic using CASE and CROSS JOIN
- handled odd-even order_id swapping
- managed last row edge case
- learned CROSS JOIN usage"

learnt to find the Running total for each month: (co pilot suggested to use sub query but i did it using CTE :) )
WITH
  running_total AS (
    SELECT
      DATE_TRUNC(shipping_limit_date, MONTH) AS year_month,
      SUM(price) AS total_price
    FROM `vf-grp-gbissdbx-dev-1.gsamples_olists.rank_samples`
    GROUP BY year_month
  ),
  real_running_total AS (
    SELECT
      year_month,
      ROUND(total_price, 0) AS total_price,
      ROUND(SUM(total_price) OVER (ORDER BY year_month), 2) AS running_total
    FROM running_total
  )
SELECT
 year_month,
  CASE
    WHEN total_price >= 1000000000
      THEN FORMAT('%.1fB', total_price / 1000000000)
    WHEN total_price >= 1000000 THEN FORMAT('%.1fM', total_price / 1000000)
    WHEN total_price >= 1000 THEN FORMAT('%.1fK', total_price / 1000)
    ELSE CAST(total_price AS STRING)
    END
    AS formatted_price_value,
  CASE
    WHEN running_total >= 1000000000
      THEN FORMAT('%.1fB', running_total / 1000000000)
    WHEN running_total >= 1000000 THEN FORMAT('%.1fM', running_total / 1000000)
    WHEN running_total >= 1000 THEN FORMAT('%.1fK', running_total / 1000)
    ELSE CAST(running_total AS STRING)
    END
    AS formatted_value
FROM real_running_total
ORDER BY year_month;
---------------------------------------------------------------------------------------------------



