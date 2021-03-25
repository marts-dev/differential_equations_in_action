import math
import numpy
import matplotlib.pyplot as plt

t = 0.1  # time step
g = 9.81  # m/s^2
acceleration = numpy.array([0.0, -g])
initial_speed = 20.0  # m/s


def trajectory():
    angles = numpy.linspace(20.0, 70.0, 6)

    num_steps = 30
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])

    for angle in angles:
        angle = angle * math.pi / 180
        x[0, 0] = 0.0
        x[0, 1] = 0.0
        v[0, 0] = initial_speed * math.cos(angle)
        v[0, 1] = initial_speed * math.sin(angle)
        for step in range(num_steps):
            v[step + 1] = v[step] + (t * acceleration)
            x[step + 1] = x[step] + (t * v[step])
        plt.plot(x[:, 0], x[:, 1])
    plt.axis("equal")
    axes = plt.gca()
    axes.set_xlabel("Horizontal position in m")
    axes.set_ylabel("Vertical position in m")
    plt.show()
    return x, v


x, v = trajectory()