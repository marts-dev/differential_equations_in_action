import math
import matplotlib.pyplot as plt
import numpy

moon_distance = 384e6


def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])

    for step in range(num_steps + 1):
        angle = 2.0 * math.pi * step / num_steps
        x[step, 0] = moon_distance * math.cos(angle)
        x[step, 1] = moon_distance * math.sin(angle)
    return x


def plot_orbit():
    plt.axis("equal")
    x = orbit()
    plt.plot(x[:, 0], x[:, 1])
    axes = plt.gca()
    axes.set_xlabel("Longitudinal position in m")
    axes.set_ylabel("Lateral position in m")
    plt.show()


plot_orbit()
