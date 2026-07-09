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

**build 1)**
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

***Build 2)***
 **Top lifetime valued Customers:**
SELECT
  orders.customer_id,
  SUM(sales.price) AS total_price,
  DENSE_RANK() OVER (
    ORDER BY SUM(sales.price) DESC
  ) AS customer_rank
FROM `vf-grp-gbissdbx-dev-1.gsamples_olists.olists_raw_csv` orders
JOIN `vf-grp-gbissdbx-dev-1.gsamples_olists.rank_samples` sales
  ON orders.order_id = sales.order_id
GROUP BY orders.customer_id
limit 10;

**Build 3)**
 **Finding first and last customer order:**

SELECT
  customer_id,
  order_delivered_customer_date,
  FIRST_VALUE(order_delivered_customer_date IGNORE NULLS) OVER (ORDER BY order_delivered_customer_date asc) AS first_order_default_window_ignoring_nulls,
  FIRST_VALUE(order_delivered_customer_date IGNORE NULLS) OVER (ORDER BY order_delivered_customer_date desc ) AS latest_order_full_window_ignoring_nulls 
FROM
  `vf-grp-gbissdbx-dev-1`.`gsamples_olists`.`olists_raw_csv` AS orders;
---------------------------------------------------------------------------------------------------
**Day 3**
**Python for Data ingestion through API's :**
-> have used json file which we convert from API because of an error, but loaded the json with the required columns and created a table in big query.

import json
import pandas as pd
import pandas as pd

df = pd.DataFrame(list(data["rates"].items()), columns=["currency", "rate"])
df["base"] = data["base_code"]
df["timestamp"] = data["time_last_update_utc"]

print(df)
from google.cloud import bigquery

# Create client
client = bigquery.Client(project='vf-grp-gbissdbx-dev-1')

**# Define table (change this)**
table_id = table_id = "vf-grp-gbissdbx-dev-1.gsamples_olists.exchange_rates"
# Load dataframe
job = client.load_table_from_dataframe(df, table_id)
job.result()  # wait until done
print("✅ Data loaded to BigQuery")

good for creating tables in BQ and automating the live data fetching from internet.

how do we handle API rate limitting in data pipelines:
Answer -
in the data pipeline, we can handle the API rate limit by controlling how frequently the pipeline calls the external API's.
we can also reduce calls by storing data and avoid duplicates in pipeline.

--------------------------------------------------------------------------------------------------------

**Day 4:**
**SQL Hard: Joins + Subqueries**

