
# Time Complexity: O(n)
# Space Complexity: O(1)

Arr = [-2, 1, 2, 4, 7, 11]
target = 13
def twoSum(Arr, target):
  i = 0
  j = len(Arr) - 1
  while i < j:
    if Arr[i] + Arr[j] == target:
      print(Arr[i], Arr[j])
      return True
    elif Arr[i] + Arr[j] < target:
      i += 1
    else:
      j -= 1
  return False

print(twoSum(Arr,target))
