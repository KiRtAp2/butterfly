import math


class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Vector2(self.x+o.x, self.y+o.y)

    def __sub__(self, o):
        return Vector2(self.x-o.x, self.y-o.y)

    def __mul__(self, o):
        return Vector2(self.x*o, self.y*o)

    def __abs__(self):
        return math.sqrt(self.abssq())

    def abssq(self):
        return self.x*self.x + self.y*self.y

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def tup(self):
        return self.x, self.y

    def normalize(self):
        size = abs(self)
        if size < 1e-9:
            return
        self.x /= size
        self.y /= size

    def __neg__(self):
        return self * (-1)

    def copy(self):
        return Vector2(self.x, self.y)


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
