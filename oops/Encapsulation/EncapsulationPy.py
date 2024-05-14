# Encapsulation : Wrapping for method and variables by using private variables and methods

#scope level is within the own class with __ (two underscores)

# private variable __a , can be accessed within the class

'''
class Encap:
    __x=10;
    def method1(self):
        print(self.__x)
        print()

obj=Encap()
obj.method1()
'''

# private method __method , can be accessed within the class
#approach 1
class Encap:
    __x=10;
    def __method1(self):
        print(self.__x)
    def method2(self):
        print("Display the method")
        self.__method1() # calling private method inside a class

obj=Encap()
obj.method2()

