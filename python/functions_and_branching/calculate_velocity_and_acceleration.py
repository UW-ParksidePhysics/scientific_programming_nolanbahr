def calculate_velocity_and_acceleration(positions, index, time_step=1e-6):

    x_next = positions[index + 1]
    x_current = positions[index]
    x_previous = positions[index - 1]

    velocity = (x_next - x_previous) / (2 * time_step)

    acceleration = (x_next - 2 * x_current + x_previous) / (time_step * time_step)

    return velocity, acceleration


def test_kinematics():

    v = 2.2

    t0 = 0.0
    t1 = 0.5
    t2 = 1.5

    time_step = t1 - t0

    x0 = v * t0
    x1 = v * t1
    x2 = v * t2

    positions = [x0, x1, x2]

    velocity, acceleration = calculate_velocity_and_acceleration(positions, 1, time_step)

    print("positions:", positions)
    print("velocity:", velocity)
    print("acceleration:", acceleration)


if __name__ == "__main__":

    test_kinematics()