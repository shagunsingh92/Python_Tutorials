'''
Dunder method are those methods that start with two underscores and ends with two underscores.
__init__ is a special dunder method because it is a constructor and it gets called automatically whenever
an object of that class is created. __add__ is called special dunder add method because it does an operator overloading
of "+" operator. All the dunder methods cannot perform operator overloading eg. __str__ and __repr__ dunder methods.
They are explained in the foot note
'''

class A:
    var1 = 9
    def __init__(self,money):
        self.var3 = 'This is in the constructor of class A' # direct value assignment is happening here and that is why var3 is not mentioned in the function arguments.
        self.money = money

    def __repr__(self):
        return f'A({self.money},{self.var1})'#The repr dunder method usually contains inforations like the one given here'

    def __str__(self):
        return 'This usually used to speak about the object'

    def __add__(self,other): # example of operator overloading
        return self.money+ other.money
class B(A):
    var2 = 10

obj1 = B(30)
obj2 = A(10)
print(obj1+obj2) # the add dunder method of the parent will be called here automatically
print(repr(obj1)) # repr need to be specified if there is already an str in the base class else
print(str(obj1))# str is default. The same outout will be printed if we do not use str
print(obj1)
print(dir(obj1))
'''
If the parent class doesn't have an str dunder method the above statement will simply print the memory location 
of the obj1. In order to avoid that output we can use str or repr dunder methods. repr usually has information 
like Class_name(var_value1,var_value2). str dunder usually has information related to the object.
In case there is no str but has repr in the base class then print(obj1) will print the output of dunder repr

Method overloading Documentation: https://docs.python.org/3/library/operator.html
'''