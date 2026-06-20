import pandas as pd

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "healthcare_sales_100k.csv"
output_csv_path = script_dir / "healthcare_sales_5M.csv"

# Load the existing dataset
df = pd.read_csv(csv_path)

# Number of times to repeat the data
# 100,000 rows × 50 = 5,000,000 rows
multiplier = 50

# Create the large dataset
large_df = pd.concat([df] * multiplier, ignore_index=True)

# Update Sale_ID so it remains unique
large_df["Sale_ID"] = range(1, len(large_df) + 1)

# Save to CSV
large_df.to_csv(output_csv_path, index=False)

print("Large dataset generated successfully!")
print(f"Total rows: {len(large_df):,}")