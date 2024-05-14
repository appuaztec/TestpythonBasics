#iteration and looping statements

#list and range function
'''
print(list(range(10)))
print(list(range(1,10,2)))
print(list(range(2,10,2)))
'''

#------------------------------for loop in python----------------------

#print numbers between 1-10(starting value is always 0)
'''
for i in range(10):
    print(i)
    '''

#print even numbers(starting value is always 0)
'''
for i in range(2,10,2):
    print(i)
    '''


#print odd numbers(starting value is always 0)
'''
for i in range(1, 10, 2):
        print(i)
'''
#print decreasing numbers(starting value is always 0)
'''
for i in range(10, 1, -1):
        print(i)
        '''

#------------------------------while loop in python----------------------

i=1
while i<10: #condition # 1 2 3 4 5 6 7 8 9
    print(i)
    i = i + 1 #incrementation

i=10
while i>1: # 10 9 8 7 6 5 4 3 2
    print(i)
    i = i - 1



