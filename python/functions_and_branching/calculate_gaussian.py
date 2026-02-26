import math


def gaussian(position, mean=0, standard_deviation=1):

    coefficient = 1 / (math.sqrt(2 * math.pi) * standard_deviation)

    exponent_part = (position - mean) / standard_deviation
    exponent_part = exponent_part * exponent_part
    exponent_part = -0.5 * exponent_part

    value = coefficient * math.exp(exponent_part)

    return value


if __name__ == "__main__":

    mean = 0
    standard_deviation = 1
    n = 11

    start = mean - 5 * standard_deviation
    end = mean + 5 * standard_deviation

    step = (end - start) / (n - 1)

    print("x", "f(x)")
    print("----------------")

    x = start

    for i in range(n):

        fx = gaussian(x, mean, standard_deviation)

        print(x, fx)

        x = x + step