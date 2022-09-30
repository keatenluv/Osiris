from ftplib import FTP

#accessing the ftp server in Timo's office
#IP: 138.47.132.114 - wireless, 138.47.99.64 - ethernet, both the same files
#he has more files stored in directories "/10" and "/7"
IP = "138.47.157.24"
PORT = 8008
USER = "osiris"
PASSWORD = "encryptiongods"
FOLDER1 = "/.secretstorage/.folder2/.howaboutonemore"
FOLDER2 = "/.secretstorage/.folder3/.becausewhynot"
USE_PASSIVE = True

ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)



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

def double_method(files):
    charList7=""
    charList10=""
    directory_list=[]
    #iterate through files, select only files with "---" as first three permissions, 
    #append the last 7 characters of permissions to charList
    for file in files:
        #if[file[0] == "d"]:
            #directory_list.append(file)
        if (file[0] == '-' and file[1] == '-' and file[2] == '-'):
            charList7 += file[3:10]

    #iterate through the files, appened the entire permissions of each file to charList
    for file in files:
        charList10 += file[0:10]
    return(charList7, charList10)#, directory_list)


def get_files_from(Directory, ftp_object):
    #list to hold our files
    files=[]
    #change into desired directory
    ftp_object.cwd(Directory)
    #list files and append to list
    ftp_object.dir(files.append)

    #ftp_object.readlines(files.append)
    #return files
    return(files)

#decode output (7 & 10) of one directory at a time
def one_dir(files):
   
    #get charlist from retrived file permissions
    #charList7, charList10, directory_list= double_method(files)
    charList7, charList10 = double_method(files)

    #convert 7-bit charList to binary
    binary7 = charToBinary(charList7)

    #convert 10-bit charlist to binary
    binary10 = charToBinary(charList10)

    #convert 7-bit binary to user output
    seven_bit_output = binaryToOutput(binary7)

    #convert 10-bit binary to user output
    ten_bit_output = binaryToOutput(binary10)

    #attemp to print both of the covert messages
    print("7-bit output: {}".format(seven_bit_output))
    print("10-bit output: {}".format(ten_bit_output))
    print("\n")

#traverse directories to find messages hidden in other directories
def dir_loop():
    print("Current Directory: {}".format(FOLDER1))
    files=get_files_from(FOLDER1, ftp)
    one_dir(files)

    print("Current Directory: {}".format(FOLDER2))
    files=get_files_from(FOLDER2, ftp)
    one_dir(files)
    


####MAIN####
dir_loop()
ftp.quit()