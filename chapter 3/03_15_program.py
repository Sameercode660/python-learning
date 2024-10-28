#creating a clock using time and os module

#import time and os module
import time
import os

#declaring the time of the beginning

miliSecond = 0
second = 0
minute = 0
hours = 0

while 1:
    miliSecond += 1

    if miliSecond == 10:
        miliSecond = 0
        second += 1
        
    elif second == 60:
        second = 0
        minute += 1

    elif minute == 60:
        minute = 0
        hours += 1
    
    os.system('cls')
    print(hours,":",minute,":",second)