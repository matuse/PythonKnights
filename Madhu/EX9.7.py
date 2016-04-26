def tCDL(wrd):
    lt=len(wrd)
    i=1
    if lt>=6:
        while(i<lt):
            if wrd[i-1] == wrd[i] and i+4<lt:
                if(wrd[i+1]==wrd[i+2] and wrd[i+3] == wrd[i+4]):
                    #print(wrd)
                    return True
            i+=1
        return False





def readFile(fob):
    cntr=0
    while True:
        wrd=(fob.readline()).strip()
        if wrd == '':
            break
        else:
            if tCDL(wrd):
                print(wrd)
                cntr+=1
    return cntr


fob = open('words.txt')

#print(abcderian('adhu'))
print(readFile(fob))
