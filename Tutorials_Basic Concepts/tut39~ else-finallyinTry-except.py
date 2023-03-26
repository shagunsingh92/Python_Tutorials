'''
1. Finally - is used to clean up the code i.e if there are any files which are open will be closed when finally will get
executed.

2. Either code under except will run or the code under "else" will run - not both
Note : Else always comes before finally - finally(in the end)

3. Finally will always get executed irrespective of code is in Try or Except or Else.

4. We can also use multiple except statements, check step 1 - EOFERROR and IOERROR are types of errors. They take the
position of Exception if someone wants to be more specific

'''

f1 = open('../Projects and Assignments/bibha.txt')

try:
    f2 = open('shagun.txt') # note if the file is in an other directory the we cannot open the file here. create a new file to work with instead. There is a different way to import files from a separate directory - not learnt

except Exception as e:
    print(e)

#step 1:
# except EOFError as e:
#     print('The error which I received is',e)
# except IOError as i:
#     print('The error which I received is',i)

else:
    print('this will run only when except is not running')

finally:
    f1.close()
    f2.close()

