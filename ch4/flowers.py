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

for i in range(7):
    arc(bob, 50, 60)
    rt(bob, 240)
    arc(bob, 50, 60)
    rt(bob, 240)
    rt(bob, (360.0/7))


wait_for_user()
