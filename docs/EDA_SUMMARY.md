# Exploratory Data Analysis (EDA) Summary

This document summarizes the insights and findings obtained from the Exploratory Data Analysis (EDA) of the healthcare sales dataset (`healthcare_sales_100k.csv`).

---

## 📊 Summary Statistics

The dataset contains **100,000 rows** of commercial sales data. Below is a summary of key metrics:

| Metric | Minimum | Average (Mean) | Median (50%) | Maximum | Standard Deviation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Quantity Sold** | 1 unit | 251 units | 251 units | 500 units | 144.48 |
| **Unit Price** | $100.00 | $2,545.83 | $2,537.00 | $5,000.00 | $1,416.91 |
| **Discount** | 0.00% | 12.53% | 12.53% | 25.00% | 7.21% |
| **Revenue** | $129.00 | $638,613.16 | $480,761.00 | $2,489,004.00 | $550,943.50 |
| **Profit** | $27.79 | $175,622.00 | $125,962.46 | $967,565.61 | $163,203.05 |

---

## 🏷️ Categorical Variable Distribution

- **Sales Channel** (4 unique values):
  - *Top*: Retail Pharmacy (25,132 occurrences)
  - *Others*: Online, Distributor, Institutional Hospital.
- **Payment Type** (4 unique values):
  - *Top*: UPI (25,179 occurrences)
  - *Others*: Credit Card, Debit Card, Cash.
- **Customer Type** (2 unique values):
  - *Top*: New (50,199 occurrences)
  - *Others*: Returning (49,801 occurrences)

---

## 🔍 Key Insights

### 1. Revenue Correlation
- Strong positive correlation between **Quantity_Sold** and **Revenue**.
- Strong positive correlation between **Unit_Price** and **Revenue**.
- **Discount** has a minor moderating impact on total revenue.

### 2. Outlier Detection
- The outlier detection process (using the IQR method) showed that the `Revenue` column contains no extreme mathematical outliers due to a uniform/normal synthetic distribution, though high-value accounts represent significant leverage points.

### 3. Customer Segments
- The dataset is evenly split between **New** (50.2%) and **Returning** (49.8%) customers.
- Hypothesis testing (T-Test) confirmed **no statistically significant difference** in average revenue between New and Returning customers ($p\text{-value} = 0.7250$).
