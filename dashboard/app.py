import streamlit as st

st.set_page_config(
    page_title="E-Commerce Customer Intelligence",
    page_icon="📊",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style="margin-bottom:0.2em;">📈 E-Commerce Customer Intelligence Dashboard</h1>
    <p style="font-size:1.1rem; color:#cfcfcf;">
    Executive-grade analytics platform for understanding customer value, cohort behavior,
    churn risk, and strategic growth opportunities.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- WHAT THIS DASHBOARD DOES ----------
st.subheader("🎯 What This Dashboard Solves")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        **Business Questions Answered**
        - Who are our most valuable customers?
        - How is customer acquisition evolving over time?
        - Which customer segments are at risk of churn?
        - Where should we focus retention and upsell efforts?
        """
    )

with col2:
    st.markdown(
        """
        **Who This Is For**
        - Product Managers
        - Growth & Marketing Teams
        - Customer Success
        - Executive & Strategy Teams
        """
    )

st.divider()

# ---------- HOW TO USE ----------
st.subheader("🧭 How to Use the Dashboard")

st.markdown(
    """
    Use the navigation panel on the left to explore different analytical views:

    - **Executive** – High-level KPIs and business summary  
    - **Customer Value** – Revenue tiers and value distribution  
    - **Retention** – Cohort-based customer growth insights  
    - **Recommendations** – Actionable strategies driven by data  
    - **Churn Intelligence** – RFM-based churn risk segmentation  
    - **Churn Explainability** – Why customers churn and how to prevent it  
    - **Executive Report** – Summary insights for leadership
    """
)

st.divider()

# ---------- ANALYTICS PHILOSOPHY ----------
st.subheader("🧠 Analytics Philosophy")

st.markdown(
    """
    This dashboard is designed with a **decision-first mindset**:
    - No vanity metrics
    - No misleading charts
    - Clear mapping from data → insight → action

    All visuals are aligned with the **actual structure of the underlying data** and
    are intended to support real business decisions.
    """
)

st.divider()

# ---------- FOOTER / STATUS ----------
st.success("Select a section from the left sidebar to begin exploring insights.")
