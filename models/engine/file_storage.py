#!/usr/bin/python3
"""Defines a FileStorage Class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage class provides methods to serialize instances to a JSON file &
    deserialize the JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def all(self):
        """
        Returns the dictionry __objects storing all objects by class name & ID
        Overridden to include User objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        rdict = {}
        for k, v in FileStorage.__objects.items():
            rdict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as myfile:
            json.dump(rdict, myfile)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the JSON file exists;
        otherwise, does nothing
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as myf:
                rdict = json.load(myf)
                for k, v in rdict.items():
                    cl_name = k.split(".")[0]
                    if cl_name not in self.__classes:
                        continue
                    re_cls = eval(cl_name)
                    obj = re_cls(**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
