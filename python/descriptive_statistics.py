
import pandas as pd

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "healthcare_sales_100k.csv"
output_csv_path = script_dir / "descriptive_statistics.csv"

# Load dataset
df = pd.read_csv(csv_path)

# Display descriptive statistics
print("=" * 50)
print("Descriptive Statistics")
print("=" * 50)
print(df.describe(include="all"))

# Save statistics to CSV
df.describe(include="all").to_csv(output_csv_path)

print("\nDescriptive statistics saved as descriptive_statistics.csv")