from array import *

arr= array('i',[])
n=int(input("Enter the length of the array : "))

for i in range(n):
    x=input("Enter the value "+str(i+1)+" : ")
    arr.append(x)

print(arr)

k=0
val=int(input("Enter the value to be searched "))
for e in arr:
    if e==val:
        print("The number is present in "+ str(k))
        break
    k+=1
else:
    print("The number is not present")

#Or by using buit-in function

print(arr.index(val))


