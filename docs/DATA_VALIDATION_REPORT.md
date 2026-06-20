# Data Validation Report

## Overview

This document summarizes the data quality validation process performed during the ETL pipeline for the **Healthcare Commercial Analytics Platform**. The objective was to ensure that the dataset loaded into the analytics platform is accurate, consistent, and suitable for SQL analysis, business intelligence dashboards, and machine learning models.

---

## 📌 Validation Objectives

The validation process was designed to:

* Ensure data completeness and consistency.
* Detect and handle missing values.
* Identify duplicate records.
* Verify numeric fields for invalid values.
* Validate date formats and identifiers.
* Improve data quality before loading into the data warehouse.

---

## Validation Checks Performed

* **Missing Values:** Checked all columns for null or missing values before processing. ✅ Passed
* **Duplicate Records:** Verified the dataset for duplicate records and handled duplicates during the ETL process. ✅ Passed
* **Revenue Validation:** Confirmed that all revenue values were valid and non-negative. ✅ Passed
* **Quantity Validation:** Verified that `Quantity_Sold` contained valid positive values. ✅ Passed
* **Date Validation:** Ensured that date fields followed the expected format and contained valid values. ✅ Passed
* **Foreign Key Validation:** Verified that Doctor, Product, Hospital, Region, and Time IDs were consistent with the corresponding dimension tables. ✅ Passed
* **Data Type Validation:** Confirmed that numeric and categorical columns used appropriate data types for analytics and reporting. ✅ Passed


## 🔄 ETL Data Cleaning Process

The ETL pipeline included the following preprocessing steps:

1. Loaded raw healthcare sales data from CSV files.
2. Inspected the dataset for missing values.
3. Checked for duplicate records and removed them when necessary.
4. Standardized data formats and column types.
5. Validated revenue and quantity fields to prevent invalid values.
6. Verified identifier columns used for joins with dimension tables.
7. Prepared the cleaned dataset for loading into the MySQL data warehouse.

---

## 🎯 Validation Outcome

After applying the validation checks, the dataset was considered suitable for:

* Business Intelligence reporting
* SQL analytics
* Revenue forecasting
* Machine learning model training
* Doctor churn prediction
* Power BI dashboards
* Tableau dashboards

No critical data quality issues remained after preprocessing.

---

## 🏁 Conclusion

The data validation process improved the reliability and consistency of the healthcare sales dataset. Performing these checks before analysis helps ensure accurate reporting, trustworthy machine learning predictions, and better business decision-making.
