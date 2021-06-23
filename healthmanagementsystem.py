import datetime
print('''Health Management system
        -Created by Shagun Singh\n''')

def my_health():
    '''This is a health management system which lets you add all your activities in a text file.
    With the help of this program you can even retrieve the data which you logged. For this program to work,
    you should have three text files created in your system i.e "shagun.txt","gunjan.txt" and "bibha.txt" '''

    clients = {'Shagun':1,'Gunjan':2,'Ankur':3}
    client_num = input("What is your client's name: ")

    def getdate():
        """This function will capture the date and time when the log was entered"""

        my_log=[]
        x= datetime.datetime.now()
        date=x.strftime('%d-%m-%Y')
        time=x.strftime('%H:%M:%S')
        my_log.append(date)
        my_log.append(time)
        return my_log

    def Writing_data():
        """This function will help the user log their activities"""

        if clients[client_num]==1:
            s = open('shagun.txt','a+')
            s.write('\n')
            s.write(str(getdate()))
            s.write(': ')
            s.write(input('What did you do?:'))
            s.close()

        elif clients[client_num] == 2:
            g = open('gunjan.txt','a+')
            g.write('\n')
            g.write(str(getdate()))
            g.write(': ')
            g.write(input('What did you do?: '))
            g.close()
        else:
            b = open('bibha.txt','a+')
            b.write('\n')
            b.write(str(getdate()))
            b.write(': ')
            b.write(input('What did you do?: '))
            b.close()

    def retrieving_data():
        """This function will help the user and the trainer to check the logged data"""

        if clients[client_num] == 1:
            sh=open('shagun.txt')
            print(sh.read())
        elif clients[client_num]==2:
            gu=open('gunjan.txt')
            print(gu.read())
        else:
            bi=open('bibha.txt')
            print(bi.read())

    Writing_data()

    my_retrieve = input('Do you want to retrieve your data? Write "Y" for yes and "N" for no: ')
    if my_retrieve =='Y':
        retrieving_data()
    else:
        pass

my_health()