#!/usr/bin/python3
""" more more more comment Base """
import json
import os


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

    @classmethod
    def create(cls, **dictionary):
        """class method"""

        if cls.__name__ == "Rectangle":
            tonto = cls(16, 16)
        else:
            tonto = cls(16)
        tonto.update(**dictionary)
        return tonto

    @classmethod
    def load_from_file(cls):
        """class method"""

        file = cls.__name__ + ".json"
        if os.path.exists(file):
            with open(file, mode="r") as filee:
                dict = cls.from_json_string(filee.read())
                list = []
                for x in dict:
                    list.append(cls.create(**x))
                return list
        else:
            return []
