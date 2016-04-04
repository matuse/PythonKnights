from polygon import *


def draw_a(t, size):
    lt(t, 60)
    fd(t, size)
    rt(t, 120)
    fd(t, size)
    lt(t, 60)


def draw_b(t, size):
    lt(t)
    fd(t, size)
    bk(t, size)
    rt(t)
    arc(t, (size / 4), 180)
    rt(t, 180)
    arc(t, (size / 4), 180)
    lt(t)
    fd(t, size)
    lt(t)
    pu(t)
    fd(t, size/2)
    pd(t)


def draw_c(t, size):
    pu(t)
    fd(t, size/2)
    lt(t)
    fd(t, size)
    rt(t)
    rt(t, 180)
    pd(t)
    arc(t, size/2, 180)


def skip(t, size):
    pu(t)
    fd(t, 2 * size)
    pd(t)
