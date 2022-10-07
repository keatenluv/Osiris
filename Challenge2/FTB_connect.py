from ftplib import FTP

# IP = "138.47.132.114"
# IP = "138.47.99.64"
IP = "138.47.134.55"
PORT = 21
USER = "anonymous"
# USER = "osiris"
PASSWORD = ""
FOLDER = "/"
USE_PASSIVE = True
METHOD = 7


ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

ftp.cwd(FOLDER)

files = []

ftp.dir(files.append)

ftp.quit()

for f in files:
    print(f) # they are strings
    # print(type(f))
    
if METHOD == 7:
    temp = []
    for f in files:
        if f[0] != "-" or f[1] != "-" or f[2] != "-":
            continue
        
        temp.append(f[3:10])
    
    # for f in temp:
    #     print(f)
    
    newList = []
    for item in temp:
        s = ""
        for c in item:
            if c == '-':
                s = s + "0"
            else:
                s = s + "1"
        newList.append(s)
    
    # for f in newList:
    #     print(f)

    decodedMessage = ""
    for item in newList:
        decodedMessage = decodedMessage + chr(int(item, 2))
    
    print(decodedMessage)

if METHOD == 10:
    encodedStr = ""
    for f in files:
        temp = ""
        item = f[0:10]
        # print(item)
        for c in item:
            if c == '-':
                encodedStr += "0"
            else:
                encodedStr += "1"
    
    print(encodedStr)
    
    message = ''
    for i in range(len(encodedStr)//7):
        chara = (chr(int(encodedStr[i*7:i*7+7],2)))
        message = message + chara
        # print(chara, end="")
    print()
    print(message)
    
