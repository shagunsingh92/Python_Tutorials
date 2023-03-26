'''
 1. if we want certain part of a code not be executed when the file is imported somewhere else then
 we should keep that part of the code under "if __name__=='__main__':"

 2. The value of __name__ will always return __main__ if run in a python file. if __name__='__main__' is used in a file
 the code under that section will not get executed if this file is imported somewhere else because in the imported file
 the value of __name__ becomes the source file name and not __main__, the conditional statement will fail and hence the
 code mentioned under if __name__='__main__': will not get executed.

 3. The file names are not in the correct syntax and hence might throw error while you try to import this file somewhere else.
    Create a new file instead for practice.

Note: If we print something inside a function there will be an extra None in the output. The only way out is
to make the function return something and not simply print a value

'''

def my_test_file():
    return 'this is a trial for name&main functions'
print(my_test_file())

print(f'print the value of {__name__}') #this statement will return __main__ in the current file but if this file is imported, __name__ will take the value of the source file name i.e. tut22 ~name_main_func
if __name__=='__main__':
    print('Whatever is written under __name__=="__main__", will not get executed if this file is imported')