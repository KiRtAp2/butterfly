import pygame

from point import Point
import colors
from vector import Vector2
from math import *


G = 0.005
R = 1000
Mz = 1e6

dim = [
    -5000,
    5000,
    -5000,
    5000
]


def debug(points):
    pass


def get_start_points():
    vel = sqrt(G * Mz / (4*R))
    return [
        # zvezdi
        Point(Vector2(R, 0), colors.YELLOW, radius=10, trace=False, velocity=Vector2(0, -vel), mass=Mz),
        Point(Vector2(-R, 0), colors.YELLOW, radius=10, trace=False, velocity=Vector2(0, vel), mass=Mz),

        # planeti
        Point(Vector2(2*R, 0), colors.BLUE, velocity=Vector2(0, 1)),
        Point(Vector2(2*R, 0), colors.RED, velocity=Vector2(0, 1.01))
    ]


def do_physics(dt, points):
    for p in points:
        p.a = Vector2(0, 0)
        for o in points[:2]:
            if p is o: continue
            a = G * o.mass / (abs(o.pos-p.pos)**3)
            p.a += (o.pos - p.pos) * a

        p.pos += p.velocity * dt
        p.velocity += p.a * dt


def additional_draw(window, points, translate):
    pass
