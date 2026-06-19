```sql
-- =====================================================
-- Healthcare Commercial Analytics Platform
-- Stored Procedures
-- =====================================================

USE healthcare_commercial_analytics;

DELIMITER $$

CREATE PROCEDURE GetTopProducts()
BEGIN
    SELECT
        p.Product_Name,
        SUM(f.Revenue) AS Total_Revenue,
        SUM(f.Quantity_Sold) AS Total_Quantity
    FROM Fact_Sales f
    JOIN Dim_Product p
        ON f.Product_ID = p.Product_ID
    GROUP BY p.Product_Name
    ORDER BY Total_Revenue DESC
    LIMIT 5;
END $$

DELIMITER ;

-- Execute the procedure
CALL GetTopProducts();
```
