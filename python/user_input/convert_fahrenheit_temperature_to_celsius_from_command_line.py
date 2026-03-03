def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


file = open("scientific_programming_nolanbahr/python/user_input/temperature.txt", "r")
lines = file.readlines()
file.close()

out_file = open("converted3.txt", "w")

for line in lines:
    if "Fahrenheit degrees:" in line:
        f = float(line.split(":")[1])
        c = fahrenheit_to_celsius(f)
        out_file.write("Fahrenheit: " + str(f) + "   Celsius: " + str(c) + "\n")

out_file.close()

print("Finished")