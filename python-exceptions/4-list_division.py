#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        for one in my_list_1:
            pass
        for two in my_list_2:
            pass
        new_list = []
        for i in range(list_length):
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return new_list
