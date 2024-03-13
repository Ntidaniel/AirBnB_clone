# models/city.py
from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ""  # will be State.id
    name = ""
