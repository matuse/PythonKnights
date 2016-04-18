def printbackwards(string):
    index = 0
    while index < len(string):
        letter = string[-index]
        print letter
        index += 1

def printbackwards1(string):
    index = len(string) - 1
    while index >= 0:
        letter = string[index]
        print letter
        index -= 1

printbackwards("hello")
printbackwards1("hello")
