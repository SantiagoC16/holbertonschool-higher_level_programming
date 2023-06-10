#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for p in range(x):
        try:
            if isinstance(p, int):
                print("{:d}".format(p), end="")
                printed += 1
                if printed == x:
                    break
        except (TypeError, ValueError):
            pass
    print()
    return printed
