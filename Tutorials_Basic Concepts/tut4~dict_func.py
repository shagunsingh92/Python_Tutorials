'''
1.Value of a key can be a tuple,list or dict
2.inorder to delete a key-value pair from a dictionary one should use "del" keyword: imp- it is not
a function
3. my_dict1=my_dict; this statement will not create a copy of my_dict and in case my_dict1 is deleted
all the info in my_dict will be lost too
4.in order to create a copy of a dictionary use-> my_dict1=my_dict.copy()
5. get('key') returns the value of the key - need to print the result else won't work
6. update({'key':value}) - this function takes in a dictionary and updates the dictionary
with it's key-value pair
7. keys() returns the list of keys
8. items() returns the list of key-value pair
9. values() returns the list of values in that particular dictionary
10.The update function will update the value of a key or create a new key-value pair if it is not available in the
dictionary
'''

# my_dict = {'shagun':29,'gunjan':25,'ankur':22}

# my_dict['bibha']=50
# print(my_dict)
#
# # Note: there is one more way of doing the same thing:
# my_dict.update({'Sanjay':60})
# print(my_dict)
#
# my_dict.update({'bibha':60})
# print(my_dict)
#
# print(my_dict.get('bibha'))

# print(25 in my_dict.values())
# del my_dict['bibha']
# print(my_dict)
# print(my_dict.values())


#exercise on dict:
# my_oxford={'brother':'https://en.wikipedia.org/wiki/Brother',
#            'sister':'https://en.wikipedia.org/wiki/Sister',
#            'mother':'https://en.wikipedia.org/wiki/Mother'}
# my_word=input('Ask me the meaning of a word: ')
# print(my_oxford[my_word])

