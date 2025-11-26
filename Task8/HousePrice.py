import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print("Train Shape:", train.shape)
print("Test Shape:", test.shape)

test_ids = test["Id"]

y = train["SalePrice"]
train.drop(["SalePrice"], axis=1, inplace=True)

full = pd.concat([train, test], axis=0, sort=False)

num_cols = full.select_dtypes(include=['int64', 'float64']).columns
full[num_cols] = full[num_cols].fillna(full[num_cols].median())

cat_cols = full.select_dtypes(include=['object']).columns
full[cat_cols] = full[cat_cols].fillna(full[cat_cols].mode().iloc[0])

quality_map = {
    "Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "NA": 0
}

ordinal_features = [
    "ExterQual", "ExterCond", "BsmtQual", "BsmtCond",
    "HeatingQC", "KitchenQual", "FireplaceQu",
    "GarageQual", "GarageCond", "PoolQC"
]

for col in ordinal_features:
    if col in full.columns:
        full[col] = full[col].map(quality_map)

skew_limit = 0.75
skew_vals = full[num_cols].skew().sort_values(ascending=False)
skewed_features = skew_vals[abs(skew_vals) > skew_limit].index

for col in skewed_features:
    full[col] = np.log1p(full[col])

print("\nSkewed Columns transformed:", list(skewed_features))

full = pd.get_dummies(full, drop_first=True)
print("Final shape after encoding:", full.shape)

X_train = full.iloc[:len(train), :]
X_test = full.iloc[len(train):, :]

model = RandomForestRegressor(
    n_estimators=350,
    max_depth=15,
    random_state=42
)

model.fit(X_train, y)

X_tr, X_val, y_tr, y_val = train_test_split(X_train, y, test_size=0.2, random_state=42)
model.fit(X_tr, y_tr)
pred_val = model.predict(X_val)

rmse = np.sqrt(mean_squared_error(y_val, pred_val))
print("\nValidation RMSE:", rmse)

model.fit(X_train, y)

test_preds = model.predict(X_test)
submission = pd.DataFrame({
    "Id": test_ids,
    "SalePrice": test_preds
})

submission.to_csv("submission.csv", index=False)

print("\nsubmission.csv created successfully!")
