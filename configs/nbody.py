from point import Point
import colors
from vector import Vector2
from math import *


# sonce: 27100000 mas lune
# venera: 66.3 mase lune
# zemlja: 81.3 mase lune
# G = 9.85381e-4 r^3 / mL*h^2
# r je desetina razdalje lune od zemlje
# mL je masa lune
# h je ura


# Newton's gravitational constant
G = 1

dim = [
    -5000,
    5000,
    -5000,
    5000
]


# sinus and cosinus of degrees
def sind(angle):
    return sin(radians(angle))


def cosd(angle):
    return cos(radians(angle))


def get_start_points():
    # orbital_vel = sqrt(G * masses[star] / R)
    M = 27100000
    velocity = 0.5
    R = 1000
    return [
        Point(Vector2(0, -R), colors.RED, velocity=Vector2(velocity, 0), mass=1000),
        Point(Vector2(cosd(30)*R, sind(30)*R), colors.BLUE, velocity=Vector2(-sind(30)*velocity, cosd(30)*velocity), mass=1000),
        Point(Vector2(-cosd(30)*R, sind(30)*R), colors.GREEN, velocity=Vector2(-cosd(60)*velocity, -sind(60)*velocity), mass=1000),
    ]


def do_physics(dt, points):
    # dt is measured in miliseconds

    for p in points:
        p.a = Vector2(0, 0)
        for o in points:
            if p is o:
                continue
            dist = abs(o.pos-p.pos)
            a = G * o.mass / dist**3
            p.a += (o.pos - p.pos) * a

        p.pos += p.velocity * dt
        p.velocity += p.a * dt


def debug(points):
    pass


def additional_draw(window, points, translate):
    pass
