#reverse a string using recursion

def revStr(mystr):
    #base case
    if len(mystr) <= 1:
        return mystr

    #recursion
    total=revStr(mystr[1:]) + mystr[0] 
    print(total)
    return total


revStr("abcde")