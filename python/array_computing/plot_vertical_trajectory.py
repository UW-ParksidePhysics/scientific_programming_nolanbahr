import sys
import numpy as np
import matplotlib.pyplot as plt

g = float(sys.argv[1])

v0_values = []
for i in range(2, len(sys.argv)):
    v0_values.append(float(sys.argv[i]))

for v0 in v0_values:
    t = np.linspace(0, 2 * v0 / g, 100)
    y = v0 * t - 0.5 * g * t**2
    plt.plot(t, y)
plt.savefig("plot2.png")
plt.show()
