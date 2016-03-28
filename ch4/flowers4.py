from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()


def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    t.delay = 0.001
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

petals = 20

for i in range(petals):
    petal(bob, 180, 30)
    rt(bob, 360.0/petals)


wait_for_user()
