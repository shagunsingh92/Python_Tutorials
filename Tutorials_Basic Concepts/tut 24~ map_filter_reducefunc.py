'''
1. map function lets one to map a function on a list of items. The basic syntax of map function is:
 list(map(func_name,list_name)) - we need to apply list function on the map output as map will return a list of items.

2. Filter function returns the list of elements where a given function returns true. Filter function is
also an inline function. The basic syntax of a filter function is:
list(filter(function_name, iterable))

3. reduce is a function of functools module. reduce function can apply a function on an entire iterable and
can reduce it to one single output. Basic syntax of reduce function is:
reduce(func_name,iterable) - we need not to typecast it in a list because reduce returns only single output
'''

my_list =['apple','mango','orange']

# 1. using map with a lambda function
# my_list= list(map(lambda x:x+x,my_list))
# print(my_list)


# 2. using map function with a normal function
# def my_func(x):
#     return x+x
# my_list = list(map(my_func,my_list))
# print(my_list)

# 3. very important. you might forget this. Printing lists of squares and cubes of numbers
# def sq(x):
#     return x*x
# def cu(x):
#     return x*x*x
# my_func = [sq,cu]
# for i in range(5):
#     my_num= list(map(lambda x: x(i),my_func)) # calling the functions here in the lambda expression. Items of my_func will take the place of x. we are returnin x(i) in the lambada expression and not i because we want to get sq and cube of i and not just i.
#     print(my_num)

# 4. Filter function:
# def my_num(x):
#     return x>5
# my_list = [1,2,3,4,5,6,7,8]
# my_newlist=list(filter(my_num,my_list))
# print(my_newlist)

# 5. Reduce function:
# import functools
# from functools import reduce
# my_num2 =[1,2,3,4]
# my_num2 = reduce(lambda x,y: x+y,my_num2)
# print(my_num2)