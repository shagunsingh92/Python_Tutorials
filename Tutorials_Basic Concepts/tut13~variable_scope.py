"""
Global Variable - are the variables which are completely outside any loop. We can access global values in a function but
need to use global keyword to change the value of global variable.
Local variables - are the variables which are local to a function.

Check Harry's lecture to understand if confused.

Source of the question below is not clear. the question itself is not clear.
"""

'''Question : Take an integer as an input and return the sum of 0 till that number. If the entered number is not
an integer then return zero'''

# First code:
#
# my_num= input('provide me a single integer: ')
#
# def add_it_up():
#     my_add = 0
#     if my_num
#     for num in range(my_num+1):
#         my_add = my_add+num
#     return my_add
# print(add_it_up()) # in order to see the returned value in pycharm you need to add print while calling the function


'''Problems with this first code :
1. I am unable to return the variable my_add. Need to print it essentially in order to get an output. 
2. if I put my_add as a global variable, the function throws an error. 
3. The first code did not work as if take input from a user using input statement then all the inputs will be in 
string format and if typecast it into integer we will not be able to answer the second problem i.e - the program 
should return 0 if the input given is not integer.
'''


# Second Code:

# def add_it_up(n):
#     sum = 0
#     if type(n)!= int:
#         print(0)
#     else:
#         for num in range(n+1):
#             sum = sum+num
#     #return sum # return keyword did not work here as well
#     print(sum)
#
# add_it_up(2)

'''Problems with second code: 
1. The return keyword and if sum is used as a global keyword did not work - This happened because global keywords 
can only be read and cannot be altered. There is only one way to do that, call global keyword on that variable 
i.e global sum 
'''

# Third Code:Using While loop

# def add_it_up(num):
#     sum=0
#     n=0
#     while n<num+1:
#         sum=sum+num
#         n+=1
#     return sum # functions are not returning values
# add_it_up(3)



# Fourth Code: Using Sum function

# def add_it_up(n):
#     return sum(range(n+1))
#
# print(add_it_up(3))




#important:
# x=3
# def harry():
#     x= 20
#     def larry():
#         '''This function can only change the value of a global variable. Global keyword will not let the function larry
#         use x variable as a local variable.'''
#         global x
#         x = 88
#     print('before calling larry',x)
#     larry()
#     print('after calling larry',x) # both the print statement will return local value of variable x which is 20
# harry()
# print(x) # this statement will prove that function larry has changed the value of a global variable