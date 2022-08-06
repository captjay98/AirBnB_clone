#!/usr/bin/python3
"""Place class that inherits from BaseClass"""
from models.base_model import BaseModel


class Place:
    """creates a new instance of Place"""
    city_id = ""

    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
