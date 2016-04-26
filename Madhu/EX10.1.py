def nested_sum(nls):
    nsm=0
    for lst in nls:
        if isinstance(lst,list):
            nsm+=nested_sum(lst)
        else:
            nsm+=lst

    return nsm




myList = [1,2,3,4,[5,6],[7,[8,9,10]]]

print(nested_sum(myList))