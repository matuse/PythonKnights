from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()


def draw_square(t, length):

    for i in range(4):
        fd(t, length)
        lt(t)


draw_square(bob, 35)

wait_for_user()
