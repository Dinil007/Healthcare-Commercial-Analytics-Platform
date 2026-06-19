USE healthcare_commercial_analytics;

Top 5 Doctors by Quantity Sold
SELECT
    d.Doctor_Name,
    SUM(f.Quantity_Sold) AS Total_Quantity
FROM Fact_Sales f
JOIN Dim_Doctor d
ON f.Doctor_ID = d.Doctor_ID
GROUP BY d.Doctor_Name
ORDER BY Total_Quantity DESC
LIMIT 5;


Revenue by Sales Channel
SELECT
    Sales_Channel,
    SUM(Revenue) AS Total_Revenue
FROM Fact_Sales
GROUP BY Sales_Channel
ORDER BY Total_Revenue DESC;


Revenue by Customer Type
SELECT
    Customer_Type,
    SUM(Revenue) AS Total_Revenue
FROM Fact_Sales
GROUP BY Customer_Type;


Profit by Product
SELECT
    p.Product_Name,
    SUM(f.Profit) AS Total_Profit
FROM Fact_Sales f
JOIN Dim_Product p
ON f.Product_ID = p.Product_ID
GROUP BY p.Product_Name
ORDER BY Total_Profit DESC;


Top 5 Hospitals by Revenue
SELECT
    h.Hospital_Name,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Hospital h
ON f.Hospital_ID = h.Hospital_ID
GROUP BY h.Hospital_Name
ORDER BY Total_Revenue DESC
LIMIT 5;


Window Function
SELECT
    p.Product_Name,
    SUM(f.Revenue) AS Total_Revenue,
    RANK() OVER (ORDER BY SUM(f.Revenue) DESC) AS Revenue_Rank
FROM Fact_Sales f
JOIN Dim_Product p
ON f.Product_ID = p.Product_ID
GROUP BY p.Product_Name;