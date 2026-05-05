"""
Create a combined plot of data points and a fit curve.
"""

__author__ = "Nolan Bahr"

import numpy as np
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="o", fit_format=""):
    """
    Plot data points and a fit curve.

    Parameters:
        data: ndarray
            Two-row x-y data array.
        fit_curve: ndarray
            Two-row x-y fit curve array.
        data_format: str
            Format string for data points.
        fit_format: str
            Format string for fit curve.

    Returns:
        combined_plot: list
            List of Line2D objects from pyplot plot.
    """
    if data.ndim != 2 or data.shape[0] != 2:
        raise IndexError("data must have shape (2, M).")

    if fit_curve.ndim != 2 or fit_curve.shape[0] != 2:
        raise IndexError("fit_curve must have shape (2, N).")

    data_plot = plt.plot(data[0], data[1], data_format)
    fit_plot = plt.plot(fit_curve[0], fit_curve[1], fit_format)

    combined_plot = data_plot + fit_plot

    return combined_plot


if __name__ == "__main__":
    data = np.array([
        [-2, -1, 0, 1, 2],
        [4, 1, 0, 1, 4]
    ])

    x_values = np.linspace(-2, 2)
    fit_curve = np.array([x_values, x_values**2])

    plot_data_with_fit(data, fit_curve, "x", "--")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()