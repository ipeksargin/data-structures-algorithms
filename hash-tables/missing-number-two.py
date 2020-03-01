#Time complexity is equal to O(n) (sorting function is ignored)

arrayOne = [7,2,5,4,6,3,5,3]
arrayTwo = [7,2,5,3,5,3]

def missingNumber(arrayOne, arrayTwo):
    table = {} 
  #table is a dictionary and is created to store values of arrayOne.
    for i in range(len(arrayOne)):
   # if value already in the dictionary.
        if(arrayOne[i] in table):
            table[arrayOne[i]] = table[arrayOne[i]] + 1 # increase its value by one.
        else:
            table[arrayOne[i]] = 1 # else add it to dict and have value of one.
    
   #for each value in arrayTwo decrease dict value count by 1 
    for j in range(len(arrayTwo)):
        if(arrayTwo[j] in table):
            table[arrayTwo[j]] = table[arrayTwo[j]] - 1
    print(table)

  
  # Check dict by keys to get missing numbers
    keys = table.keys()
    final = []
    for x in keys:
      if(table[x] > 0):
        final.append(x)
        #sort missing values
        final.sort()

  # Therefore, the ones whose value is more than one are missing values.
    print("Missing elements are",final)

missingNumber(arrayOne, arrayTwo)