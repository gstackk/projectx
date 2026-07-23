# 📦 SupplyPulse

AI-powered inventory risk monitoring platform built using BigQuery, dbt, Python, Streamlit and AI.

SupplyPulse helps operations teams identify stockout risks before inventory is depleted, prioritize replenishment actions, and analyze inventory using natural language instead of manual SQL queries.

---

# 🚨 Business Problem

Inventory stockouts can lead to:

- Lost sales opportunities
- Delayed order fulfillment
- Poor customer experience
- Increased operational costs
- Reactive inventory management

Operations teams often rely on static reports and manual SQL queries to identify inventory risks.

SupplyPulse provides a centralized inventory intelligence platform that surfaces risk early and enables faster decisions.

---


# Test

![Dashboard](screenshots/dashboard.png)

![Dashboard](./screenshots/dashboard.png)
![Dashboard](screenshots/dashboard.png)

# ✅ Solution

SupplyPulse combines:

- BigQuery data warehouse
- dbt transformation layer
- AI-powered natural language querying
- Streamlit application
- Inventory alert engine

into a single inventory monitoring platform.

---

# 🏗 Architecture

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

# 🤖 Key Features

## AI Inventory Copilot

Ask inventory questions using plain English.

Examples:

- Which SKUs run out in 3 days?
- Show all CRITICAL electronics
- Average days of stock remaining?

The AI converts business questions into SQL and executes them directly against BigQuery.

---

## 🚨 Critical Stockout Alert Engine

Automatically identifies products at CRITICAL stockout risk and surfaces inventory alerts requiring immediate action.

---

## 📊 Inventory Risk Dashboard

Provides visibility into:

- Products At Risk
- Critical Alerts
- High Alerts
- Average Days Remaining

---

## 📈 Risk Analytics

Visualizes inventory risk distribution and helps prioritize inventory actions.

---

# 📸 Product Walkthrough

### Dashboard Overview

![Dashboard](screenshots/dashboard.png)

The dashboard provides inventory visibility, stockout monitoring, KPI tracking and operational alerts.

---

### AI Inventory Copilot

![AI Copilot](screenshots/chatbot.png)

Users can ask inventory questions in natural language and receive inventory insights immediately.

---

### Natural Language → SQL

![Natural Language to SQL](screenshots/natural_language_to_sql.png)

Business questions are automatically converted into SQL and executed against BigQuery.

---

### Critical Stockout Alert Engine

![Critical Alert](screenshots/critical_alert.png)

Products requiring immediate operational attention are surfaced automatically.

---

### dbt Lineage

![dbt Lineage](screenshots/DBT_DAG-lineagegraph.png)

Analytics engineering workflow built using staging, intermediate, fact and mart layers.

---

# 🛠 Technology Stack

### Data Warehouse

- BigQuery

### Data Transformation

- dbt Core

### Application Layer

- Streamlit

### Programming

- Python

### AI Layer

- Groq LLM
- Natural Language → SQL

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
supplypulse-ai-inventory-monitor
│
├── screenshots/
├── architecture/
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── marts/
│
├── app.py
├── alerts.py
├── nl_to_sql.py
├── requirements.txt
└── README.md
```

---

# 🚀 How To Run

### Build Warehouse

```bash
dbt build
```

### Launch Dashboard

```bash
python -m streamlit run app.py
```

Open the Streamlit application and begin querying inventory data.

---

# 💼 Business Impact

SupplyPulse helps inventory and operations teams:

- Detect stockout risk early
- Prioritize replenishment decisions
- Reduce manual analysis effort
- Improve inventory visibility
- Surface critical products requiring immediate review

---

# 🔮 Future Enhancements

- Email notifications
- Cloud Scheduler automation
- Cloud Run deployment
- Forecasting enhancements
- Multi-location inventory monitoring

---

# 👤 Author

**Gowtham R**

Analytics Engineering • BigQuery • dbt • Python • AI Data Products
