###TEAM OSIRIS###
import sys

#Sentinel Value used to denote the end of a file
SV = bytearray(b'\x00\xff\x00\x00\xff\x00')


#function to handle proper program usage
def parameters():
	#handle parameters
	if sys.argv[1] == "-r" and ((len(sys.argv) < 4) or (len(sys.argv) > 6)):
		print("Invalid Syntax")
		print("Usage: python Steg.py -r -B -o1024 -i256 -wnew.jpg > extracted.jpg")
		quit()
	if sys.argv[1] == "-s" and ((len(sys.argv) < 5) or (len(sys.argv) > 7)):
		print("Invalid Syntax")
		print("Usage: python Steg.py -s -B -o1024 -i256 -wnew.jpg -hsecret.jpg > extracted.jpg")
		quit()
	if ((sys.argv[1] != "-r") and (sys.argv[1] != "-s")) or (len(sys.argv) < 4):
		print("No mode specified\nQuiting")
		quit()
	#return parameters to not include the python file itself
	params= sys.argv[1:(len(sys.argv))]
	return params

#seperate flags from relevate data
def process_params(parameters):
	#mode should always be the first parameter specified in the command line
	mode=parameters[0].strip("-")
	Bmode=''
	offset=0
	interval=1
	wrapper_file=""
	hidden_file=""
	for i in parameters[1:len(parameters)]:
		if i=="-B":Bmode="B"
		if i=="-b":Bmode="b"
		if "-i" in i: interval=int(i.strip("-i"))
		if "-o" in i: offset=int(i.strip("-o"))
		if "-w" in i: wrapper_file=i.strip("-w")
		if "-h" in i: hidden_file=i.strip("-h")
	'''if mode=="r":
		return mode, Bmode, offset, interval, wrapper_file
	if mode=="s":'''
	return mode, Bmode, offset, interval, wrapper_file, hidden_file

#Store mode (both Byte and bit mode)
def store(Bmode, offset, interval, wrapper_file, hidden_file):
	#Get bytes of wrapper file
	w=open(wrapper_file, "rb")
	wrapper_bytes=bytearray(w.read())
	w.close()

	#Get bytes of hidden file that we intend to store
	H = open(hidden_file, "rb")
	hidden_bytes=bytearray(H.read())
	H.close()

	#Byte Mode
	if Bmode == "B":
		#Storage of our hidden file/data
		i=0
		while i < len(hidden_bytes):
			wrapper_bytes[offset] = hidden_bytes[i]
			offset += interval
			i+=1

		#Storage of Sentinel Bytes so we can acutally extract what we have hidden
		i=0
		while i < len(SV):
			wrapper_bytes[offset] = SV[i]
			offset += interval
			i+=1
	#Bit Mode
	if Bmode == "b":
		i=0
		#Storage of our hidden file/data
		while i < len(hidden_bytes):
			for j in range(8):
				wrapper_bytes[offset] &= 0b11111110
				wrapper_bytes[offset] |= ((hidden_bytes[i] & 0b10000000 >> 7))
				hidden_bytes[1] <<= 1 #This could result in values greater than 1 byte
				offset +=interval
			i+=1
		i=0
		#Storage of Sentinel BYtes so we can acutaly extract what we have hidden
		while i < len(SV):
			for j in range(8):
				wrapper_bytes[offset] &= 0b11111110
				wrapper_bytes[offset] |= ((SV[i] & 0b10000000 >> 7))
				SV[i] <<= 1#This could result in values greater than 1 byte
				offset+=interval
	#Write file to stdout
	sys.stdout.buffer.write(wrapper_bytes)

#retrieve mode (both Byte and bit mode)
def retrieve(Bmode, offset, interval, wrapper_file):
	
	#Get bytes of wrapper file
	w=open(wrapper_file, "rb")
	wrapper_bytes = bytearray(w.read())
	w.close()

	#Empty array that we will hold our exracted file
	#we will turn it into a byte array later
	#This is to better handle the data moving around
	H=[]

	#Conditional Byte or bit check
	#Byte mode
	if Bmode == "B":
		#Variable to check how many sentinel bytes we have hit in a row
		sentinel_byte_iteration=0
		while offset < len(wrapper_bytes):
			B = wrapper_bytes[offset]

			#First check if the Byte does NOT match the current sentinel byte
			#If so add the byte to the return array and reset of sentinel value iteration
			if B != SV[sentinel_byte_iteration]:
				H.append(B)
				sentinel_byte_iteration=0

			#Otherwise it will be a sentinel byte
			else:
				#increase sentinel byte iteration
				sentinel_byte_iteration+=1
				#add the byte to the list
				H.append(B)
				#Check if we have hit all six sentinel bytes in a row
				#If so we are at the end of our file and need to break 
				if sentinel_byte_iteration==6:
					break
			#iterate offset via the interval
			offset+=interval
		

	#bit mode
	if Bmode == "b":
		#Variable to check how many sentinel bytes we have hit in a row
		sentinel_byte_iteration=0
		while offset < len(wrapper_bytes):
			b = 0
			for i in range(8):
				b |= (((wrapper_bytes[offset])) & 0b00000001 )
				if i < 7:
					b <<= 1
					offset+=interval
			#if b is not equal to the current sentinel byte append the byte
			if b != SV[sentinel_byte_iteration]:
				H.append(b)
				sentinel_byte_iteration=0
			#Otherwise increase the sentinel byte iteration and append the byte
			else:
				sentinel_byte_iteration+=1
				H.append(b)
			#Check if we have hit all the sentinel bytes and if so then we break out of the loop and return our extracted file
			if sentinel_byte_iteration==6:
				break
			#iterate the offset value by the interval
			offset+=interval

	#finally we cut off the last 6 appened bytes from the byte array
	#this is to handle the sentinel value that we do not want in our final byte array
	H = H[0:len(H)-6]
	sys.stdout.buffer.write(bytearray(H))

	
def main():
	#Get parameters to pass to retrieve/store function
	mode, Bmode, offset, interval, wrapper_file, hidden_file = process_params(parameters())
	#If mode is set to retrieve
	if mode == "r":
		retrieve(Bmode, offset, interval, wrapper_file)
	#If mode is set to store
	if mode == "s":
		store(Bmode, offset, interval, wrapper_file, hidden_file)

##########
###MAIN###
##########
main()

