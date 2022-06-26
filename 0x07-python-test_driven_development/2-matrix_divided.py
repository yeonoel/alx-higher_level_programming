#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ Divide all elemnts of matrix
    Args:
        matrix(list): the matrix content liste of elemnts
        div(int or float): the devide all element in the list
            of matrix
    Return:
        new matrix with the result of all elemnts devide by div
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(num, list) for num in matrix) or
            not all((isinstance(item, (int, float)))
                    for item in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    newmatrix = [[round((i/div), 2)for i in num] for num in matrix]
    return (newmatrix)
