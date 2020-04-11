class TracePoint:

    def __init__(self, point):
        self.x, self.y = point.pos.tup()
        self.point = point

    @property
    def color(self):
        c = self.point.color
        return c[0]*0.5, c[1]*0.5, c[2]*0.5
