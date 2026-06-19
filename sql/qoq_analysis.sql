```sql
USE healthcare_commercial_analytics;

SELECT
    dt.Year_Number,
    dt.Quarter_Name,
    SUM(fs.Revenue) AS Total_Revenue
FROM Fact_Sales fs
JOIN Dim_Time dt
    ON fs.Time_ID = dt.Time_ID
GROUP BY
    dt.Year_Number,
    dt.Quarter_Name
ORDER BY
    dt.Year_Number,
    dt.Quarter_Name;
```
