import pygame

from point import Point
import colors
from vector import Vector2
from math import *


a = 0.1
b = 0.1
c = 14


dim = [
    -100,
    100,
    -100,
    100
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
    ]


def do_physics(dt, points):
    for p in points:
        dx = (-p.y -p.z) * dt / 1000
        dy = (p.x + a*p.y) * dt / 1000
        dz = (b + p.z * (p.x - c)) * dt / 1000

        p.x += dx
        p.y += dy
        p.z += dz

        translate_xz(p)


def additional_draw(window, points, translate):
    pass
