import streamlit as st
from utils import load_output_csv

st.title("📌 Executive Overview")

df = load_output_csv("executive_metrics_summary.csv")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Customers", f"{int(df['total_customers'][0]):,}")
c2.metric("Total Revenue", f"${df['total_revenue'][0]:,.0f}")
c3.metric("Avg Revenue / Customer", f"${df['avg_revenue_per_customer'][0]:.2f}")
c4.metric("Champions Count", int(df['champions_count'][0]))

st.markdown("""
### 🧠 Executive Insights
- Revenue is concentrated among a small champion segment
- Large customer base with moderate average value
- Clear opportunity for tier-based upsell strategies
""")
