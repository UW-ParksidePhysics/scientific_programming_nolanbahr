m = 0.5
g = 9.8
b = 0.1
v = 10

gravity_force = m * g
drag_force = -b * v

net_force = gravity_force + drag_force

print("Gravity force:", gravity_force, "N")
print("Drag force:", drag_force, "N")
print("Net force:", net_force, "N")