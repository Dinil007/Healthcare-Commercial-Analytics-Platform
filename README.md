# Healthcare Commercial Analytics Platform (HCAP)

Welcome to the **Healthcare Commercial Analytics Platform (HCAP)** repository. This enterprise-grade platform is designed to ingest, process, and analyze healthcare commercial data (such as claims, prescriptions, sales, and CRM data) to provide actionable insights for commercial excellence, market access, sales force effectiveness, and marketing ROI.

## 📁 Repository Structure

This repository is structured as follows:

*   **`data/`**: Storage for datasets.
    *   `raw/`: Raw, unprocessed source files (e.g., vendor feeds, raw database dumps).
    *   `processed/`: Cleaned, transformed, and aggregated datasets optimized for analytics and BI.
*   **`sql/`**: SQL scripts for ETL/ELT pipelines, database schema creation, data warehouse modeling, and analytical queries.
*   **`python/`**: Python scripts and modules for data engineering, automation, API integrations, and general utility functions.
*   **`powerbi/`**: Power BI templates (`.pbit`), reports (`.pbix`), and Power Query M/DAX scripts.
*   **`tableau/`**: Tableau workbooks (`.twbx`), data source files (`.tds`), and dashboards.
*   **`sas/`**: SAS programs (`.sas`) used for statistical analysis, clinical-commercial correlation, or legacy ETL operations.
*   **`docs/`**: Project documentation, data dictionaries, methodology notes, and business requirement documents.
*   **`screenshots/`**: Visual artifacts, dashboard mockups, and execution logs.
*   **`ml/`**: Machine learning models, feature engineering pipelines, training notebooks, and evaluation scripts (e.g., targeting, churn, segmentation).

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ (see `python/requirements.txt` when available)
- Power BI Desktop / Tableau Desktop
- SAS Environment (optional, for running legacy scripts)
- SQL database engine (e.g., PostgreSQL, Snowflake, SQL Server)

---
*Created for Healthcare Commercial Analytics and Insights.*
