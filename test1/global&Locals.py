#global variables
a=10
b=20
c=30
d=40

def something():
    a=100       #local variables
    global b
    b=200
    x=globals()['c']
    x=300
    globals()['d']=400
    print("local a",a)
    print("local b",b)
    print("local c",c)
    print("local x",x)
    print("local d", d)

something()

print("global a",a) #global
print("global b",b) #change in global
print("global c",c) #global
print("global d",d) #change in global
