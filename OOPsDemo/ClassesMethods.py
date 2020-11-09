
class Computer():

    def __init__(self,cpu,ram):   #constructor method
        self.cpu=cpu
        self.ram=ram
        print("from init")      #to show init runs without calling
    def config(self):
        print "Config is : ", self.cpu, self.ram

comp1=Computer("i5",32)
comp2=Computer("i8",64)

comp1.config()
comp2.config()