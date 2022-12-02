# Computer-Network-Security
**Repo for University Cyber Security Class**
	
This class introduced us to topics such as:
* Computer Networks
* Cryptography 
* Computer Network Defense
* Covert Channels
* Reverse Engineering
* Keystroke Dynamics
* Access Control
* Database Management Systems & Exploits
* Web Site Exploitation

*This repo houses all programs developed for this class and directions for using them.*<br>


## Osiris_binary.py program file
This is a Binary decoder python program that can auto-detect and decode 7 or 8-bit binary encoded files
Syntax Example:
```
python Osiris_binary.py File_to_decode.txt
```
## Osiris_xor.py program file
This is an XOR encryptor and decrypter program that implements the XOR cryptography method

Encryption Syntax example:
```
python Osiris_xor.py < plaintext.txt > ciphertext.txt
```
Decryption Syntax Example:
```
pyhton Osiris_xor.py < ciphertext.txt > extracted_plaintext.txt
```
## steg.py steganography file
This a steganography program that can both store and retrieve hidden files either via bytes or bits
The required flags include: 
- (-r or -s) for retrieving or storing
- (-B or -b) for Byte mode or bit mode
- (-o) for the byte offset
- (-i) for the interval
- (-w) for the wrapper file
- (-h) for the hidden file that will be stored, this is only used for storing mode

Syntax examples:
```
python steg.py -r -B -o1024 -i8 -wsecret_file.jpg > extracted_data.jpg

pyhton steg.py -s -b -o1024 -i8 -wnormal_file.jpg -hmy_secret_message.txt > secret_picture.jpg

```
## Vigenere.py program file
Encodes/decodes secret messages with a key. Usually, the key is given.

Encryption Syntax example:
```
python vigenere.py -e mykey
```
Decryption Syntax example:
```
python vigenere.py -d mykey
```
## timelock.py program file
Reads in an epoch time and the current system time to output a code from an MD5 hash typically used to enter an FTP server.
Can change the epoch time and current system time manually. Can change the code from the hash. Use debug mode.

Syntax example:
```
echo “1999 12 31 23 59 59” | python timelock.py
```
## chat_client.py & chat_server.py program files
Reads a covert message from the binary of 2 different time gaps between letters being sent in an overt message, ends on “EOF”.
Use debug mode to reveal time gaps and alter times in code accordingly. If no "EOF" ending, hardcode while loop for a certain number of intervals.
Server code shouldn't be used but shows what the server side looks like.

Syntax example:
```
python chat_client.py
```
## fetch.py program file
Extracts a secret message from the file permissions of an FTP server. Can change the IP address of the server, the port, username, password, folder, and method (right-most 7 bits or all 10 bits).

Syntax example:
```
python fetch.py
```
## iter.bash steganography file
This is a bash file that does several iterations of steg.py. When using this file, the file steg.py must be in the same directory.
Note:
- This file should be used in a separate subfolder/directory because it will cause a lot of clutter
- It takes one argument, the name of the file to retrieve data from
- If you want to change the values used for the offset and intervals, change to two lists in the file 

Syntax examples
```
bash iter.bash filename.txt
```
## Vigenere Website with a nice user interface
[Vigenere Decoder](https://www.dcode.fr/vigenere-cipher)
