mom=20
son=2
print(mom,son)
for i in range(1,79,1):
    mom+=1
    if int(str(mom)[::-1]) == (son+i):
        print(mom,son+i)

