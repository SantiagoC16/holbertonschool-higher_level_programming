#!/usr/bin/python3
def pascal_triangle(n):
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
