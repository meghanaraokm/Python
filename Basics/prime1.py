import math

num=input("Enter the number")
isPrime=1
for i in range(2,int(math.sqrt(num))):
    if num%i==0:
        isPrime=0
        break
if isPrime==1:
    print("Prime number")
else:
    print("Not Prime")
