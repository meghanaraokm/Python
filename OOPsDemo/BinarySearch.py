
pos=0

def search(li,key):
    l=0
    u=len(li)-1
    while l<=u:
        mid=(l+u)//2
        if li[mid]==key:
            globals()['pos']=mid
            return True
        else:
            if li[mid]<key:
                l=mid+1
            else:
                u=mid-1
    return False

li=[3, 5, 6, 8, 9]

key=int(input("Enter the number to be searched : "))

if search(li,key):
    print("The number is found at the index : {}".format(pos+1))
else:
    print("Error: The provided number is not in the list")