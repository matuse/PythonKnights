def avoids(wrd,s):
    for let in s:
        if let in wrd:
            return False

    return True

def readFile(fob,line):
    cntr=0
    while True:
        wrd=(fob.readline()).strip()
        if wrd == '':
            break
        else:
            if avoids(wrd,line):
                print(wrd)
                cntr+=1
    return cntr


fob = open('words.txt')
line = input('> ')



print(readFile(fob,line))