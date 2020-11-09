class A():                                 #parent class or super class of A

    def __init__(self):
        print("init in A")

    def feature1(self):
        print("feature 1 A working")


class B(A):                               #child (sub) class of A & parent class of C

    def __init__(self):
        print("init in B")

    def feature1(self):
        print("feature 1 B working")

    def feature2(self):
        print("feature 2 B working")


class C(B):                               #child (sub) class of B which is a subclass of A --> Multilevel inheritence

    def __init__(self):
        super().__init__()
        print("init in C")


    def feature3(self):
        print("feature 3 C working")

class D():                                              #parent class of D

    def __init__(self):
        print("init in D")

    def feature4(self):
        print("feature 4 D working")


class E(A,D):                                       #child (sub) class of A & D --> mutiple inheritence

    def __init__(self):
        print("init in E")

    def feature4(self):
        print("feature 4 E working")



a1=A()

b1=B()

c1=C()