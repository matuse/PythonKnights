import copy

class Point(object):
    """
    Represents a point
    """
    x = int()
    y = int()


class Rectangle(object):
    """
    Represents a rectangle
    """

    length = int()
    width = int()
    corner = Point()

    def area(self):
        return self.length * self.width


def print_point(p):
    """
    :param p: Point to print
    :return:
    """
    print '(%f, %f)' % (p.x, p.y)


def move_rectangle(r, dx, dy):
    r.corner.x += dx
    r.corner.y += dy


def move_and_copy(r, dx, dy):
    n = copy.deepcopy(r)
    n.corner.x += dx
    n.corner.y += dy
    return n

box = Rectangle()
box.length = 10
box.width = 9

print box.area()
print_point(box.corner)
move_rectangle(box, 12, 13)
print_point(box.corner)
new_box = move_and_copy(box, 12, 13)
print_point(new_box.corner)
