def cuSum(lst):
    newLst = []
    newSum=0
    for l in lst:
        newSum+=l
        newLst.append(newSum)
    return newLst



print cuSum([1,2,3,4,5])