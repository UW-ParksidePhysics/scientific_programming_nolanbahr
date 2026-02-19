# values given
v0 = 10.0
n = 8

# gravity values
g1 = 14.12
g2 = 12.94

# max times
t_max1 = 2 * v0 / g1
t_max2 = 2 * v0 / g2

# time steps
dt1 = t_max1 / n
dt2 = t_max2 / n

# for loop
print("using a for loop")
print("t (s)   y (m)      t (s)   y (m)")

for i in range(n + 1):
    t1 = i * dt1
    t2 = i * dt2

    y1 = v0 * t1 - 0.5 * g1 * t1 * t1
    y2 = v0 * t2 - 0.5 * g2 * t2 * t2

    print(round(t1, 3), round(y1, 3), "   ",
          round(t2, 3), round(y2, 3))

# while loop
print("\nusing a while loop")
print("t (s)   y (m)      t (s)   y (m)")

i = 0

while i <= n:
    t1 = i * dt1
    t2 = i * dt2

    y1 = v0 * t1 - 0.5 * g1 * t1 * t1
    y2 = v0 * t2 - 0.5 * g2 * t2 * t2

    print(round(t1, 3), round(y1, 3), "   ",
          round(t2, 3), round(y2, 3))

    i = i + 1
