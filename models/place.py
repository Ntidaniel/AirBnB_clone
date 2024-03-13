# models/place.py
from models.base_model import BaseModel

class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    city_id = ""  # will be City.id
    user_id = ""  # will be User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # will be the list of Amenity.id later
