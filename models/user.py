#!/usr/bin/python3
"""Definition of the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representing a User.

    Attr:
        email (str): The user's email.
        passkey (str): The user's passkey.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    email = ""
    passkey = ""
    first_name = ""
    last_name = ""
