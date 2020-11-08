
def wish():
    print("Happy Birthday")

def add(a,b):
    c=a+b
    return c

def arith(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e

def person(name,age=1):
    print("Name is", name)
    print("Age is ", age)

def sum(a,*b):
    print(a,b)
    c=a
    for i in b:
        c=c+i
    print c

def muliplication(*b):
    print(b)
    c=1
    for i in b:
        c=c*i
    print c

def student(name,**data):
    print("name ",name)
    for i,j in data.items():
        print(i,j)




wish()

resultAdd=add(3,5)
print(resultAdd)

r1,r2,r3=arith(2,4)
print r1,r2,r3

person(age=6,name="Megh")

person(name="Vish")

sum(1,2,3,4)

muliplication(10,2,1)

student("Vish",age=16,city="London")