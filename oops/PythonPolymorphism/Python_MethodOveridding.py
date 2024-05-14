

#Method overriding

class Parent1:
    def method1(self):
        print("This method1")

class Child1(Parent1):
    def method1(self):
        print("this is method 2 of child")

c=Child1()
c.method1()


