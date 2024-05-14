
#Hierarcial inheritance

class Parent1:
    x,y=20,50
    def method1(self):
        print(self.x*self.y)

class Child1(Parent1):
    a,b=11,22
    def method2(self):
        print(self.a+self.b)

class Child2(Parent1):
    i, j = 10, 20

    def method3(self):
        print(self.j / self.i)

p=Parent1()
p.method1()

c=Child1()
c.method1()
c.method2()

c1=Child2()
c1.method1()
c1.method3()

# o/p : 1000
# 1000
# 33
# 1000
# 2.0
