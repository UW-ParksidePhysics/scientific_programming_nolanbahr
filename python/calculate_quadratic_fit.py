"""
Fit a quadratic polynomial to two-row x-y data.
"""

__author__ = "Nolan Bahr"

import numpy as np


def calculate_quadratic_fit(data):
    """
    Fit a quadratic polynomial to x-y data.

    Parameters:
        data: ndarray
            Two-row array containing x-y data.

    Returns:
        quadratic_coefficients: ndarray
            Coefficients ordered constant, linear, quadratic.
    """
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] < 3:
        raise IndexError("Data must have shape (2, M) with M at least 3.")

    x_values = data[0]
    y_values = data[1]

    quadratic_coefficients = np.polynomial.polynomial.polyfit(
        x_values,
        y_values,
        2
    )

    return quadratic_coefficients


if __name__ == "__main__":
    x_values = np.linspace(-1, 1)
    y_values = x_values**2
    data = np.array([x_values, y_values])

    coefficients = calculate_quadratic_fit(data)
    print(f"{coefficients=}")