'''
1. If a function takes time to run we can save the desired number of commands in the form of cache(which will be stored
in our system memory) so that the next time when the same function is called it will be fetched from the memory and will
not take the run time which it took on the first instance.

2. Cache - stores data in the system memory which results in speeding up a program

3. In order to perform function caching there is a builtin module named functools which has a decorator named
lru_cache.lru_cache takes in an argument called maxsize. By assigning some value to maxsize we are informing the
system that cache those many number of commands of the function from the end.

4 basic syntax:
from functools import lru_cache
@lru_cache(maxsize= x)
function

5. You cannot call same function twice just one after another. example - step 1

6. In order to resolve above mentioned issue we can simply use main function as shown in step 2
'''

# import time
# from functools import lru_cache
#
# @lru_cache(maxsize=2)
# def my_function():
#     time.sleep(3)
#
# #step 1
# # my_function()
# # my_function()
#
# if __name__== '__main__':
#     print('I have started')
#     my_function() # the lru_cache decorator will create a cache at this point
#     print('I have stopped')
#     my_function() # this execution will not take time as there is a cache created for it already
#     print('I woke up again')
