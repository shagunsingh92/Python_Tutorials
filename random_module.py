import random

# in order to generate random integer number we can use "randint" function of the random module
x = random.randint(1,3)# gives random integer between two numbers
print(x)

# in order to generate random number(integer or non-integer) the user can use "random" function of the random module
# y= random.random() # this function doesn't take any argument
# print(y)

#in order to generate random choice from a list we can use "choice" function of random module
my_list=['shagun','gunjan','ankur']
a=random.choice(my_list)
print(a)
