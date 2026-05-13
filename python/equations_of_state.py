"""
Contains energy-volume equations of state and a function for fitting them.
"""

import numpy as np
from scipy.optimize import curve_fit


def fit_eos(volumes, energies, quadratic_coefficients, equation_of_state="birch-murnaghan", number_of_points=400):
    equation_fit_curve, equation_parameters = fit_equation_of_state(
        volumes,
        energies,
        quadratic_coefficients,
        equation_of_state=equation_of_state,
        number_of_points=number_of_points
    )

    return equation_fit_curve, equation_parameters


def fit_equation_of_state(volumes, energies, quadratic_coefficients, equation_of_state="birch-murnaghan", number_of_points=400):
    function_dictionary = {
        "vinet": vinet,
        "murnaghan": murnaghan,
        "birch-murnaghan": birch_murnaghan,
        "birch_murnaghan": birch_murnaghan
    }

    eos_function = function_dictionary[equation_of_state.lower()]

    minimum_volume = np.amin(volumes)
    maximum_volume = np.amax(volumes)

    quadratic_axis_of_symmetry = -quadratic_coefficients[1] / (
        2 * quadratic_coefficients[0]
    )

    quadratic_minimum = (
        quadratic_coefficients[2]
        - quadratic_coefficients[1] ** 2 / (4 * quadratic_coefficients[0])
    )

    quadratic_bulk_modulus = (
        2 * quadratic_coefficients[0] / quadratic_axis_of_symmetry
    )

    bulk_modulus_derivative = 3.7

    initial_parameters = [
        quadratic_minimum,
        quadratic_bulk_modulus,
        bulk_modulus_derivative,
        quadratic_axis_of_symmetry
    ]

    equation_parameters, equation_covariances = curve_fit(
        eos_function,
        volumes,
        energies,
        p0=initial_parameters,
        method="trf",
        maxfev=10000
    )

    fit_curve_volumes = np.linspace(
        minimum_volume,
        maximum_volume,
        num=number_of_points
    )

    equation_fit_curve = eos_function(
        fit_curve_volumes,
        equation_parameters[0],
        equation_parameters[1],
        equation_parameters[2],
        equation_parameters[3]
    )

    return equation_fit_curve, equation_parameters


def murnaghan(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
    k0pm1 = bulk_modulus_derivative - 1.0

    return equilibrium_energy + (
        bulk_modulus
        * equilibrium_volume
        * (
            (
                1.0 / (bulk_modulus_derivative * k0pm1)
            )
            * np.power(
                volumes / equilibrium_volume,
                -k0pm1
            )
            + volumes / (
                bulk_modulus_derivative * equilibrium_volume
            )
            - 1.0 / k0pm1
        )
    )


def birch_murnaghan(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
    reduced_volume_area = np.power(
        volumes / equilibrium_volume,
        -2.0 / 3.0
    )

    return equilibrium_energy + (
        9.0
        * bulk_modulus
        * equilibrium_volume
        / 16.0
    ) * (
        np.power(
            reduced_volume_area - 1.0,
            3.0
        )
        * bulk_modulus_derivative
        + np.power(
            reduced_volume_area - 1.0,
            2.0
        )
        * (
            6.0
            - 4.0 * reduced_volume_area
        )
    )


def vinet(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
    k0pm1 = bulk_modulus_derivative - 1.0
    k0pm1_squared = np.power(k0pm1, 2.0)

    reduced_volume_lengths = np.cbrt(
        volumes / equilibrium_volume
    )

    exponential_argument = (
        -1.5
        * k0pm1
        * (
            reduced_volume_lengths
            - 1.0
        )
    )

    exponential_factor = np.exp(exponential_argument)

    return equilibrium_energy + (
        2.0
        * bulk_modulus
        * equilibrium_volume
        / k0pm1_squared
    ) * (
        2.0
        - (
            5.0
            + 3.0
            * reduced_volume_lengths
            * k0pm1
            - 3.0
            * bulk_modulus_derivative
        )
        * exponential_factor
    )


if __name__ == "__main__":
    test_volumes = np.array([10, 11, 12, 13, 14])
    test_energies = np.array([-18, -21, -22, -21, -18.5])

    quadratic_coefficients = np.polyfit(
        test_volumes,
        test_energies,
        2
    )

    fit_curve, fit_parameters = fit_eos(
        test_volumes,
        test_energies,
        quadratic_coefficients
    )

    print(fit_parameters)
