
# __init__() ------This is a constructor


'''
#Class , object and constructors
class Construct:
    def Constructm1(self):
        print("Test the constructor")
    def __init__(self):
        print("This is the constructor ")


c=Construct() # always constructor is invoked while creating an object of the class
c.Constructm1()

#o/p :
# This is the constructor
# Test the constructor

'''

# converting local into global variables
'''
class Construct1:
    def m1val(self,v1,v2):  # local variables
        print(v1) # printing local variables  ----#24
        print(v2)                             #23
        self.v1 = v1 # class variables
        self.v2 = v2


    def m2add(self):
        print(self.v1+self.v2) #printing class variables # 47


c=Construct1() # always constructor is invoked while creating an object of the class
c.m1val(24,23)
c.m2add()

# O/p : 24
# 23
# 47
'''

# using constructor method
'''
class Construct2:
    def __init__(self,v1,v2):  # local variables
        print(v1) # printing local variables  ----#24
        print(v2)                             #23
        self.v1 = v1 # class variables
        self.v2 = v2


    def m3add(self):
        print(self.v1+self.v2) #printing class variables # 47


c=Construct2(24,23) # always constructor is invoked while creating an object of the class
c.m3add()

#O/p : 24
#23
#47
'''
'''
# calling one method to another method in a same class
class Construct3:
    def m1(self):  # local variables
        print("method one ") # printing local variables
        self.m2(4)


    def m2(self,x):
        print("method two",x) #printing class variables # 47


c1=Construct3() # always constructor is invoked while creating an object of the class
c1.m1() # method two 4

#O/p : method one
# method two 4
'''

# Pass arguments to the constructor
'''
class Construct4:
    name="Basu" #Class variable
    def __init__(self,name):# constructor local variables(__init__ is a constructor)
        print(name) # constructor argument , printing local variables
        print(self.name) # calling class variables (created inside a class and outside method)


c1=Construct4(name="Appu") # always constructor is invoked while creating an object of the class
# we have to mention the parameter while invoking object and  call the constructor local variable.
#O/p :
#Appu
#Basu
'''


# Pass multiple arguments  to the constructor

class Construct5:
    # Class variable
    def __init__(self, empname, empid, empsal):  # constructor local variables(__init__ is a constructor)
        self.empname = empname  # constructor argument , printing local variables#
        self.empid = empid
        self.empsal = empsal
    def empdisplay(self):
        print("Empid:{} EmpName:{} EmpSal:{}".format(self.empname, self.empid,
                                                 self.empsal))  # calling class variables (created inside a class and outside method)


e1 = Construct5("Aparupa", 12, 45000)
e1.empdisplay()

# o/p " Empid:Aparupa EmpName:12 EmpSal:45000

