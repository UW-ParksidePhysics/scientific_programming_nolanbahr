import math

# physical properties of the egg
egg_density = 1.038
egg_specific_heat = 3.7
egg_thermal_conductivity = 5.4e-3

# temperatures
boiling_water_temperature = 100
target_yolk_temperature = 70

# egg masses
small_egg_mass = 47
large_egg_mass = 67

# initial egg temperatures
fridge_temperature = 4
room_temperature = 20


small_egg_fridge_cook_time = (small_egg_mass**(2/3) * egg_specific_heat * egg_density**(1/3)) / (egg_thermal_conductivity * (4*math.pi/3)**(2/3)) * math.log(0.76 * (boiling_water_temperature - fridge_temperature) / (target_yolk_temperature - fridge_temperature))
print("Small egg from fridge:", small_egg_fridge_cook_time, "seconds =", small_egg_fridge_cook_time/60, "minutes")

small_egg_room_cook_time = (small_egg_mass**(2/3) * egg_specific_heat * egg_density**(1/3)) / (egg_thermal_conductivity * (4*math.pi/3)**(2/3)) * math.log(0.76 * (boiling_water_temperature - room_temperature) / (target_yolk_temperature - room_temperature))
print("Small egg from room temperature:", small_egg_room_cook_time, "seconds =", small_egg_room_cook_time/60, "minutes")

large_egg_fridge_cook_time = (large_egg_mass**(2/3) * egg_specific_heat * egg_density**(1/3)) / (egg_thermal_conductivity * (4*math.pi/3)**(2/3)) * math.log(0.76 * (boiling_water_temperature - fridge_temperature) / (target_yolk_temperature - fridge_temperature))
print("Large egg from fridge:", large_egg_fridge_cook_time, "seconds =", large_egg_fridge_cook_time/60, "minutes")

large_egg_room_cook_time = (large_egg_mass**(2/3) * egg_specific_heat * egg_density**(1/3)) / (egg_thermal_conductivity * (4*math.pi/3)**(2/3)) * math.log(0.76 * (boiling_water_temperature - room_temperature) / (target_yolk_temperature - room_temperature))
print("Large egg from room temperature:", large_egg_room_cook_time, "seconds =", large_egg_room_cook_time/60, "minutes")
