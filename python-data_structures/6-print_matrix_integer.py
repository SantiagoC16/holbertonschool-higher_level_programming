#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            print("{:d} ".format(matrix[n][m]), end="")
        print()
