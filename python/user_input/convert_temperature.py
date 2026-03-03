def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return c + 273.15

def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return c * 9 / 5 + 32


file = open("scientific_programming_nolanbahr/python/user_input/temperature.txt", "r")
lines = file.readlines()
file.close()

out_file = open("converted2.txt", "w")

for line in lines:
    if "Fahrenheit degrees:" in line:
        f = float(line.split(":")[1])
        c = fahrenheit_to_celsius(f)
        k = fahrenheit_to_kelvin(f)
        out_file.write(str(f) + " F    " + str(c) + " C    " + str(k) + " K\n")

out_file.close()

print("Finished")