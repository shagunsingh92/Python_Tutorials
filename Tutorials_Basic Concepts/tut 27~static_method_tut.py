'''
1. If we wish to create a normal method inside a class then we need to use @staticmethod decorator to do that
2. The function written under @staticmethod decorator doesn't take self as an argument.
3. We can create a function inside a class which takes self as an argument but doesn't use self to initiate any instance
variables. We can simply ignore self and use the instance function like a normal function but it will impact the program's
efficiency
'''

class My_name:

    def my_name(self): # this will impact the  efficiency of the program as
        return 'This is my name'

    @staticmethod
    def your_name():
        return 'This is your name'

my_obj = My_name()
print(my_obj.your_name())
print(my_obj.my_name())