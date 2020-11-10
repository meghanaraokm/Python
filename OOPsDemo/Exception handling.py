
evens=[2,4,6,8,10]
x = input("Enter the index : ")

try:
    print("connection opens..")
    a=int(x)
    b=evens[a]
    print("The number in list is {} ".format(b))
except IndexError as e:
    print("Provided index is out of range for the list. Please provide lower number : ", e)
except ValueError as e:
    print("Invalid input : ",e)
except Exception as e :
    print("There is some error, try again later : ", e)
finally:
    print("connection is closed.")


