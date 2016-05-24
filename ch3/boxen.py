
def draw_top():
    print('+----+----+')

def draw_mid():
    print('|    |    |')

def draw_box():
    draw_top()
    draw_mid()
    draw_mid()
    draw_mid()
    draw_mid()
    draw_top()
    draw_mid()
    draw_mid()
    draw_mid()
    draw_mid()
    draw_top()

draw_box()

def big_box_top():
    print('+----+----+----+----+')

def big_box_mid():
    print('|    |    |    |    |')

def draw_big_section():
    big_box_top()
    big_box_mid()
    big_box_mid()
    big_box_mid()
    big_box_mid()

def draw_big_box():
    draw_big_section()
    draw_big_section()
    draw_big_section()
    draw_big_section()
    big_box_top()

draw_big_box()