#example 1 :
'''
def add(*args):
    s=0
    for i in args:
        s += i # 1 2 3 ....
        print("product of addition " ,s)

add(5,6,2)
'''


#example 2: with three parameters and arguments, parameters should be same as arguments.

'''
def threevar(a,b,c):
    print(a,b,c)

args=[1,3,5] # argument list
threevar(*args)

'''

# kwargs - key arguments - with key and value pair. this example is for passing parameters

'''
def mykwargs(a,b,c):
    print(a,b,c)

kw = {'a':"aaa", 'b':"bbb", 'c':'ccc'}
mykwargs(**kw) # why ** means it verifies the key and value .
'''

# o/p : aaa bbb ccc

# kwargs - key arguments - with key and value pair. this example is for passing parameters in kwargs and then s

def kw1(**kwargs):
    for a,c in kwargs.items(): # looping the kwargs items .
        print(a,c)

kw1(env1='QA', env2='Dev' , env3='Prod', env4='uat') # here we can use any number of arguments
# because kw1 function takes ** kwargs key values parameters(any number of arguments)

#o/p :

# env1 QA
# env2 Dev
# env3 Prod

