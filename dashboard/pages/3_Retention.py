import streamlit as st
import plotly.express as px
from utils import load_output_csv

st.title("📊 Customer Cohort Growth (Month 0)")

df = load_output_csv("customer_cohort_retention.csv")

df["cohort_month"] = df["cohort_month"].astype(str)

fig = px.line(
    df,
    x="cohort_month",
    y="0",
    markers=True,
    title="Customer Count by Cohort (Initial Month)"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 🧠 Cohort Insight
- Customer acquisition accelerated through 2017
- Growth stabilized entering 2018
- This represents **cohort size**, not retention decay
""")
