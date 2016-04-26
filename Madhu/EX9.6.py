def abcderian(wrd):
    lt=len(wrd)
    i=1
    if lt==1:
        return True
    else:
        while(i<lt):
            if wrd[i-1] > wrd[i]:
                return False
            i+=1
        return True





def readFile(fob):
    cntr=0
    while True:
        wrd=(fob.readline()).strip()
        if wrd == '':
            break
        else:
            if abcderian(wrd):
                print(wrd)
                cntr+=1
    return cntr


fob = open('words.txt')

print(abcderian('adhu'))
print(readFile(fob))
