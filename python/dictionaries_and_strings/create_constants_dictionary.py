def parse_constants_file(filename):
    constants = {}
    file = open(filename, "r")

    for line in file:
        parts = line.split()

        for i in range(len(parts)):
            try:
                value = float(parts[i])
                name = " ".join(parts[:i])
                constants[name] = value
                break
            except ValueError:
                pass

    file.close()
    return constants


if __name__ == "__main__":
    constants = parse_constants_file("scientific_programming_nolanbahr/python/dictionaries_and_strings/constants.txt")
    print(constants)