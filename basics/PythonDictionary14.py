# Dictionary is used for key value pair, its related to Maps(HashMaps) in Java
# It is used to retrive add, modify, delete values using key
# Dictionaries are mutable

#Create dictionary
'''
cars={'Toyota': 'Rav4',
      'Nissan':'Rogue',
      'Tesla': 'SE'}
print(cars)

#add new value
print(cars['Toyota'])
cars['Nissan']='big Rogue'
print(cars)

#modify a value in a key
cars['Nissan']='Rogue XL'
print(cars)

#delete a key
del cars['Nissan']
print(cars)
'''

#-----------------looping in dictionary---------

#for loop
'''
cars={'mileage': '100',
      'rpm':'200',
      'rate': '300'}
for i in cars:
    print(i, ":", cars[i])
    '''

#length of the dictionary
'''
cars={'mileage': '100',
      'rpm':'200',
      'rate': '300'}
print(cars) #{'mileage': '100', 'rpm': '200', 'rate': '300'}
print(len(cars)) #3

#equality in dictionary(== and != )

#  equal to (==)
cars={'mileage': '100', 'rpm':'200', 'rate': '300'}
bike={'mileage': '100', 'rpm':'200', 'rate': '300'}
print(cars==bike)

#  equal to (!=)
cars={'ram': '100', 'rpm':'200', 'rate': '300'}
bike={'mileage': '100', 'rpm':'200', 'rate': '300'}
print(cars==bike)
'''

#Dictionary methods

cars={'mileage': '100', 'rpm':'200', 'rate': '300'}
#popitem
cars.pop('mileage') # {'rpm': '200', 'rate': '300'}
print(cars)
#clear
print(cars.clear()) #None
print(cars) #{}
# keys()

cars={'mileage': '100', 'rpm':'200', 'rate': '300'}
print(cars.keys()) # dict_keys(['mileage', 'rpm', 'rate']) , retunrs dictionary as tuples format
print(cars.values()) #dict_values(['100', '200', '300'])
print(cars.clear())
print(cars)
print(cars.get('mileage'))

cars={'mileages': '100', 'rpm':'200', 'rates': '300'}
print(cars)
print(cars.get('mileages'))
print(cars.pop('mileages'))
print(cars)








