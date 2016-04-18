def find(word, letter, index=0):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


def count(word, ltr):
    occurs = 0
    index = 0
    while index < len(word):
        index = find(word, ltr, index)
        if index > 0:
            occurs += 1
        if index == -1:
            return occurs
        index += 1
    return occurs

print 'there are',
print count('banana', 'a'),
print "letter a's in the word banana"

print 'there are',
print count('mississippi', 's'),
print "letter s's in the word Mississippi"
