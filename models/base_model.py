#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel():
    """BaseModel defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if kwargs is not None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        for key, value in kwargs.items():
            """created_at && updated_at converted to ISO format string"""
            if key in ["created_at", "updated_at"]:
                setattr(self, key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))

    def __str__(self):
        """prints strings"""
        return ('[{}] ({}) {}'.format
                (self.__class__.__name__, self.id, self.__dict__))

    """Public instance methods:"""
    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
