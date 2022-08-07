#!/usr/bin/python3
"""class descended from BaseClass"""
from models.base_model import BaseModel


class Review(BaseModel):
    """creates new review object"""
    place_id = ""
    user_id = ""
    text = ""
