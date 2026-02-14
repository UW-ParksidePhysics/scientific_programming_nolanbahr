import math

drag_coefficient = 0.2
air_density = 1.2
ball_radius = 0.11
ball_mass = 0.43
gravitational_acceleration = 9.81

cross_section_area = math.pi * ball_radius**2

soft_kick_velocity_kmh = 10
hard_kick_velocity_kmh = 120

soft_kick_velocity = soft_kick_velocity_kmh / 3.6
hard_kick_velocity = hard_kick_velocity_kmh / 3.6

gravitational_force = ball_mass * gravitational_acceleration

soft_kick_drag_force = 0.5 * drag_coefficient * air_density * cross_section_area * soft_kick_velocity**2
hard_kick_drag_force = 0.5 * drag_coefficient * air_density * cross_section_area * hard_kick_velocity**2

soft_kick_ratio = soft_kick_drag_force / gravitational_force
hard_kick_ratio = hard_kick_drag_force / gravitational_force

print("Soft kick velocity (km/h):", soft_kick_velocity_kmh)
print("Soft kick velocity (m/s):", soft_kick_velocity)
print("Soft kick drag force:", round(soft_kick_drag_force, 1))
print("Gravity force:", round(gravitational_force, 1))
print("Soft kick ratio (drag/gravity):", round(soft_kick_ratio, 3))
print()

print("Hard kick velocity (km/h):", hard_kick_velocity_kmh)
print("Hard kick velocity (m/s):", hard_kick_velocity)
print("Hard kick drag force:", round(hard_kick_drag_force, 1))
print("Gravity force:", round(gravitational_force, 1))
print("Hard kick ratio (drag/gravity):", round(hard_kick_ratio, 3))
