import random

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
    t.sort(reverse=True)
    #print t
    res = []
    for length, blah, word in t:
        res.append(word)
    return res

def sort_by_length_mj(words):
    t = []
    for word in words:
        t.append((len(word) + random.random(), word))
    t.sort(reverse=True)
    #print t
    res = []
    for length, word in t:
        res.append(word)
    return res

mjlist = ['hat', 'fox', 'box', 'cat', 'jumbo', 'Matt', 'If I were a rich man', 'enie', 'menie', 'miney', 'mo']

print sort_by_length(mjlist)
print sort_by_length_mj(mjlist)

print sort_by_length(mjlist)
print sort_by_length_mj(mjlist)

print sort_by_length(mjlist)
print sort_by_length_mj(mjlist)