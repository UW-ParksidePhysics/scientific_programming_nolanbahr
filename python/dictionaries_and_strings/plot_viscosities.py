import matplotlib.pyplot as plt

def parse_viscosity_data(filename):
    viscosity_data = {}
    file = open(filename, "r")

    for line in file:
        if line.startswith("#"):
            continue

        parts = line.split()

        if len(parts) == 0:
            continue

        if parts[0] == "gas":
            continue

        if len(parts) == 5:
            gas = parts[0] + "_" + parts[1]
            C = float(parts[2])
            T0 = float(parts[3])
            mu0 = float(parts[4])
        else:
            gas = parts[0]
            C = float(parts[1])
            T0 = float(parts[2])
            mu0 = float(parts[3])

        viscosity_data[gas] = {}
        viscosity_data[gas]["C"] = C
        viscosity_data[gas]["T0"] = T0
        viscosity_data[gas]["mu0"] = mu0

    file.close()
    return viscosity_data


def calculate_viscosity(temperature, gas, viscosity_data):
    C = viscosity_data[gas]["C"]
    T0 = viscosity_data[gas]["T0"]
    mu0 = viscosity_data[gas]["mu0"]

    mu = mu0 * ((T0 + C) / (temperature + C)) * (temperature / T0) ** 1.5
    return mu


def plot_viscosities(viscosity_data):
    temperatures = []

    for T in range(223, 374):
        temperatures.append(T)

    gases = ["air", "carbon_dioxide", "hydrogen"]

    for gas in gases:
        viscosities = []

        for T in temperatures:
            mu = calculate_viscosity(T, gas, viscosity_data)
            viscosities.append(mu)

        plt.plot(temperatures, viscosities, label=gas)

    plt.xlabel("Temperature (K)")
    plt.ylabel("Viscosity")
    plt.title("Viscosity vs Temperature")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    viscosity_data = parse_viscosity_data(
        "scientific_programming_nolanbahr/python/dictionaries_and_strings/viscosity_of_gases.dat"
    )
    plot_viscosities(viscosity_data)