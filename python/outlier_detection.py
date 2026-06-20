import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "healthcare_sales_100k.csv"
output_image_path = script_dir / "revenue_outliers.png"

# Load dataset
df = pd.read_csv(csv_path)

# Plot Revenue boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df["Revenue"], vert=True)

plt.title("Revenue Outlier Detection")
plt.ylabel("Revenue")

plt.savefig(output_image_path)
plt.show()

# Calculate IQR
Q1 = df["Revenue"].quantile(0.25)
Q3 = df["Revenue"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Revenue"] < lower) | (df["Revenue"] > upper)]

print("Number of outliers:", len(outliers))
print(outliers.head())