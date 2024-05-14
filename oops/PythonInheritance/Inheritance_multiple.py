
#multiple inheritance

class Parent1:
    x,y=20,50
    def method1(self):
        print(self.x*self.y)

class Parent2:
    a,b=11,22
    def method2(self):
        print(self.a+self.b)

class Child1(Parent1,Parent2):
            i, j = 10, 23

            def method3(self):
                print(self.a + self.b)


c=Child1()
c.method1()
c.method2()
c.method3()

#O/p: 1000
# 33
# 33
