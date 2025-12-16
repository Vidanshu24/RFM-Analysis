# 📊 RFM Analysis Project – Retail Customer Segmentation

## 👋 Project Overview
This project focuses on understanding **customer purchasing behavior** using **RFM (Recency, Frequency, Monetary) analysis**.

The main goal is to identify:
- High-value customers
- Loyal customers
- Customers who are at risk of churning

The project is built end-to-end using **Python, SQL, and Power BI**.

---

## 🤔 What is RFM Analysis?
RFM analysis is a customer segmentation technique based on three factors:

- **Recency (R)** – How recently a customer made a purchase  
- **Frequency (F)** – How often a customer makes purchases  
- **Monetary (M)** – How much money a customer spends  

By combining these three values, customers can be grouped into meaningful segments.

---

## 🧰 Tools Used
- **Python** – Data cleaning and RFM scoring
- **MySQL (SQL)** – RFM metric calculation
- **Power BI** – Data visualization and dashboard creation

---

## 🔄 Project Workflow (Step by Step)

### 1️⃣ Data Cleaning (Python)
The raw retail data contained missing and invalid records. The following cleaning steps were performed:
- Removed records with missing Customer IDs
- Removed cancelled transactions
- Removed zero or negative quantity and price values
- Created a new column:  
  **Total Amount = Quantity × Unit Price**

📄 File: `python/rfm_clean.py`

---

### 2️⃣ RFM Metric Calculation (SQL)
After cleaning, the data was loaded into MySQL to calculate RFM metrics:
- **Recency** – Number of days since the last purchase
- **Frequency** – Number of unique invoices per customer
- **Monetary** – Total spending by each customer  

The final result was stored in a table named `rfm_scores`.

📄 File: `sql/rfm_queries.sql`

---

### 3️⃣ RFM Scoring & Customer Segmentation (Python)
Customers were scored using a quartile-based method:
- Each R, F, and M value was assigned a score from 1 to 4
- A combined **RFM Score** was calculated
- Customers were grouped into the following segments:
  - **Best Customers**
  - **Loyal Customers**
  - **Potential Loyalists**
  - **At Risk Customers**

📄 File: `python/rfm_analysis.py`

---

### 4️⃣ Power BI Dashboard
A Power BI dashboard was created to visualize customer insights:
- Customer distribution by RFM segment
- Revenue contribution by each segment
- Key performance indicators (KPIs)
- Interactive filters for analysis

📄 File: `powerbi/RFM_Analysis.pbix`

> ⚠️ GitHub cannot preview `.pbix` files.  
> The file can be downloaded and opened using **Power BI Desktop**.

---

## 📸 Dashboard Screenshots

### 🔹 RFM Dashboard Overview
![RFM Dashboard Overview](images/dashboard_overview.png)

### 🔹 Customer Segment Distribution
![Customer Segment Distribution](images/segment_distribution.png)

### 🔹 Key KPI Cards
![KPI Cards](images/kpi_cards.png)

---

## 📊 Business Value
This project helps businesses:
- Identify high-value and loyal customers
- Target the right customers with marketing campaigns
- Detect at-risk customers early
- Improve customer retention and lifetime value

---

## 📂 Dataset
Online Retail Dataset (Kaggle)  
A real-world retail transaction dataset used for customer analysis.

---

## ✅ Project Summary
This project demonstrates a **complete data analytics workflow**, starting from raw data cleaning and ending with business-ready insights through an interactive dashboard.

---

## 👤 Author
**Vidanshu Rautela**  
Aspiring Data Analyst  
Skills: Python | SQL | Power BI
