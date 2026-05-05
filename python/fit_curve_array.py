"""
Create a fit curve array from polynomial coefficients.
"""

__author__ = "Nolan Bahr"

import numpy as np


def fit_curve_array(
    quadratic_coefficients,
    minimum_x,
    maximum_x,
    number_of_points=100
):
    """
    Create x-y data from quadratic polynomial coefficients.

    Parameters:
        quadratic_coefficients: ndarray
            Polynomial coefficients ordered constant, linear, quadratic.
        minimum_x: float
            Starting x-value.
        maximum_x: float
            Ending x-value.
        number_of_points: int
            Number of points in the fit curve.

    Returns:
        fit_curve: ndarray
            Two-row array containing x-y fit curve data.
    """
    if maximum_x < minimum_x:
        raise ArithmeticError("maximum_x must be greater than minimum_x.")

    if number_of_points <= 2:
        raise IndexError("number_of_points must be greater than 2.")

    x_values = np.linspace(minimum_x, maximum_x, number_of_points)

    y_values = np.polynomial.polynomial.polyval(
        x_values,
        quadratic_coefficients
    )

    fit_curve = np.array([x_values, y_values])

    return fit_curve


if __name__ == "__main__":
    coefficients = np.array([0, 0, 1])
    fit_curve = fit_curve_array(coefficients, -2, 2)

    print(f"{fit_curve=}")