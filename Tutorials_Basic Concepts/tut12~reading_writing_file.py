'''
Modes:
1. "r" : open for reading (read mode) - default mode
2. "w" : open for writing (write mode). Deletes previous content and writes new one.
3. "x" : This operation fails if the file already exists. Creates a file if it doesn't exist (exclusive creation).
    Can only write in the file after creation using this operation. For reading need to close the file and open file in read mode.
4. "a" : This mode is used to add more content to a file(append mode). Cannot read in append mode.
5. "t" : If one wants to deal with the data as a string than they can open the file in a text mode (text mode) - default mode
6. "b" : if one wants to deal with binary data(binary mode)
7. "+" : This mode is used to update a file(read+write mode). can be used with append, read or write.

Important points:

1. basic syntax to read a file is : variable = open('name of the file')
   # open function returns a pointer and not the content of the file. In order to read the content and perform
   action on a file one needs to assign it to some variable.
   # different types of IO modes can then be passed to this new pointer variable eg. content = variable.read()
                                                                                     print(content)
   # name of the file needs to be passed as a string inside the open function.
2. Note: After performing a function on a file one should always close it. Syntax:  file_name.close()
   the reason why closing a file is a good practice because that way one can free the system
   resources used to perform functions on that file. If one follows this practice the programs will behave as expected

3. The second argument of open function is modes, eg. : open("file_name", "r")
   "r" - stands for read mode and can also be written as "rt" which means read text mode(default)
   "rb" - stands for read binary mode and will give binary output

4. seek(0) : This function is used to bring back the control on the very first letter of the text file.
            this is required if the file was read already - cursor is at the end of the string hence will not give
            any output. If we want the cursor  to move at a particular location is the text then we can pass on
            its index value to seek function.

5. Line in a text file can be read by using iterations. syntax: for line in variable:
                                                                    print(line)
    Note: here one should not iterate on content or on variable.read() because once read() is applied to a pointer
    the pointer looses all its contents and hence will not return anything. iterate on the file pointer

6. readline() : readline function is also applied on the file pointer and returns one line at a time from the file

7. readlines() : returns list of all the lines in the text file

8. tell() : If this function is applied on a file pointer, then it releases the location of the cursor

9. with block - If we open a file with the help of with block we need not to worry about closing it as it gets closed
automatically. syntax: with open('file name') as f:
                            a= f.readlines()
                            print(a)
    here f is the file pointer.

10. my_new = open("xyz","r") -> here my_new is a pointer. can be used to iterate through each line.
    my_content = my_new.read() -> here my_content is container. can be used to iterate through each word in the file.
'''

# examples:

# my_pointer = open('practice_text_file.txt')
# print(my_pointer.read())
# print(my_pointer.tell())
# my_pointer.seek(0)
# print(my_pointer.read())
# my_pointer.seek(0)
# print(my_pointer.read())
# print(my_pointer.readline())
# print(my_pointer.readline()) # need to run the code multiple times in order to print all the lines in the text file
# print(my_pointer.readlines()) # returns the list of all the lines in the text file
# my_pointer.close()

# my_new_pointer = open('practice_text_file.txt', 'w')
# my_new_content = my_new_pointer.write('write this content in my file')
# # this part will delete all the existing content in the text file and will write the content provided.
# # use append to add more content to an existing file
# my_new_pointer.close()

# my_brand_new_pointer = open('practice_text_file.txt', 'a+')
# brand_content = my_brand_new_pointer.write('\n you are spicy')
# '''there is no append function in IO of files in Python, one needs to mention the mode in while opening the file and
# use write function to append something to the existing file
# Note: the '+' mode need to be with at least one of the modes else it won't work eg. "+"- won't work. "a+" will work'''
# my_brand_new_pointer.close()

# my_next = open('practice_text_file.txt.txt')
# content = my_next.read()
# print each letter of the text file by iterating on the container:
# for letter in content:
#     print(letter)


# for printing all the lines in a text file is by iterating on the pointer and not on the container(content)
# for lines in my_next:
#     print(lines)

# my_next.close()

