s=''
fob = open('words.txt')
while True:
    s=(fob.readline()).strip()
    if len(s)>=20:
        print(s)
    if s == '':
        break
