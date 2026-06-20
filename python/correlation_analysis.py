import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "healthcare_sales_100k.csv"
output_image_path = script_dir / "correlation_matrix.png"

# Load dataset
df = pd.read_csv(csv_path)

# Select numeric columns
numeric_df = df.select_dtypes(include=["number"])

# Compute correlation matrix
correlation = numeric_df.corr()

# Print correlation matrix
print("Correlation Matrix:")
print(correlation)

# Plot heatmap using matplotlib
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.matshow(correlation)

plt.colorbar(cax)

ax.set_xticks(range(len(correlation.columns)))
ax.set_yticks(range(len(correlation.columns)))

ax.set_xticklabels(correlation.columns, rotation=90)
ax.set_yticklabels(correlation.columns)

plt.title("Correlation Matrix", pad=20)

plt.tight_layout()
plt.savefig(output_image_path)
plt.show()