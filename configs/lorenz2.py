import pygame

from point import Point
import colors
from vector import Vector2
from math import *


sigma = 10
beta = 8/3
ro = 28

dim = [
    -70,
    70,
    -70,
    70
]

dim = [
    -35,
    35,
    -70,
    0
]


def translate_xy(p):
    p.pos.x = p.x
    p.pos.y = p.y


def translate_xz(p):
    p.pos.x = p.x
    p.pos.y = -p.z


def translate_yz(p):
    p.pos.x = p.y
    p.pos.y = p.z


def debug(points):
    # p = points[0]
    # dx = sigma * (p.y - p.x)
    # dy = p.x * (ro - p.z) - p.y
    # dz = p.x * p.y - beta * p.z
    # print(dx, dy, dz)
    pass


def get_start_points():
    return [
        Point(Vector2(), colors.BLUE, x=1, y=1, z=1),
        Point(Vector2(), colors.RED, x=1, y=1, z=1.0001)
    ]


def do_physics(dt, points):
    for p in points:
        dx = (sigma * (p.y - p.x)) * dt / 1000
        dy = (p.x * (ro - p.z) - p.y) * dt / 1000
        dz = (p.x * p.y - beta * p.z) * dt / 1000

        p.x += dx
        p.y += dy
        p.z += dz

        translate_xz(p)


def additional_draw(window, points, translate):
    pass
