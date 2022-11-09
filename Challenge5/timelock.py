# Team Osiris
# Ethan Hebert, Amiyah Frierson, Jay Reich, Jace Peloquin
# Keaton Love, Madeline Ballew, Noah Jones
# Program 5 - TimeLock
# 10-20-22
# CSC-442

from curses.ascii import isdigit
from lzma import FORMAT_ALONE
from sys import stdin 
from datetime import datetime
from hashlib import md5
import pytz


INTERVAL = 60
DATETIME_FORMAT = "%Y %m %d %H %M %S"
DEBUG = 1

#switiching btwn inputted or hardcoded time
#must input the epoch when running, curr is the current system time
#MANUAL_EPOCH = "2017 04 23 18 02 30"
MANUAL_EPOCH = ""
#MANUAL_CURR = "2017 04 26 15 14 30"
MANUAL_CURR = ""


def getHash(str):
    #double md5 hash the input
    hash = md5(str.encode()).hexdigest()
    hash2 = md5(hash.encode()).hexdigest()

    code = ""
    #append the first 2 letters [a-f] left-to-right
    for char in hash2:
        if (ord('a') <= ord(char) <= ord('f')):
            code += char
            if (len(code) == 2):
                break

    #append the first 2 digits [0-9] right-to-left in the hash
    for char in reversed(hash2):
        if (char.isdigit()):
            code += char
            if (len(code) == 4):
                break
            
    #append charater forom the middle of the hash
    code += hash2[len(hash2)//2]
    
    if (DEBUG):
        print("MD5 #1: " + hash)
        print("MD5 #2: " + hash2)
        print("Code: " + code)

    return code

def utc(time):
    time_local = datetime.strptime(time, DATETIME_FORMAT)
    time_utc = time_local.astimezone(pytz.UTC)
    return time_utc

def calcSeconds(curr, epoch):
    #convert both times to UTC timezone
    curr_utc = utc(curr)
    epoch_utc = utc(epoch)

    #calculate the seconds difference btwn 2 times in UTC
    seconds = int((curr_utc - epoch_utc).total_seconds())

    #rollback the seconds based on the interval
    secondsInterval = seconds - (seconds % INTERVAL)

    #print out both times in UTC and both seconds values
    if (DEBUG):
        print("Current (UTC): " + curr_utc.strftime(DATETIME_FORMAT))
        print("Epoch (UTC): " + epoch_utc.strftime(DATETIME_FORMAT))
        print("Seconds: " + str(seconds))
        print("Seconds Interval: " + str(secondsInterval))

    return secondsInterval

### MAIN PROGRAM ###
#read the epoch time from stdin or hardcoded
if (MANUAL_EPOCH == ""):
    epoch = stdin.readline().rstrip()
else:
    epoch = MANUAL_EPOCH

#read the current computer time or hardcoded value
if (MANUAL_CURR == ""):
    curr = datetime.now()
    curr = curr.strftime(DATETIME_FORMAT)
else:
    curr = MANUAL_CURR

#calculate the seconds difference btwn 2 times
#and scale it back based on the interval
secondsInterval = calcSeconds(curr, epoch)

#hash the resulting seconds value
code = getHash(str(secondsInterval))

print(code)
