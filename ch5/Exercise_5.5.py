from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length * n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2 * angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length * n)

bob.delay = 0.001

draw(bob, 3, 10)

die(bob)

wait_for_user()
