CREATE DATABASE healthcare_commercial_analytics;

USE healthcare_commercial_analytics;

SHOW DATABASES;

CREATE TABLE Dim_Doctor (
    Doctor_ID INT PRIMARY KEY,
    Doctor_Name VARCHAR(100),
    Specialty VARCHAR(100),
    Experience_Years INT,
    City VARCHAR(100)
);

CREATE TABLE Dim_Hospital (
    Hospital_ID INT PRIMARY KEY,
    Hospital_Name VARCHAR(150),
    Hospital_Type VARCHAR(100),
    City VARCHAR(100)
);

CREATE TABLE Dim_Product (
    Product_ID INT PRIMARY KEY,
    Product_Name VARCHAR(100),
    Category VARCHAR(100),
    Brand VARCHAR(100)
);

CREATE TABLE Dim_Region (
    Region_ID INT PRIMARY KEY,
    Region_Name VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100)
);

CREATE TABLE Dim_Time (
    Time_ID INT PRIMARY KEY,
    Full_Date DATE,
    Month_Name VARCHAR(20),
    Quarter_Name VARCHAR(10),
    Year_Number INT
);

CREATE TABLE Fact_Sales (
    Sale_ID INT PRIMARY KEY,
    Doctor_ID INT,
    Hospital_ID INT,
    Product_ID INT,
    Region_ID INT,
    Time_ID INT,
    Quantity_Sold INT,
    Revenue DECIMAL(12,2),

    FOREIGN KEY (Doctor_ID) REFERENCES Dim_Doctor(Doctor_ID),
    FOREIGN KEY (Hospital_ID) REFERENCES Dim_Hospital(Hospital_ID),
    FOREIGN KEY (Product_ID) REFERENCES Dim_Product(Product_ID),
    FOREIGN KEY (Region_ID) REFERENCES Dim_Region(Region_ID),
    FOREIGN KEY (Time_ID) REFERENCES Dim_Time(Time_ID)
);

INSERT INTO Dim_Doctor VALUES
(1, 'Dr. Rajesh Kumar', 'Cardiology', 15, 'Bangalore'),
(2, 'Dr. Priya Nair', 'Neurology', 10, 'Kochi'),
(3, 'Dr. Amit Sharma', 'Orthopedics', 8, 'Chennai'),
(4, 'Dr. Sneha Patel', 'General Medicine', 12, 'Hyderabad'),
(5, 'Dr. Arjun Menon', 'Dermatology', 6, 'Calicut');

INSERT INTO Dim_Hospital VALUES
(1, 'City Care Hospital', 'Private', 'Bangalore'),
(2, 'Apollo Health Center', 'Private', 'Chennai'),
(3, 'Government Medical College', 'Government', 'Kochi'),
(4, 'Sunrise Hospital', 'Private', 'Hyderabad'),
(5, 'Aster Clinic', 'Private', 'Calicut');

INSERT INTO Dim_Product VALUES
(1, 'CardioPlus', 'Cardiology', 'PharmaX'),
(2, 'NeuroMax', 'Neurology', 'MediLife'),
(3, 'OrthoHeal', 'Orthopedics', 'HealthCorp'),
(4, 'SkinCare Pro', 'Dermatology', 'BioMed'),
(5, 'GeneralCare', 'General Medicine', 'Wellness Pharma');

INSERT INTO Dim_Region VALUES
(1, 'South', 'Karnataka', 'India'),
(2, 'South', 'Kerala', 'India'),
(3, 'South', 'Tamil Nadu', 'India'),
(4, 'South', 'Telangana', 'India'),
(5, 'South', 'Kerala', 'India');

INSERT INTO Dim_Time VALUES
(1, '2025-01-15', 'January', 'Q1', 2025),
(2, '2025-02-15', 'February', 'Q1', 2025),
(3, '2025-03-15', 'March', 'Q1', 2025),
(4, '2025-04-15', 'April', 'Q2', 2025),
(5, '2025-05-15', 'May', 'Q2', 2025);

INSERT INTO Fact_Sales VALUES
(1, 1, 1, 1, 1, 1, 120, 240000.00),
(2, 2, 3, 2, 2, 2, 95, 180500.00),
(3, 3, 2, 3, 3, 3, 75, 150000.00),
(4, 4, 4, 5, 4, 4, 200, 320000.00),
(5, 5, 5, 4, 5, 5, 60, 90000.00);

SELECT * FROM Fact_Sales;

SELECT SUM(Revenue) AS Total_Revenue
FROM Fact_Sales;

SELECT SUM(Quantity_Sold) AS Total_Quantity
FROM Fact_Sales;

SELECT
    p.Product_Name,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Product p
ON f.Product_ID = p.Product_ID
GROUP BY p.Product_Name
ORDER BY Total_Revenue DESC;

SELECT
    d.Doctor_Name,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Doctor d
ON f.Doctor_ID = d.Doctor_ID
GROUP BY d.Doctor_Name
ORDER BY Total_Revenue DESC;

SELECT
    h.Hospital_Name,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Hospital h
ON f.Hospital_ID = h.Hospital_ID
GROUP BY h.Hospital_Name
ORDER BY Total_Revenue DESC;

SELECT
    r.State,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Region r
ON f.Region_ID = r.Region_ID
GROUP BY r.State
ORDER BY Total_Revenue DESC;

SELECT
    p.Product_Name,
    SUM(f.Quantity_Sold) AS Total_Quantity
FROM Fact_Sales f
JOIN Dim_Product p
ON f.Product_ID = p.Product_ID
GROUP BY p.Product_Name
ORDER BY Total_Quantity DESC;

CREATE TABLE Fact_Prescriptions (
    Prescription_ID INT PRIMARY KEY,
    Doctor_ID INT,
    Hospital_ID INT,
    Product_ID INT,
    Region_ID INT,
    Time_ID INT,
    Prescription_Count INT,

    FOREIGN KEY (Doctor_ID) REFERENCES Dim_Doctor(Doctor_ID),
    FOREIGN KEY (Hospital_ID) REFERENCES Dim_Hospital(Hospital_ID),
    FOREIGN KEY (Product_ID) REFERENCES Dim_Product(Product_ID),
    FOREIGN KEY (Region_ID) REFERENCES Dim_Region(Region_ID),
    FOREIGN KEY (Time_ID) REFERENCES Dim_Time(Time_ID)
);

SHOW TABLES;

ALTER TABLE Fact_Sales
ADD COLUMN Unit_Price DECIMAL(10,2);

ALTER TABLE Fact_Sales
ADD COLUMN Discount DECIMAL(5,2);

ALTER TABLE Fact_Sales
ADD COLUMN Profit DECIMAL(12,2);

ALTER TABLE Fact_Sales
ADD COLUMN Sales_Channel VARCHAR(50);

ALTER TABLE Fact_Sales
ADD COLUMN Payment_Type VARCHAR(50);

ALTER TABLE Fact_Sales
ADD COLUMN Customer_Type VARCHAR(50);

DESCRIBE Fact_Sales;

SELECT COUNT(*) FROM Fact_Sales;

SELECT * FROM Fact_Sales LIMIT 10;

SELECT
    p.Product_Name,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Product p
ON f.Product_ID = p.Product_ID
GROUP BY p.Product_Name
ORDER BY Total_Revenue DESC
LIMIT 10;

SELECT
    r.State,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Region r
ON f.Region_ID = r.Region_ID
GROUP BY r.State
ORDER BY Total_Revenue DESC;

SELECT
    d.Doctor_Name,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Doctor d
ON f.Doctor_ID = d.Doctor_ID
GROUP BY d.Doctor_Name
ORDER BY Total_Revenue DESC
LIMIT 10;

SELECT
    h.Hospital_Name,
    SUM(f.Revenue) AS Total_Revenue
FROM Fact_Sales f
JOIN Dim_Hospital h
ON f.Hospital_ID = h.Hospital_ID
GROUP BY h.Hospital_Name
ORDER BY Total_Revenue DESC
LIMIT 10;

SELECT AVG(Revenue) AS Average_Revenue
FROM Fact_Sales;


