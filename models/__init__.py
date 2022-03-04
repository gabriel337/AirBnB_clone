#!/usr/bin/python3
"""instance of FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class_name = {'BaseModel': BaseModel}

storage = FileStorage()
storage.reload()
