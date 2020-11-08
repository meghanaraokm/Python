n=input("Enter the factorial of number required : ")

def fact(n):
    if n==1:
        return 1
    else :
        return (n*fact(n-1))

print("{}! is {}".format(n,fact(n)))