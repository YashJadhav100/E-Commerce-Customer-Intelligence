import streamlit as st
import plotly.express as px
from utils import load_output_csv

st.title("💰 Customer Value Tiers")

df = load_output_csv("customer_value_tiers.csv")

tier_counts = df["value_tier"].value_counts().reset_index()
tier_counts.columns = ["value_tier", "customers"]

fig = px.bar(
    tier_counts,
    x="value_tier",
    y="customers",
    color="value_tier",
    title="Customer Distribution by Value Tier"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 🧠 Insight
- Majority of customers fall into Bronze/Silver tiers
- Platinum customers represent high-value retention targets
""")
