import numpy as np
import math
import matplotlib.pyplot as plt

def g(x):
    return (1 / math.sqrt(2 * math.pi)) * np.exp(-x**2 / 2)

x_values = np.linspace(-4, 4, 41)
y_values = g(x_values)

plt.plot(x_values, y_values)
plt.savefig("plot1.png")
plt.show()
