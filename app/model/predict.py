import joblib
import numpy as np
from app.schemas import PredictionRequest

def load_model():
    return joblib.load("app/model/model.joblib")

def make_prediction(model, request: PredictionRequest) -> float:
    data = np.array([[request.square_feet, request.bedrooms]])
    prediction = model.predict(data)
    return round(float(prediction[0]), 2)
