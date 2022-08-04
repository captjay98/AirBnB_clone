#!/usr/bin/python3
"""File Storage class that serializes and deserializes Json"""


from json import dump, load
from models.base_model import BaseModel
from models.user import User
from models.place import place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """File Storage class"""

    __file_path = "file.json"
    __objects = dict()


    def all(self):
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        i_d = obj.id
        self.__objects[f"{class_name}.{i_d}"] = obj

    def save(self):
        dict_store = {}
        with open(self.__file_path, 'w') as f:
            for k, v in self.__objects.items():
                dict_store[k] = v.to_dict()
            dump(dict_store, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                for obj in load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
