#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for p in my_list:
            if isinstance(p, int):
                print("{}".format(p), end="")
                printed += 1
                if printed == x:
                    break
    except IndexError:
        pass
    print()
    return printed
