from module3d import Module3D
from vector3 import Vector3


G = 100
tempo = 1


class Grav3D(Module3D):
    def __init__(self, points=[], masses=[], velocities=[]):
        self.masses = masses
        self.velocities = velocities
        super(Grav3D, self).__init__(
            points,
            (-100, 100),
            (-100, 100),
            (-100, 100),
            plotmode="."
        )

    def new_point(self, t):
        for i, plist in enumerate(self.points):
            p = plist[0]
            acc = Vector3()
            for j, olist in enumerate(self.points):
                if i == j: continue
                o = olist[0]
                dist = abs(o-p)
                a = G * self.masses[j] / dist**3
                acc += (o - p) * a

            p += self.velocities[i] * tempo
            self.velocities[i] += acc * tempo
            plist[0] = p

        self.redraw()


if __name__ == "__main__":
    grav = Grav3D(
        [
            [Vector3(0.0, 0.0, 0.0)],
            [Vector3(50.0, 0.0, 0.0)],
            [Vector3(-50.0, 0.0, 0.0)]
        ],
        [1, 0.001, 0.001],
        [Vector3(0, 0, 0), Vector3(0, 1, 0), Vector3(0, -1, 0)]
    )
