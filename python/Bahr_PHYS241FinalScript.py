import warnings
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from datetime import date

from equations_of_state import fit_eos
from generate_matrix import generate_matrix


warnings.filterwarnings("ignore")

display_graph = True

data_file_name = "Sn.Fd-3m.GGA-PBE.volumes_energies.dat"

fit_function_name = "Birch-Murnaghan"

potential_name = "Harmonic"

potential_parameter = 1

Ndim = 200

eigenvector_indices = [0, 1, 2]

number_of_atoms = 2


def parse_file_name(file_name):
    pieces = file_name.split(".")
    chemical_symbol = pieces[0]
    crystal_symbol = pieces[1]
    approximation = pieces[2]
    return chemical_symbol, crystal_symbol, approximation


def read_two_columns_text(file_name):
    data = np.loadtxt(file_name)
    return data


def calculate_bivariate_statistics(data):
    x = data[:, 0]
    y = data[:, 1]

    stats = {
        "min_x": np.min(x),
        "max_x": np.max(x),
        "min_y": np.min(y),
        "max_y": np.max(y)
    }

    return stats


def calculate_quadratic_fit(data):
    x = data[:, 0]
    y = data[:, 1]

    coefficients = np.polyfit(x, y, 2)

    return coefficients


def convert_units(value, units_from, units_to):
    units_from = units_from.strip().lower()
    units_to = units_to.strip().lower()

    bohr_to_angstrom = constants.physical_constants["Bohr radius"][0] * 1e10

    rydberg_to_ev = constants.physical_constants[
        "Rydberg constant times hc in eV"
    ][0]

    ev_per_angstrom3_to_gpa = constants.electron_volt / 1e-30 / 1e9

    if units_from == "bohr^3/atom" and units_to == "angstrom^3/atom":
        return value * bohr_to_angstrom**3

    elif units_from == "rydberg/atom" and units_to == "ev/atom":
        return value * rydberg_to_ev

    elif units_from == "rydberg/bohr^3" and units_to == "gpa":
        return (
            value
            * rydberg_to_ev
            / bohr_to_angstrom**3
            * ev_per_angstrom3_to_gpa
        )

    else:
        raise ValueError(
            f"Unsupported conversion from '{units_from}' to '{units_to}'"
        )


def calculate_lowest_eigenvectors(matrix, indices):
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)

    selected_values = eigenvalues[indices]
    selected_vectors = eigenvectors[:, indices]

    return selected_values, selected_vectors


def annotate_plot(text, x, y, fontsize=10, ha="left"):
    plt.annotate(
        text,
        xy=(x, y),
        xycoords="axes fraction",
        fontsize=fontsize,
        ha=ha
    )


def make_equation_of_state_plot():
    chemical_symbol, crystal_symbol, approximation = parse_file_name(
        data_file_name
    )

    data = read_two_columns_text(data_file_name)

    data[:, 0] = data[:, 0] / number_of_atoms
    data[:, 1] = data[:, 1] / number_of_atoms

    stats = calculate_bivariate_statistics(data)

    quadratic_coefficients = calculate_quadratic_fit(data)

    volume_fit = np.linspace(
        stats["min_x"],
        stats["max_x"],
        400
    )

    energy_fit, eos_parameters = fit_eos(
        data[:, 0],
        data[:, 1],
        quadratic_coefficients,
        equation_of_state="birch-murnaghan",
        number_of_points=400
    )

    equilibrium_energy = eos_parameters[0]
    bulk_modulus = eos_parameters[1]
    bulk_modulus_derivative = eos_parameters[2]
    equilibrium_volume = eos_parameters[3]

    volume_data_converted = convert_units(
        data[:, 0],
        "bohr^3/atom",
        "angstrom^3/atom"
    )

    energy_data_converted = convert_units(
        data[:, 1],
        "rydberg/atom",
        "eV/atom"
    )

    volume_fit_converted = convert_units(
        volume_fit,
        "bohr^3/atom",
        "angstrom^3/atom"
    )

    energy_fit_converted = convert_units(
        energy_fit,
        "rydberg/atom",
        "eV/atom"
    )

    equilibrium_volume_converted = convert_units(
        equilibrium_volume,
        "bohr^3/atom",
        "angstrom^3/atom"
    )

    bulk_modulus_converted = convert_units(
        bulk_modulus,
        "rydberg/bohr^3",
        "GPa"
    )

    x_range = np.max(volume_data_converted) - np.min(volume_data_converted)
    y_range = np.max(energy_data_converted) - np.min(energy_data_converted)

    x_min = np.min(volume_data_converted) - 0.10 * x_range
    x_max = np.max(volume_data_converted) + 0.10 * x_range

    y_min = np.min(energy_data_converted) - 0.10 * y_range
    y_max = np.max(energy_data_converted) + 0.10 * y_range

    minimum_energy = np.min(energy_fit_converted)

    plt.figure(figsize=(8, 6))

    plt.plot(
        volume_fit_converted,
        energy_fit_converted,
        color="black",
        linestyle="-"
    )

    plt.scatter(
        volume_data_converted,
        energy_data_converted,
        color="blue"
    )

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.xlabel(r"$V$ [$\mathrm{\AA^3/atom}$]")
    plt.ylabel(r"$E$ [$\mathrm{eV/atom}$]")

    plt.axvline(
        equilibrium_volume_converted,
        color="black",
        linestyle="--"
    )

    plt.text(
        equilibrium_volume_converted,
        y_min + 0.5 * (minimum_energy - y_min),
        rf"$V_0$ = {equilibrium_volume_converted:.2f} $\mathrm{{\AA^3/atom}}$",
        fontsize=10
    )

    annotate_plot(
        chemical_symbol,
        0.05,
        0.92,
        fontsize=14
    )

    annotate_plot(
        rf"$\it{{{crystal_symbol}}}$",
        0.50,
        0.70,
        fontsize=14,
        ha="center"
    )

    annotate_plot(
        rf"$B_0$ = {bulk_modulus_converted:.1f} GPa",
        0.50,
        0.78,
        fontsize=12,
        ha="center"
    )

    today = date.today().isoformat()

    plt.figtext(
        0.02,
        0.01,
        f"Created by Nolan Bahr {today}",
        ha="left",
        fontsize=9
    )

    plt.title(
        f"{fit_function_name} Equation of State for "
        f"{chemical_symbol} in DFT {approximation}"
    )

    plt.tight_layout()

    file_out = (
        f"Bahr."
        f"{chemical_symbol}."
        f"{crystal_symbol}."
        f"{approximation}."
        f"{fit_function_name.replace('-', '')}"
        f"EquationOfState.png"
    )

    if display_graph:
        plt.show()
    else:
        plt.savefig(file_out, dpi=300)

    plt.close()


def make_eigenvector_plot():
    matrix = generate_matrix(
        -10,
        10,
        Ndim,
        potential_name,
        potential_parameter
    )

    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(
        matrix,
        eigenvector_indices
    )

    x_grid = np.linspace(-10, 10, Ndim)

    plt.figure(figsize=(8, 6))

    largest_component = np.max(np.abs(eigenvectors))

    for i in range(len(eigenvector_indices)):
        index = eigenvector_indices[i]
        eigenvalue = eigenvalues[i]
        eigenvector = eigenvectors[:, i]

        if index == 0 and np.sum(eigenvector) < 0:
            eigenvector = -1 * eigenvector

        plt.plot(
            x_grid,
            eigenvector,
            linestyle="-",
            label=rf"$\psi_{{{index}}}$, "
                  rf"$E_{{{index}}}$ = "
                  rf"{eigenvalue:.3f} a.u."
        )

    plt.axhline(
        0,
        color="black",
        linestyle="-"
    )

    plt.ylim(
        -2 * largest_component,
        2 * largest_component
    )

    plt.xlabel("x [a.u.]")
    plt.ylabel(r"$\psi$ [a.u.]")

    plt.legend()

    today = date.today().isoformat()

    plt.figtext(
        0.02,
        0.01,
        f"Created by Nolan Bahr {today}",
        ha="left",
        fontsize=9
    )

    plt.title(
        f"Select Wavefunctions for a "
        f"{potential_name} Potential "
        f"on a Spatial Grid of {Ndim} Points"
    )

    plt.tight_layout()

    file_out = (
        f"Bahr."
        f"{potential_name}."
        f"Eigenvector"
        f"{eigenvector_indices[0]}"
        f".png"
    )

    if display_graph:
        plt.show()
    else:
        plt.savefig(file_out, dpi=300)

    plt.close()


if __name__ == "__main__":
    make_equation_of_state_plot()
    make_eigenvector_plot()