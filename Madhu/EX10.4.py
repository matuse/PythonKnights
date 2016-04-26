def chop(lst):
    newLst = []
    l = len(lst)
    del lst[l-1]
    del lst[0]
    newLst.append(lst)
    return newLst
t = [1,2,3,4,5,7,8,9,6]
print chop(t)