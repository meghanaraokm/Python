class Student():

    def __init__(self,name,roll,laptop):
        self.name=name
        self.roll=roll
        self.lap=laptop

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop():

        def __init__(self,brand,ram):
            self.brand=brand
            self.ram=ram

        def show(self):
            print(self.brand, self.ram)

lap2=Student.Laptop("Mac",64)

s1=Student("manasa",7,Student.Laptop("Lenovo",32))
s2=Student("Sushanth",6,lap2)

s1.show()
s2.show()
