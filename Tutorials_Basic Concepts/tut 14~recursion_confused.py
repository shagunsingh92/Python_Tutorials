'''Recursion - recursion is using a function inside a function.
We will try writing a factorial with the help of iterative and a recursive method'''

# def factorial_recursive(n): # calculation is done from larger to smaller
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# '''in this step when n-1=1 then the function "factorial_recursive" will return 1 and
# the function will stop.'''
# print(factorial_recursive(5))



# def iterative_factorial(n): # calculation is done from smaller to larger
# def my_fact(n):
#     fac = 1
#     for i in range(1,n+1):
#         fac= fac*i
#     return fac
#
# print(my_fact(5))
# '''n decides the number of iterations and i gets the value for the particular iteration.
# With each iteration the value of i will increase'''

#0 1 1 2 3 5 8 13
# def febonacchi_func(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return febonacchi_func(n-1)+febonacchi_func(n-2)

# print(febonacchi_func(7))