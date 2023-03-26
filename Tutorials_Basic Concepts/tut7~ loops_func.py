'''
1. All the data types cannot be iterated - cannot be iterated on a dictionary in the way it
works with a list
2. iteration can be used for list unpacking
3.In oder to do a dictionary unpacking ".items()" need to be used
4. If someone wants the list of keys of a dictionary -call items on dictionary
5. text.isnumeric() - this function determines that if all the elements of a string are numeric or not
6. Else part of the conditional statements are not compulsory and can be dropped if not required
'''

# eg. of list unpacking
# my_list= [['Harry', 1], ['shagun', 2], ['bibha', 3]]
# for name,num in my_list:
#     print(name, num)

# eg. we cannot iterate on a dictionary in the way we do it on a list
# dict1 = dict(my_list)
# print(dict1)

# for key,values in dict1:
#     print(key,value)# it will throw an error


# eg. we can iterate on a dictionary and do an unpacking by using ".items()"
# for key,values in dict1.items():
#     print(key)
#     print(values)


# eg. in order to get all the keys of a particular dictionary one can also call items directly on the dict name
# for items in dict1:
#     print(items)



'''Practice exercise: create a list and print only those elements which are number and are above 6'''

#First method
# my_new_list = [1, 2, 3, 4, 5, 6, 7, 8, 'shagun', 'gunjan']
# for items in my_new_list:
#     if type(items)==int:
#         if items>=6:
#             print(items)


#Second method
# for items in my_new_list:
#     if str(items).isnumeric() and items>=6:
#         print(items)

#Third method
# x= ['shagun','yeswanth',8,7,9,10,3,2,1]
# for num in x:
#     if str(num).isnumeric():
#         if int(num) >= 6:
#             print(num)