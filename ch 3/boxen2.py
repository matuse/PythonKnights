width = 2
height = 2


def draw_div(width):
    return'+----' * width + '+\n'


def draw_mid(width):
    return'|    ' * width + '|\n'


def draw_section(width):
    return draw_div(width) + draw_mid(width)*4


print (draw_section(width) * height + draw_div(width))
