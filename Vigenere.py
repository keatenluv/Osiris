key = input('What is the key?\n')
text = input('What would you like to encode?\n')
#key_repeat = []

def fix_key(text,key):
    #key.split()
    global keylist
    keylist = [char for char in key]

    for index in range(len(text)):
        keylist.append(key)
    return key




# The code below this is an almost working way to make the key long enough to cypher text longer than the given key
#    while True: #make a list of the key repeating so that it's long enough for the string to be deciphered
#        key_repeat.append(key)
#        if (len(key_repeat) >= len(text)): 
#            for x in key_repeat:
#                global keyString 
#                keyString = ''
#                keyString += x
#            #key_repeat = ('' .join(key_repeat))
#            return(keyString)
#            break
    #return("" .join(key_repeat))


def vigenereCypher(text, keylist):
    to_cypher = []

    #make an empty list for the cyphered string to go into
    for i in range(len(text)):
        new = (ord(text[i]) + ord(keylist[i])) % 26
        print(new)
        # % gives the remainder after a division has taken place = that positioning is our letter
        #ord() returns the number representing the unicode code of a specified character
        new += ord('A')
        to_cypher.append(chr(new)) #add the new character to the list
   
    return('' .join(to_cypher)) #.join makes everything into a string


fix_key(text,key)    
print(key)
print(vigenereCypher(text,keylist))