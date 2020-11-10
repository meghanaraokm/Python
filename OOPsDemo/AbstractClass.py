from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car is starting - kirrr..")

    def stop(self):
        print("Car is stopping - kreeech")


class Bike(Vehicle):

    def start(self):
        print("Bike is starting - grrr..")

    def stop(self):
        print("Bike is stopping - ceeeeerrr..")


class Driver:

    def work(self,vehicle):
        print("Driver is working")
        vehicle.start()
        vehicle.stop()


c1=Car()
b1=Bike()

d1=Driver()

d1.work(c1)
d1.work(b1)
