def count(word, ltr):
    occurs = 0
    for letter in word:
        if letter == ltr:
            occurs += 1
    return occurs

print count('banana', 'a')