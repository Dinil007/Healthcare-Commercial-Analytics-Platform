
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from pathlib import Path

# Resolve paths relative to project root
project_root = Path(__file__).resolve().parent.parent
csv_path = project_root / "python" / "healthcare_sales_100k.csv"

# Load Dataset
df = pd.read_csv(csv_path)

# --------------------------------------------------
# Create a synthetic churn label
# Rule:
# Doctors with Quantity_Sold < 50 are considered
# likely to stop prescribing (Churn = 1)
# --------------------------------------------------
df["Churn"] = (df["Quantity_Sold"] < 50).astype(int)

# --------------------------------------------------
# Features and Target
# --------------------------------------------------
X = df[["Quantity_Sold", "Unit_Price", "Discount", "Revenue"]]
y = df["Churn"]

# --------------------------------------------------
# Train/Test Split
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------------------------------
# Train Random Forest Classifier
# --------------------------------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# --------------------------------------------------
# Predictions
# --------------------------------------------------
y_pred = model.predict(X_test)

# --------------------------------------------------
# Evaluation
# --------------------------------------------------
print("=" * 50)
print("Doctor Churn Prediction Results")
print("=" * 50)

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

