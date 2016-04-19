def rotate_word(word, n):
    result = ''

    for c in word:
        temp = ord(c)
        temp += n
        result += chr(temp)

    return result

print rotate_word('cheer', 7)
print rotate_word('melon', -10)
