#!/usr/bin/python3
"""Defining Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing a review.

    Attr:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the reviewer.
    """

    place_id = ""
    user_id = ""
    text = ""
