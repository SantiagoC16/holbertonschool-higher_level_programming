#!/usr/bin/python3
"""task 6"""
import json


def load_from_json_file(filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.loads(file.read())
