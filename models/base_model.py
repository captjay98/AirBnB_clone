#!/usr/bin/python3
"""creates BaseModel that defines all common attributes/methods
for other classes"""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """creates Base class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel"""

        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    v = datetime.fromisoformat(v)
                if k not in ['__class__']:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of BaseModel object"""
        return f"[{self.__class__.__name__}] (<{self.id}>) <{self.__dict__}>"

    def save(self):
        """Updates datetime of instance to current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict representation"""

        myDict = dict(self.__dict__)
        myDict["__class__"] = self.__class__.__name__
        myDict["created_at"] = self.created_at.isoformat()
        myDict["updated_at"] = self.updated_at.isoformat()
        return myDict
