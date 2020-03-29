def numSum(n):
    if n==0:
        return 0
    else:
        total = n + numSum(n-1)
        return total


print(numSum(4))


def digitSum(n):
    if len(str(n))==1:
        return n
    else:
        sumof = n%10 + digitSum(n/10)
        #print(sumof)
        return sumof

print(digitSum(5426))


def fibonacci(n):
    #base case
    if n==1 or n==0:
        return n

    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
        
  

