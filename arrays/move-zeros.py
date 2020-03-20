arr = [1,0,1,3,0,12]

def moveZeros(arr):
    myArr = []
    for i in range(len(arr)):
        if(arr[i] == 0):
            myArr.append(arr[i])
            arr.remove(arr[i])
    finalArr = []
    finalArr.append(arr)
    finalArr.append(myArr)

    print(finalArr)


moveZeros(arr)
