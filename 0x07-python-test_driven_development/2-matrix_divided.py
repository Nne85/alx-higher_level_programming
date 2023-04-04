#!/usr/bin/python3

"""
This module divides all elements of a matrix whose row
contains int or float data type with an int or float divider

"""



def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    matrix: list of lists of integers/floats representing a matrix
    div: number (integer or float) to divide the matrix with

    Returns:
    new_matrix: new matrix with all elements divided by div and rounded to 2 decimal places
    """

    # Check if matrix is a list of lists of integers/floats
    if type(matrix) is not list or not all(type(row) is list for row in matrix) \
            or not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of matrix is of the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of matrix by div and round the result to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
