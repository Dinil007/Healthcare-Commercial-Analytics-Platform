import pandas as pd

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
input_file = script_dir / "healthcare_sales_100k.csv"
output_file = script_dir / "healthcare_sales_cleaned.csv"

df = pd.read_csv(input_file)

print("=" * 50)
print("Healthcare ETL Pipeline")
print("=" * 50)

# -----------------------------
# Initial Summary
# -----------------------------
print(f"Rows before cleaning: {len(df)}")

# -----------------------------
# Check Missing Values
# -----------------------------
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Fill missing values (if any)
df = df.fillna(0)

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
duplicates_before = len(df)
df = df.drop_duplicates()
duplicates_removed = duplicates_before - len(df)

print(f"\nDuplicates Removed: {duplicates_removed}")

# -----------------------------
# Validate Data
# -----------------------------
# Remove negative revenue
df = df[df["Revenue"] >= 0]

# Remove invalid quantity sold
df = df[df["Quantity_Sold"] > 0]

# -----------------------------
# Save Cleaned Data
# -----------------------------
df.to_csv(output_file, index=False)

# -----------------------------
# Final Summary
# -----------------------------
print(f"\nRows after cleaning: {len(df)}")
print(f"Cleaned file saved as: {output_file}")

print("\nETL Pipeline Completed Successfully!")