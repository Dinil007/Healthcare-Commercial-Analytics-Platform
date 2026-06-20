import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "healthcare_sales_100k.csv"
output_image_path = script_dir / "sales_trend.png"

# Load dataset
df = pd.read_csv(csv_path)

# Create a sequential index for plotting
df["Record_Number"] = range(1, len(df) + 1)

# Plot Revenue Trend
plt.figure(figsize=(10, 5))
plt.plot(df["Record_Number"], df["Revenue"])
plt.title("Revenue Trend")
plt.xlabel("Record Number")
plt.ylabel("Revenue")
plt.grid(True)

# Save the chart
plt.savefig(output_image_path)

# Display the chart
plt.show()

print("Sales trend chart saved as sales_trend.png")