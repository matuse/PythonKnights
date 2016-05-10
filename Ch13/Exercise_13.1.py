import string
fin = open('eng_opp.txt')
d = {}

for line in fin:
    for word in line.split():
        newword = word.strip(string.punctuation).strip(string.whitespace).lower()
        #print newword
        key = newword
        w = d.get(key, 0)
        d[key] = w + 1

for key, val in d.items():
    print key, val