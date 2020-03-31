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

#count specific letters in string
def recursiveCountStr(mystr):
    letters = "aeuio"
    if len(mystr)==0:
        return 0

    newstr = mystr[0].lower()
    if newstr[0] not in letters:
        return recursiveCountStr(mystr[1:])
    else:
        return 1 + recursiveCountStr(mystr[1:])


print(recursiveCountStr("Welcometoeducative"))

