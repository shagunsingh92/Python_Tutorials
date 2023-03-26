'''
1. Note: Global variable can be edited inside a loop but cannot be edited inside a
function without using global keyword

2. enumerate functions can return index as well as the value at the particular index position simultaneously.
Basic syntax of the enumerate function is:
for index,items in enumerate(name_of_list):
    if index%2==0:
        print(items)

3. If someone want the values at only even positions in a list of items, they can achieve this by two ways
    a. is by using the general for loop method
    b. is by using enumerate functions

4. Enumerate function works for all the data types where an index position can be allocated eg. list, tuple and set.
'''

my_list= ['shagun','bibha','land','sky']

# Bellow is the general way of solving the above problem:
# i=1
# for items in my_list:
#     if i%2 != 0:
#         print(items)
#     i+=1 # here we want i to impact items and hence is a part of for loop and is not in if statement


# Same can also be done in the following way:
# for items in my_list:
#     if my_list.index(items) % 2 ==0:
#         print(items)
#         print(my_list.index(items))
#     else:
#         pass


# The same problem can be solved using an enumerate function:
# for index,items in enumerate(my_list):
#     if index%2==0:
#         print(items)