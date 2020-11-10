class Order:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __add__(self, other):                                   #Overloading operator "+" for obejct order
        return self.price+other.price


o1=Order("Sanitizer",10)
o2=Order("Mask",6)

total=o1+o2                                                     #addition using overloading operator

print("Total Payment is: {}".format(total))