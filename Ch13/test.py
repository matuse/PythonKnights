import string

line = "I! want. to, eat#       some@ and$ then%                       some^ please?"

for word in line.split():
    print word.strip(string.punctuation).lower()