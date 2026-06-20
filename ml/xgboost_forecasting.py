import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor

from pathlib import Path

# Resolve paths relative to project root
project_root = Path(__file__).resolve().parent.parent
csv_path = project_root / "python" / "healthcare_sales_100k.csv"

# Load data
df = pd.read_csv(csv_path)

# Features and target
X = df[["Quantity_Sold", "Unit_Price", "Discount"]]
y = df["Revenue"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("XGBoost Results")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))