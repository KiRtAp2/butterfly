import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sqrt
from mpl_toolkits.mplot3d import Axes3D


SEED = 0
G = 1e-5


rng = np.random.default_rng(SEED)


class Points:
    def __init__(self, n):
        self.n = n
        self.points = rng.random((n, 3))
        self.velocities = rng.random((n, 3))
        self.masses = rng.random((n,))

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.graph, = self.ax.plot(self.points[:,0], self.points[:,1], self.points[:,2], linestyle="", marker="o")

        print("Starting points:")
        for i in range(self.n):
            print(self.points[i])

    def update(self, *args):
        for i in range(self.n):
            acc = np.zeros((3,))
            for j in range(self.n):
                if i == j:
                    continue
                dist = sqrt(np.sum((self.points[j] - self.points[i])**2))
                apart = G * self.masses[j] / dist**3
                acc += (self.points[j]-self.points[i]) * apart

            self.points[i] += self.velocities[i]
            self.velocities[i] += acc

        self.graph.set_data(self.points[:,0], self.points[:,1])
        self.graph.set_3d_properties(self.points[:,2])
        return self.graph,

points = Points(20)
animation = FuncAnimation(points.fig, points.update, interval=2000, blit=True)
# points.fig.show()
plt.show()
