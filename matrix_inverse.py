from __future__ import annotations

from decimal import Decimal


def inverse_of_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """

    >>> inverse_of_matrix([[2, 5], [2, 0]])
    [[0.0, 0.5], [0.2, -0.2]]
    >>> inverse_of_matrix([[2.5, 5], [1, 2]])
    Traceback (most recent call last):
    ...
    ValueError: This matrix has no inverse.
    >>> inverse_of_matrix([[12, -16], [-9, 0]])
    [[0.0, -0.1111111111111111], [-0.0625, -0.08333333333333333]]
    >>> inverse_of_matrix([[12, 3], [16, 8]])
    [[0.16666666666666666, -0.0625], [-0.3333333333333333, 0.25]]
    >>> inverse_of_matrix([[10, 5], [3, 2.5]])
    [[0.25, -0.5], [-0.3, 1.0]]
    """

    D = Decimal  # An abbreviation for conciseness

    # Check if the provided matrix has 2 rows and 2 columns
    # since this implementation only works for 2x2 matrices
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Please provide a matrix of size 2x2.")

    # Calculate the determinant of the matrix
    determinant = D(matrix[0][0]) * D(matrix[1][1]) - D(matrix[1][0]) * D(matrix[0][1])
    if determinant == 0:
        raise ValueError("This matrix has no inverse.")

    # Creates a copy of the matrix with swapped positions of the elements
    swapped_matrix = [[0.0, 0.0], [0.0, 0.0]]
    swapped_matrix[0][0], swapped_matrix[1][1] = matrix[1][1], matrix[0][0]
    swapped_matrix[1][0], swapped_matrix[0][1] = -matrix[1][0], -matrix[0][1]

    # Calculate the inverse of the matrix
    return [[float(D(n) / determinant) or 0.0 for n in row] for row in swapped_matrix]
