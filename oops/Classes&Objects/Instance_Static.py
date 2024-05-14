class MyPython:
    def instancemethod(self): # this is a instance method
        print("This is a instance method")

    @staticmethod # This is a static method . Python has static methods and not variables
    def staticmethod(self,name): # static method doesn't contain any self.
                            # if we give self then it will act as an argument
        print("Static method: ", name)

im=MyPython()
im.instancemethod()
MyPython.staticmethod("testing python is good",name="appu")