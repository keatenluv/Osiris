import sys

#read the binary input
binaryWord = sys.stdin.read()
binary = ""
for letter in binaryWord:
    if (letter == "O"):
        binary += "1"
    elif (letter == "Z"):
        binary += "0"

#convert binary with 7 bit ASCII
charBinary = ""
plaintext7 = ""
for digit in binary:
    charBinary += digit
    #every 7 bits, convert binary to integer to char, append to plaintext7
    if (len(charBinary) % 7 == 0):
        plaintext7 += chr(int(charBinary, 2))
        charBinary = ""

#convert binary with 8 bit ASCII
charBinary = ""
plaintext8 = ""
for digit in binary:
    charBinary += digit
    #every 8 bits, convert binary to integer to char, append to plaintext8
    if (len(charBinary) % 8 == 0):
        plaintext8 += chr(int(charBinary, 2))
        charBinary = ""

#print the 7 and 8 bit ASCII outputs, in case of error print nothing
try:
    sys.stdout.write("7-bit:\n")
    sys.stdout.write(plaintext7 + "\n")
except:
    print()
    
print()

try:
    sys.stdout.write("8-bit:\n")
    sys.stdout.write(plaintext8 + "\n")
except:
    print()
