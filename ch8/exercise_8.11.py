def any_lowercase1(s):
    # This will only check the first character as it returns in either case after the first iteration
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    # This literally only checks the character "c" and also returns a string "True" or "False" instead of the bool value
    for c in s:
        if 'c'.islower():
            return 'True'
    else:
        return 'False'


def any_lowercase3(s):
    # This only really checks the last character as it resets the value of flag every time through
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    # This one does exactly what we want.
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    # This will only say there are lower case if they are _all_ lower case
    for c in s:
        if not c.islower():
            return False
    return True

print any_lowercase5('matt')