# Week 1 SQL Learning Log

## Overview

Week 1 focused on building fundamentals in:

- BigQuery
- SQL
- Window Functions
- Joins
- Subqueries
- dbt Core
- Data Quality Testing

---

# 01 July 2026

## BigQuery Setup

### Completed
- Created BigQuery environment
- Loaded Olist dataset into BigQuery
- Verified data in BigQuery console

### Learned
- Difference between Project, Dataset, and Table
- Basic querying in BigQuery
- Working with raw tables

---

# SQL Foundations

## Concepts Learned

### Common Table Expressions (CTEs)

Used CTEs to simplify SQL logic and improve readability.

Example:

```sql
WITH customer_orders AS (
    SELECT *
    FROM orders
)
SELECT *
FROM customer_orders;
```

### Window Functions

Learned and practiced:

- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- FIRST_VALUE()
- SUM() OVER()
- LAG()
- LEAD()

### Joins

Practiced:

- INNER JOIN
- LEFT JOIN
- FULL OUTER JOIN
- SELF JOIN

### Subqueries

Practiced:

- Basic subqueries
- Nested subqueries
- Filtering using subqueries

---

# Practice Queries Completed

## 1. Running Revenue Total

Concepts Used:
- SUM() OVER()
- Window Functions

Example:

```sql
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER (
        ORDER BY order_date
    ) AS running_total
FROM orders;
```

Business Purpose:
Track cumulative revenue growth over time.

---

## 2. Customer Lifetime Value (LTV)

Concepts Used:
- Aggregation
- DENSE_RANK()

Example:

```sql
DENSE_RANK() OVER (
    ORDER BY total_spend DESC
)
```

Business Purpose:
Identify highest-value customers.

---

## 3. Customer First and Latest Order

Concepts Used:
- FIRST_VALUE()

Business Purpose:
Understand customer purchase history.

---

## 4. Customers Who Ordered But Never Reviewed

Concepts Used:
- LEFT JOIN
- NULL Filtering

Business Purpose:
Identify missing customer feedback.

---

## 5. Sellers With Above-Average Delivery Time

Concepts Used:
- JOINS
- Aggregations
- Subqueries

Business Purpose:
Identify operational delays.

---

## 6. Products Bought Together

Concepts Used:
- SELF JOIN

Business Purpose:
Product affinity analysis.

---

# dbt Core

## Completed

### Day 05

Built:

- dbt Core project
- BigQuery connection
- profiles.yml configuration
- First staging model

Created:

- stg_orders

Verified:

```bash
dbt run
```

Successfully created model in BigQuery.

---

### Day 06

Built:

- sources.yml
- stg_orders
- stg_products
- stg_sellers
- stg_order_items

Implemented Data Quality Tests:

- not_null
- unique

Executed:

```bash
dbt test
```

Result:

✅ PASS = 5

✅ ERROR = 0

---

# Key Learnings

### SQL

- CTEs are easier to read and maintain than large nested subqueries.
- Window functions are critical for Analytics Engineering interviews.
- Joins are foundational for data modeling.
- Business questions should drive SQL development.

### BigQuery

- BigQuery acts as the central warehouse.
- Data should be modeled before analysis.

### dbt

- source() is used for raw warehouse tables.
- ref() is used for dbt-managed models.
- Data quality checks should be built into pipelines.

---

# Interview Questions Reviewed

### BigQuery

1. Difference between Project, Dataset, and Table

### SQL

2. RANK() vs DENSE_RANK() vs ROW_NUMBER()

3. LEFT JOIN vs INNER JOIN vs FULL OUTER JOIN

### Data Engineering

4. Handling API rate limiting in production pipelines

### dbt

5. What does dbt provide beyond raw SQL?

6. Difference between source() and ref()

---

# Week 1 Outcome

✅ BigQuery Setup Completed

✅ Olist Dataset Loaded

✅ Window Functions Practiced

✅ Joins & Subqueries Practiced

✅ dbt Installed & Configured

✅ Sources Created

✅ Staging Layer Built

✅ Data Quality Tests Passing

✅ GitHub Commits Completed

---

## Next Steps

Week 2:
- Intermediate dbt models
- Business logic transformations
- Fact and Dimension modeling
- Analytics Engineering best practices
