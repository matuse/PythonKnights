def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]

w = 'raceicar'

def is_palindrome(word, recurse=0):
    print len(word)
    if len(word) == 0 and recurse > 0:
        return True
    if first(word) == last(word):
        print 'recursing on ' + word
        return is_palindrome(middle(word), recurse + 1)
    else:
        return False

if w == '':
    print "You must enter a word"
    exit()

wrd = str.lower(w)

print 'Check to see if ' + w + ' is a palindrome:'
print is_palindrome(wrd)
