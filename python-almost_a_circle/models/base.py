#!/usr/bin/python3
""" more more more comment Base """
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

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of dictionaries to a jason file"""

        if list_objs is None:
            return []
        else:
            if cls.__name__ == "Rectangle":
                with open("Rectangle.json", "w") as file:
                    json.dump(list_objs, file)
            else:
                with open("Square.json", "w") as file:
                    json.dump(list_objs, file)
