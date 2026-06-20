SELECT
    Time_ID,
    SUM(Revenue) AS Monthly_Revenue,
    SUM(SUM(Revenue)) OVER (
        ORDER BY Time_ID
        ROWS BETWEEN 11 PRECEDING AND CURRENT ROW
    ) AS Rolling_12_Month_Revenue
FROM Fact_Sales
GROUP BY Time_ID
ORDER BY Time_ID;