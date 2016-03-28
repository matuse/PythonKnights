# Part 1
def is_triangle(a, b, c):
    if a + b > c:
        if b + c > a:
            if c + a > b:
                print 'yes'
            else:
                print 'no'
        else:
            print 'no'
    else:
        print 'no'

# Part 2
a = int(raw_input('Stick A size:\n'))
b = int(raw_input('Stick B size:\n'))
c = int(raw_input('Stick C size:\n'))

is_triangle(a, b, c)