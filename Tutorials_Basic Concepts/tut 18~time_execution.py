import time

'''
1.We can calculate a program's execution time with the help of time module. time module in time function of
datetime package returns number of ticks i.e seconds
2. in order to calculate local time we can use time.localtime function of the time module. 
3. time.time() returns ticks, time.localtime() returns localtime in a tuple format and time.asctime() converts a 
tuple of time in a more readable format.
4. time.sleep() makes the program sleep for the seconds that are passed in as an argument. 
eg. time.sleep(2) will make the program sleep for 2 sec
'''

initial_time= time.time()

i=0
while i<45:
    print(f'This loop  is to learn the execution time of a while loop which is:{(time.time())- initial_time}')
    i+=1

initial2= time.time()
for i in range(45):
    print(f'This loop  is to learn the execution time of a for loop which is:{(time.time())- initial_time}')

mt= time.asctime((time.localtime(time.time())))
print(mt)
