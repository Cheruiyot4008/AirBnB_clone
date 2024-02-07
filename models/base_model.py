#!/usr/bin/python3
"""Definition of BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representing BaseModel of HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializing a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dictionary): Key or the value pairs of attr.
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for l, v in kwargs.items():
                if l == "created_at" or l == "updated_at":
                    self.__dict__[l] = datetime.strptime(v, form)
                else:
                    self.__dict__[l] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updating the updated_at to the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returning the dict of the BaseModel instance."""

        gdict = self.__dict__.copy()
        gdict["created_at"] = self.created_at.isoformat()
        gdict["updated_at"] = self.updated_at.isoformat()
        gdict["__class__"] = self.__class__.__name__
        return gdict

    def __str__(self):
        """Returning print or string representing the BaseModel instance."""
        glname = self.__class__.__name__
        return "[{}] ({}) {}".format(glname, self.id, self.__dict__)
