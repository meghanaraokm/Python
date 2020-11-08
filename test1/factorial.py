
n=input("Enter the factorial of number required : ")
result=1

def fact(n):
    for i in range(n,1,-1):
        global result
        result=result*i
    return result

print(fact(n))

