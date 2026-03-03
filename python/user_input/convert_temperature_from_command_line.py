import sys

try:
    fahrenheit = float(sys.argv[1])

    celsius = (fahrenheit - 32) * 5 / 9

    print("Temperature in Fahrenheit:", fahrenheit)
    print("Temperature in Celsius:", celsius)

except:
    print("Please enter a temperature on the command line.")