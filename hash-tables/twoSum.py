arr = [2,7,11,15]

def twoSum(arr, number):
    table = {}
    for i in range(len(arr)):
        target = number - arr[i]
        if(arr[i] not in table):
            table[arr[i]] = target
        #print(table)
        #print(table[arr[i]])
        if(table[arr[i]] in arr):
            print(arr[i])


twoSum(arr,18)

