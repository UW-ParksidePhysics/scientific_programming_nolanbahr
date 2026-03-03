file = open("scientific_programming_nolanbahr/python/user_input/temperature.txt", "r")

lines = file.readlines()

file.close()

line = lines[2]

fahrenheit = float(line.split(":")[1])

celsius = (fahrenheit - 32) * 5 / 9

print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Celsius:", celsius)