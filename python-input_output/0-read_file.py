#!/usr/bin/python3
"""task 0"""


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
