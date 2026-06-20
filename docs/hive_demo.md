# Hive Demonstration

## Objective
Use Apache Hive to query large healthcare sales datasets stored in Hadoop.

## Create External Table

```sql
CREATE EXTERNAL TABLE healthcare_sales (
    Sale_ID INT,
    Doctor_ID INT,
    Hospital_ID INT,
    Product_ID INT,
    Region_ID INT,
    Time_ID INT,
    Quantity_Sold INT,
    Revenue DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

## Sample Queries

### Total Revenue

```sql
SELECT SUM(Revenue) AS Total_Revenue
FROM healthcare_sales;
```

### Revenue by Product

```sql
SELECT Product_ID,
       SUM(Revenue) AS Total_Revenue
FROM healthcare_sales
GROUP BY Product_ID;
```

### Top 5 Regions by Revenue

```sql
SELECT Region_ID,
       SUM(Revenue) AS Total_Revenue
FROM healthcare_sales
GROUP BY Region_ID
ORDER BY Total_Revenue DESC
LIMIT 5;
```

## Benefits

- SQL-like interface for big data
- Easy aggregation and reporting
- Integrates with Hadoop