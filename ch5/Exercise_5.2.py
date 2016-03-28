def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n-1)