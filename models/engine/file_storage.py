#!/usr/bin/python3
"""Defines a dfgjdfg sdf class FileStorage.
"""
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity



class FileStorage():
    """Class that serializes jeiowej weokpsd dskjsdinstances to 
    a JSON file and sdfsdf sdfsfd deserializes
    JSON file to sdrijewor instances.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Creates new  weijowe instances of class.
        """
        pass

    def all(self):
        """Returns the jwoer weio dictionary objects.
        Returns:
            dict: objects.
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key sdfuisf <obj class name>.id.
        Args:
            obj jweoi (any): object.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to sdfio sdos- the JSON file (path: __file_path).
        """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as myFile:
            json.dump(dictionary, myFile)

    def reload(self):
        """Deserializes the  isjdfo JSON file to __objects only if the JSON file
        (__file_path) exists ; otherwise, sdfjo do nothing. If the file doesn’t
        exist, no exception dsofl should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                my_obj_dump = myFile.read()
        except Exception:
            return
        objects = eval(my_obj_dump)
        for (key, value) in objects.items():
            objects[key] = eval(key.split('.')[0] + '(**value)')
        self.__objects = objects

    def delete(self, obj):
        """remove obj from __objects
        """
        try:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del self.__objects[key]
            return True
        except Exception:
            return False
