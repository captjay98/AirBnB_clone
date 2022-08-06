#!/usr/bin/python3
"""BaseModel class that defines all
common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Creates a BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """initialize a BaseModel from Dict Representation"""

        if args:
            pass
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.fromisoformat(v))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation"""
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """updates to the current time and saves to json"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of all key/value pairs"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ["created_at", "updated_at"]:
                v =  self.__dict__[k].isoformat()
                my_dict[k] = v
        return my_dict
