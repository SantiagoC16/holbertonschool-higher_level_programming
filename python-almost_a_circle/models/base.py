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
        """class method x jason"""

        lista = []
        with open(cls.__name__ + ".json", "w") as archivo:

            if list_objs is None:
                archivo.write("[]")
            else:
                for file in list_objs:
                    lista.append(file.to_dictionary())

                archivo.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """static method"""

        if json_string is None:
            return []
        else:
            return json.loads(json_string)
