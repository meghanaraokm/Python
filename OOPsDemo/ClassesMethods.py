
class Computer():

    def __init__(self,cpu,ram):   #constructor method
        self.cpu=cpu
        self.ram=ram
        print("from init")      #to show init runs without calling
    def config(self):
        print("Config is : ", self.cpu, self.ram)

comp1=Computer("i5",32)
comp2=Computer("i8",64)

comp1.config()
comp2.config()

print("\n\n\n")

class Student():

    school="ABC"                             # class / static variable

    def __init__(self,name,age,m1,m2,m3):    # init method - constructor
        self.name=name                      # instance variables
        self.age=age
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):                          # instance method
        return (self.m1+self.m2+self.m3)/3

    def get_name(self):                 #Accessor (get method or getter)
        return self.name

    def get_age(self):                  #Accessor (get method or getter)
        return self.age

    def get_marks(self):                #Accessor (get method or getter)
        return self.m1,self.m2,self.m3

    def set_name(self,name1):           #Mutator (set method or setter)
        self.name=name1

    def set_age(self,age1):           #Mutator (set method or setter)
        self.age=age1

    def set_marks(self,m1,m2,m3):       #Mutator (set method or setter)
        self.m1=m1
        self.m2=m2
        self.m3=m3

    @classmethod                        #decorator for class method
    def get_school(cls):                #class method (uses class variables and takes class as argument automatically)
        return Student.school

    @staticmethod                       #decorator for static method
    def info():                         #static method (does not use any class or instance variables)
        print("This is a student class")
        print(Student.school)


s1=Student("Megh",29,90,80,70)
s2=Student("Vish",31,82,96,76)

print(s2.get_age())
print(s1.get_name())

print(s1.avg())

s1.set_marks(92,87,79)
print(s1.get_marks())
print(s2.get_marks())

print(Student.get_school())

Student.info()