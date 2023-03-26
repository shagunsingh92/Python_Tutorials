'''
Lambda function or anonymous functions
Lamda are one liner functions that needs to be used only once in the code and hence is written in one line
'''

# basic syntax

# func_name = lambda x,y : x-y
# print(func_name(5,4))
#
# # this is just like writing
#
# def func_name(x,y):
#     return x-y

a=[[1,32],[3,14],[5,6]] # This is imp and is confusing
a.sort(key=lambda x:x[1]) # sort function's attribute "key" takes in a function as an argument
print(a) # here the list is getting sorted on the basis of second arguments of the list
# each list in the list a is considered as an item for the above example. here x = smaller list.