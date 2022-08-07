#!/usr/bin/python3
"""class for serializing and deserializing JSON instances"""

from json import load, dump
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """The FileStorage class"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name = obj.__class__.__name__
        i_d = obj.id
        key = name + "." + i_d
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file path: __file_path"""
        store_dict = dict()
        with open(FileStorage.__file_path, 'w') as f:
            for k, v in FileStorage.__objects.items():
                store_dict[k] = v.to_dict()
            dump(store_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        my_dic = dict()
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r') as f:
                my_dic = load(f)
                for obj in my_dic.values():
                    self.new(eval(obj["__class__"])(**obj))
        else:
            pass
