'''
Iterable - __iter__() or __getitem__(): iterable are those objects where these two methods are defined.
These two methods when applied to the the object returns an iterator. If an object is iterable it will run __iter__()
function and will generate an iterator.

iterator - __next__(): Iterator is an object where this method is defined. Once an iterator is generated it can
run __next__() function and will keep providing the next item of the iterable. If all the elements of the iterable are exausted
and we still run __next__() in the object it will throw an error

Iteration - The process of doing iteration

Generators - Generators are a kind of iterator. We can iterate using a generator only once. For example range is a generator.
basic syntax of creating a generator can be seen in step 1. We use generators to save memory as the generators don't save
a value but generates it on a fly

Note: "For loop" handles the end error of a generator automatically and that is why we do not get any error if we use
range function (a generator) with for loop.

Note - use print if there is no function. With function use return and with generators use yield because return will simply
throw you out of the loop
'''

# step 1 - a function is defined which is a generator, we use yield which is a generator and will return values on a fly
# def gen(n):
#     for i in range(n):
#         yield i
#
# g=gen(3) #After printting till 3 with the help of __next__() it will throw an error because the generators can iterate only once
# print(g.__next__()) # __next__() method is only defined on iterators and generators are a kind of iterator
# print(g.__next__())


# my_str = 'This is a test string'
# x= my_str.__iter__() # creating an iterator/generator
# x= iter(my_str)
# print(x.__next__()) # Iterating through the elements of the iterator
# print(x.__next__())



# def gen(n):
#     for i in range(n):
#         return i
# g= gen(3)
# print(g.__next__()) # will not work without yield



# Febonachi series using generators

def feb(n):

    mera_feb =[]

    for i in range(2):
        mera_feb.append(i)
        yield i

    for i in range(2,n):
        z = mera_feb[i-1]+mera_feb[i-2]
        mera_feb.append(z)
        yield z

# 0 1 1 2 3 5 8

x = feb(8) # here x is the  iterator
# print(x.__next__()) # by running __next__ on an iterator one can get next elements of the object
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

for items in x:
    print(items,end=',')