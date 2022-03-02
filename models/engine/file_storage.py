#!/usr/bin/python3

from models.base_model import BaseModel
import json


class FileStorage():
    """Class that serializes instances and deserializes JSON file"""

    def __init__(self, __file_path, objects):
        """Initializes this class"""
        self.__file_path = file.json
        self.__objects = {}


    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.name + '.' + obj.id
        __objects.update(key, obj)

    def save(self):
    """Serializes __objects to the JSON file with __file_path"""
        for key, value in __objects.items():
            __objects[key] = value.__objects

        with open(__file_path, 'wb') as file:
            json.dump(__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(__file_path, 'rb') as file:
                __objects = json.load(file)

        except FileNotFoundError:
            pass

