/* Import healthcare sales data */
PROC IMPORT DATAFILE="healthcare_sales_100k.csv"
    OUT=healthcare_sales
    DBMS=CSV
    REPLACE;
    GETNAMES=YES;
RUN;

/* PROC SQL: Total Revenue */
PROC SQL;
    SELECT SUM(Revenue) AS Total_Revenue
    FROM healthcare_sales;
QUIT;

/* PROC FREQ: Customer Type Distribution */
PROC FREQ DATA=healthcare_sales;
    TABLES Customer_Type;
RUN;

/* PROC MEANS: Revenue Statistics */
PROC MEANS DATA=healthcare_sales
    N MEAN MIN MAX STD;
    VAR Revenue Quantity_Sold;
RUN;