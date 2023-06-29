#!/usr/bin/python3
""" more more more Base """
import json


class Base:
    """comment"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
