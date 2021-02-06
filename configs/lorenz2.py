import pygame

from point import Point
import colors
from vector import Vector2
from math import *


# Parameters for Lorenz equations
sigma = 10
beta = 8/3
ro = 28


dim_xy = [
    -50,
    50,
    -50,
    50
]

dim_yz = [
    -35,
    35,
    0,
    70
]

dim_xz = [
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


# translate: which plane should appear on screen
translate = translate_xz

# dim: coordinates of points to appear on screen.
# use of dim variables above is recommended
dim = dim_xz


def debug(points):
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

        translate(p)


def additional_draw(window, points, translate):
    pass
