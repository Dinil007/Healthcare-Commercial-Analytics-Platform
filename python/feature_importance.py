
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

from pathlib import Path

# Resolve paths relative to script directory
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "healthcare_sales_100k.csv"
output_image_path = script_dir / "feature_importance.png"

# Load dataset
df = pd.read_csv(csv_path)

# Features and target
X = df[["Quantity_Sold", "Unit_Price", "Discount"]]
y = df["Revenue"]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Get feature importance
importance = model.feature_importances_

# Create dataframe
feature_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

# Print results
print(feature_df)

# Plot
plt.figure(figsize=(8, 5))
plt.bar(feature_df["Feature"], feature_df["Importance"])
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()

# Save image
plt.savefig(output_image_path)
plt.show()