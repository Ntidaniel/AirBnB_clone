# models/review.py
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""  # will be Place.id
    user_id = ""  # will be User.id
    text = ""
