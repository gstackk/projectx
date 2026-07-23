# 📦 SupplyPulse

AI-powered inventory risk monitoring platform built using BigQuery, dbt, Python and Streamlit.

SupplyPulse identifies products at risk of stockouts, provides natural-language inventory analysis using AI, and surfaces critical inventory alerts before stock is depleted.

---

## 🚨 Business Problem

Inventory stockouts cause lost sales, delayed fulfillment and poor customer experience.

Operations teams often rely on static reports and manual SQL queries to identify inventory risks.

SupplyPulse provides:

- Automated inventory risk monitoring
- Natural language inventory analysis
- Real-time critical stockout alerts
- Centralized inventory visibility

---

## ✅ Solution

SupplyPulse combines:

- BigQuery warehouse
- dbt transformation layer
- AI-powered SQL generation
- Streamlit dashboard
- Alert engine

to create a single inventory intelligence platform.

---

## 🏗 Architecture

```text
Inventory Data
      ↓
   BigQuery
      ↓
      dbt
      ↓
fct_stockout_risk
      ↓
 mart_alerts
      ↓
 Streamlit Dashboard
      ↓
 AI Copilot
      ↓
 Alert Engine
```

---

## 🤖 Features

### AI Inventory Copilot

Ask inventory questions using plain English.

Examples:

- Which SKUs run out in 3 days?
- Show all CRITICAL electronics
- Average days of stock remaining?

The AI converts questions into SQL and executes queries directly against BigQuery.

### Critical Stockout Alerts

Automatically identifies products at critical stockout risk and displays business alerts.

### Inventory Risk Dashboard

Provides:

- Products At Risk
- Critical Alerts
- High Alerts
- Average Days Remaining

### Risk Analytics

Visualizes inventory risk distribution and prioritizes inventory actions.

---

## 📸 Screenshots

## 📸 Dashboard

![Dashboard](screenshots/dashboard.png)

## 🤖 AI Copilot

![AI Copilot](screenshots/chatbot.png)

## 🧠 Natural Language to SQL

![Natural Language to SQL](screenshots/natural_language_to_sql.png)

## 🚨 Alert Engine

![Critical Alert](screenshots/critical_alert.png)

## 🏗 dbt Lineage

![dbt Lineage](screenshots/DBT_DAG-lineagegraph.png)

---

## 🛠 Technology Stack

- BigQuery
- dbt Core
- Python
- Streamlit
- Groq LLM
- SQL
- GitHub

---

## 🚀 How To Run

```bash
dbt build
```

```bash
python -m streamlit run app.py
```

Open the Streamlit application and begin querying inventory data.

---

## 💼 Business Impact

SupplyPulse helps operations teams:

- Identify stockout risk early
- Prioritize inventory replenishment
- Improve inventory visibility
- Reduce stockout-related revenue loss

---

## 🔮 Future Enhancements

- Automated email notifications
- Cloud Scheduler integration
- Cloud Run deployment
- Multi-warehouse support
- Forecasting enhancements

---

## 👤 Author

Gowtham R

Analytics Engineering & AI Data Products
