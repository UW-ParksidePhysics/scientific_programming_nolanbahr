"""
Read two columns of numerical data from a text file.
"""

__author__ = "Nolan Bahr"

import numpy as np


def read_two_columns_text(filename):
    """
    Read two columns of data from a text file.

    Parameters:
        filename: str
            Name of the file to read.

    Returns:
        data: ndarray
            Two-row array containing x-y data.
    """
    try:
        data = np.loadtxt(filename, unpack=True)
    except OSError as error:
        raise OSError(f"Could not read file: {filename}") from error

    return data


if __name__ == "__main__":
    data = read_two_columns_text("volumes_energies.dat")
    print(f"{data=}, shape={data.shape}")