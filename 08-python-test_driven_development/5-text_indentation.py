#!/usr/bin/python3
"""task 5"""


def text_indentation(text):
    """task 5"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    bool = False
    i = 0
    while i < len(text):
        if bool:
            bool = False
            continue
        if text[i] == "." or text[i] == ":" or text[i] == "?":
            print(f"{text[i]}")
            print("")
            j = i + 1
            count = 0
            while j < len(text) and text[j] == " ":
                count += 1
                j += 1
            i += count
        else:
            print(f"{text[i]}", end="")
        i += 1
