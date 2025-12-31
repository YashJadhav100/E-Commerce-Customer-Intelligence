import streamlit as st
from utils import load_output_csv
from datetime import date

st.title("📄 Executive Summary")

# Load executive metrics
metrics = load_output_csv("executive_metrics_summary.csv").iloc[0]

# ----------- ON-SCREEN SUMMARY -----------
st.markdown("""
## Key Findings
- Customer base scaled rapidly during 2017, followed by stabilization
- Revenue is highly concentrated within a small high-value (champion) segment
- Mid-tier customers present strong upsell and lifecycle growth potential

## Recommended Actions
- Invest in lifecycle-based retention programs
- Expand loyalty and tier-based incentives
- Develop predictive churn and engagement scoring
""")

# ----------- DOWNLOADABLE CONTENT -----------
report_text = f"""
EXECUTIVE SUMMARY
E-Commerce Customer Intelligence Dashboard
Generated on: {date.today().strftime('%B %d, %Y')}

--------------------------------------------------
BUSINESS CONTEXT
--------------------------------------------------
This report summarizes customer behavior, revenue concentration,
and churn risk patterns derived from transactional and RFM-based
customer analytics. The objective is to support data-driven
decisions across growth, retention, and customer strategy.

--------------------------------------------------
KEY METRICS SNAPSHOT
--------------------------------------------------
Total Customers: {int(metrics['total_customers']):,}
Total Revenue: ${metrics['total_revenue']:,.2f}
Average Revenue per Customer: ${metrics['avg_revenue_per_customer']:,.2f}
Champion Customers: {int(metrics['champions_count']):,}
Champion Revenue Share: {metrics['champions_revenue_share_pct']:.2f}%

--------------------------------------------------
STRATEGIC FINDINGS
--------------------------------------------------
1. Customer Growth
Customer acquisition accelerated significantly through 2017,
indicating strong market traction and demand generation.

2. Revenue Concentration
A small segment of high-value customers ("Champions") contributes
a disproportionate share of total revenue, increasing dependency
risk but also highlighting retention leverage.

3. Value Tier Opportunity
The majority of customers fall into mid-value tiers, representing
the highest opportunity for targeted upsell, bundling, and
engagement campaigns.

4. Churn Risk Signals
RFM segmentation reveals early warning indicators among low-recency
and low-frequency customers, enabling proactive churn mitigation.

--------------------------------------------------
RECOMMENDED ACTION PLAN
--------------------------------------------------
Short-Term (0–3 months)
- Implement lifecycle-based engagement after first purchase
- Launch targeted offers for mid-tier customers

Mid-Term (3–6 months)
- Expand loyalty tiers with differentiated incentives
- Introduce RFM-driven customer messaging

Long-Term (6–12 months)
- Build predictive churn models
- Integrate behavioral and transactional signals
- Track cohort movement and retention KPIs over time

--------------------------------------------------
NEXT PHASE ANALYTICS ROADMAP
--------------------------------------------------
- Full cohort retention matrix from raw transactions
- Customer Lifetime Value (CLV) forecasting
- Churn probability scoring and explainability
- Automated executive reporting

--------------------------------------------------
Prepared for strategic planning and leadership review.
"""

st.download_button(
    label="⬇️ Download Executive Summary",
    data=report_text,
    file_name="Executive_Customer_Intelligence_Summary.txt",
    mime="text/plain"
)
