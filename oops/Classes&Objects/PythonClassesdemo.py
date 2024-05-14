
class Mytest:
    def test1(self): # self here means it belongs to the Mytest class this is an instance method
        pass
    def test2(self,testname):
        print("Name os the test: ",testname)

mt=Mytest() # This is object creation of class Mytest
mt.test1() # calling method test1()
mt.test2('python testing') #O/P-- Name os the test:  python testing


