'''
1. We can create a copy of function 1 into a variable named func2.
In case func1 is deleted after the above statement, still the func2 will run because func2 has a copy of 
func1 in it.
See eg 1, "func2 = func1()" will store the o/p of func1 in the variable and we can directly print func2 in order to
get the value of func1(). "func2=func1" will store only the location/pointer of func1 in the variable and we will have
to print func2() to get the results of func1.
2.A function can be deleted by "del function_name". 
3.We can return a function with the help of another function. Also, we can pass a function as an 
argument to another function. pass the func name and not func().
4. If we want to perform the same tasks before and after a function then we can use decorators.The two
features of a function i.e creating the copy of a function in another variable and calling a function 
inside a function are used in decorators.

5. Other way of writing "func3 = deck1(func3)" is :
                    @deck1
                    def func3():
                        print('I am the test string')

6. Decorators are the functions which can modify the functionality of a function. Functions are first class variables
as they can be treated as a normal variable too as seen here.
7. If we want to return the name of the function we can write - "func.__name__" here func is a variable which takes the
value of the function.

8. Follow the following standard process to write decorators:
 def decorator_name(func_name):
    def wrapper_func(*args,**kwargs): # we are using *args and **kwargs here to avoid any error when we call func_name. args and kwargs need to be introduced at func beginning.
        decorator code
        variable = func_name(*args, **kwargs) # call the function here and assign it to some variable, so that it could be returned
        decorator code
        return variable
    return wrapper_func #here the wrapper func is treated as a variable of decorator_name function.

'''

# #eg of point 1.
# def func1():
#     print('subscribe')
# func2 = func1
# func2()

#eg of point 3, a function is returning another function:
# def my_func(num):
#     if num==0:
#         return print
#     else:
#         return sum
# print(my_func(3))
#
# eg of point 3, a function can be passed in as an argument to another function:
# def my_new(func):
#     return func(2)
# print(my_new(my_func))


#decorator example
# import time
# def time_it(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
#         return result
#     return wrapper # we are using wrapper as a variable here. loose the parenthesis if
#
# @time_it
# def calc_square(numbers):
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     return result
#
# @time_it
# def calc_cube(numbers):
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#     return result
#
# array = range(1,10)
# out_square = calc_square(array)
# out_cube = calc_cube(array)
# print(out_square)
# print(out_cube)

#Another decorator example
# def my_deck(func):
#     def my_wrapper(*args,**kwargs):
#         print('We are playing SUM game!')
#         x= func(*args,**kwargs)
#         print('I hope you got your SUM')
#         return x
#     return my_wrapper
#
# @my_deck
# def my_func():
#     x= int(input('Enter a num:'))
#     y= int(input('Enter another num:'))
#     return x+y
#
# print(my_func())