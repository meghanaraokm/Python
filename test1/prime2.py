
import math
num=input("Enter the number")

for i in range(2,int(math.sqrt(num))+1):
    if num%i==0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")

