#!/usr/bin/python3
def uppercase(str):
    for s in range(str):
        ordd = ord(s)
        if ordd > 64 and ordd < 91:
            print("{}".format(chr(ordd)))
        else:
            strm = chr(ordd - 32)
            print("{}".format(strm))
