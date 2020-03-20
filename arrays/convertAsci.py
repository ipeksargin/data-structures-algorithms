#Asci numaralarına gore harfleri buyukten kucuge siralar.
def sort_str(s):
    s = list(s)
    print(s)
    arr = []
    secondArr = []

    for i in range(len(s)):
        x = ord(s[i])
        arr.append(x)
        arr.sort()
    #print(arr)

    for k in range(len(arr)):
        char = chr(arr[k])
        secondArr.append(char)
    print(secondArr)

sort_str("hello")