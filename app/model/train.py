from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
from math import sqrt
import joblib

# Data Set
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="MedHouseVal")

# Extend the dataset with additional features later
features = ["MedInc", "AveRooms", "HouseAge", "AveOccup"]
X = X[features]

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "app/model/model.joblib")
print("Model trained and saved.")

# Evaluate
y_pred = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.3f}")
