my_string = input('enter a string for me: ')
my_shift = int(input('give me a shift value: '))

'''Note: in order to return the list of all punctuation marks in a string format one can use "string.punctuations" 
command, but we cannot use it here because in the second "for loop" we need to compare the values with numbers. 
Integers cannot be compared with string and integer typecasting doesn't work on "string.punctuation" command.'''

def cacesar_cipher():
    """ This function takes in a string as an input and an integer from the user and returns a statement which is
    encrypted. For encryption each alphabet of the string needs to be increased by the number provided by the user
    as an integer eg. a -> c( if the integer given by the user was 2). This program will give some junk value in place
    of punctuation if punctuations apart from comma, full stop and space are used
    """
    my_list = []
    new_list = []
    my_code = ''

    # The for loop will convert letters into numbers
    for letter in my_string:
        if letter in [' ',',','.']:
            my_list.append(letter)
        else:
            my_list.append(ord(letter))
            '''if you want the actual position of the letters in the alphabetical series than you need to
                subtract 96 i.e. (ord(letter)-96) otherwise the ord(letter) will return ASCII value of the letter
                As 'a'=97 in ASCII hence we are subtracting 96 from the ord(letter) output. Takes only 1 letter
                as an input and not a string'''

    # this for loop will make the shift in the letters
    for num in my_list :
        if num in [' ',',','.']:
            new_list.append(num)
        else:
            new_list.append(chr(num+my_shift)) # chr function is opposite of ord()- converts num to string

    # This for loop will create the encrypted code
    for word in new_list:
        my_code = my_code+word  # can concatenate punctuations like normal string

    return my_code

print(cacesar_cipher())