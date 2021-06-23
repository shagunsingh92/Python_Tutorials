'''
1. OS module is an inbuilt module.
2. OS stands for operating system like windows, linux etc which takes care of the hardware.
3. With the help of OS module one can change the working directory, open a file, rename a file etc.
4. We can change the current working directory using the OS module. This will be helpful if we want to read a file
which is not available in the current working directory. This will be helpful if we are not providing the complete
path while fetching a file
5. os.listdir - this function of OS module will give out all the files present in the current directory in the form
of a list
6. os.mkdir("folder_name") - this function of os module will create a new folder in the current directory
7. os.makedirs("folder1/folder2") - this function will create folder1 as a directory and folder2 as a subdirectory of
folder1
8. os.rename("old_name","new_name") - This function will change the name of the old file. The content of the file
will remain unchanged
9. os.environ.get("variable_name") - this function will read an environment variable if there is any which goes by the
name variable_name.
10. os.path.join("C://","harry.txt") - this function is an effective way of joining two different paths. By joining
the paths this way we need not to worry about any extra slashes
11. os.path.exists("C://") - Returns True/False based on a particular path exists or not
12. os.path.isfile("Name_of_the_file") - will return true/false based on the name passed is a file or not
12. os.path.isdir("Name_of_the_directory") - will return true/false based on the name passed is a directory or not
 '''

import os
print(dir(os)) # will give out all the functions which can be performed using OS module
print(os.getcwd()) # this will give out the current working directory
# os.chdir("C://") # this will change the current working directory to c://
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C://")) #we can also pass in the complete path of any particular directory

