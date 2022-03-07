#!/usr/bin/python3
"""contains subclass user
"""
import json
from models.base_model import BaseModel


class User(BaseModel):
    """users email, password, first and last name"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
