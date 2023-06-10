#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ab = a + b
    except ZeroDivisionError:
        if a == 0 or b == 0:
            return None
    finally:
        print("{}".format(ab))
        return ab
