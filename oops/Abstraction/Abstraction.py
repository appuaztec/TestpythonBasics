from abc import ABC, abstractmethod

class X(ABC):

    @abstractmethod
    def ab1(self):
        pass
class Y(X):
    def ab1(self):
        print("test the abstract class and method")

obj1=Y()
obj1.ab1()