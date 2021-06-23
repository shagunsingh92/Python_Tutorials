'''Recursion - recursion is using a function inside a function.
We will try writing a factorial with the help of iterative and a recursive method'''

# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# '''in this step when n-1=1 then the function "factorial_recursive" will return 1 and
# the function will stop.'''
# print(factorial_recursive(5))



# def iterative_factorial(n):
#     fac=1
#     for i in range(n):
#         fac= fac*(i+1)
# '''n decides the number of iterations and i gets the value for the particular iteration.
# With each iteration the value of i will increase till i+1==5'''
#     return fac
# print(iterative_factorial(5))

#0 1 1 2 3 5 8 13
def febonacchi_func(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febonacchi_func(n-1)+febonacchi_func(n-2)




print(febonacchi_func(6))