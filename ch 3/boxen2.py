width = 2
height = 2


def draw_div(w):
    return'+----' * w + '+\n'


def draw_mid(w):
    return'|    ' * w + '|\n'


def draw_section(w):
    return draw_div(w) + draw_mid(w)*4


print (draw_section(width) * height + draw_div(width))
