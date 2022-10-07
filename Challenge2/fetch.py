# Team Osiris
# Ethan Hebert, Amiyah Frierson, Jay Reich, Jace Peloquin
# Keaton Love, Madeline Ballew, Noah Jones
# Program 3 - FTP Covert Channel
# 9-28-22
# CSC-442

from ftplib import FTP

#value to decode the last 7 bits of each file permission (7) or all 10 bits (10)
METHOD = 7

#accessing the ftp server in Timo's office
#IP: 138.47.132.114 - wireless, 138.47.99.64 - ethernet, both the same files
#he has more files stored in directories "/10" and "/7"
IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7"
USE_PASSIVE = True

ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)
ftp.cwd(FOLDER)

#append the files in the current directory to the list files
files = []
ftp.dir(files.append)

#log off of the ftp server once done
ftp.quit()


### DECODING COVERT MESSAGE ###
charList = ""
binary = ""
output = ""

def charToBinary(charList):
    binary = ""
    #"-" encodes a 0, any other character encodes a 1, append to binary
    for char in charList:
        if (char == "-"):
            binary += "0"
        else:
            binary += "1"
    return binary

def binaryToOutput(binary):
    #convert binary with 7 bit ASCII
    charBinary = ""
    output = ""
    for digit in binary:
        charBinary += digit
        #every 7 bits, convert binary to integer to char, append to output
        if (len(charBinary) % 7 == 0):
            output += chr(int(charBinary, 2))
            charBinary = ""
    return output

if (METHOD == 7):
    #iterate through files, select only files with "---" as first three permissions, 
    #append the last 7 characters of permissions to charList
    for file in files:
        if (file[0] == '-' and file[1] == '-' and file[2] == '-'):
            charList += file[3:10]

elif (METHOD == 10):
    #iterate through the files, appened the entire permissions of each file to charList
    for file in files:
        charList += file[0:10]


#convert charList to binary
binary = charToBinary(charList)

#convert binary to user output
output = binaryToOutput(binary)

#print the covert message
print(output)