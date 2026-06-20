import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

from pathlib import Path

# Load data
project_root = Path(__file__).resolve().parent.parent
csv_path = project_root / "python" / "healthcare_sales_100k.csv"
df = pd.read_csv(csv_path)

# Features and target
X = df[["Quantity_Sold", "Unit_Price", "Discount", "Profit"]]
y = df["Revenue"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
print("Linear Regression")
print("MAE:", mean_absolute_error(y_test, predictions))
print("R²:", r2_score(y_test, predictions))

import matplotlib.pyplot as plt

# Resolve image save path
output_image_path = project_root / "python" / "actual_vs_predicted.png"

# Plot first 100 predictions
plt.figure(figsize=(10, 6))
plt.plot(y_test.values[:100], label="Actual")
plt.plot(predictions[:100], label="Predicted")
plt.title("Actual vs Predicted Revenue (Linear Regression)")
plt.xlabel("Sample")
plt.ylabel("Revenue")
plt.legend()
plt.tight_layout()

# Save plot
plt.savefig(output_image_path)
plt.show()