arr = [1,2,3,1,3]

def findDuplicate(arr):
  mydict = {}
  for i in range(len(arr)):
    if(arr[i] not in mydict):
      mydict[arr[i]] = 1
    else:
      mydict[arr[i]] = mydict[arr[i]] + 1
    #else saglanirsa duplicate vardir.
    #print(mydict)
    if(mydict[arr[i]] > 1):
      print("Duplicate olan sayi", arr[i])


findDuplicate(arr)