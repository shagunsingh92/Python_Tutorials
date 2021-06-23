print('''\nLet's play Tik-Tak-Toe\n
            -Created by Shagun Singh''')

while True:
    # Face values are given to places on the board so that reassignment can take place
    print('''\n\n Enter a variable from the board given below: \n
     T1|T2|T3
    __________
     M1|M2|M3
    __________
     R1|R2|R3''')

    my_list = ['T1','T2','T3','M1','M2','M3','R1','R2','R3'] # List of accepted variables
    my_valid = [] #List will check that the user should not enter an already occupied position

    # my_board is a dictionary so that we can assign user's input to a particular location on the board
    my_board = {'T1': '', 'T2': '', 'T3': '', 'M1': '', 'M2': '', 'M3': '', 'R1': '', 'R2': '', 'R3': ''}

    def winner_check():
        ''' This function has all the conditions when a user can be a winner'''

        if my_board['T1']==my_board['T2']==my_board['T3']=='X':
            return '\nFirst Player won!'
        elif my_board['T1']==my_board['T2']==my_board['T3']=='O':
            return '\nSecond player won!'
        elif my_board['M1']==my_board['M2']==my_board['M3']=='X':
            return '\nFirst Player won!'
        elif my_board['M1'] == my_board['M2'] == my_board['M3'] == 'O':
            return '\nSecond Player won!'
        elif my_board['R1']==my_board['R2']==my_board['R3']=='X':
            return '\nFirst Player won!'
        elif my_board['R1'] == my_board['R2'] == my_board['R3'] == 'O':
            return '\nSecond Player won!'
        elif my_board['T1']==my_board['M1']==my_board['R1']=='X':
            return '\nFirst Player won!'
        elif my_board['T1'] == my_board['M1'] == my_board['R1'] == 'O':
            return '\nSecond Player won!'
        elif my_board['T2']==my_board['R2']==my_board['M2']=='X':
            return '\nFirst Player won!'
        elif my_board['T2'] == my_board['R2'] == my_board['M2'] == 'O':
            return '\nSecond Player won!'
        elif my_board['T3']==my_board['M3']==my_board['R3']=='X':
            return '\nFirst Player won!'
        elif my_board['T3']==my_board['M3']==my_board['R3']=='O':
            return '\nSecond Player won!'
        elif my_board['T1'] == my_board['M2'] == my_board['R3'] == 'X':
            return '\nFirst Player won!'
        elif my_board['T1'] == my_board['M2'] == my_board['R3'] == 'O':
            return '\nSecond Player won!'
        elif my_board['T3'] == my_board['M2'] == my_board['R1'] == 'X':
            return '\nFirst Player won!'
        elif my_board['T3']==my_board['M2']==my_board['R1'] == 'O':
            return '\nSecond Player won!'
        else:
            pass

    i = 1
    while True:
        if i < 5: #statement will check that not more than 9 inputs are given

            # First_player's turn
            first_player = (input('\nFirst Player: enter a number from the board: ')).upper()

            while first_player not in my_list:#checks if variable entered is acceptable or not
                print('\nInvalid entry, enter another number')
                first_player = (input('\nFirst Player: enter a number from the board: ')).upper()

            while first_player in my_valid: # checks if unique input was entered by first player or not
                print('\nInvalid entry, enter another number')
                first_player = (input('\nFirst Player: enter a number from the board: ')).upper()

            my_board[first_player] = 'X'
            my_valid.append(first_player)

            # Second Player's turn
            second_player = (input('\nSecond Player: enter a number from the board:')).upper()

            while second_player not in my_list:# check if acceptable variable was entered or not
                print('\nInvalid entry, enter another number')
                second_player = (input('\nSecond Player: enter a number from the board: ')).upper()

            while second_player in my_valid:# checks if unique input was entered by second player or not
                print('\nInvalid entry, enter another number')
                second_player = (input('\nSecond Player: enter a number from the board: ')).upper()

            my_board[second_player] = 'O'
            my_valid.append(second_player)

            i = i + 1
            # Print the new board
            print('\n', my_board['T1'], '|', my_board['T2'], '|', my_board['T3'], '\n________', '\n',
                  my_board['M1'], '|',
                  my_board['M2'], '|', my_board['M3'], '\n________', '\n', my_board['R1'], '|', my_board['R2'], '|',
                  my_board['R3'])


            # The below statements will check if someone won - after each loop
            check = winner_check()
            if check == None:#this will happen if the last statement of winner_check() is getting executed.
                pass
            else:
                print(check) #winner name will get printed
                break


        else:
            '''Control will come to this segment when all but one box are filled. If none of the 
            conditions mentioned in the winner_check() function satisfies after executing this statement, 
            it means that the game was a tie.'''

            first_player = (input('\nFirst Player: enter a number from the board: ')).upper()

            while first_player not in my_list:#checks if acceptable variable was entered or not
                print('\nInvalid entry, enter another number')
                first_player = (input('\nFirst Player: enter a number from the board: ')).upper()

            while first_player in my_valid:  # checks if unique input was entered by first player or not
                print('\nInvalid entry, enter another number')
                first_player = (input('\nFirst Player: enter a number from the board: ')).upper()

            my_board[first_player] = 'X'

            # Print the current board
            print('\n', my_board['T1'], '|', my_board['T2'], '|', my_board['T3'], '\n________', '\n',
                  my_board['M1'], '|',
                  my_board['M2'], '|', my_board['M3'], '\n________', '\n', my_board['R1'], '|', my_board['R2'], '|',
                  my_board['R3'])


            #At this level if check==None means no more inputs can be taken and hence it is a tie
            check = winner_check()
            if check == None:
                print('\nIt is a tie!')
            break

    command = (input('\nDo you want to play more? :')).upper()
    if command == 'YES':
        continue
    else:
        print('\nGame over!')
        break