from abc import ABC, abstractmethod

class X(ABC):

    def __init__(self,val):
        self.val=val


    @abstractmethod  # only declaration of abstract method
    def ab1(self):
        pass

    @abstractmethod  # only declaration of abstract method
    def abs(self):
        pass
class Y(X): # implementation of abstract method in child class
    def ab1(self):
        print(self.val+20) #120

    def abs(self):
        print(self.val-5) #95

obj2=Y(100)
obj2.ab1()
obj2.abs()

# O/p " 120 95


# Abstract method we cannot create objects directly thats why these methods cannot be instantiated.
# If we have to create an object of abstract class then we need to extend to another class and complete the implementation
#of the same methods then we can create objects.
# basically used for security
# if we dont know the implementation of a method then we can only create abstract classes .