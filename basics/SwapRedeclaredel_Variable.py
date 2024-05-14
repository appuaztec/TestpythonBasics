#Swapping variables
x=20
y=5
print("Before swapping:",x,y)
x,y=y,x
print("After swapping: ",x,y)

#Redeclaration of variables
a=10
print(a)
a=25
print(a)

#Deletion of variables
a=22
print(a)
del a
print(a) # name error - name 'a' is not defined
