import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D


class Module3D:
    def __init__(self, start_points, xlim, ylim, zlim, interval=5):
        self.points = start_points
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_xlim(*xlim)
        self.ax.set_ylim(*ylim)
        self.ax.set_zlim(*zlim)

        self.plots = []
        for __ in range(len(start_points)):
            self.plots.append(
                self.ax.plot([], [], [], linewidth=1)[0]
            )

        self.animation = FuncAnimation(self.fig, self.new_point, interval=interval)
        plt.show()

    def new_point(self, t):
        self.redraw()

    def redraw(self):
        for i, plot in enumerate(self.plots):
            plot.set_data_3d(
                [p[0] for p in self.points[i]],
                [p[1] for p in self.points[i]],
                [p[2] for p in self.points[i]]
            )

