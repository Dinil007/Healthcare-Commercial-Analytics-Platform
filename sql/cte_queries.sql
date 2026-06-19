-- ==========================================
-- Common Table Expression (CTE) Example
-- Top Products by Revenue
-- ==========================================

WITH ProductRevenue AS (
    SELECT
        p.Product_Name,
        SUM(f.Revenue) AS Total_Revenue
    FROM Fact_Sales f
    JOIN Dim_Product p
        ON f.Product_ID = p.Product_ID
    GROUP BY p.Product_Name
)

SELECT *
FROM ProductRevenue
ORDER BY Total_Revenue DESC;