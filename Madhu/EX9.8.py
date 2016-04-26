cntr=0
for i in range(100000,999996,1):

    s=str(i)
    subStr=s[1:]
    subStr2=s[2:]
    subStr3=s[1:5]
    if cntr==0:
        if subStr2[:] == subStr2[::-1]:
            #print(subStr2,subStr2[::-1])
            cntr+=1
        else:
            cntr=0
    elif cntr==1:
        if subStr[:]==subStr[::-1]:
            cntr+=1
        else:
            cntr=0
    elif cntr==2:

        if subStr3[:]==subStr3[::-1]:
            #print(i-2,i-1,i)
            cntr+=1
        else:
            cntr=0
    elif cntr==3:
        if s[:]==s[::-1]:
            print(i-3,i-2,i-1,i)
        else:
            cntr=0


