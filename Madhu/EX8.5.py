def rotateWord(s,i):
    csrString = ''
    lcsLolt=97
    lcsUplt=122
    ucsUplt=90
    ucsLolt=65
    newOrd=0
    for ltr in s:
        if ord(ltr)>=lcsLolt and ord(ltr)<=lcsUplt:
            newOrd=ord(ltr)+i
            if newOrd>lcsUplt:
                newOrd = (newOrd-lcsUplt)+lcsLolt-1
            elif newOrd<lcsLolt:
                newOrd = lcsUplt-(lcsLolt-newOrd)+1
        elif ord(ltr)>=ucsLolt and ord(ltr)<=ucsUplt:
            newOrd=ord(ltr)+i
            if newOrd>ucsUplt:
                newOrd = (newOrd-ucsUplt)+ucsLolt-1
            elif newOrd<ucsLolt:
                newOrd = ucsUplt-(ucsLolt-newOrd)+1
        else:
            newOrd=ord(ltr)

        csrString= csrString+chr(newOrd)
    print(csrString)


rotateWord('Madhu.Kiran.Thamma',39)


print('order of a z')
print(ord('a'),ord('z'))
print('order of A Z')
print(ord('A'),ord('Z'))