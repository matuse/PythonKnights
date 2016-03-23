def do_twice(f):
    f()
    f()


def print_spam():
    print 'spam'


do_twice(print_spam)


def do_twice_w_arg(f, arg):
    f(arg)
    f(arg)


def print_twice(string):
    print string
    print string


do_twice_w_arg(print_twice, 'spam')


def do_four(f, arg):
    do_twice_w_arg(f, arg)
    do_twice_w_arg(f, arg)
