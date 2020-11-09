
n=input("Enter the factorial of number required : ")


def fact(n):
    result = 1
    for i in range(n,1,-1):
        result=result*i
    return result

print("{}! is {}".format(n,fact(n)))

