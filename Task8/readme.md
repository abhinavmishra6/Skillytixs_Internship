# **Improving House Price Predictions through Feature Engineering**

## **Task Overview**

This task focuses on applying **Feature Engineering techniques** to the **House Prices – Advanced Regression Techniques** dataset.
 The goal is to enhance the predictive performance of a machine learning model by transforming data, handling missing values, encoding categorical features, and applying statistical techniques.

---

## **Key Insights**

- Correct handling of **ordinal categories** (quality/condition ratings) significantly influences prediction quality.
- One-Hot Encoding for non-ordinal features removes model confusion.
- **Log-transforming skewed variables** improves model performance and reduces overfitting.
- Missing values in key columns (LotFrontage, GarageYrBlt, Basement fields) must be treated carefully for accurate predictions.
- Random Forest performed well without needing heavy hyperparameter tuning.

---

## **Repository Contents**

| File                     | Description                                                                |
| ------------------------ | -------------------------------------------------------------------------- |
| **train.csv**      | Training dataset containing features + SalePrice                           |
| **test.csv**       | Test dataset used for predictions                                          |
| **submission.csv** | Final model predictions                                                    |
| **HousePrice.py**  | Python script containing full preprocessing, feature engineering, modeling |
| **README.md**      | readme file                                                                |

---

## **Tools & Libraries Used**

- **Python**, **Pandas**, **NumPy**
- **Scikit-learn** (RandomForestRegressor, train_test_split)
- **Matplotlib**, **Seaborn**
