```sql
-- =====================================================
-- Healthcare Commercial Analytics Platform
-- SQL Views
-- =====================================================

USE healthcare_commercial_analytics;

-- -----------------------------------------
-- View: Product Revenue Summary
-- -----------------------------------------
CREATE OR REPLACE VIEW vw_product_revenue AS
SELECT
    p.Product_Name,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Quantity_Sold) AS Total_Quantity
FROM Fact_Sales f
JOIN Dim_Product p
    ON f.Product_ID = p.Product_ID
GROUP BY p.Product_Name;

-- Test the view
SELECT * FROM vw_product_revenue;
```
