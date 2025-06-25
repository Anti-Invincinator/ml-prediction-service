# app/main.py
from fastapi import FastAPI
from app.schemas import PredictionRequest, PredictionResponse
from app.model.predict import load_model, make_prediction

app = FastAPI(
    title="Housing Price Prediction API",
    description="A lightweight ML prediction service to estimate housing prices based on square footage and number of bedrooms.",
    version="0.1.0",
)

model = load_model()

@app.get("/", summary="Health Check", description="Check if the API is running.")
def root():
    return {"message": "Housing Price Prediction API is running."}

@app.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict Housing Price",
    description="""
Estimate the price of a house based on its square footage and number of bedrooms.

**Input:**
- `square_feet` (float): Total area of the house in square feet
- `bedrooms` (int): Number of bedrooms

**Output:**
- `predicted_price` (float): Estimated price in USD
""")
def predict(request: PredictionRequest):
    prediction = make_prediction(model, request)
    return {"predicted_price": prediction}
