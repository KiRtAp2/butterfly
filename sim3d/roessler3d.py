from module3d import Module3D


a = 0.1
b = 0.1
c = 14


FACTOR = 1e-2


class Roessler3D(Module3D):
    def __init__(self, num_points=1):
        super(Roessler3D, self).__init__(
            [[[1, 1, 1+0.01*i]] for i in range(num_points)],
            (-100, 100),
            (-100, 100),
            (-100, 100),
            interval=1
        )

    def new_point(self, t):
        for plist in self.points:
            p = plist[-1]
            dx = (-p[1] - p[2]) * FACTOR
            dy = (p[0] + a*p[1]) * FACTOR
            dz = (b + p[2] * (p[0] - c)) * FACTOR
            nx, ny, nz = p[0] + dx, p[1] + dy, p[2] + dz
            if t > 150:
                plist.append([nx, ny, nz])
            else:
                plist[-1] = [nx, ny, nz]

        self.redraw()


if __name__ == "__main__":
    r3d = Roessler3D()
