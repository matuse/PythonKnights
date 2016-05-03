def sumall(*args):
    s = 0
    i = 0
    while i <= len(args)-1:
        s += args[i]
        i += 1

    return s


def sumall2(*args):
    s = 0
    for i in args:
        s += i

    return s

print sumall(1,2,3,4,5,6,7)
print sumall(123,45676)
print sumall(9,8,7,6,5,5,6,7,8,9,9,98,6,5,4,3,32,2,222,4,5,6,67,673674,0,2,34562345,2,342,52,65,2,345,42,6,34576)
print sumall()

print sumall2(1,2,3,4,5,6,7)
print sumall2(123,45676)
print sumall2(9,8,7,6,5,5,6,7,8,9,9,98,6,5,4,3,32,2,222,4,5,6,67,673674,0,2,34562345,2,342,52,65,2,345,42,6,34576)
print sumall2()