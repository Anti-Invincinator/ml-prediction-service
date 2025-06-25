from pydantic import BaseModel

class PredictionRequest(BaseModel):
    square_feet: float
    bedrooms: int

class PredictionResponse(BaseModel):
    predicted_price: float
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    MedInc: float     # Median income
    AveRooms: float   # Average rooms per household
    HouseAge: float   # Age of the house
    AveOccup: float   # Average occupancy

class PredictionResponse(BaseModel):
    predicted_price: float
