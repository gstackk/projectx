
import streamlit as st
from google.cloud import bigquery
from groq import Groq
from dotenv import load_dotenv
import os

# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="Your Product Name",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Your Product Name")

st.markdown(
    """
    ### AI-Powered Inventory Monitoring

    Replace this description with your business problem.
    """
)

# -------------------------
# CONFIGURATION
# -------------------------

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("YOUR_API_KEY")
)

# -------------------------
# SCHEMA CONFIGURATION
# -------------------------

SCHEMA = """
Table:
your_dataset.your_table

Columns:
column_1
column_2
column_3
"""

SYSTEM_PROMPT = f"""
You are a BigQuery SQL expert.

Return ONLY valid BigQuery SQL.

Rules:
- Return SQL only
- No explanations
- No markdown
- SELECT statements only
- Use only approved tables

Schema:

{SCHEMA}
"""

# -------------------------
# AI COPILOT
# -------------------------

def generate_sql(question):

    response = groq_client.chat.completions.create(
        model="your_model",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    sql = response.choices[0].message.content.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()

# -------------------------
# BIGQUERY CONNECTION
# -------------------------

# Replace 'your_dataset'
# with your own dataset name.

client = bigquery.Client()

query = """
SELECT *
FROM your_dataset.your_table
"""

df = client.query(query).to_dataframe()

# -------------------------
# DASHBOARD FILTERS
# -------------------------

st.sidebar.header("Filters")

filter_selection = st.sidebar.multiselect(
    "Select Filter",
    options=[],
    default=[]
)

# -------------------------
# KPI CARDS
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Metric 1", 0)

with col2:
    st.metric("Metric 2", 0)

with col3:
    st.metric("Metric 3", 0)

with col4:
    st.metric("Metric 4", 0)

# -------------------------
# ALERT ENGINE
# -------------------------

alert_count = 0

if alert_count > 0:

    st.error(
        f"🚨 ALERT: {alert_count} items require attention."
    )

else:

    st.success(
        "✅ No critical risks detected."
    )

# -------------------------
# AI COPILOT UI
# -------------------------

st.markdown("---")

st.subheader("🤖 AI Copilot")

st.caption(
    "Ask business questions in plain English."
)

question = st.text_input(
    "",
    placeholder="Ask your question..."
)

run_ai = st.button(
    "🚀 Ask AI"
)

# -------------------------
# BUSINESS IMPACT
# -------------------------

st.info(
    """
    🎯 Business Impact

    Explain why the project matters.
    """
)

# -------------------------
# INVENTORY ALERTS
# -------------------------

st.subheader("🚨 Current Alerts")

st.dataframe(df)

# -------------------------
# RISK DISTRIBUTION
# -------------------------

st.subheader("Risk Distribution")

st.bar_chart(df)

# -------------------------
# AI QUERY EXECUTION
# -------------------------

if run_ai and question:

    try:

        sql = generate_sql(question)

        st.subheader("Generated SQL")

        st.code(
            sql,
            language="sql"
        )

        query_job = client.query(sql)

        results_df = query_job.to_dataframe()

        st.subheader("Results")

        st.dataframe(results_df)

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )
