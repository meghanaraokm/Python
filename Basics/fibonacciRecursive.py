from array import *

n=input("Enter the number of fibonacci series required : ")
a=array('i',[])

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else :
        result=fibonacci(n-1)+fibonacci(n-2)
        return result

for i in range(1,n+1):
    result=fibonacci(i)
    a.append(result)
    print(result)


print(a)

