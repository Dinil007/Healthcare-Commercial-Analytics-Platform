```sql
-- =====================================================
-- Healthcare Commercial Analytics Platform
-- Database Schema (MySQL)
-- =====================================================

-- Create Database
CREATE DATABASE IF NOT EXISTS healthcare_commercial_analytics;
USE healthcare_commercial_analytics;

-- =====================================================
-- Dimension Tables
-- =====================================================

-- Doctor Dimension
CREATE TABLE IF NOT EXISTS Dim_Doctor (
    Doctor_ID INT PRIMARY KEY,
    Doctor_Name VARCHAR(100) NOT NULL,
    Specialty VARCHAR(100),
    Experience_Years INT,
    City VARCHAR(100)
);

-- Hospital Dimension
CREATE TABLE IF NOT EXISTS Dim_Hospital (
    Hospital_ID INT PRIMARY KEY,
    Hospital_Name VARCHAR(150) NOT NULL,
    Hospital_Type VARCHAR(100),
    City VARCHAR(100)
);

-- Product Dimension
CREATE TABLE IF NOT EXISTS Dim_Product (
    Product_ID INT PRIMARY KEY,
    Product_Name VARCHAR(100) NOT NULL,
    Category VARCHAR(100),
    Brand VARCHAR(100)
);

-- Region Dimension
CREATE TABLE IF NOT EXISTS Dim_Region (
    Region_ID INT PRIMARY KEY,
    Region_Name VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100)
);

-- Time Dimension
CREATE TABLE IF NOT EXISTS Dim_Time (
    Time_ID INT PRIMARY KEY,
    Full_Date DATE,
    Month_Name VARCHAR(20),
    Quarter_Name VARCHAR(10),
    Year_Number INT
);

-- =====================================================
-- Fact Tables
-- =====================================================

-- Sales Fact Table
CREATE TABLE IF NOT EXISTS Fact_Sales (
    Sale_ID INT PRIMARY KEY,

    Doctor_ID INT,
    Hospital_ID INT,
    Product_ID INT,
    Region_ID INT,
    Time_ID INT,

    Quantity_Sold INT,
    Revenue DECIMAL(12,2),

    Unit_Price DECIMAL(10,2),
    Discount DECIMAL(5,2),
    Profit DECIMAL(12,2),

    Sales_Channel VARCHAR(50),
    Payment_Type VARCHAR(50),
    Customer_Type VARCHAR(50),

    CONSTRAINT FK_Sales_Doctor
        FOREIGN KEY (Doctor_ID)
        REFERENCES Dim_Doctor(Doctor_ID),

    CONSTRAINT FK_Sales_Hospital
        FOREIGN KEY (Hospital_ID)
        REFERENCES Dim_Hospital(Hospital_ID),

    CONSTRAINT FK_Sales_Product
        FOREIGN KEY (Product_ID)
        REFERENCES Dim_Product(Product_ID),

    CONSTRAINT FK_Sales_Region
        FOREIGN KEY (Region_ID)
        REFERENCES Dim_Region(Region_ID),

    CONSTRAINT FK_Sales_Time
        FOREIGN KEY (Time_ID)
        REFERENCES Dim_Time(Time_ID)
);

-- Prescription Fact Table
CREATE TABLE IF NOT EXISTS Fact_Prescriptions (
    Prescription_ID INT PRIMARY KEY,

    Doctor_ID INT,
    Hospital_ID INT,
    Product_ID INT,
    Region_ID INT,
    Time_ID INT,

    Prescription_Count INT,

    CONSTRAINT FK_Prescription_Doctor
        FOREIGN KEY (Doctor_ID)
        REFERENCES Dim_Doctor(Doctor_ID),

    CONSTRAINT FK_Prescription_Hospital
        FOREIGN KEY (Hospital_ID)
        REFERENCES Dim_Hospital(Hospital_ID),

    CONSTRAINT FK_Prescription_Product
        FOREIGN KEY (Product_ID)
        REFERENCES Dim_Product(Product_ID),

    CONSTRAINT FK_Prescription_Region
        FOREIGN KEY (Region_ID)
        REFERENCES Dim_Region(Region_ID),

    CONSTRAINT FK_Prescription_Time
        FOREIGN KEY (Time_ID)
        REFERENCES Dim_Time(Time_ID)
);

-- =====================================================
-- End of Schema
-- =====================================================
```
