'''
1. If want to run a function half way and run the later part whenever we wish, we can use a coroutine
2. If we want to run from def searcher() to time.sleep(3) only( once as it takes time to run, we can use coroutine.
The segment of the code which comes after time.sleep(3) will keep running from the second time on
3. If we write variable =(yield) inside an infinite while loop, then the function under which it is written is
considered as a coroutine
4. The below given code is not a function but a coroutine because it will perform the activities mentioned in
point 1 only once - as that process can be time consuming. But once that part of code has run it will take the control
 to the while loop mentioned in the coroutine and will make it run from there. It will save the execution time as the
 time consuming process is performed only once
5. Coroutine is mostly used to read machine learning models as they are time consuming tasks
6. We can use search.close() in order to close the coroutine. Once a coroutine is closed and if we try to run it again
it will throw an "StopIteration error". Closing the coroutine will simply free all the resources which were getting used
by the existing coroutine - there is a drawback though i.e. that if we want to start the coroutine again in future
it will initially take time to execute.
7. Coroutine are generators
'''

# import time
#
# def searcher():
#     book = 'This is a book which has content from code with harry website and youtube channel'
#     time.sleep(3) # Here,there can be any task which consumes 3 sec to execute
#
#     while True:# This infinite while makes a function, coroutine
#         text = (yield) #Whatever input is given to the instance of the coroutine will come in place of yield
#         if text in book:
#             print('Your text is in the book')
#         else:
#             print('Your text is not in the book')
#
# search = searcher() # Instance of the searcher coroutine
# next(search) #as searcher is a generator that is why we need to use next function in order to run the code mentioned under searcher
# #As searcher is a coroutine that is why we need to run next only once
#
# search.send('kamala') # This statement will assign "kamala" to yield.
# input('Press a Key')
# # The above statement is used to show that how much delay is there in order to execute the next line of code
#
# search.send('Harris')
# input('Press a key')
# search.send('harry')
#
# search.close()# closing the coroutine
# input('Press a key')
# search.send('marry')


#example of coroutine:
def my_cor():
    r= open("../Projects and Assignments/coroutine_chalange.txt")
    my_text= r.read()

    while True:
        my_fam = (yield)
        if my_fam in my_text:
            print('You are in the family')
        else:
            print('I am not in the family')

my_coroutine = my_cor()
next(my_coroutine)
my_coroutine.send('Shagun')
input('Press a key')
my_coroutine.send('Gunjan')
