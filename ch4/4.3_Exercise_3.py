from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()


def draw_polygon(t, length, n):

    for i in range(n):
        fd(t, length)
        lt(t, (360.0/n))

draw_polygon(bob, 40, 8)

wait_for_user()
