import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D


sigma = 10
beta = 16/3
ro = 28


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = [Point(1, 1, 1)]
p2 = [Point(1, 1, 1.01)]
points = [p1, p2]
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_zlim(0, 45)
plot1, = ax.plot([], [], [], linewidth=1)
plot2, = ax.plot([], [], [], linewidth=1, color="green")

plots = [plot1, plot2]


def new_point(t):
    for plist in points:
        p = plist[-1]
        dx = (sigma * (p.y - p.x)) / 100
        dy = (p.x * (ro - p.z) - p.y) / 100
        dz = (p.x * p.y - beta * p.z) / 100
        nx, ny, nz = p.x + dx, p.y + dy, p.z + dz
        if t > 150:
            plist.append(Point(nx, ny, nz))
        else:
            plist[-1].x = nx
            plist[-1].y = ny
            plist[-1].z = nz

    for i, plot in enumerate(plots):
        plot.set_data_3d(
            [p.x for p in points[i]],
            [p.y for p in points[i]],
            [p.z for p in points[i]]
        )


ani = FuncAnimation(fig, new_point, interval=5)

plt.show()
