#!/usr/bin/python3
"""Defining State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representing a state.

    Att:
        name (str): The state's name.
    """

    name = ""
