# Team Osiris
# Ethan Hebert, Amiyah Frierson, Jay Reich, Jace Peloquin
# Keaton Love, Madeline Ballew, Noah Jones
# Program 4 - Chat (Timing) Covert Channel
# 10-7-22
# CSC-442

# use Python 3
import socket
import time

# set the port for client connections
port = 1337

#covert message time gaps
ZERO = 0.01
ONE = 0.1

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

# listen for clients
# this is a blocking call
s.listen(0)
print("Server is listening...")

# a client has connected!
c, addr = s.accept()

# set the overt message
msg = "Around the world, around the world, around the world, around the world, around the world. -- Daft Punk\n"

#set the covert message and convert to binary
covert = "COV3RT" + "EOF"
covert_bin = ""
for i in covert:
    covert_bin += bin(ord(i))[2:].zfill(8)
    #character to ascii value to binary, remove the 0b at the beginning with [2:], 
	# make it 8 bits by adding a 0 at front with .zfill(8)
curr = 0

# send the message, one letter at a time
for i in msg:
	c.send(i.encode())

	# delay a bit in between each letter based on binary
	if (covert_bin[curr] == "0"):
		time.sleep(ZERO)
	else:
		time.sleep(ONE)

	curr = (curr + 1) % len(covert_bin)

# send EOF and close the connection to the client
c.send("EOF".encode())
print("Message sent...")
c.close()