def no_e(s):
    if s.count('e') > 0:
        return False
    return True

fin = open('words.txt')
line_count = 0
hits = 0
for line in fin:
    word = line.strip()
    line_count += 1
    if no_e(word):
        print word
        hits += 1

print str(hits) + ' Results or ',
print str((float(hits) / line_count) * 100) + '%'
