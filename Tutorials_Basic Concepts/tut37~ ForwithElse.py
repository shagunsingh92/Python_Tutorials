'''
1. We can use else with the for loop
2. Step 1 - this is an already known way but here the entire for loop will run and will not break out until all the
elements of mylist are over. This will happen even if the if statement doesn't satisfy.
3. If we want the loop to end and print what is there in the else statement, syntax is mentioned in step 2
'''

my_list = ['shagun','gunjan','ankur','bibha']

#Step 1
# for items in my_list:
#     if items=='shagun':
#         print(items)
#     else:
#         print('This loop has ended')

#Step 2
# By following for-else loop if the loop breaks for any reason the output of the else statement will get printted
# for items in my_list:
#     if items=='gunjan':
#         print(items)
# else:
#     print('This loop has ended')