n=input("Enter the factorial of number required : ")

def fact(n):
    if n==0:
        return 1

    return (n*fact(n-1))

print("{}! is {}".format(n,fact(n)))