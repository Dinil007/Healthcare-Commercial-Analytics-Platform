import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Load data
df = pd.read_csv("healthcare_sales_100k.csv")

# Features and target
X = df[["Quantity_Sold", "Unit_Price", "Discount"]]
y = df["Revenue"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

import matplotlib.pyplot as plt

# Plot first 100 predictions
plt.figure(figsize=(10, 6))
plt.plot(y_test.values[:100], label="Actual")
plt.plot(y_pred[:100], label="Predicted")
plt.title("Actual vs Predicted Revenue")
plt.xlabel("Sample")
plt.ylabel("Revenue")
plt.legend()

plt.savefig("actual_vs_predicted.png")
plt.show()