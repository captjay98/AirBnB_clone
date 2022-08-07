#!/usr/bin/python3
"""class that inherits from BaseClass"""
from models.base_model import BaseModel


class Review(BaseModel):
    """creates new review object"""
    place_id = ""
    user_id = ""
    text = ""
