def avoids(s, bad_cars):
    flag = False
    for bcar in bad_cars:
        flag = flag or s.count(bcar) > 0
    return not flag


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
            #print word,
            hits += 1

    print '\n'

    print str(hits) + ' Results or ',
    print str((float(hits) / line_count) * 100) + '%'

    fin.close()
