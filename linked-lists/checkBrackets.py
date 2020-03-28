def checkBrackets(mystr):
    opening = ['(', '{', '[']
    matches = [('(',')'), ('[',']'),('{','}')]
    stack = []
    for i in mystr:
        if i in opening:
            stack.append(i)
            #print(stack)
        else:
            top = stack.pop() #take the last item which enters last in stack 
            if (top,i) not in matches:
                print("Proper match not found for",top)
            else:
                print("Proper match found for", top, i)
 

            
checkBrackets("{{()})")

                


