

#String operations
# + is used for concatenation , * is used to repeat multiple times

# concatenation(+)
'''
s="Welcome to python"
print(s+"programming")
# repeating multiple times (*)
s1="Welcome to python"
print(s1 * 4)
'''

#Slicing ons strings
'''
str="Welcome"
print(str[1:4]) # elc
print(str[:2]) #We
print(str[5:]) #me
'''

# ord is used to check the ASCII value a character
'''
print(ord("S"))
# chr is used to check the ASCII value of a number
print(chr(83))
'''

# len(length of the string, max(maximun ASCII value of string), min(minimum ASCII value of a String)
'''
names = "Python"
print(len(names))
print(max(names))
print(min(names))
'''
# in and not in operator in python
'''
ss= " operations"
print("rations" not in ss)
print("nations" in ss)
'''

# < ,> , <= , >= , == , ! (comaparision operators)

# iterating strings using for loop. How number of characters , that many number of repeatations
'''
n="test"
for i in n:
    print(n)
'''

# Testing strings , isalnum , isalpha, isupper, islower, isdigit,

# isalnum - give alphanumeric
'''
s='tree3423'
print(s.isalnum())
print("Welcome".isalpha())
print("welcome".isupper())
'''

# Searching substrings of a string

# startswith, endswith, find, rfind, count(substring)

'''
x="substring of string"
print(x.endswith("rings"))
print(x.startswith("sub"))
print(x.find("ring"))
print(x.rfind("of"))
print(x.count("g"))
'''

# Conversion of strings - upper, lower, title , replace, capitalzie
'''
y="Welcome the python programming"
print(y.replace("the","to"))
print(y.upper())
print(y.lower())
print(y.capitalize())
print(y.title())
'''