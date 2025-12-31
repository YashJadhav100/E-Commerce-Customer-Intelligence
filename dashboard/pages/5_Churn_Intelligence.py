import streamlit as st
import plotly.express as px
from utils import load_output_csv

st.title("🚨 Churn Intelligence (RFM Segments)")

# Load raw RFM data
df = load_output_csv("customer_rfm_segments.csv")

# Aggregate customers per segment
segment_counts = (
    df.groupby("segment")
      .size()
      .reset_index(name="customer_count")
)

fig = px.pie(
    segment_counts,
    names="segment",
    values="customer_count",
    title="Customer Distribution by RFM Segment",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 🧠 Churn Risk Interpretation
- **Low-Value / At-Risk segments** indicate churn exposure
- **Champions & Loyal customers** should be protected via rewards
- Segment movement over time is a key retention KPI
""")
