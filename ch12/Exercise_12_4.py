fin = open('words.txt')

#li = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'bob', 'alice', 'licea']
d = {}
'''
for line in li:
    key = (list(line))
    key.sort()
    key = ''.join(key)
    print key
    w = d.get(key, [])
    print w
    d[key] = w + [line]

print d
'''

for line in fin:
    key = (list(line))
    key.sort()
    key = ''.join(key)
    word = line.strip().lower()
    w = d.get(key, [])
    d[key] = w + [word]

for key, val in d.items():
    print key, val