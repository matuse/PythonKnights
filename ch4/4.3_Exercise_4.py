from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()


def draw_polygon(t, length, n):
    """
    Draws a simple Polygon given the following parameters:

    :param t: Turtle Object
    :param length: Length of the sides of the polygon
    :param n: The number of sides
    :return: None
    :rtype: None
    """

    for i in range(n):
        fd(t, length)
        lt(t, (360.0/n))


def draw_circle(t, r):
    """
    Draws a circle given the following arguments:

    :param t: Turtle Object
    :param r: Radius of the circle
    :return: None
    :rtype: None
    """
    t.delay = 0.01
    circumference = 2 * 3.14159 * r
    l = circumference / 25.0

    draw_polygon(t, l, 25)


draw_circle(bob, 30)

wait_for_user()
