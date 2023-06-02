#!/usr/bin/python3
def fizzbuzz():
    for n in range(0, 101):
        if n != 0 and n % 3 == 0 and n % 5 != 0:
            print("Fizz".format(n), end=" ")
        elif n != 0 and n % 5 == 0 and n % 3 != 0:
            print("Buzz".format(n), end=" ")
        elif n != 0 and n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz".format(n), end=" ")
        else:
            print("{:01d}".format(n), end=" ")
