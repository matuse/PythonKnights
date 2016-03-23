def right_justify(string):
    string_len = len(string)
    indent = 70 - string_len
    print " " * indent + string


right_justify('I love bananas')
right_justify('said the monkey')
right_justify('yummmmm')