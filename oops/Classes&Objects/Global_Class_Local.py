
# example 1 with different names for global, class and local variables
'''
x,y=10,22 #global variables
class GlobalClassLocal:
    a,b = 20,40 #class variables
    def add1(self,i,j): # local variables
        print(i+j)  # accessing local variables
        print(self.a+self.b) #accesing class variables using self keyword
        print(x+y) # accessing global variables directly without any self keyword

gcl=GlobalClassLocal()
gcl.add1(20,56)

# o/p :
# 76
# 60
# 32
'''

# example 2 with same names for global, class and local variables

x,y=22,12 #global variables
class GlobalClassLocal:
    x,y = 20,40 #class variables
    def add2(self,x,y): # local variables
        print(x+y)  # accessing local variables #76
        print(self.x+self.y) #accesing class variables using self keyword #60
        print(globals()['x']+globals()['y']) # accessing global variables directly without any self keyword
                                            #globals() is called when global variables names are same
                                            # Syntax : globals()['x'] # 34


gcl2=GlobalClassLocal()
gcl2.add2(20,56)

# o/p :
# 76
# 60
# 32
