

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd


lst=[1,2,3,4,5]

even,odd=count(lst)
print(even,odd)
print("Even : {} and Odd: {}".format(even,odd))



