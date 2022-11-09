###TEAM: OSIRIS (Noah Jones, Ethan Herbert, Jace Peloquin, Amiyah Frierson, Jay Reich, Keaton Love, Madeline Ballew )
import sys

#Read from stdin (first file passed in command line)
to_be_xord = sys.stdin.buffer.read()

#Open hard coded key file in binary read mode
key=open("k3y", "rb")
#key=open("key2", "rb")

#Turn key value into a byte array and close key file
key_bytes=bytearray(key.read())
key.close()

#List to hold our final output (either ciphertext or plaintext)
final=[]

#Loop through both the (plain or cipher text) and the key values
#The zip function will loop through 2 lists until the loop reaches the end of one
for i, j in zip(to_be_xord, key_bytes):
	final.append(i ^ j)

#write output to a file if provided with an output redirection, otherwise it will print it to stdout
sys.stdout.buffer.write(bytes(final))