import numpy as np
import matplotlib.pyplot as plt

# constants
k = 1e-6
A1 = 15
A2 = 7
P1 = 365
P2 = 24

w1 = 2 * np.pi / P1
w2 = 2 * np.pi / P2

a1 = np.sqrt(w1 / (2 * k))
a2 = np.sqrt(w2 / (2 * k))

T0 = 10

# depth values
z = np.linspace(0, 1, 100)

# time values
t = np.linspace(0, P2, 100)

# make grid
T = []

for ti in t:
    row = []
    for zi in z:
        temp = T0 \
        + A1 * np.exp(-a1 * zi) * np.sin(w1 * ti - a1 * zi) \
        + A2 * np.exp(-a2 * zi) * np.sin(w2 * ti - a2 * zi)
        row.append(temp)
    T.append(row)

T = np.array(T)

plt.imshow(T, aspect='auto')
plt.colorbar()
plt.xlabel("Depth")
plt.ylabel("Time")
plt.savefig("plot3.png")
plt.show()
