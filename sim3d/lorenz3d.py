from module3d import Module3D


sigma = 10
beta = 16/3
ro = 28


class Lorenz3D(Module3D):
    def __init__(self, num_points=1):
        super(Lorenz3D, self).__init__(
            [[[1, 1, 1+0.01*i]] for i in range(num_points)],
            (-50, 50),
            (-50, 50),
            (0, 45)
        )

    def new_point(self, t):
        for plist in self.points:
            p = plist[-1]
            dx = (sigma * (p[1] - p[0])) / 100
            dy = (p[0] * (ro - p[2]) - p[1]) / 100
            dz = (p[0] * p[1] - beta * p[2]) / 100
            nx, ny, nz = p[0] + dx, p[1] + dy, p[2] + dz
            if t > 150:
                plist.append([nx, ny, nz])
            else:
                plist[-1] = [nx, ny, nz]

        self.redraw()


class Lorenz3Ddiff(Lorenz3D):
    def __init__(self):
        super(Lorenz3Ddiff, self).__init__(2)


if __name__ == "__main__":
    # l3d = Lorenz3D()
    l3ddiff = Lorenz3Ddiff()
