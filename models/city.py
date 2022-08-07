#!/usr/bin/python3
"""City class that inherits from BaseClass"""

from models.base_model import BaseModel


class City(BaseModel):
    """creates city object"""

    state_id = ""
    name = ""
