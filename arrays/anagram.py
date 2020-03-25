#this function check if two words have the same letters. 

def anagram(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    #print (str1, str2)
    if len(str1) != len(str2):
        print("They dont have the same length. They cant be an anagram.")
    else:    
        mylist = {}
        for letter in str1:
            if letter in mylist:
                mylist[letter] = mylist[letter] + 1
            else:
                mylist[letter] = 1

        for letter in str2:
            if letter in mylist:
                mylist[letter] = mylist[letter] - 1
        
        for i in mylist:
            if mylist[i] != 0:
                x = 1
            else:
                x = 0
    
        if x == 0:
            print("anagram")

        print(mylist)

anagram("public relationsa","crap built on lies")