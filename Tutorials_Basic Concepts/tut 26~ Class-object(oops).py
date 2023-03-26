'''
1. Class are nothing but blueprints with the help of which one can create different objects.

2. Objects are nothing but the instances of the class

3. Objects of a class can have their own instance variables

4. Class variable is a property of the class. It can be accessed using the objects of the class or by using the
name of the class itself.

5. If we want to change the class variable we cannot do it with the help of object variables,this can only
be achieved with the help of class method decorator - point 9, we need to use class name for that.

6. .__dict__ when applied to an object or to a class it returns all the variables of the class or object along with
their values in an key-dictionary format.

7. self and init : __init__ is a constructor and is used if we want to initialise the instance variables of an object.
if function in a class has self keyword the self is replaced by the object name.

8. Note: Self keyword takes in the object/instance of the class. If a function is written inside a class it should
essentially have a self keyword so that the objects can be placed in place of the self.

9. @classmethod. Check the example below. We cannot change a class variable with the help of an instance of the class,
but that can be done using a class method decorator. Class method decorator uses cls for initialization of the class
variable and not self. self is used to initialize the instance variables only. If a function mentioned under a
class method decorator is called on an object, that particular object gets an ability to change the class variables provided
 the variable was initialized in the class method decorator.

10. @classmethods can be used as an alternative constructor. the syntax for it is as follows: ** Confused **
                @classmethod
                def func_name(cls,string):
    1st method: var = string.split('_') # here it can be anything in place of "-". It basically represents how string objects are joined together.
                return cls(var[0],var[1],var[2] etc) #this does the same thing as given in eg of point 7

    2nd method: return cls(*string.split("_")) #grab the entire string, split it and then pass it to the class as parameters.


    my_obj= classname.func_name('Prateek_29_male')
    # check out eg point 10

Note - even if we are using classmethod decorator as an alternative constructor but we still need to use __init__ as a
constructor in order to initialize the instance variables. Class method decorator if used as an alternative constructor can
only do the value assignment to already initialized instance variables.
'''

# # eg of a class and its objects:
# # Class name should be in camel case
# class MyFirst:
#     my_var = 8
#     pass
#
# # The syntax given  below is used to create objects/instances of a class
# obj1 = MyFirst()
# obj2 = MyFirst()
#
# # the syntax given below is used to create instance variables of an object
# # Check eg of point 7, that is the other way of writing all the variable initiations in one line
# obj1.name = 'Shagun'
# obj1.age= 29
# obj2.name = 'Gunjan'
# obj2.age = 25
# obj2.sub = ['Hindi','English','Maths']
#
# print(obj1.name) # This is how we can get the value of variable of an object
#
# print(obj1.my_var)# class variable can be accessed with the help of an instance of a class
# print(MyFirst.my_var)# class variable can be accessed with the help of class name
#
# obj1.my_var= 9
# print(obj1.my_var) # this statement is not changing the class variable but it is creating another instance variable
# print(obj1.__dict__) # this statement proofs the above point

# print(MyFirst.__dict__) # this statement proofs that the original class variable was not changed by the above statement
#
# MyFirst.my_var = 10
# print(MyFirst.my_var) # Now the above statement has changed the value of my_var





# eg. of point 7
# class MySecond:
#     def __init__(self,name,age,sex):  # This is a constructor it is used to initialise the object variables
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def my_ex(self):
#         print(f'Name of my ex is {self.name}, his age was {self.age} and he was a {self.sex}')
#
# new_obj = MySecond("Prateek",29,"Male") # this step is same as writting new_obj.name ='Prateek' etc
# new_obj.my_ex()





# eg. of point 9:
# class MySecond:
#     his_nick = 'Baba'#class variable. This variable can be changed using class object provided @classmethod decorator is used in the class and variable has been initialized
#
#     def __init__(self,name,age,sex):  # This is a constructor it is used to initialise the object variables
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def my_ex(self):
#         print(f'Name of my ex is {self.name}, his age was {self.age} and he was a {self.sex}')
#
#     @classmethod
#     def change_nick(cls,new_nick):
#         '''class method doesn't take self but cls for initialization.it gives the object an ability to change the
#         value of a class variable'''
#         cls.his_nick = new_nick #change the class variable to the new given value
#
#
# new_obj = MySecond("Prateek",29,"Male") # this step is same as writing new_obj.name ='Prateek' etc
# new_obj.my_ex()
#
# new_obj2 = MySecond("Bala",30,"Male")
# new_obj2.my_ex()
#
# print(new_obj.his_nick) # prints the old value of the class variable
# new_obj.change_nick('Lost love') #this way an object can also change a class variable. Class variable changed to "lost love"
# print(new_obj2.his_nick) #accessing the class variable again which now has the changed value to prove the point
# print(new_obj.__dict__) # no new variable got created in the object of the class by following this method




# eg point 10 - @classmethod as an alternative constructor is confusing.
# class MySecond:
#     his_nick = 'Baba'#class variable
#
#     def __init__(self,name,age,sex):  # This is a constructor it is used to initialise the object variables
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def my_ex(self):
#         print(f'Name of my ex is {self.name}, his age was {self.age} and he was a {self.sex}')
#
#     @classmethod
#     def change_nick(cls,new_nick,string):
#         '''class method doesn't take self but cls for initialization.it gives the object an ability to change the
#         value of a class variable'''
#         cls.his_nick= new_nick #class variables are getting initialized here
#         return cls(*string.split("-"))
#
#
#
# new_obj = MySecond("Prateek",29,"Male") # this step is same as writing new_obj.name ='Prateek' etc
# new_obj.my_ex()
#
# new_obj2 = MySecond.change_nick('harami','Bala-30-male') #Directly using the class method as an alternative consructor
# # all the values for instance variables are taken as a string and passed while creating an object
# new_obj2.my_ex()
# print(new_obj2.his_nick)
# print(new_obj2.__dict__)
# print(new_obj2.name)
