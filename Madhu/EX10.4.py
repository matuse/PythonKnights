def chop(lst):
    l = len(lst)
    del lst[l-1]
    del lst[0]
    print lst
t = [1,2,3,4,5,7,8,9,6]
print chop(t)