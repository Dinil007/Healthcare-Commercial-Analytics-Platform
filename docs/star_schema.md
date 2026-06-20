# Star Schema Data Warehouse Design

This document details the **Star Schema** designed for the **Healthcare Commercial Analytics Platform**. 

---

## 🏗️ Architecture Diagram

The data warehouse uses a Star Schema design to optimize query speeds and simplify BI data loading in tools like Power BI and Tableau.

```text
                 +---------------+
                 |  Dim_Doctor   |
                 +---------------+
                        |
+-------------+  +---------------+  +--------------+
| Dim_Product |--|   Fact_Sales  |--| Dim_Hospital |
+-------------+  +---------------+  +--------------+
                        |
                +---------------+
                |  Dim_Region   |
                +---------------+
                        |
                +---------------+
                |   Dim_Time    |
                +---------------+
```

---

## 🗄️ Table Definitions

### 1. Fact Table: `Fact_Sales`
The core fact table stores individual transactional sales data.

* **Primary Key**: `Sale_ID`
* **Foreign Keys**:
  - `Doctor_ID` referencing `Dim_Doctor(Doctor_ID)`
  - `Hospital_ID` referencing `Dim_Hospital(Hospital_ID)`
  - `Product_ID` referencing `Dim_Product(Product_ID)`
  - `Region_ID` referencing `Dim_Region(Region_ID)`
  - `Time_ID` referencing `Dim_Time(Time_ID)`
* **Metrics / Measures**:
  - `Quantity_Sold` (integer)
  - `Unit_Price` (decimal)
  - `Discount` (decimal)
  - `Revenue` (decimal)
  - `Profit` (decimal)
* **Metadata Columns**:
  - `Sales_Channel` (e.g., Retail, Institutional, Online)
  - `Payment_Type` (e.g., UPI, Credit Card, Cash)
  - `Customer_Type` (e.g., New, Returning)

### 2. Fact Table: `Fact_Prescriptions`
Tracks prescription activity at the doctor/product level.

* **Primary Key**: `Prescription_ID`
* **Foreign Keys**: Same as `Fact_Sales`.
* **Metrics**:
  - `Prescription_Count` (integer)

### 3. Dimension Tables

#### `Dim_Doctor`
Contains information about doctors who prescribe the pharmaceutical products.
* **Attributes**: `Doctor_ID` (PK), `Doctor_Name`, `Specialty`, `Experience_Years`, `City`.

#### `Dim_Hospital`
Contains information about hospitals and clinical institutions.
* **Attributes**: `Hospital_ID` (PK), `Hospital_Name`, `Hospital_Type`, `City`.

#### `Dim_Product`
Contains product brand and therapeutic category details.
* **Attributes**: `Product_ID` (PK), `Product_Name`, `Category`, `Brand`.

#### `Dim_Region`
Provides regional metadata for geographical slicing.
* **Attributes**: `Region_ID` (PK), `Region_Name`, `State`, `Country`.

#### `Dim_Time`
Provides granular date hierarchies for time-series analysis.
* **Attributes**: `Time_ID` (PK), `Full_Date`, `Month_Name`, `Quarter_Name`, `Year_Number`.

---

## 🔑 Design Decisions & Benefits

1. **Denormalization**: Dimensions are fully denormalized to ensure single-join retrieval for all analytical attributes.
2. **Surrogate Keys**: Integer-based surrogate keys (`Time_ID`, `Sale_ID`, etc.) are used for fast indexing.
3. **Referential Integrity**: Strict FOREIGN KEY constraints are enforced at the database level to ensure data quality and clean joins.