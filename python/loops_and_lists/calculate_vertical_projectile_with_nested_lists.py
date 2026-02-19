v0 = 10.0
g = 9.8
n = 8

t_max = 2 * v0 / g
dt = t_max / n

times = []
positions = []

for i in range(n + 1):
    t = i * dt
    y = v0 * t - 0.5 * g * t * t

    times.append(t)
    positions.append(y)

times_positions = [times, positions]

print("t (s)    y (m)")

for i in range(len(times_positions[0])):
    print(f"{times_positions[0][i]:.2f}    {times_positions[1][i]:.2f}")

time_positions = []

for i in range(n + 1):
    row = [times[i], positions[i]]
    time_positions.append(row)

print("\nt (s)    y (m)")

for row in time_positions:
    print(f"{row[0]:.2f}    {row[1]:.2f}")
