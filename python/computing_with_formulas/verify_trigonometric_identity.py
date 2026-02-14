import math

angle = math.pi / 4

sin_value = math.sin(angle)
cos_value = math.cos(angle)

left_side_value = sin_value**2 + cos_value**2
right_side_value = 1

print("angle:", angle)
print("sin(angle):", sin_value)
print("cos(angle):", cos_value)
print("sin(angle)^2 + cos(angle)^2:", left_side_value)
print("Should equal:", right_side_value)
