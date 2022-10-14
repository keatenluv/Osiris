# use Python 3
import socket
from sys import stdout
from time import time

# enables debugging output
DEBUG = 0

# set the server's IP address and port
# my server/client: ip = "localhost", port = 1337
# Timo server/client: ip= "138.47.99.64", port = 1337
# 2nd Timo server: ip= "138.47.102.167", port = 1337
IP = "138.47.102.167"
PORT = 33333

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#print connection message
print("[connect to the chat server]")
print("...")

# connect to the server
s.connect((IP, PORT))

#contains the covert in binary
covert_bin = ""

# receive data until EOF
data = s.recv(4096).decode()
i = 0
while (i < 2000):
	# output the data
	i += 1
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096).decode()
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)

    #debug - print out the time for every character
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

	#read the time gaps to append to covert binary
	if (delta > 0.15):
		covert_bin += "1"
	else:
		covert_bin += "0"
	
# close the connection to the server
s.close()

#print disconnection message
print("...")
print("[disconnent from the chat server]")

#print the binary of the covert message
#print(covert_bin)

#convert binary with 8 bit ASCII
charBinary = ""
covert = ""
for digit in covert_bin:
    charBinary += digit
    #every 8 bits, convert binary to integer to char, append to plaintext8
    if (len(charBinary) % 8 == 0):
        covert += chr(int(charBinary, 2))
        charBinary = ""

#cut off any repeat in the covert message and print it
repeatIndex = covert.find("EOF")
covert = covert[:repeatIndex]
print("Covert message: " + covert)