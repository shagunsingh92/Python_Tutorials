'''
1. We can create a copy of function 1 into a variable named func2.
In case func1 is deleted after the above statement, still the func2 will run because func2 has a copy of 
func1 in it. 
2.A function can be deleted by "del function_name". 
3.We can return a function with the help of another function. Also, we can pass a function as an 
argument to another function
4. If we want to perform the same tasks before and after a function then we can use decorators.The two
features of a function i.e creating the copy of a function in another variable and calling a function 
inside a function are used in decorators.

5. Other way of writing "func3 = deck1(func3)" is :
                    @deck1
                    def func3():
                        print('I am the test string')

6. Decorators are the functions which can modify the functionality of a function.
'''

# #eg of point 1.
# def func1():
#     print('subscribe')
# func2 = func1
# func2()

# #eg of point 3, a function is returning another function:
# def my_func(num):
#     if num==0:
#         return print
#     else:
#         return sum
# print(my_func(3))
#
# # eg of point 3, a function can be passed in as an argument to another function:
# def my_new(func):
#     return func(0)
# print(my_new(my_func))

# eg of point 4, creating a decorators:
def deck(func):
    a = int(input('Enter a number:'))
    b = int(input('Enter b number:'))
    print(f'my sum is {a+b}')
    func()
    print(f'my product is {a * b}')
# @ deck
def my_func():
    print('I am decorating')

# my_func() - **
# print(type(my_func()))
my_func = deck(my_func) #this way of writing will not throw any error ****



# def deck1(func1):
#     def func2():
#         print('execute statement 1')
#         func1()
#         print('executed everything')
#     return func2
#
# @deck1 # or this
# def func3():
#     print('I am the test string')

# func3 = deck1(func3) # either this
# func3() # need to call the function which is being passed in the decorator function - ***


'''
Confusion : in the '**' example of the decorator, if we call the function on which decorator is applied it is throwing 
an error, but doesn't throw the error in '***' example 
'''