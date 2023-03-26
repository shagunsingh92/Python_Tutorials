'''
1. Property Decorator- If we create an attribute in the constructor and assign a value to it like the one done below
with variable email,if we later try to change the value of the variable it cannot be changed in a normal way. In order
to do that either one needs to create a function which return the same value as the variable did but that way we
need to call the function rather than the variable. If we don't want to do that we can simply create a function
under property decorator and use the name of the function as a variable to perform the job.

2. Setters - if we want to set different values to an attribute which uses instance variables, we need to use setter
decorator. check out example step 4

3. The way we are creating our emails here by concatenating the strings will not help in printing obji.email once it is
deleted with the help of a deleter because "Nontype" cannot work with "+" operand

4. Deleter - If we want to delete an attribute then we can only do it by creating a deleter in the class and setting
the values of the variables to None

5. Functions can not be deleted using "del". But we can delete the instance variable using "del" alone. If property
decorator was used to create a variable like the one done here, we need to use a deleter for the del function to work.
We never delete the variables in Oops but we set them to none.
'''

class Employees:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # Step 1
        # self.email = f'{self.fname}.{self.lname}@harry.com'

    def explain(self):
        return f'The employee is {self.fname} {self.lname}'


    # Step 2
    # def email(self):
    #     return self.fname+self.lname+'@gmail.com'


    # Step 3
    @property
    def email(self):
        return self.fname+'.'+self.lname+'@'+'gmail.com'


    #Step 5
    @email.setter
    def email(self,string):
        x = string.split('@')[0]
        self.fname = x.split('.')[0]
        self.lname = x.split('.')[1]


    # Step 6
    @email.deleter
    def email(self):
        self.fname= None
        self.lname=None


obj1 = Employees('Shagun','Singh')
obj2 = Employees('Gunjan','Singh')

# Example Step 1- Value of variables can not be changed by creating a variable in the constructor
# This happens because the variable value is initiated when the constructor runs
# print(obj1.print_email)

# Example Step 2- Value of variables can be changed by creating a function
# print(obj1.email())
# obj1.fname = 'Changed'
# print(obj1.email)

# Example Step 3 - We can create function under property decorator and use that function name as a normal variable
# print(obj1.email)
# obj1.fname = 'Changed'
# print(obj1.email)


#Example Step 4-  We cannot set a different value to email untill we use a setter decorator
# this problem can be solved using setters
# obj1.email = 'left.right@gamil.com'

# Example Step 5 - this problem can be solved using setters
# obj1.email = 'left.right@gmeiil.com'
# print(obj1.email)
# print(obj1.fname)

# del obj1.email
# # print(obj1.email)
# print(obj1.fname)
