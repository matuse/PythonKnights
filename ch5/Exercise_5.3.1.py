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


check_fermat(1,1,2,3)
