import string
fin = open('eng_opp.txt')
d = {}
start = False

for line in fin:
    if line.split()[0] == "***START":
        start = True

    if start:
        for word in line.split():
            newword = word.strip(string.punctuation).lower()
            key = newword
            w = d.get(key, 0)
            d[key] = w + 1

for key, val in d.items():
    print key, val