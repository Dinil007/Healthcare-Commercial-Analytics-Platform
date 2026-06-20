import pandas as pd
from scipy.stats import ttest_ind

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "healthcare_sales_100k.csv"

# Load dataset
df = pd.read_csv(csv_path)

# Create two groups
new_customers = df[df["Customer_Type"] == "New"]["Revenue"]
returning_customers = df[df["Customer_Type"] == "Returning"]["Revenue"]

# Perform independent t-test
t_stat, p_value = ttest_ind(
    new_customers,
    returning_customers,
    equal_var=False
)

print("===== Hypothesis Testing =====")
print(f"T-Statistic : {t_stat:.4f}")
print(f"P-Value     : {p_value:.4f}")

# Interpret the result
alpha = 0.05

if p_value < alpha:
    print("\nConclusion:")
    print("Reject the Null Hypothesis (H0)")
    print("There is a statistically significant difference in average revenue between New and Returning customers.")
else:
    print("\nConclusion:")
    print("Fail to Reject the Null Hypothesis (H0)")
    print("There is no statistically significant difference in average revenue between New and Returning customers.")