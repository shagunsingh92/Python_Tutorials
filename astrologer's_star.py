print(''' Astrologer's star pattern
        - Created by Shagun Singh\n\n''')

my_variable = '*'
my_list=[] # needed for astrologer star

my_stars = int(input("How many rows do you want in your astrologer's star: "))

for num in range(1,my_stars+1):
    new_var= my_variable*num # rows will get changed automatically as print takes an end operator whose default value is \n
    my_list.append(new_var)

print("\nHere is your Astrologer's star pattern:\n")
for items in my_list:
    print(items)

print("\nHere is your reverse Astrologer's star pattern:\n")
my_new= my_list[::-1] # needed for reverse astrologer star series
for items in my_new:
    print(items) # printed the reversed list of *