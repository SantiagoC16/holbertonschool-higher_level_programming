#!/usr/bin/python3
"""task 5"""
import json


def save_to_json_file(my_obj, filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dump(my_obj, file))
