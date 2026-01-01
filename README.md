# 🛒 E-Commerce Customer Intelligence Dashboard

An **executive-grade analytics dashboard** built with **Python and Streamlit** to analyze customer behavior, revenue concentration, retention cohorts, and churn risk in an e-commerce business.

This project transforms raw transactional insights into **actionable intelligence** for leadership, growth, and retention teams.

## 🚀 Project Overview

The dashboard provides a **360° view of customers**, covering:

* Customer value distribution (RFM & revenue tiers)
* Retention and cohort behavior over time
* Churn intelligence and risk segmentation
* Executive-level KPIs and strategic recommendations

It is designed to simulate a **real-world analytics product** that a data analyst, data scientist, or business intelligence engineer would deliver to stakeholders.

## 🧠 Key Business Questions Answered

* Who are our highest-value customers?
* How concentrated is revenue among top segments?
* How well do customers retain after their first purchase?
* Which segments show high churn risk?
* Where should the business invest to maximize LTV?

## 📊 Dashboard Modules

### 1️⃣ Executive Overview

High-level KPIs for leadership:

* Total customers
* Total revenue
* Average revenue per customer
* Revenue concentration among top “champion” customers

### 2️⃣ Customer Value Analysis

* Customer segmentation by revenue tiers (Bronze, Silver, Gold, Platinum)
* Identification of high-impact customers
* Insights into upsell and monetization opportunities

### 3️⃣ Retention & Cohort Analysis

* Cohort-based customer retention tracking
* Month-over-month engagement patterns
* Identification of drop-off points in the customer lifecycle

### 4️⃣ Recommendations Engine

* Data-driven strategic recommendations
* Targeted actions for retention, loyalty, and revenue growth

### 5️⃣ Churn Intelligence (RFM Segments)

* Customer segmentation using **Recency, Frequency, Monetary (RFM)** analysis
* Distribution of customers across behavioral segments
* Early identification of churn-prone users

### 6️⃣ Churn Explainability

* Business-friendly explanations of churn risk
* Segment-level insights for marketing and retention teams

### 7️⃣ Executive Report

* Concise executive summary
* Key findings and strategic actions
* Downloadable report for leadership review

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – interactive dashboard framework
* **Pandas & NumPy** – data processing
* **Plotly** – interactive visualizations

## 📂 Project Structure

```
ecommerce-transaction-analytics/
├── dashboard/
│   ├── app.py
│   ├── utils.py
│   └── pages/
│       ├── 1_Executive.py
│       ├── 2_Customer_Value.py
│       ├── 3_Retention.py
│       ├── 4_Recommendations.py
│       ├── 5_Churn_Intelligence.py
│       ├── 6_Churn_Explainability.py
│       └── 7_Executive_Report.py
├── outputs/
│   ├── customer_cohort_heatmap.png
│   ├── customer_cohort_retention.csv
│   ├── customer_rfm_segments.csv
│   ├── customer_value_tiers.csv
│   └── executive_metrics_summary.csv
├── notebook/
│   └── 01_data_overview.ipynb
├── requirements.txt
└── README.md
```

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YashJadhav100/E-Commerce-Backend-Platform.git
cd ecommerce-transaction-analytics
```

### 2️⃣ (Optional but recommended) Create & activate a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Streamlit app

```bash
python -m streamlit run dashboard/app.py
```

---

### 5️⃣ Open in browser

## 📈 Outputs & Data

* The `outputs/` folder contains **pre-computed analytics results**
* These files allow the dashboard to run instantly without recomputation
* No sensitive or raw customer data is included

## 🎯 Why This Project Matters

This project demonstrates:

* End-to-end analytical thinking
* Business-oriented storytelling with data
* Dashboard design for non-technical stakeholders
* Practical customer analytics used in real companies

It reflects how analytics teams **turn data into decisions**, not just charts.

## 🔮 Future Enhancements

* Predictive churn modeling (ML)
* Automated cohort generation
* Live database integration
* Deployment on Streamlit Cloud or AWS
* Role-based dashboards for executives vs marketing teams

## 👤 Author

**Yash Jadhav**
Graduate Student, 
Computer Science

Syracuse University



