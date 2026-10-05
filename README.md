# Vendor Performance Analysis
## 📌 Business Problem Statement
Effective inventory and sales management are critical for optimizing profitability in the retail and wholesale industry. Companies must ensure they do not incur losses due to inefficient pricing, poor inventory turnover, or over-dependency on specific vendors.

### 🎯 Key Objectives:
- **Underperforming Brands:** Identify brands needing promotional or pricing adjustments.
- **Top Vendor Contributions:** Determine top vendors driving sales and gross profit margins.
- **Bulk Purchasing Impact:** Analyze the effect of bulk volume purchasing on overall unit costs.
- **Inventory Turnover:** Assess inventory turnover rates to reduce holding costs and improve efficiency.
- **Profitability Variance:** Investigate profit margins between high-performing and low-performing vendors.

![Dashboard Preview](dashboard_preview.png)

## Final Recommendations

- Re-evaluate pricing for low-sales, high-margin brands to boost sales volume without sacrificing profitability.
- Diversify vendor partnerships to reduce dependency on a few suppliers and mitigate supply chain risks.
- Leverage bulk purchasing advantages to maintain competitive pricing while optimizing inventory management.
- Optimize slow-moving inventory by adjusting purchase quantities, launching clearance sales, or revising storage strategies.
- Enhance marketing and distribution strategies for low-performing vendors to drive higher sales volumes without compromising profit margins.
- By implementing these recommendations, the company can achieve sustainable profitability, mitigate risks, and enhance overall operational efficiency.

## 📌 Project Overview
This project presents an end-to-end data analytics solution for analyzing vendor sales, procurement costs, profit margins, and unsold capital risk. By integrating **Python**, **SQL (PostgreSQL)**, and **Power BI**, it empowers business stakeholders to identify high-performing vendors, monitor brand distribution, and eliminate inefficiencies in inventory management.

---

## 📊 Key Business Metrics
- **Total Sales:** $451.62M
- **Total Purchase:** $321.90M
- **Gross Profit:** $129.72M
- **Profit Margin:** 28.72%
- **Unsold Capital:** $8.75M
- **Top 10 Vendors Purchase Contribution:** 65.33%

---

## 🛠️ Tech Stack & Tools Used
- **Data Ingestion & ETL:** Python (`Pandas`, `SQLAlchemy`, `PostgreSQL`)
- **Exploratory Data Analysis (EDA):** Python (`Pandas`, `Matplotlib`, `Seaborn`)
- **Database Management:** PostgreSQL 16 / pgAdmin 4
- **Data Visualization & BI:** Power BI (`DAX`, `Power Query`, `Data Modeling`)

---

## 📂 Repository Structure

```text
Vendor_Performance_Analysis_Project/
│
├── logs/                      # System logs for ingestion and data execution
│   ├── ingestion_db.log
│   └── get_vendor_summary.log
│
├── scripts/                   # Python scripts for data ingestion and automation
│   └── ingestion_db.py
│
├── notebooks/                 # Jupyter Notebooks for exploratory data analysis
│   ├── Exploratory Data Analysis.ipynb
│   └── Vendor Performance Analysis.ipynb
│
├── Vendor_Performance_Dashboard.pbix   # Power BI Dashboard file
├── get_vendor_summary.txt              # Vendor metric summary text output
├── dashboard_preview.png               # High-resolution dashboard view
└── README.md                           # Project documentation
