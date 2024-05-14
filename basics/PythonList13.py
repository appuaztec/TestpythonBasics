
# List is a collection where group of elements are stored
'''
list1=list()
print(list1)

list2=list([1,2,3,4,5])
print(list2)

list3=list(["appu","manju"])
print(list3)

list4=list("welcome")
print(list4)
'''


#=-----------Accesing elements in list----------
'''
l=[5,4,3,2,6]
print(l[3]) # 2
'''

# list of common operations in list ( max, min, len, in , no in, count, sum)
'''
l1=[10,13,14,18,19]
print(13 in l1)

l1=[10,13,14,18,19]
print(len(l1))
'''

# list slicing
'''
lis = [22,99,33,45,56]
print(lis[:4]) # 45
'''

# ---- + and * operator in list
'''
la= [1,5,4,3,5] 
la2=[2,4,5]
print(la+la2)
print(la* 3)
'''

# travesing list using for loop

'''
ll=[1,2,3,4,5,6,7,8]
for i in ll:
    print(i, end=" ")
    '''
# commonly used list methods with return type
'''
li1 =[2,3,4,5,6,9,2]
li1.append(4) # [2, 3, 4, 5, 6, 9, 2, 4]
print(li1)

print(li1.count(2))

li2=[3,6,8]
li2.extend(li1)
print(li2) # [3, 6, 8, 2, 3, 4, 5, 6, 9, 2, 4]
print(li1.index(3))
print(li1.insert(5,28))
print(li1)
print(li1.pop(2))
li1.reverse()
print(li1)
'''

# List comprehension

'''
liss=[a for a in range(10)]
print(liss)
li2=[a+2 for a in range(10)]
print(li2)

lis1=[a for a in range(10) if a%2==0]
print(lis1)
'''







