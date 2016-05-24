import math


class Point(object):
    """ contains an x and y value for a point on a cartesian plane

    """
    x = int()
    y = int()

a = Point()
b = Point()

b.x = 43
b.y = -33


def distance_between_points(p1, p2):
    """
    Takes two point objects and determines the distance between the two
    :param p1: First Point
    :param p2: Second Point
    :return: Distance between first and second point
    """
    x = abs(p1.x - p2.x)
    y = abs(p1.y - p2.y)
    dist = math.sqrt(x**2 + y**2)

    return dist


def print_point(p):
    print '(%f, %f)' % (p.x, p.y)


print a
print b
print_point(a)
print_point(b)

print distance_between_points(a, b)
