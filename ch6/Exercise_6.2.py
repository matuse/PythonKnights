from math import *


def hypotenuse0(a, b):
    return 0.0


def hypotenuse1(a, b):
    a_squared = a**2
    b_squared = b**2
    print a_squared
    print b_squared
    return 0.0


def hypotenuse2(a, b):
    a_squared = a**2
    b_squared = b**2
    print a_squared
    print b_squared
    c_squared = a_squared + b_squared
    print c_squared
    return 0.0


def hypotenuse3(a, b):
    a_squared = a**2
    b_squared = b**2
    print a_squared
    print b_squared
    c_squared = a_squared + b_squared
    print c_squared
    c = sqrt(c_squared)
    print c
    return 0.0


def hypotenuse(a, b):
    a_squared = a**2
    b_squared = b**2
    c_squared = a_squared + b_squared
    c = sqrt(c_squared)
    return c

print hypotenuse0(2, 4)
print hypotenuse1(2, 4)
print hypotenuse2(2, 4)
print hypotenuse3(2, 4)
print hypotenuse(2, 4)
