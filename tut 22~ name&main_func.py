'''
 1. if we want certain part of a code not be executed when the file is imported somewhere else then
 we should keep that part of the code under __name__==__main__

 2. If we print the value of __name__ in the main function, it will return __main__

 3. the value of __name__ in the file where the main file was imported, will return the name of
 the file which has the __name__=__main__ function. Here you need not to explicitly print the value of __name__.
 The print(__name__) in the original class with return __main__ but in the imported file the same statement will return
 the original file name.

Note: If we print something inside a function there will be an extra None in the output. The only wat out is
to make the function return something and not simply print a value

'''

def my_test_file():
    return 'this is a trial for name&main functions'
print(my_test_file())

print(f'print the value of {__name__}') #this statement will return __main__
if __name__=='__main__':
    print('Whatever is written under __name__=="__main__", will not get executed if this file is imported')