

# __str__ ----------This is to print a reference variable

'''
class Pythonstr:
    def __str__(self):
      return "Test"


p1=Pythonstr() # This is to print a reference variable after object creation of class
print(p1)

# O/p : Test
'''

class Construct5:
    # Class variable
    def __init__(self, empname, empid, empsal):  # constructor local variables(__init__ is a constructor)
        self.empname = empname  # constructor argument , printing local variables#
        self.empid = empid
        self.empsal = empsal
    def __str__(self):
        return "Testing"# calling class variables (created inside a class and outside method)


e1 = Construct5("Aparupa", 12, 45000)
print(e1)