file = open("scientific_programming_nolanbahr/python/user_input/temperature.txt", "r")
lines = file.readlines()
file.close()

out_file = open("converted.txt", "w")

for line in lines:
    if "Fahrenheit degrees:" in line:
        f = float(line.split(":")[1])
        c = (f - 32) * 5 / 9
        out_file.write(str(f) + "    " + str(c) + "\n")

out_file.close()

print("Finished")