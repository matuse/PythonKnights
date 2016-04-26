def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d

print histogram('balls')
print histogram('Mississippi')
print histogram('My mother your mother hanging up the clothes. My mother punched your mother in the nose. What color was the blood?')
