#!/usr/bin/python3
"""task 12"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """

    list = [[1]]
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        for one in range(n):
            list.append([1])
            for two in range(one):
                if two == one - 1:
                    list[one].append(1)
                else:
                    list[one].append(
                        list[one - 1][two + 1] + list[one - 1][two])
        return list
