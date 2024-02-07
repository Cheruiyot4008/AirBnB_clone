#!/usr/bin/python3
"""Defining the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Representing a city.

    Attr:
        state_id (str): The id of the state.
        name (str): The city's name.
    """

    state_id = ""
    name = ""
