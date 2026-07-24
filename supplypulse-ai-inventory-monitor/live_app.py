import streamlit as st
#from groq import Groq
#from dotenv import load_dotenv
#from alerts import get_critical_alerts
import os

st.set_page_config(
    page_title="SupplyPulse",
    page_icon="📦",
    layout="wide"
)

st.title("📦 SupplyPulse")

st.markdown(
    """
    ### AI-Powered Inventory Risk Monitoring

    Detect stockout risks, ask inventory questions
    in natural language, and surface critical alerts.
    """
)

import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).parent

df = pd.read_csv(BASE_DIR / "demo_inventory.csv")

st.sidebar.header("Filters")
st.sidebar.markdown("---")




risk_filter = st.sidebar.multiselect(
    "Risk Level",
    options=df["risk_level"].unique(),
    default=df["risk_level"].unique()
)

filtered_df = df[
    df["risk_level"].isin(risk_filter)
]

def color_risk(val):
    if val == "CRITICAL":
        return "background-color: red; color: white"
    elif val == "HIGH":
        return "background-color: orange"
    return ""

avg_days = round(
    filtered_df["days_of_stock_remaining"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Products At Risk",
        len(filtered_df)
    )

with col2:
    st.metric(
        "🚨 Critical Alerts",
        len(
            filtered_df[
                filtered_df["risk_level"] == "CRITICAL"
            ]
        )
    )

with col3:
    st.metric(
        "⚠️ High Alerts",
        len(
            filtered_df[
                filtered_df["risk_level"] == "HIGH"
            ]
        )
    )

with col4:
    st.metric(
        "⏳ Avg Days Remaining",
        avg_days
    )
critical_count = len(
    filtered_df[
        filtered_df["risk_level"] == "CRITICAL"
    ]
)

if critical_count > 0:

    st.error(
        f"🚨 CRITICAL STOCKOUT ALERT: {critical_count} products require immediate attention."
    )

else:

    st.success(
        "✅ No critical stockout risks detected."
    )
st.markdown("---")

st.subheader("🤖 SupplyPulse AI Copilot")

st.caption(
    "Ask inventory questions in plain English. AI converts questions to SQL and queries BigQuery automatically."
)

question = st.text_input(
    "",
    placeholder="Ask: Which SKUs run out in 3 days?"
)

run_ai = st.button(
    "🚀 Ask SupplyPulse AI"
)
st.info(
    """
    🎯 Business Impact

    SupplyPulse helps operations teams identify stockout
    risks before inventory depletion, prioritize inventory
    replenishment, and reduce lost sales from unavailable stock.
    """
)
st.subheader("🚨 Current Inventory Alerts")
styled_df = filtered_df.style.map(
    color_risk,
    subset=["risk_level"]
)

st.dataframe(styled_df)

risk_summary = (
    filtered_df.groupby("risk_level")
      .size()
      .reset_index(name="count")
      .set_index("risk_level")
)

st.subheader("Risk Distribution")
st.bar_chart(risk_summary)
if run_ai:

    st.info(
        """
        Demo Mode

        AI Copilot disabled in public demo version.

        Full implementation available in GitHub repository.
        """
    )
