'''
1. If one wants to create a function which is for numerous variables we can use *args

2. syntax : func_name(*args):
                for items in args:
                    print(args)
   har = ['shagun', 'gunjan', 'ankur']
   func_name(*har)

   Note: args take in variables as a tuple eg. here even har is a list but when it is passed in to args it will
   be taken as a tuple.

3. It is ok to pass in a normal variable along with args
    syntax: func_name(normal_variable,*args):

4. Any variable name can be used in place of args but by convention we use "args"

5. It will throw an error if this syntax is used: func_name(*args, normal_variable) - args come after normal variable

6. "kwargs" come after args while passing them to a function i.e func_name(normal_var,*args,**kwargs)

7. args and kwargs are optional i.e even if they are mentioned in the function definition but the variable
passed to that function doesn't contain args, kwargs- it won't throw any error.
syntax: func_name(normal_variable, *args, **kwargs):
            print(normal_variable)
            for item in args:
                print(item)
            for key,value in kwargs.items():
                print(key,value)
        func_name(5) - No args or kwargs is given here, but it will not throw any error

8. kwargs are dictionary or key-value pairs.
'''


normal_variable ='this is a test string'
my_list= ['shagun', 'gunjan', 'ankur']
my_new_list = {'name':'shagun','age':29,'sex':'female'}

def my_func(x, *args,**kwargs):
    print(x)
    for items in args:
        print(items)
    for key,value in kwargs.items():
        print(f'My key is {key} and my value is {value}')

my_func(normal_variable, *my_list, **my_new_list)