'''There are three ways of formatting a string.
1. by using %s
2. by using .format method
3. by using f"" or f-strings
'''

'''1.first way of formatting a string by using %s. problem with this method is that it will become confusing 
incase we want to insert multiple letters'''
# my = 'Shagun'
# your='Gunjan'
# my_str= 'my name is %s'%my
# our_str='your name is %s and your name is %s'%(my,your)
# print(my_str)
# print(our_str)


'''2. Second way of formatting is by using .format method. problem here is again readability will be
compromised if multiple letters are to be inserted'''
# my = 'Shagun'
# your= 'Gunjan'
# my_str = 'my name is {}'.format(my)
# our_str='your name is {} and your name is {}'.format(my,your)
# # Notes:
# # the curly braces takes in the index values, eg. first curly braces will take in value in variable my and so on
# # if we don't want braces to take in the default values then we can pass in the index values in the braces
# # eg. 'your name is {1} and your name is {0}'.format(my,your)
# print(my_str)
# print(our_str)


'''3. Third way of formatting is by using f string method.This is the most new and favoured method because 
the variables can be directly inserted in the string'''

# my='Shagun'
# your='Gunjan'
# our_str = f'My name is {my} and your name is {your}'
# print(our_str)

# Note: even o/p of functions of a module can be inserted {math.cos(65)} - o/p of this function will be inserted
