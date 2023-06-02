#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        ordd = ord(str[s])
        if ordd > 96 and ordd < 123:
            ordd = ordd - 32
        print("{}".format(chr(ordd)), end="")
print()
