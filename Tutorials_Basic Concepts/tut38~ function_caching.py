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

'''

import time
from functools import lru_cache

@lru_cache(maxsize=2)# maxsize decides that how many previous commands will be stored in the memory.
def my_function():
    time.sleep(3)

# step 1
print("I have started")
my_function()
print("I have cached")
my_function()
print('Called the function again')
my_function()

#step 2 - other way of writing the same code as in step 1
# if __name__== '__main__':
#     print('I have started')
#     my_function() # the lru_cache decorator will create a cache at this point
#     print('I have stopped')
#     my_function() # this execution will not take time as there is a cache created for it already
#     print('I woke up again')