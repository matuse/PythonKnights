def check_fermat(a, b, c, n):
    if a%1 == 0 and b%1 == 0 and c%1 == 0:
        if a >= 0 and b >= 0 and c >= 0:
            if n > 2:
                # Check Fermat
                if a ** n + b ** n == c ** n:
                    print "Holy smokes, Fermat was wrong!"
                else:
                    print "No, that doesn't work."
            else:
                print "n has to be greater than 2"
        else:
            print "a, b, and c have to be positive"
    else:
        print "a, b, and c have to integers"

print 'Please input a, b, c, and n so we can check Fermat.'

a = int(raw_input('a:\n'))
b = int(raw_input('b:\n'))
c = int(raw_input('c:\n'))
n = int(raw_input('n:\n'))

print 'Checking ' + str(a) + '^' + str(n) + " + " + str(b) + '^' + str(n) + " = "  + str(c) + '^' + str(n)

check_fermat(a, b, c, n)
