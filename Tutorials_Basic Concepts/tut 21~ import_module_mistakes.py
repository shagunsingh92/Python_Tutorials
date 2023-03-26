'''
1. We should never create a file with the name of a module/package because if we import that module in
a program the first place where python will try to find the module will be in the current directory and
will find a file with the same name as of the module but as it will not have any functions of that package
it will throw an error.

2. we can import one file into another file of the same directory and use the functions written in the former
file.

3. don't keep spaces in the file names as if you want to import the file somewhere else it will throw an error

4. The following code returns the path which the python interpreter follows in order to find a module
 import sys
 print(sys.path)
'''

# import faulty_calcu
# print(faulty_calcu.my_faulty())

