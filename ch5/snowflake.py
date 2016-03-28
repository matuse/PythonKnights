from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()


def koch(t, x):
    if x < 3:
        fd(t, x)
    else:
        koch(t, x / 3)
        lt(t, 60)
        koch(t, x / 3)
        rt(t, 120)
        koch(t, x / 3)
        lt(t, 60)
        koch(t, x / 3)

def snowflake():
    for i in range(3):
        koch(bob, 150)
        rt(bob, 120)


bob.delay = 0.001

snowflake()

die(bob)

wait_for_user()