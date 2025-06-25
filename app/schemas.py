from pydantic import BaseModel

class PredictionRequest(BaseModel):
    square_feet: float
    bedrooms: int

class PredictionResponse(BaseModel):
    predicted_price: float
