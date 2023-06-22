#!/usr/bin/python3
"""task 4"""


def inherits_from(obj, a_class):
    """comment"""
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    else:
        return False
