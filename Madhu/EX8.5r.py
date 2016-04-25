def rotateWord(s,i):
    csrString = ''
    lcsLolt=97
    #lcsUplt=122
    #ucsUplt=90
    ucsLolt=65
    newOrd=0
    for ltr in s:
        if ltr.islower():
            newOrd=ord(ltr)+i
            newOrd = (newOrd-lcsLolt)%26+lcsLolt

        elif ltr.isupper():
            newOrd=ord(ltr)+i
            newOrd = (newOrd-ucsLolt)%26+ucsLolt

        else:
            newOrd=ord(ltr)

        csrString= csrString+chr(newOrd)
    print(csrString)


rotateWord('Madhu.Kiran.Thamma',53)


print('order of a z')
print(ord('a'),ord('z'))
print('order of A Z')
print(ord('A'),ord('Z'))