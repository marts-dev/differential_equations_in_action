import numpy
import matplotlib.pyplot as plt

t = 1.0  # s time step
earth_mass = 5.97e24  # kg
gravitational_constant = 6.67e-11  # N m^2/kg^2


def acceleration(spaceship_position):
    vector_to_earth = -spaceship_position
    return gravitational_constant * (
        earth_mass / (numpy.linalg.norm(vector_to_earth) ** 3) * vector_to_earth
    )


def ship_trajectory():
    num_steps = 13000
    x = numpy.zeros([num_steps + 1, 2])  # m
    v = numpy.zeros([num_steps + 1, 2])  # m/s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    for step in range(num_steps):
        x[step + 1] = x[step] + (t * v[step])
        v[step + 1] = v[step] + (t * acceleration(x[step]))
    return x, v


x, v = ship_trajectory()


def plot_trajectory():
    plt.plot(x[:, 0], x[:, 1])
    plt.scatter(0, 0)
    plt.axis("equal")
    axes = plt.gca()
    axes.set_xlabel("Longitudinal position in m")
    axes.set_ylabel("Lateral position in m")
    plt.show()


plot_trajectory()