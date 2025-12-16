# 📊 RFM Analysis – Retail Customer Segmentation

## 🔍 Project Objective
The goal of this project is to analyze customer purchasing behavior using **RFM (Recency, Frequency, Monetary) analysis** and segment customers into actionable business categories such as **Best Customers, Loyal Customers, Potential Loyalists, and At Risk customers**.

This project demonstrates an **end-to-end data analytics workflow** using Python, SQL, and Power BI.

---

## 🧰 Tech Stack
- **Python**: Data cleaning, RFM scoring & segmentation
- **MySQL**: RFM metric calculation
- **Power BI**: Interactive dashboard & insights

---

## 📁 Project Workflow

### 1️⃣ Data Cleaning (Python)
- Removed null customer IDs
- Removed cancelled transactions
- Removed zero/negative quantity & price
- Created `Total Amount = Quantity × Price`

📄 File: `python/rfm_clean.py`

---

### 2️⃣ RFM Metric Calculation (SQL)
- **Recency**: Days since last purchase
- **Frequency**: Number of unique invoices
- **Monetary**: Total customer spending
- Stored results in `rfm_scores` table

📄 File: `sql/rfm_queries.sql`

---

### 3️⃣ RFM Scoring & Segmentation (Python)
- Quartile-based scoring using `pd.qcut()`
- Created:
  - R Score
  - F Score
  - M Score
  - RFM Score
- Business Segments:
  - Best Customers
  - Loyal Customers
  - Potential Loyalists
  - At Risk

📄 File: `python/rfm_analysis.py`

---

### 4️⃣ Power BI Dashboard
- Customer distribution by segment
- Revenue contribution by segment
- Key KPIs (Total Customers, Avg Monetary Value)
- Segment-based filtering

📄 File: `powerbi/RFM_Analysis.pbix`

---

## 📊 Business Impact
- Identifies high-value customers for retention
- Helps design targeted marketing campaigns
- Improves customer lifetime value (CLV)
- Reduces churn by identifying at-risk customers

---

## 📂 Dataset
Online Retail Dataset (Kaggle)

---

## 🚀 Conclusion
This project showcases strong skills in **data cleaning, SQL analytics, customer segmentation, and dashboard storytelling**, aligned with real-world business use cases.
