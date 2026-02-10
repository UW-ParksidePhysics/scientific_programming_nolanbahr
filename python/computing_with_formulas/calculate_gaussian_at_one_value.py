import math
x = 1.0
mu = 0.0
sigma = 1.0
gaussian = (1 / (sigma* math.sqrt(2 * math.pi))) * math.exp(-((x -mu)**2) / (2 * sigma**2))
print("Gaussian value:", gaussian)