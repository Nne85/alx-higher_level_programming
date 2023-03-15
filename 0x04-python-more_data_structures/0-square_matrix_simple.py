def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix"""
    # Create a new matrix with the same size as the input
    result = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
    # Fill in the values by squaring the corresponding input value
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2
    return result

