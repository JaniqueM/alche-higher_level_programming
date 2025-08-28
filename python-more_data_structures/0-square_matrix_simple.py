#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions
    # Each element squared, without modifying the original matrix
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix

