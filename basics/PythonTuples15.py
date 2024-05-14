#Tuples are immutable
# Once created , cannot modify, cannot delete, cannot edit

# different types to create tuples
'''
test1=()
test2=(11,55,33)
test3=("abc","xyz","app")
test4=([1,2,3,4,5,6])
test5=tuple("aparupa")
print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
'''

# tuple function( len, min, max , sum)
'''
a1=(1,2,3,55,6,32,12,32,56)
print(len(a1))
print(min(a1))
print(max(a1))
print(sum(a1))
'''

# tuple iteration using loops
'''
a1=(1,2,3,55,6,32,12,32,56)
for i in a1:
    print(i, end=" " )
    '''

#slicing for tuples
'''
a1=(1,2,3,55,6,32,12,32,56)
print(a1[2:5]) #(3, 55, 6)
print(a1[:6]) #(1, 2, 3, 55, 6, 32)
print(88  in a1)
print(2 in a1)
'''

