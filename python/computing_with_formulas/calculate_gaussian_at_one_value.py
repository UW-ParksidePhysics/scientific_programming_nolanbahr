import math

mean = 0
standard_deviation = 2
input_value = 1

gaussian_value = (1 / (math.sqrt(2*math.pi) * standard_deviation)) * math.exp(-0.5 * ((input_value - mean) / standard_deviation)**2)

print("mean:", mean)
print("standard_deviation:", standard_deviation)
print("input_value:", input_value)
print("gaussian_value:", gaussian_value)
