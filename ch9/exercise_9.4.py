def uses_only(s, chars):
    flag = True
    for ltr in chars:
        flag = flag and s.count(ltr) > 0
    return flag


nono = ''
while nono != '!':
    fin = open('words.txt')
    line_count = 0
    hits = 0
    nono = raw_input('Please enter characters you wish to avoid:\nOr enter ! to quit.\n')
    if nono == '!':
        quit()
    for line in fin:
        word = line.strip()
        line_count += 1
        if avoids(word, nono):
            hits += 1

    print '\n'

    print str(hits) + ' Results or ',
    print str((float(hits) / line_count) * 100) + '%'

    fin.close()
