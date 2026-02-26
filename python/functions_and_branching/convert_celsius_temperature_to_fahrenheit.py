def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    celsius = (5 / 9) * (fahrenheit_temperature - 32)
    return celsius

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    fahrenheit = (9 / 5) * celsius_temperature + 32
    return fahrenheit

if __name__ == "__main__":

    # Celsius Temps
    freezing_c = 0
    room_temp_c = 21
    boiling_c = 100

    celsius_temperatures = [freezing_c, room_temp_c, boiling_c]

    print("Celsius -> Fahrenheit -> Celsius")
    print("--------------------------------")

    for temp_c in celsius_temperatures:
        temp_f = convert_celsius_temperature_to_fahrenheit(temp_c)
        converted_back_c = convert_fahrenheit_temperature_to_celsius(temp_f)

        print(f"{temp_c:6.1f} C -> {temp_f:6.1f} F -> {converted_back_c:6.1f} C")