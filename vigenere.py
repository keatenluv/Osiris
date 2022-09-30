import sys

def keySolve():
    key = sys.argv[2].lower() #turn the key to all lowercase
    #an array of the key values a-z mapped 0-25
    keyArray=[]
    for char in key:
        if (ord('a') <= ord(char) <= ord('z')): #ignore any characters that aren't letters
            keyArray.append(ord(char) - ord('a'))
    
    return keyArray

def encrypt():
    #read the user input
    plaintext = input()
    ciphertext = ""
    keyValue = 0
    
    #iterate through the input and encrypt it
    for char in plaintext:

        #lowercase - transfer to values 0-25, shift by keyValue, transfer back up to ASCII
        if (ord('a') <= ord(char) <= ord('z')):
            newChar = ord(char) - ord('a')
            newChar = (newChar + keyArray[keyValue]) % 26
            newChar += ord('a')
            ciphertext += chr(newChar)
            keyValue = (keyValue + 1) % len(keyArray) #iterate keyValue
        
        #uppercase - transfer to values 0-25, shift by keyValue, transfer back up to ASCII
        elif (ord('A') <= ord(char) <= ord('Z')):
            newChar = ord(char) - ord('A')
            newChar = (newChar + keyArray[keyValue]) % 26
            newChar += ord('A')
            ciphertext += chr(newChar)
            keyValue = (keyValue + 1) % len(keyArray)

        #extra characters (ignore)
        else:
            ciphertext += char

    #output ciphertext
    return ciphertext

def decrypt():
    #read the user input
    ciphertext = input()
    plaintext = ""
    keyValue = 0

    #iterate through the input and encrypt it
    for char in ciphertext:

        #lowercase - transfer to values 0-25, shift by keyValue, transfer back up to ASCII
        if (ord('a') <= ord(char) <= ord('z')):
            newChar = ord(char) - ord('a')
            newChar = (26 + newChar - keyArray[keyValue]) % 26
            newChar += ord('a')
            plaintext += chr(newChar)
            keyValue = (keyValue + 1) % len(keyArray)
        
        #uppercase - transfer to values 0-25, shift by keyValue, transfer back up to ASCII
        elif (ord('A') <= ord(char) <= ord('Z')):
            newChar = ord(char) - ord('A')
            newChar = (26 + newChar - keyArray[keyValue]) % 26
            newChar += ord('A')
            plaintext += chr(newChar)
            keyValue = (keyValue + 1) % len(keyArray)

        #extra characters (ignore)
        else:
            plaintext += char
        
    #output ciphertext
    return plaintext
    
#check if user inputs correct arguments
if (len(sys.argv) == 3):

    #get the key as an array of shift values
    keyArray = keySolve()
    
    #encryption
    if (sys.argv[1] == "-e"): 
        while(1):
            try:
                output = encrypt()
                sys.stdout.write(output + "\n")
            except:
                break
        
    #decryption
    elif (sys.argv[1] == "-d"):
        while(1):
            try:
                output = decrypt()
                sys.stdout.write(output + "\n")
            except:
                break

    else:
        print("Format: python vigenere.py mode key\nmode: '-e' = encryption, '-d' = decryption, key: custom key")

else:
    print("Format: python vigenere.py mode key\nmode: '-e' = encryption, '-d' = decryption, key: custom key")