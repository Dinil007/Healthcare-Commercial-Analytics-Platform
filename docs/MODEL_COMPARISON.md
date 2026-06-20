# Model Comparison Report

## Objective

The objective of this analysis is to compare multiple machine learning models used for healthcare sales prediction and identify the best-performing model.

## Models Evaluated

- **Linear Regression**: A baseline regression model mapping feature coefficients to revenue.
- **Random Forest Regressor**: An ensemble decision-tree method.
- **XGBoost Regressor**: An optimized gradient-boosting model.
- **Random Forest Classifier**: Used to classify doctor churn probability.

## Performance Comparison (Regression Models)

The following table summarizes the performance metrics of the regression models predicting `Revenue` based on the features: `Quantity_Sold`, `Unit_Price`, `Discount` (and `Profit` where applicable).

| Model | MAE | R-squared ($R^2$) | Advantages | Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Regression** | 115,310.86 | 0.9274 | Simple, fast, highly interpretable. | Assumes linear relationships; higher prediction error. |
| **Random Forest Regressor** | 2,724.25 | 0.9999 | Handles non-linear data well, extremely low error. | Slower to train; model size can be large. |
| **XGBoost Regressor** | 4,123.82 | 0.9999 | High predictive accuracy, very fast execution. | Requires tuning; complex decision trees. |

## Doctor Churn Prediction (Classification Model)

To proactively retain prescribers, we built a classifier to identify doctors likely to stop prescribing (Churn = 1) using `Quantity_Sold`, `Unit_Price`, `Discount`, and `Revenue`.

- **Model Type**: Random Forest Classifier
- **Accuracy**: 100% (Accuracy: 1.0, F1-Score: 1.0)
- **Confusion Matrix**:
  - True Negative (Active): 18,086
  - True Positive (Churned): 1,914
  - False Positives/Negatives: 0
  - *Note: The perfect accuracy is due to the deterministic rule applied for synthetic label generation (`Quantity_Sold < 50`).*

## Conclusion

The **Random Forest Regressor** achieved the lowest Mean Absolute Error (MAE: 2,724.25) and the highest $R^2$ score (0.9999) among the regression models, making it the most accurate model for predicting sales revenue. For production deployment, **XGBoost** is a strong alternative due to its faster inference time and comparable accuracy.
