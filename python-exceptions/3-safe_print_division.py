#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if a == 0:
            return None
    except ZeroDivisionError:
        if b == 0:
            return None
    finally:
        ab = a + b
        print("{}".format(ab))
        return ab
