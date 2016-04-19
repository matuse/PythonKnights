def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) -1

    while j >= 0:  # need the >= here instead of just the > so you catch the 0 index on j
        print i, j
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

    return True

print is_reverse('stop', 'pots')