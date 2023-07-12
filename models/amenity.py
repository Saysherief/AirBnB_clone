#!/usr/bin/python3
"""Defines he Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an Amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
