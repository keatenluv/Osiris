#TEAM NAME: Osiris
import sys,re
def get_data():
	file=open(sys.argv[1], "r")	#open file from passed arguments
	data=file.read()			#put the contents into a string
	file.close()				#close file
	data=data.strip()			#get rid of new line characters (the actual ones not the ones encoded in binary)
	size=bit_size(data)			#separate the bytes based on bit size
	if size == 7:
		res=re.findall('.......', data)		#regular expression
	elif size == 8:
		res=re.findall('........', data)
	return res

#function to figure out if we are in 7 or 8 bit encoding
def bit_size(data):
	if(len(data)%8 == 0):		#8 bit size
		bit_size=8
	
	if(len(data)%7 == 0):		#7 bit size
		bit_size=7

	return bit_size				#return bit size to use in further calculations

def main():
	if len(sys.argv) < 2:		#program usage check
		print("Usage: Osiris_binary.py file_to_decrypt.txt\nExiting")
		exit()
	data=get_data()				#get the bytes to decode
	for i in data:				#for loop to print out message
		x = (int(i,2))			#convert byte to integer 
		print(chr(x), end="")	#convert integer to character


###	MAIN ###
main()

