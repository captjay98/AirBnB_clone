#!/usr/bin/python3
"""BaseModel class that defines all
common attributes/methods for other classes"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Creates a BaseModel Class"""

    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """Returns string representation"""
        return (f"[<{self.__class__.__name__}>]"
                f"<({self.id}>) <{self.__dict__}>")

    def save(self):
        """updates to the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of all key/value pairs"""
        my_dict = self.__dict__.copy()
        for k, v in my_dict.items():
            if k in ["created_at", "updated_at"]:
                my_dict[k] = v

        my_dict["__class__"] = self.__class__.__name__
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict
