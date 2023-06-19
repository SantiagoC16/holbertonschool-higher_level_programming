#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for n in range(len(matrix)):
        square.append(list(map(lambda x: x ** 2, matrix[n])))
    return square
