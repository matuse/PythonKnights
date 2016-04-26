def capitalize_nested(t):
    res = []
    for s in t:
        if isinstance(s,list):
            res.append(capitalize_nested(s))
        else:
            res.append(s.capitalize())
    return res


print capitalize_nested(['madhu','kiran',['mad',['max','madus']],"thamma"])