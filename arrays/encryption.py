import math

str = "feed the dog"
str = str.replace(' ','')
strlength = len(str)
sqrt = math.sqrt(strlength)
row = math.floor(sqrt)
column = math.ceil(sqrt)

# ROW x COL check
if row*column<strlength:
  row = math.ceil(sqrt)

def encryption(str):
  arr = []
  for i in range(row):
    colList = []
    for j in range(column):
      if (column*i)+j<len(str):
        colList.append(str[(column*i)+j])
    arr.append(colList)
  
  print(arr)
  newStr =''
  for i in range(column):
    for j in range(row):
      if i<len(arr[j]):
        newStr += arr[j][i]
    newStr+=' '

  print(newStr)

encryption(str)
