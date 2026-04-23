import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

planets = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Moon": 1.62,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.69,
    "Neptune": 11.15
}

planet_names = list(planets.keys())
gravities = list(planets.values())

start_height = 100
time_step = 0.07
total_time = 12

times = np.arange(0, total_time, time_step)

positions = []
for g in gravities:
    y = start_height - 0.5 * g * times**2
    y = np.maximum(y, 0)
    positions.append(y)

fig, ax = plt.subplots(figsize=(12, 6))

x_positions = np.arange(len(planet_names))

ax.set_xlim(-0.5, len(planet_names) - 0.5)
ax.set_ylim(0, start_height + 10)
ax.set_xticks(x_positions)
ax.set_xticklabels(planet_names, rotation=45, fontsize=11)
ax.set_ylabel("Height (meters)", fontsize=12)
ax.set_title("Balls Falling on Different Planets", fontsize=14)

planet_colors = [
    "gray", "goldenrod", "blue", "lightgray",
    "red", "orange", "khaki", "lightblue", "darkblue"
]

planet_sizes = [80, 140, 150, 60, 100, 300, 260, 220, 210]

# start them at the initial height instead of empty arrays
balls = ax.scatter(
    x_positions,
    [start_height] * len(planet_names),
    s=planet_sizes,
    c=planet_colors
)

planet_labels = []
for i in range(len(planet_names)):
    label = ax.text(
        x_positions[i], start_height + 2, planet_names[i],
        ha="center", fontsize=11, fontweight="bold"
    )
    planet_labels.append(label)

height_labels = []
for i in range(len(planet_names)):
    label = ax.text(x_positions[i], start_height + 7, "", ha="center", fontsize=9)
    height_labels.append(label)

def init():
    offsets = np.column_stack((x_positions, [start_height] * len(planet_names)))
    balls.set_offsets(offsets)
    for i in range(len(planet_names)):
        planet_labels[i].set_position((x_positions[i], start_height + 2))
        height_labels[i].set_text("")
        height_labels[i].set_position((x_positions[i], start_height + 7))
    return [balls] + planet_labels + height_labels

def update(frame):
    current_y = []

    for i in range(len(planet_names)):
        current_y.append(positions[i][frame])

    offsets = np.column_stack((x_positions, current_y))
    balls.set_offsets(offsets)

    for i in range(len(planet_names)):
        planet_labels[i].set_position((x_positions[i], current_y[i] + 2))
        height_labels[i].set_position((x_positions[i], current_y[i] + 7))
        height_labels[i].set_text(str(round(current_y[i], 1)) + " m")

    return [balls] + planet_labels + height_labels

anim = FuncAnimation(
    fig,
    update,
    frames=len(times),
    init_func=init,
    interval=50,
    blit=True
)

anim.save("planet_gravity.gif", writer="pillow", fps=20)

plt.close()
HTML(anim.to_jshtml())
