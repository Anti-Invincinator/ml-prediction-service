import joblib
import numpy as np
from app.schemas import PredictionRequest

def load_model():
    return joblib.load("app/model/model.joblib")

def make_prediction(model, request: PredictionRequest) -> float:
    # Access correct attributes based on current schema
    input_array = np.array([[request.MedInc, request.AveRooms, request.HouseAge, request.AveOccup]])
    prediction = model.predict(input_array)
    return round(float(prediction[0]), 3)
