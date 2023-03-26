'''
1. Try-except-exception handling : If we want the code not to throw any error and stop executing the rest
of the program then we can user try-except-exception handling
2. Basic syntax:

                try:
                    some_code # in case this part of the code throws an error the control of the program
                    will go to the exception part and will print the error rather than stopping the
                    execution
                except Exception as e:
                    print(e) # this statement will print the error and will not stop the execution of
                    of the program.

                print('This is a very important code and we want its execution hence using',
                'try-except-exception handling')


3. We use Try-Except-Exception handling in the scenarios where we use an internet connectivity
'''
