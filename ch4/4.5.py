from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()


def draw_polygon(t, length, n):

    for i in range(n):
        fd(t, length)
        lt(t, (360.0/n))

def draw_circle(t, r):
    t.delay = 0.01
    circumfrance = 2 * 3.14159 * r
    l = circumfrance / 25.0

    draw_polygon(t, l, 25)


draw_circle(bob, 30)


wait_for_user()
