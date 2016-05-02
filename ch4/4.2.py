from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()


def draw_square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

draw_square(bob)

wait_for_user()
