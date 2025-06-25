import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Test Data Set
data = {
    'square_feet': [1500, 1800, 2400, 3000, 3500],
    'bedrooms': [3, 4, 3, 5, 4],
    'price': [300000, 350000, 400000, 500000, 550000]
}

df = pd.DataFrame(data)

X = df[['square_feet', 'bedrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'app/model/model.joblib')
print("Model trained and saved.")