from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()


def draw_arc(t, r, angle):
    """
    Draws an arc given the following:
    :param t: Turtle Object
    :param r: Radius of the circle
    :param angle: Number of degress to draw for the arc
    :return: None
    :rtype: None
    """
    t.delay = 0.001
    circumference = 2 * pi * r
    l = circumference / 360

    for i in range(angle):
        fd(t, l)
        lt(t, 1)

draw_arc(bob, 30, 180)


wait_for_user()
