#!/usr/bin/python3
"""Defining FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Representing abstracted storage engine.

    Attributes:
        __fil_path (str): Name of the file to save objcts to.
        __objtcts (dict): A dict of instantiated objcts.
    """
    __fil_path = "file.json"
    __objtcts = {}

    def all(self):
        """Returning the dict __objtcts."""
        return FileStorage.__objtcts

    def new(self, objt):
        """Set in __objtcts objt with key <objt_class_name>.id"""
        ocname = objt.__class__.__name__
        FileStorage.__objtcts["{}.{}".format(ocname, objt.id)] = objt

    def save(self):
        """Serializing __objtcts to the JSON file __fil_path."""
        odict = FileStorage.__objtcts
        objtdict = {objt: odict[objt].to_dict() for objt in odict.keys()}
        with open(FileStorage.__fil_path, "w") as f:
            json.dump(objtdict, f)

    def reload(self):
        """Deserializing the JSON file __fil_path to __objtcts."""
        try:
            with open(FileStorage.__fil_path) as f:
                objtdict = json.load(f)
                for p in objtdict.values():
                    cls_name = p["__class__"]
                    del p["__class__"]
                    self.new(eval(cls_name)(**p))
        except FileNotFoundError:
            return
