#!/usr/bin/python3
"""Defines a BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods."""

    def __init__(self, *args, **kwargs):
        """Initializes all attributes

        Args:
            *args (any): Unused.
            **kwargs (dict): key/value pairs of attributes.
        """
<<<<<<< HEAD
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
=======
>>>>>>> 994e5cdb81ec42fd7aecccacf21e537925dcf56a
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(v)
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """Return class name, id and attributes dictionary."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of BaseModel instance

        Includes the key/value pair __class__  representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
