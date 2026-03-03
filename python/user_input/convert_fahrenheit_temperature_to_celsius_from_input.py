try:
    text = input("Enter temperature in Fahrenheit: ")
    fahrenheit = float(text)

    celsius = (fahrenheit - 32) * 5 / 9

    print("Temperature in Fahrenheit:", fahrenheit)
    print("Temperature in Celsius:", celsius)

except:
    print("Please enter a valid number.")