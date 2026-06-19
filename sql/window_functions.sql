Running Total query

SELECT
    Sale_ID,
    Revenue,
    SUM(Revenue) OVER (
        ORDER BY Sale_ID
    ) AS Running_Total
FROM Fact_Sales
LIMIT 20;


Rolling Revenue query

SELECT
    Sale_ID,
    Revenue,
    SUM(Revenue) OVER (
        ORDER BY Sale_ID
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS Rolling_3_Record_Revenue
FROM Fact_Sales
ORDER BY Sale_ID
LIMIT 20;