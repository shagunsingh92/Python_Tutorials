import random
'''
1. For loop works till all the iterations are complete
2. While loop works until a condition is true
3. general syntax of while loop is : while condition: loop
4. With each loop there should be a change in the conditions otherwise the while loop will run infinitely
5. In order to use while loop with a condition (eg. i<45) we need to initiate i outside the while loop
6. "While True" - This loop will run until a break statement is satisfied.
7. If control finds a break keyword then it comes out of the immediate enclosing loop
8. if control finds a continue keyword then it jumps to the next iteration and doesn't execute the later
steps
'''

#exercise1- the program should keep taking the input from user until user enters a number above 100

# i=0
# while i<100:
#     i = int(input('input a number : '))
# print('you have entered a number above 100')


'''exercise2 - guess the number. limit the number of guesses to 5. print the number of guesses remaining.
print game over if the user has exhausted all his trials'''

# my_num=random.choice(range(20))
# i=1
# while i<6:
#     user_num =int(input('Guess a number:')) # asking input from a user
#     if my_num==user_num:
#         print('Congrats, you won!')
#         print('You won in',i, 'attempts') #the number of attempts to guess the right number
#         break
#     elif user_num<my_num:
#         print('You have entered a smaller number')
#         print('number of guesses remaining:', 5-i)
#         i=i+1
#         continue
#     else:
#         print('You have entered a larger number')
#         print('number of guesses remaining:', 5 - i)
#         i=i+1
#         continue
# print('You have exhausted all your available attempts')
# print('The number you had to guess was:', my_num)
