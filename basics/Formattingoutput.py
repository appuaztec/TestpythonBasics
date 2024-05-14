#Formatting operators


n="Aparupa"
n1=9739
n2=10000.00

#1
print("name is:",n)
print("number is:",n1)
print("sal is:",n2)

#2By using %s-String, %d-int, %g-float - formattting
print("name: %s number:%d sal:%g"%(n,n1,n2))


#3 here value is important
print("name:{} number:{} sal:{}".format(n,n1,n2))

#4 by using indexing(index and value is important)- index always starts from 0
print("name:{0} number:{1} sal:{2}".format(n,n1,n2))

