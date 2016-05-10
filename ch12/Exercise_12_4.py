fin = open('words.txt')
d = {}

for line in fin:
    key = (list(line))
    key.sort()
    key = ''.join(key)
    word = line.strip().lower()
    w = d.get(key, [])
    d[key] = w + [word]

for key, val in d.items():
    if len(val) >= 2:
        print key, val
