# ProjectX — Analytics Engineering Journey

## 🎯 Main Goal

This repository follows the Agent-X 90 Day Roadmap.

Goal:
Become an Analytics Engineer capable of building AI-powered data systems using:

- BigQuery
- SQL
- Python
- dbt Core
- GCP
- OpenAI API
- Streamlit

Roadmap:
See AgentX_90Days.html

Week 1 focused on:
- BigQuery setup
- SQL fundamentals
- Window functions
- Joins and subqueries
- dbt Core
- Staging layer
- Data quality testing

---

## 🧱 Architecture

```text
┌─────────────────┐
│ Olist CSV Files │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ BigQuery Raw    │
│ Tables          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ dbt Sources     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Staging Models  │
│ stg_orders      │
│ stg_products    │
│ stg_sellers     │
│ stg_order_items │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Data Tests      │
│ not_null        │
│ unique          │
└─────────────────┘
