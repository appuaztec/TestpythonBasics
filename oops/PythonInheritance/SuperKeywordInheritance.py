#Super keyword is used to get the parent class method, variable, constructor.

#parent class method

'''
class Parent1:
    def method1(self):
        print("This method1 from parent")

class Child1(Parent1):
    def method2(self):
        print("this is method 2 of child")
        super().method1() # Calling parent class method from the child class method

c=Child1()
c.method2()
'''

#calling parent class variables from child method
#Appraoch 1
'''
class Parent2:
    x, y = 10, 20

class Child2(Parent2):
    a, b = 22, 44
    def method2(self,i,j):

        print(i+j)
        print(self.a+self.b)
        print(self.x + self.y)
      # Calling parent class method from the child class method

c=Child2()
c.method2(12,44)
'''

#Appraoch 2
'''
x,y=10,20
class Parent2:
    x, y = 15, 25

class Child2(Parent2):
    x, y = 30, 40
    def method2(self,i,j):

        print(i+j)
        print(self.a+self.b)
        print(self.x + self.y)
      # Calling parent class method from the child class method

c=Child2()
c.method2(12,44)
'''

# super keyword can invoke parents class variables
#approach 2
'''

x,y=10,20
class Parent2:
    x, y = 15, 25

class Child2(Parent2):
    x, y = 30, 40
    def method2(self,x,y): #local variable

        print(x+y)
        print(self.x+self.y) #Class variable
        print(super().x+super().y)
        print(globals()['x'] + globals()['y']) #global variable
        # Calling parent class method from the child class method

c1=Child2()
c1.method2(12,44)
'''

# calling parent class constructor from child class

class Par2:
    def __init__(self): #constructor 1 of Parent class
        print("constructor from parent")

class Chi(Par2):
    def __init__(self): #constructor 2 of child class
        print("constructor from child")
        # super().__init__() #calling constructor1 of parent class(approach 1)
        Par2.__init__(self) #calling constructor1 of parent class(approach 2)


c2=Chi() # object creation of child class


