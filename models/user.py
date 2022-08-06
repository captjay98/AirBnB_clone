#!/usr/bin/python3
"""user class that Inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new User object"""

    email = ""
    password = ""
    first_name = ""
    lastname = ""
