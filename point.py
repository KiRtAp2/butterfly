import math

from vector import Vector2
from trace import TracePoint


class Point:

    def __init__(self, pos, color, radius=2, trace=True, export=True, **kwargs):
        self.pos = pos
        self.color = color
        self.radius = radius
        self.do_trace = trace
        self.export = export
        self.args = kwargs
        self.last_trace = None

    def distsq(self, o):
        return (o.pos - self.pos).abssq()

    def dist(self, o):
        return math.sqrt(self.distsq(o))

    def trace(self):
        return TracePoint(self)

    def __getattr__(self, name):
        return self.args[name]

    def compress(self):
        l = [self.pos.x, self.pos.y]
        for k in self.args.keys():
            try:
                l.append(self.__getattribute__(k))
            except AttributeError:
                l.append(self.__getattr__(k))
        return l

    def description(self):
        l = ["X", "Y"]
        for k in self.args.keys():
            l.append(k)
        return l
