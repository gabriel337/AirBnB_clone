#!/usr/bin/python3
"""File Storage"""

from models.base_model import BaseModel
import json
from models.user import User

class FileStorage():
    """Class that serializes instances and deserializes JSON file"""

    __file_path = 'file.json'
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User}


    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file with __file_path"""
        json_dict = {}

        for key, obj in FileStorage.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(json_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                json_dict = json.load(file)
            for key, value in json_dict.items():
                value = FileStorage.classes[value["__class__"]](value)
                FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass
