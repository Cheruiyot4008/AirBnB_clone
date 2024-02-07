#!/usr/bin/python3
"""Defining amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representing an amenity.

    Attr:
        name (str): The amenity's name.
    """

    name = ""
