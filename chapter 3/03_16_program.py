#python program for greeting the user according to time

#import time module
import time

#taking the time as an integer value from strftime method of time module
second = int(time.strftime('%S'))
minute = int(time.strftime('%M'))
hours = int(time.strftime('%H'))

timestamp = time.strftime('%H:%M:%S')

print(timestamp)
print(hours)
print(minute)
print(second)

#creating the time separation for greeting 
while 1:
    if (hours == 9 and minute == 41 and second == 50):
        print('Good Morning')