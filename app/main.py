from fastapi import FastAPI
from app.schemas import PredictionRequest, PredictionResponse
from app.model.predict import load_model, make_prediction

app = FastAPI(
    title="California Housing Price Prediction API",
    description="""
This API predicts median house prices in California (in units of $100,000) based on input features from the 
[California Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html).
""",
    version="1.0.0",
    contact={
        "name": "Dravid",
        "url": "https://github.com/Anti-Invincinator",
    }
)

# Load model at startup
model = load_model()

@app.get("/", summary="Health Check", description="Verify the API is running.")
def root():
    return {"message": "California Housing Price Prediction API is up and running!"}

@app.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict California House Price",
    description="""
Estimate the house price (in $100,000s) using the following inputs:

- `MedInc`: Median income in block group
- `AveRooms`: Average number of rooms per household
- `HouseAge`: Median age of the house in years
- `AveOccup`: Average occupancy per household

Example:  
```json
{
  "MedInc": 4.5,
  "AveRooms": 6.2,
  "HouseAge": 20,
  "AveOccup": 2.5
}
"""
)
def predict(request: PredictionRequest):
    prediction = make_prediction(model, request)
    return {"predicted_price": prediction}