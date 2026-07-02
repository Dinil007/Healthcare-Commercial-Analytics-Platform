# Healthcare Commercial Analytics Platform - Architecture

## Project Overview

This project is an end-to-end Business Intelligence solution for analyzing pharmaceutical sales, prescriptions, doctor performance, product performance, and regional trends.

## Technology Stack

* MySQL
* Python
* Power BI
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Faker

## Architecture Flow

Raw Data
↓
Python Data Generation & Cleaning
↓
MySQL Database
↓
Star Schema Data Warehouse
├── Fact_Sales
├── Fact_Prescriptions
├── Dim_Doctor
├── Dim_Hospital
├── Dim_Product
├── Dim_Region
└── Dim_Time
↓
SQL Analytics
↓
Power BI Dashboards
├── Executive Dashboard
├── Doctor Analytics
└── Regional Performance
↓
Machine Learning
└── Sales Forecasting (Linear Regression)

## Key KPIs

* Total Revenue
* Total Profit
* Total Quantity Sold
* Total Sales
* Revenue by Product
* Revenue by Doctor
* Revenue by Hospital
* Revenue by Region
* Top Products
* Top Doctors

## Machine Learning

* Algorithm: Linear Regression
* Features:

  * Quantity Sold
  * Unit Price
  * Discount
* Target:

  * Revenue

## Repository Structure

Healthcare-Commercial-Analytics-Platform/
├── sql/
├── python/
├── powerbi/
├── data/
├── docs/
├── Screenshots/
├── README.md
└── requirements.txt
