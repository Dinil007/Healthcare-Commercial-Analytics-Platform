import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
project_root = Path(__file__).resolve().parent.parent
csv_path = project_root / "python" / "healthcare_sales_100k.csv"
df = pd.read_csv(csv_path)

# Features and target
X = df[["Quantity_Sold", "Unit_Price", "Discount", "Profit"]]
y = df["Revenue"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
print("Random Forest")
print("MAE:", mean_absolute_error(y_test, predictions))
print("R²:", r2_score(y_test, predictions))