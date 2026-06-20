# KPI Definitions

| KPI                      | Description                                         | Formula                                                |
| ------------------------ | --------------------------------------------------- | ------------------------------------------------------ |
| Total Revenue            | Total income generated from all sales               | `SUM(Revenue)`                                         |
| Total Profit             | Total profit earned from all sales                  | `SUM(Profit)`                                          |
| Total Quantity Sold      | Total units sold                                    | `SUM(Quantity_Sold)`                                   |
| Total Sales              | Total number of sales transactions                  | `COUNT(Sale_ID)`                                       |
| Average Revenue          | Average revenue per transaction                     | `AVERAGE(Revenue)`                                     |
| Revenue by Product       | Revenue grouped by product                          | `SUM(Revenue) GROUP BY Product`                        |
| Revenue by Region        | Revenue grouped by region                           | `SUM(Revenue) GROUP BY Region`                         |
| Revenue by Sales Channel | Revenue grouped by sales channel                    | `SUM(Revenue) GROUP BY Sales_Channel`                  |
| Revenue by Customer Type | Revenue grouped by customer type                    | `SUM(Revenue) GROUP BY Customer_Type`                  |
| Top Products             | Products ranked by highest revenue                  | `ORDER BY Revenue DESC`                                |
| Doctor Churn Rate        | Percentage of doctors predicted to stop prescribing | Classification model output                            |
| Forecasted Revenue       | Predicted future revenue using ML models            | Linear Regression / Random Forest / XGBoost prediction |
