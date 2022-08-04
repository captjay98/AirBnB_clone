#!/usr/bin/python3
"""User class that inherits from BaseClass"""

from models.base_model import BaseClass


class User(BaseClass):
    """Creates a new User object"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
