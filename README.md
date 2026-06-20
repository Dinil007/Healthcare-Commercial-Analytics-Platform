# 🏥 Healthcare Commercial Analytics Platform

An end-to-end **Healthcare Commercial Analytics Platform**  This project combines **SQL, Python, Machine Learning, Power BI, Tableau, and Big Data concepts** to transform healthcare sales data into actionable business insights.

---

# 📌 Business Problem

Pharmaceutical companies need to understand product performance, regional sales trends, customer behavior, and future revenue opportunities. This platform provides a centralized analytics solution to support data-driven commercial decisions.

Key questions addressed:

* Which products generate the highest revenue?
* Which regions perform best?
* Which sales channels are most effective?
* How can future revenue be forecasted?
* Which doctors are likely to stop prescribing products?

---

# 🚀 Key Features

* 📊 Interactive Power BI Dashboard
* 📈 Tableau Executive Dashboard
* 🗄️ MySQL Data Warehouse with Star Schema
* 🔄 ETL Pipeline using Python
* 🤖 Machine Learning Models

  * Linear Regression
  * Random Forest
  * XGBoost
  * Doctor Churn Prediction
* 📑 Advanced SQL (CTEs, Views, Stored Procedures)
* 📉 Revenue Forecasting
* 📊 Correlation Analysis
* 📈 Feature Importance Analysis
* 📦 Hadoop, Hive, Spark Demonstrations
* 📝 SAS Examples

---

# 🛠️ Technology Stack

| Category              | Technologies               |
| --------------------- | -------------------------- |
| Programming           | Python, SQL                |
| Database              | MySQL                      |
| Data Analysis         | Pandas, NumPy              |
| Machine Learning      | Scikit-learn, XGBoost      |
| Business Intelligence | Power BI, Tableau          |
| Visualization         | Matplotlib                 |
| Big Data              | Hadoop, Hive, Apache Spark |
| Statistical Tools     | SAS                        |
| Version Control       | Git, GitHub                |

---

# 🏗️ Architecture

```
CSV Dataset
      │
      ▼
Python ETL Pipeline
      │
      ▼
MySQL Data Warehouse
      │
 ┌────┴─────────────┐
 ▼                  ▼
Power BI        Tableau
 │                  │
 └────────┬─────────┘
          ▼
Machine Learning Models
          │
          ▼
Business Insights & Forecasting
```

---

# ⭐ Star Schema

```
                 +---------------+
                 |  Dim_Doctor   |
                 +---------------+
                        |
+-------------+  +---------------+  +--------------+
| Dim_Product |--|   Fact_Sales  |--| Dim_Hospital |
+-------------+  +---------------+  +--------------+
                        |
                +---------------+
                |  Dim_Region   |
                +---------------+
                        |
                +---------------+
                |   Dim_Time    |
                +---------------+
```

---

# 📊 Dashboards

## Power BI

* KPI Cards
* Revenue Analysis
* Product Performance
* Regional Analysis
* Sales Channel Analysis
* Customer Type Analysis
* Interactive Filters

## Tableau

* Revenue by Product
* Revenue by Region
* Revenue by Sales Channel
* Revenue by Customer Type
* Executive Dashboard

---

# 🤖 Machine Learning Models

| Model                   | Purpose                                    |
| ----------------------- | ------------------------------------------ |
| Linear Regression       | Revenue Forecasting                        |
| Random Forest           | Revenue Prediction                         |
| XGBoost                 | Advanced Revenue Prediction                |
| Doctor Churn Prediction | Predict doctors likely to stop prescribing |

---

# 📈 Python Analytics

* Correlation Matrix
* Descriptive Statistics
* Feature Importance
* Outlier Detection

---

# 🗄️ SQL Features

* Star Schema Design
* Fact & Dimension Tables
* Common Table Expressions (CTEs)
* Views
* Stored Procedures
* Revenue Analysis
* Product Analysis
* Regional Analysis
* Year-over-Year (YoY) Analysis
* Quarter-over-Quarter (QoQ) Analysis

---

# 📁 Project Structure

```text
Healthcare-Commercial-Analytics-Platform/
├── data/
├── sql/
├── python/
├── ml/
├── powerbi/
├── tableau/
├── sas/
├── docs/
├── screenshots/
└── README.md
```

---

# ▶️ How to Run

1. Clone the repository.
2. Import SQL scripts into MySQL.
3. Load the dataset into Power BI or Tableau.
4. Run Python scripts for analytics and machine learning.
5. Review dashboards and documentation.

---

# 📂 Documentation

The `docs/` folder contains:

* Data Dictionary
* KPI Definitions
* Business Insights
* Future Enhancements
* Star Schema
* System Architecture
* Hadoop Demo
* Hive Demo
* Spark Demo

---

# 🔮 Future Enhancements

* Real-time streaming analytics
* Cloud deployment (AWS/Azure/GCP)
* REST API for predictions
* Docker containerization
* Automated ETL scheduling
* Deep learning forecasting models

---

# 👨‍💻 Author

Developed as an end-to-end portfolio project demonstrating practical skills in **Healthcare Analytics, Data Engineering, Business Intelligence, SQL, Python, and Machine Learning**.
