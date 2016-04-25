def newLetter(flNum,lNum,i):
    newNum=lNum+i
    newNum = (newNum-flNum)%26+flNum
    return newNum



def rotateWord(s,i):
    csrString = ''
    lcsLolt=97
    ucsLolt=65
    newOrd=0
    for ltr in s:
        if ltr.islower():
            newOrd = newLetter(lcsLolt,ord(ltr),i)

        elif ltr.isupper():
            newOrd = newLetter(ucsLolt,ord(ltr),i)

        else:
            newOrd=ord(ltr)

        csrString= csrString+chr(newOrd)
    print(csrString)


rotateWord('Madhu.Kiran.Thamma',54)


print('order of a z')
print(ord('a'),ord('z'))
print('order of A Z')
print(ord('A'),ord('Z'))