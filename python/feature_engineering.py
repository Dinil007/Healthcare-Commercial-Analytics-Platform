import pandas as pd

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "healthcare_sales_100k.csv"
output_csv_path = script_dir / "healthcare_sales_feature_engineered.csv"

# Load dataset
df = pd.read_csv(csv_path)

# -----------------------------
# Feature Engineering
# -----------------------------

# Revenue per unit sold
df["Revenue_Per_Unit"] = df["Revenue"] / df["Quantity_Sold"]

# Profit Margin
df["Profit_Margin"] = df["Profit"] / df["Revenue"]

# Discounted Revenue
df["Discounted_Revenue"] = df["Revenue"] - df["Discount"]

# Save the new dataset
df.to_csv(output_csv_path, index=False)

print("Feature engineering completed successfully!")
print(df[[
    "Revenue",
    "Quantity_Sold",
    "Revenue_Per_Unit",
    "Profit",
    "Profit_Margin",
    "Discount",
    "Discounted_Revenue"
]].head())