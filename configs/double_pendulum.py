import pygame

from point import Point
import colors
from vector import Vector2
from math import *


# length of each arm
R = 800

# gravitational acceleration
g = 0.5


dim = [-2000, 2000, -2000, 2000]


def debug(points):
    pass


def get_start_points():
    return [
        Point(Vector2(), colors.GRAY, trace=False,
              radius=3, phi=0, omega=0, mass=1, export=False),
        Point(Vector2(0, R), colors.BLUE, trace=False,
              radius=3, phi=pi/3, omega=0, mass=1),
        Point(Vector2(0, R), colors.BLUE, trace=True,
              radius=3, phi=0, omega=0, mass=1),
        Point(Vector2(0, R), colors.RED, trace=False,
              radius=3, phi=pi/3+0.01, omega=0, mass=1),
        Point(Vector2(0, R), colors.RED, trace=True,
              radius=3, phi=0, omega=0, mass=1),
    ]


def do_physics(dt, points):
    # physics for first point of first pendulum
    n1 = -g*(2*points[1].mass+points[2].mass) * sin(points[1].phi)
    n2 = - points[2].mass * g * sin(points[1].phi - 2*points[2].phi)
    n3 = - 2 * sin(points[1].phi - points[2].phi)*points[2].mass * (points[2].omega**2 * R + points[1].omega**2 * R * cos(points[1].phi - points[2].phi))
    n4 = R * (2*points[1].mass + points[2].mass - points[2].mass * cos(2*points[1].phi - 2*points[2].phi))
    dw1 = (n1+n2+n3) / n4

    # physics for second point of first pendulum
    n5 = points[1].omega**2 * R * (points[1].mass + points[2].mass)
    n6 = g * (points[1].mass + points[2].mass) * cos(points[1].phi)
    n7 = points[2].omega ** 2 * R * points[2].mass * cos(points[1].phi - points[2].phi)
    dw2 = 2*sin(points[1].phi - points[2].phi)*(n5 + n6 + n7) / n4

    # apply both accelerations
    points[1].phi += points[1].omega
    points[1].omega += dw1
    points[2].phi += points[2].omega
    points[2].omega += dw2

    # calculate x,y positions of points on the first pendulum
    points[1].pos = Vector2(R * sin(points[1].phi), R * cos(points[1].phi))
    points[2].pos = Vector2(R * sin(points[2].phi), R * cos(points[2].phi)) + points[1].pos

    # physics for first point of second pendulum
    n1 = -g*(2*points[3].mass+points[4].mass) * sin(points[3].phi)
    n2 = - points[4].mass * g * sin(points[3].phi - 2*points[4].phi)
    n3 = - 2 * sin(points[3].phi - points[4].phi)*points[4].mass * (points[4].omega**2 * R + points[3].omega**2 * R * cos(points[3].phi - points[4].phi))
    n4 = R * (2*points[3].mass + points[4].mass - points[4].mass * cos(2*points[3].phi - 2*points[4].phi))
    dw1 = (n1+n2+n3) / n4

    # physics for second points of second pendulum
    n5 = points[3].omega**2 * R * (points[3].mass + points[4].mass)
    n6 = g * (points[3].mass + points[4].mass) * cos(points[3].phi)
    n7 = points[4].omega ** 2 * R * points[4].mass * cos(points[3].phi - points[4].phi)
    dw2 = 2*sin(points[3].phi - points[4].phi)*(n5 + n6 + n7) / n4

    # apply both acceletations
    points[3].phi += points[3].omega
    points[3].omega += dw1
    points[4].phi += points[4].omega
    points[4].omega += dw2

    # calculate x,y poitions of points on the second pendulum
    points[3].pos = Vector2(R * sin(points[3].phi), R * cos(points[3].phi))
    points[4].pos = Vector2(R * sin(points[4].phi), R * cos(points[4].phi)) + points[3].pos


def additional_draw(window, points, translate):
    # draw lines between pendulum points
    pygame.draw.line(
        window,
        colors.GRAY,
        translate(*points[0].pos.tup()),
        translate(*points[1].pos.tup())
    )
    pygame.draw.line(
        window,
        colors.GRAY,
        translate(*points[1].pos.tup()),
        translate(*points[2].pos.tup())
    )
    pygame.draw.line(
        window,
        colors.GRAY,
        translate(*points[0].pos.tup()),
        translate(*points[3].pos.tup())
    )
    pygame.draw.line(
        window,
        colors.GRAY,
        translate(*points[3].pos.tup()),
        translate(*points[4].pos.tup())
    )
