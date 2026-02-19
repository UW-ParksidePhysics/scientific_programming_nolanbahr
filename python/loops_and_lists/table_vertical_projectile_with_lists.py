v0 = 10.0
g = 14.12
n = 8

t_max = 2 * v0 / g
dt = t_max / n

t_values = []
y_values = []

for i in range(n + 1):
    t = i * dt
    y = v0 * t - 0.5 * g * t * t

    t_values.append(t)
    y_values.append(y)

print("t (s)   y (m)")

for t, y in zip(t_values, y_values):
    print(round(t, 3), round(y, 3))