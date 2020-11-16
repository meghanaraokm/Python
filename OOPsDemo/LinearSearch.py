
#n=0
#while n<=len(arr):
#   if arr[n]==key:
#        print("The number is found at the index : {}".format(n))
#        break
#    n+=1

def search(li,key):
    for i in range(len(li)):
        globals()['pos']=i
        if li[i]==key:
            return True
    else:
        return False


li=[3, 5, 6, 8, 9]
key=int(input("Enter the number to be searched : "))
pos=0

if search(li,key):
    print("The number is found at the index : {}".format(pos+1))
else:
    print("Error: The provided number is not in the list")


# OR
print(li.index(key))