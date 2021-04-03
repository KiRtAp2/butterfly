import math


# copied code from ../vector.py
class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, o):
        return Vector3(self.x+o.x, self.y+o.y, self.z+o.z)

    def __sub__(self, o):
        return Vector3(self.x-o.x, self.y-o.y, self.z-o.z)

    def __mul__(self, o):
        return Vector3(self.x*o, self.y*o, self.z*o)

    def __abs__(self):
        return math.sqrt(self.abssq())

    def abssq(self):
        return self.x*self.x + self.y*self.y + self.z*self.z

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def tup(self):
        return self.x, self.y, self.z

    def normalize(self):
        size = abs(self)
        if size < 1e-9:
            return
        self.x /= size
        self.y /= size
        self.z /= size

    def __neg__(self):
        return self * (-1)

    def copy(self):
        return Vector3(self.x, self.y, self.z)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        if key == 2:
            return self.z
        raise IndexError()
