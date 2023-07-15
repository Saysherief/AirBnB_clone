#!/usr/bin/python3
"""Defines a FileStorage Class."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    FileStorage class provides methods to serialize instances to a JSON file &
    deserialize the JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionry __objects storing all objects by class name & ID
        Overridden to include User objects
        """
        rdict = {}
        for k, v in FileStorage.__objects.items():
            rdict[k] = v.to_dict()
        # User objects are added below
        for k, v in FileStorage.__objects.items():
            if isinstance(v, User):
                rdict[k] = v.to_dict()
        return rdict

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
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as myfi:
            json.dump(rdict, myfi)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the JSON file exists;
        otherwise, does nothing
        """
        try:
            with open(FileStorage.__file_path, mode="r") as myfile:
                rdict = json.load(myfile)
                tform = "%Y-%m-%dT%H:%M:%S.%f"
                for k, v in rdict.items():
                    if "User" in v["__class__"]:
                        obj = User(**v)
                    else:
                        obj = BaseModel(**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
