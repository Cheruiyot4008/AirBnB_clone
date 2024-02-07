#!/usr/bin/python3
"""Defining place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representing a specific place.

    Attr:
        city_id (str): The city id.
        user_id (str): The user id.
        name (str): The name of place.
        descript (str): The description of the place.
        no_rooms (int): The no. of rooms of the place.
        no_bathrooms (int): The no of bathrooms of the place.
        maxim_guest (int): The maximum no. of guests of the place.
        price_by_night (int): The price by night.
        latitude (float): The lat of the place.
        longitude (float): The long of the place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    descript = ""
    no_rooms = 0
    no_bathrooms = 0
    maxim_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
