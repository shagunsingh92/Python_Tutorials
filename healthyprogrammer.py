import datetime
import pygame
import schedule
import time
pygame.mixer.init()
'''
Mini project : This is an alarm system which reminds one to drink water, do physical exercise and an eye exercise.
An MP3/ogg file is played every 45 mins reminding the user to drink water. Another song is played every hour 
reminding the user about physical exercise and similarly one more song is played every 30 mins to remind the 
user about doing an eye exercise.This alarm system works only between 9:00 Am to 6:00 Pm
'''

print('''My Alarm System
        - Created by Shagun Singh\n''')

# x= time.asctime(time.localtime(time.time()))
# print(x)

# time_limit = time.strftime('%H:%M:%S') #variable is needed to put a time limitation on the activities
z = datetime.datetime.now()
time_limit = z.strftime('%H:%M:%S')

def my_time():
    '''This function logs in the time when a particular activity was performed by a user.'''
    mytime=[]
    y= datetime.datetime.now()
    mytime.append(y.strftime('%d-%b-%Y'))
    mytime.append(y.strftime('%H:%M:%S'))
    return mytime


def my_water_alarm():
    '''This function plays the alarm in an infinite loop until "yes" is given as input - drinking water
    loop.

    In part 1 of the code if we pass on -1 as an argument to the play function, the song will be played
    on an infinite loop.

    The part 2 of the code is required, if we want to play the music only for a few loops.This loops
    waits and checks with the above code is busy playing the music or not. If the below part of the code is
    not there music.play() will start and stop the music immediately and nothing can be heard

    Part 3 of the code logs the data into a text file

    In part 3 of the code music will keep playing even after we break out of the loop if we do not run the
    music.stop() function

    In part 3 of the code the data will not get logged in the text file if we do not break from the loop'''

    while True:
        # Part 1
        pygame.mixer.music.load('drink_water.ogg')
        pygame.mixer.music.play(-1)

        # Part 2
        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(15)
            #need to pass in some tick value here

        # Part 3
        Command = input('Did you drink water: ')
        if Command == 'yes':
            water_log = open('my_water_log.txt','a+')
            water_log.write(str(my_time()))
            water_log.write(':')
            water_log.write(' Shagun drank water')
            water_log.write('\n')
            pygame.mixer.music.stop()
            break
        else:
            continue

def my_physical_alarm():
    '''This function plays the alarm in an infinite loop until "yes" is given as input - physical exercise
    loop '''

    while True:
        # Part 1
        pygame.mixer.music.load('pysical_exercise.ogg') #python works quite easily with an ogg file
        pygame.mixer.music.play(-1)

        # Part 2
        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(15)

        # Part 3
        Command = input('Did you do physical exercise? : ')
        if Command == 'yes':
            water_log = open('my_phy_exercise_log.txt','a+')
            water_log.write(str(my_time()))
            water_log.write(':')
            water_log.write(' Shagun did physical exercise')
            water_log.write('\n')
            pygame.mixer.music.stop()
            break
        else:
            continue


def my_eye_alarm():
    '''Plays the alarm in an infinite loop until "yes" is given as input - eye exercise loop'''

    while True:
        # Part 1
        pygame.mixer.music.load('eye_exercise.ogg')
        pygame.mixer.music.play(-1)

        # Part 2
        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(15)

        # Part 3
        Command = input('Did you do an eye exercise? : ')
        if Command == 'yes':
            water_log = open('my_eye_exercise_log.txt', 'a+')
            water_log.write('\n')
            water_log.write(str(my_time()))
            water_log.write(':')
            water_log.write(' Shagun did eye exercise')
            pygame.mixer.music.stop()
            break
        else:
            continue


#This else-if statement will put a time limitation on the code.
if time_limit >= '09:00:00' and time_limit<= '18:00:00':
    schedule.every(1).minutes.do(my_water_alarm)
    schedule.every(1).hours.do(my_physical_alarm)
    schedule.every(3).minutes.do(my_eye_alarm)
    while True:
        schedule.run_pending()