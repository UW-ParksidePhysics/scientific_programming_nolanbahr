"""
Calculate statistics for a two-row x-y data array.
"""

__author__ = "Nolan Bahr"

import numpy as np
from scipy import stats


def calculate_bivariate_statistics(data):
    """
    Calculate requested statistics for bivariate data.

    Parameters:
        data: ndarray
            Two-row array containing x-y data.

    Returns:
        statistics: ndarray
            Mean y, standard deviation y, minimum x, maximum x,
            minimum y, and maximum y.
    """
    if data.ndim != 2 or data.shape[0] != 2 or data.shape[1] < 2:
        raise IndexError("Data must have shape (2, M) with M at least 2.")

    x_values = data[0]
    y_values = data[1]

    description = stats.describe(y_values)

    mean_y = description.mean
    standard_deviation_y = np.sqrt(description.variance)
    minimum_x = np.min(x_values)
    maximum_x = np.max(x_values)
    minimum_y = description.minmax[0]
    maximum_y = description.minmax[1]

    statistics = np.array([
        mean_y,
        standard_deviation_y,
        minimum_x,
        maximum_x,
        minimum_y,
        maximum_y
    ])

    return statistics


if __name__ == "__main__":
    x_values = np.linspace(-10, 10, 21)
    y_values = x_values**2
    data = np.array([x_values, y_values])

    statistics = calculate_bivariate_statistics(data)
    print(f"{statistics=}")