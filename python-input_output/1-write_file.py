#!/usr/bin/python3
"""task 1"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
