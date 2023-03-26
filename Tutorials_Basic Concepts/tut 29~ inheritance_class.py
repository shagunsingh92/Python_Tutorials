# single inheritance:
'''attributes were inherited from single parent'''
# class Parents:
#     num_of_kids = 3
#
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age = age
#         self.sex=sex
#
#     def kid_intro(self):
#         print(f'My name is {self.name}, age is {self.age} and I am a {self.sex}')
#
# class Child(Parents):
#     num_of_siblings = 2
#
#     def __init__(self,name,age,sex,siblings): #This is not an efficient way of initializing instance variables of an inherited class
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.siblings = siblings
#
#     def sib_intro(self):
#         print(f'My siblings are {self.siblings}')
#
# obj1 = Child('shagun',29,'Female',['Gunjan','Ankur'])
# obj1.sib_intro() # obj1 which is an instance of Child class can access the functions, variables etc of the child class
# obj1.kid_intro()# as well as of the parent class




# multiple inheritance
'''Attributes are inherited from multiple classes. Here the attributes including the constructor is fetched from the first
class whose name was passed while creating the inherited class. If an attribute is not found in the first class then only 
the control looks for that attribute in the subsequent classes. Check the example below. The object of multiple 
inheritance can have attributes of it's own and can also have the access to the attributes of it's parents'''

# class Parents:
#     num_of_kids = 3
#
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age = age
#         self.sex=sex
#
#     def kid_intro(self):
#         print(f'My name is {self.name}, age is {self.age} and I am a {self.sex}')
#
#
# class GrandParents:
#     def my_another(self):
#         return 'I am one of the grandparents'
#
#
# class Child(Parents,GrandParents):
#     num_of_siblings = 2
#     def sib_intro(self):
#         print(f'My siblings are {self.num_of_siblings}')

# #obj1 = Child()# need to pass 3 arguments here because the first class i.e Parents has three variable in it's constructor
# obj1 = Child('Gunjan',26,'Female')
# obj1.sib_intro()
# print(obj1.my_another())
# obj1.kid_intro()



# multilevel inheritance - check the eg

# class Electronics:
#     num_electrical = 1
#     my_var = 8
#     def __init__(self,parts,price,country):
#         self.parts = parts
#         self.price = price
#         self.country = country
#
#     def madein(self):
#         print(f'This electronic device has {self.parts}. It was manufactured in {self.country}.'
#               f'The price of the device is {self.price}')
#     def max(self):
#         print('xyz')
#
# class PocketGadjets(Electronics):
#     num_pocket = 2
#     my_var = 9
#     def __init__(self,devices):
#         self.devices = devices
#     def pocket_devices(self):
#         print(f'there can be {self.devices} number of pocket devices')
#
# class phone(PocketGadjets):
#     '''This class will inherit all the attributes of class pocketgadjets and electronics. But the constructor and other
#     variables will be first searched in the parent class and if not found in the parent class will be searched in the
#     grandparent class.
#     '''
#     num_phone =3
#     my_var = 10
#     def typephone(self):
#         print(f'There are {self.num_phone} number of phones available in the market')
#
# obj1 = phone(['Samsung','Nokia'])
# obj1.typephone()
# print(obj1.num_phone)
# print(obj1.my_var)
# obj1.pocket_devices()
# obj1.max() # this will get executed because the function is not using any class specific variables.

'''
Note: Here my var will be first searched in the phone class. If not found in phone class it will be searched in 
pocketgadjets class and if not found even there then only the control will go to the grandparent class.
obj1.madein() - this statement will through an error because our child case is using the constructor of the parent case
and the madein function of the grandparent class is using multiple variables which are not initialized in the child
class. 
 '''



# Public-Private-Protected access specifiers
'''
Public variables - are those which can be accessed by all the objects 
Protected variables - are those which can be accessed by the base class and by all of its derived classes only 
Private variable - are those which can be accessed by only the base class i.e the class where that variable is defined

Syntax for protected variables : _variable_name 
Syntax for private variables : __variable_name 
Note - Protected variables can be accessed by using the standard ways i.e "object_name._variable_name" but in order to 
access a private variable one needs to  take care of the name-mangling i.e. "object_name._classname__variablename"
Python saves a private variable as "_Classname__variablename" this process is called name- mangling 
'''
# class PocketGadjets:
#     '''If I want to make a variable protected, we can put a single _ before the name of the variable.In case we want
#     to make the variable private we need to put two __ before the name of the variable. '''
#     num_pocket = 2
#     _protected = 9
#     __private= 10
#     def __init__(self,devices):
#         self.devices = devices
#     def pocket_devices(self):
#         print(f'there can be {self.devices} number of pocket devices')
#
# class phone(PocketGadjets):
#     num_phone =3
#     def typephone(self):
#         print(f'There are {self.num_phone} number of phones available in the market')
#
# obj1 = phone('Samsung')
# obj2 = PocketGadjets('Nokia')
# print(obj1._protected)
# print(obj2._protected)
# # print(obj1._phone.__private) # this will not work because private variable can only be accessed by the base class
# print(obj2._PocketGadjets__private) #Pyhton uses name-mangling to save private variables.