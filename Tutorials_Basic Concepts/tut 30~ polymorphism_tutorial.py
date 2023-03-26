'''
Polymorphism - is the ability to take various forms
For example 5+6 = 11 but "5" + "6" = 56, here the + operator has taken different forms based on what it is called upon
Polymorphism can be achieved with the help of overriding an attribute or function or by the use of dunder methods
'''

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
#     def pocket_devices(self):
#         print(f'there can be {self.devices} number of pocket devices')
#
#
# obje2 = PocketGadjets(3,300,"sweden")
# print(obje2.my_var)
#
# obj1 = Electronics(1,2,3)
# print(obj1.my_var)
'''this variable was overridden in the child class. The same attribute will return two different values when called by
the instances of two different class. This is an example of polymorphism. Similar things can be done with functions
and other attributes. In pycharm if an attribute was overridden we can see an "O" on the left of that line'''


'''Note : Check harry's video for revision'''



# example of super()
'''If one wants to use the instance variables of the parent class even though the child class has its own constructor
they can use super(). Super class is used so that we can use any attribute mentioned in the constructor of 
the super class.'''

# class A:
#     var1 = 18
#     def __init__(self): # incase we do not pass any variables in the constructor we are simply making the variable which cannot be altered
#         self.var1 = 'This is a string' # the values are directly passed while initializing the variables
#         self.var2 = 24
#
# class B(A):
#     def __init__(self):
#         self.var3 = 5
#         self.var1 = 10
#         '''var1 value mentioned above will not get printed by obj1.var1 because after this step the super
#         constructor was called and it has it's own var1. But if we call super class before executing
#         self.var1 then 10 will get printed.If we want to print the instance variable of the super class
#         we can do that by using super() inside the child constructor and then accessing the instance variable
#         of super class with the help of the object of child class'''
#         super().__init__()
#         print(super().var1) #this statement will return the class variable of the super class. This is same as print(B.var1)
#
# obj1 = B()
# print(obj1.var3)
# print(obj1.var1)
# print(B.var1) # This statement will return the class variable of the super class.

# print(super().var1) #this statement will throw an error here because super() can only be called inside a constructor

'''The below way of using super class will not work out because the constructor of the child class takes in only
one variable but the super class needs to take two values from the user in order to print the variable values.
Super class works fine only when there is direct value assignment while initializing the variables in the super
class'''  #Confused
# class A:
#     var_my = 7
#     def __int__(self,pot,hot):
#         self.pot = pot
#         self.hot = hot
#
# class B(A):
#     def __init__(self):
#         self.var3 = 5
#         # super().__init__()
#         # super(B, self).__init__() # There are two different ways of writing the Supper class
#
# # obj1 = B()
# # print(obj1.var3)
# obj2 = A(4,5)
# print(obj2.var_my)
