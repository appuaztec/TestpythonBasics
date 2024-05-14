# Class having multiple objects . Named and nameless object

class MyParent:
    def child1(self):
        print("First child")

p1=MyParent() # object has a reference variable is called a named object
p1.child1() # First child

MyParent().child1() # object which doesnt have a reference variable is called nameless object
                    # First child

p2=MyParent()
p3=p2
print(id(p3)) #4494397264
print(id(p2)) #4494397264
print(id(p1)) #4494397216

# O/p :
# First child
# First child
# 4494397264
# 4494397264
# 4494397216


