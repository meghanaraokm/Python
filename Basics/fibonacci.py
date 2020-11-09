from array import *
n=input("Enter the number of values required :")

a=0
b=1
arr=array('i',[])

if n == 1:
    print(a)
    arr.append(a)
else:
    print(a)
    print(b)
    arr.append(a)
    arr.append(b)

for i in range(2,n):
    result=a+b
    print(result)
    arr.append(result)
    a=b
    b=result

print(arr)