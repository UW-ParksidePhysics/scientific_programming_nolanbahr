a = 3.3
b = 5.3

left_sum_squared = (a + b)**2
right_sum_squared = a**2 + 2*a*b + b**2

left_difference_squared = (a - b)**2
right_difference_squared = a**2 - 2*a*b + b**2

print("a:", a)
print("b:", b)

print("(a+b)^2:", left_sum_squared)
print("a^2 + 2ab + b^2:", right_sum_squared)

print("(a-b)^2:", left_difference_squared)
print("a^2 - 2ab + b^2:", right_difference_squared)
