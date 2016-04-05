# is_power checks to see if power is an even result of root raised to a power lower than the recursion-limit

def is_power(power,root):
    """ returns true if power is an even power of root, as 9 is of 3, or false otherwise"""

    print("power=" + str(power) + ", root=" + str(root))

    if power == root:
        return("YES")

    if ( power % root ) <> 0:
        return("NO: not divisible")

    if power==1 or root==1:
        return("NO: one is only a power of one and only a root of one")

    print("keep trying...")
    return( is_power( power / root,root) )


print(is_power(81,9))
print(is_power(81,3))
print(is_power(40,3))
print(is_power(1000,10))
print(is_power(81000,3))
print(is_power(23,1))
print(is_power(1,1))
print(is_power(4096,2))