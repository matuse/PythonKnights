def uses_only(wrd,s):
    for let in wrd:
        if let not in s:
            return False
    return True

print(uses_only("hapapyyh",'happy'))


