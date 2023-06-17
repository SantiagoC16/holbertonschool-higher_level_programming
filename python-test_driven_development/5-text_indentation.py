#!/usr/bin/python3
"""task 5"""


def text_indentation(text):
    """task 5"""

    if not isinstance(text, str):
        TypeError("text must be a string")
    flag = False
    for t in text:
        if t == "." or t == ":" or t == "?":
            print(t)
            print()
            flag = True
        elif t != ' ' or not flag:
            print(t, end="")
            flag = False
