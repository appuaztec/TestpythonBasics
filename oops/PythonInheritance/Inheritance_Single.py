

# Single inheritance

#example 1

'''
class Parent1:
    def method1(self):
        print("This method1")

class Child1(Parent1):
    def method2(self):
        print("this is method 2 of child")

p=Parent1()
p.method1()

c=Child1()
c.method1()
c.method2()

'''

class Parent2:
    x,y=20,50
    def method1(self):
        print(self.x*self.y)

class Child2(Parent2):
    a,b=11,22
    def method2(self):
        print(self.a+self.b)

p=Parent2()
p.method1()

c=Child2()
c.method1()
c.method2()

# o/p :
# 1000
# 1000
# 33
