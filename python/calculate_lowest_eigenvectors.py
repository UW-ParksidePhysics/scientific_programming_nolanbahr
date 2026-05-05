"""
Calculate the lowest eigenvalues and corresponding eigenvectors.
"""

__author__ = "Nolan Bahr"

import numpy as np


def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    """
    Calculate eigenvectors with the lowest eigenvalues.

    Parameters:
        square_matrix: ndarray
            Square matrix to characterize.
        number_of_eigenvectors: int
            Number of eigenvectors to return.

    Returns:
        eigenvalues: ndarray
            Lowest eigenvalues sorted from lowest to highest.
        eigenvectors: ndarray
            Eigenvectors corresponding to the sorted eigenvalues.
    """
    if square_matrix.ndim != 2:
        raise IndexError("square_matrix must be a two-dimensional array.")

    if square_matrix.shape[0] != square_matrix.shape[1]:
        raise IndexError("square_matrix must be square.")

    number_of_rows = square_matrix.shape[0]

    if number_of_eigenvectors < 1:
        raise IndexError("number_of_eigenvectors must be at least 1.")

    if number_of_eigenvectors > number_of_rows:
        raise IndexError(
            "number_of_eigenvectors cannot be greater than matrix size."
        )

    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)

    sorted_indices = np.argsort(eigenvalues)
    lowest_indices = sorted_indices[:number_of_eigenvectors]

    lowest_eigenvalues = eigenvalues[lowest_indices]
    lowest_eigenvectors = eigenvectors[:, lowest_indices].T

    return lowest_eigenvalues, lowest_eigenvectors


if __name__ == "__main__":
    square_matrix = np.array([
        [2, -1],
        [-1, 2]
    ])

    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(
        square_matrix,
        2
    )

    print(f"{eigenvalues=}")
    print(f"{eigenvectors=}")