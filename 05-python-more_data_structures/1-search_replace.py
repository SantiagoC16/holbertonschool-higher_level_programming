#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for n in range(len(new)):
        if new[n] == search:
            new[n] = replace
    return new
