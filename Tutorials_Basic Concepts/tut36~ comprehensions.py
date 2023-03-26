
# Step 1 - list comprehension:
# The below steps can be written in one lin:
# my_list = []
# for i in range(100):
#     if i%3==0:
#         my_list.append(i)
# print(my_list)

# list comprehension way of writing the code, it uses square brackets
# my_new_list= [i for i in range(100) if i%3==0 ]
# print(my_new_list)



# Step 2 - Dictionary comprehension:
# if we want to generate a dictionary which has a pattern
# my_dict = {0:'item0',3:'item3',6:'item6',9:'item9'}

# rather than writing it manually we can use a dictionary comprehension - it uses curly brackets with key value pair
# my_dict1 = {i:f'item{i}' for i in range(10) if i%3==0}

# Note - we can also reverse the key:value pair of the dictionary using dictionary comprehension
# my_dict2 = {value:key for key,value in my_dict1.items()}
# print(my_dict1,my_dict2)




#Step 3 - Set Comprehension:
# Set comprehensions will return unique values - set comprehension uses curly brackets
# dress = {dress for dress in ['dress1','dress2','dress1','dress2']}
# print(dress)




# Step 4 - Generator Comprehension:
# def evens():
#     for i in range(100):
#         if i%2==0:
#             yield  i
# x = evens()


# all the steps mentioned above can be done in a single line using generator comprehension:
# Note - generator comprehension uses common brackets
# evens = (i for i in range(100) if i%2==0)
# for i in evens:
#     print(i)


'''
input - how many items does the user wants to enter
input - take all the items as an input
input - ask the user that what kind of comprehension they want to create
print the comprehension
'''

num_item = int(input('How many items do you want to enter?:'))
my_list = []
for i in range(num_item):
    item= input('Enter your item: ')
    my_list.append(item)

type_comprehension = input('What kind of comprehension do you want to create?:')

if type_comprehension == 'List Comprehension':
    listing = [x for x in my_list]
    print(listing)
if type_comprehension== 'Dictionary Comprehension':
    dict = {i:my_list[i] for i in range(len(my_list))}
    print(dict)
if type_comprehension == 'Set Comprehension':
    setting = {i for i in my_list}
    print(setting)
