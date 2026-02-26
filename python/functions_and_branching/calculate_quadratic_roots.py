import math


def calculate_quadratic_roots(a, b, c):

    discriminant = b * b - 4 * a * c

    if discriminant > 0:

        sqrt_discriminant = math.sqrt(discriminant)

        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)

        return root1, root2

    elif discriminant == 0:

        root = -b / (2 * a)

        return root, root

    else:

        positive_discriminant = -discriminant
        sqrt_discriminant = math.sqrt(positive_discriminant)

        real_part = -b / (2 * a)
        imaginary_part = sqrt_discriminant / (2 * a)

        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)

        return root1, root2


def test_single_root():

    a = 1
    b = -2
    c = 1

    roots = calculate_quadratic_roots(a, b, c)

    print("x^2 - 2x + 1 = 0")
    print("Quadratic Roots:", roots[0])


def test_roots_float():

    a = 1
    b = -3
    c = 2

    roots = calculate_quadratic_roots(a, b, c)

    print("x^2 - 3x + 2 = 0")
    print("Quadratic Roots:", roots[0], "and", roots[1])


def test_roots_complex():

    a = 2
    b = 2
    c = 1

    roots = calculate_quadratic_roots(a, b, c)

    print("2x^2 + 2x + 1 = 0")
    print("Quadratic Roots:", roots[0], "and", roots[1])


if __name__ == "__main__":

    test_single_root()
    print()

    test_roots_float()
    print()

    test_roots_complex()