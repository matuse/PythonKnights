s=''
ltr='e'
cntr=0
eCntr=0
noteCntr=0
fob = open('words.txt')

def has_no_e(s,ltr):
    if ltr in s:
        return True
    else:
       # print(s)
        return False




while True:
    s=(fob.readline()).strip()
    if s == '':
        break
    elif has_no_e(s,ltr):
        eCntr+=1
    else:
        noteCntr+=1
    cntr+=1

print(cntr,eCntr,noteCntr,float(noteCntr*100.0/cntr))
