# ETL Workflow Diagram

```text
                +----------------------+
                |   Raw Sales Data      |
                | (CSV / Source Files)  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Data Validation     |
                | Missing Values        |
                | Duplicates            |
                | Data Type Checks      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   ETL Pipeline        |
                | Python + SQL          |
                | Cleaning & Transform  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  MySQL Data Warehouse |
                | Star Schema           |
                +----------+-----------+
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
+----------------------+        +----------------------+
| Python Analytics     |        | Machine Learning     |
| Correlation          |        | Regression           |
| Feature Engineering  |        | Churn Prediction     |
| Hypothesis Testing   |        | XGBoost              |
+-----------+----------+        +-----------+----------+
            |                               |
            +---------------+---------------+
                            |
                            v
                 +-------------------------+
                 | BI Dashboards           |
                 | Power BI & Tableau      |
                 +------------+------------+
                              |
                              v
                 +-------------------------+
                 | Business Insights       |
                 | Executive Reporting     |
                 +-------------------------+
```
