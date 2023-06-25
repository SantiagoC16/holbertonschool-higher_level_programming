#!/usr/bin/python3
"""task 10"""


class Student:
    """a"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            dicti = {}
            for iter in attrs:
                if iter in self.__dict__:
                    dicti[iter] = self.__dict__[iter]
            return dicti

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
