
# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    print("Encrypting...")
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    print("Done")
    return ("" . join(cipher_text))

def generateKey(string, kraw):
    key = list(kraw)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
    

selection = int(input("What would you like to do today?\n 1 for creating a key\n 2 for encrypting an HTML file\n 3 for Decrypting an HTML file\n"))

def kquery():
    have = str(input("Do you have a key or do you need to make one? h/m\n"))
    if have == str("h"):
         keypath = input("Enter filepath for key location (.txt file): ")
         with open(keypath,"r") as file:
            k = file.read().rstrip()
         klist = list(k)
         print(klist)
         return klist
    else:
        import random                                           #Imports Random
        keylong = int(input("Enter Key Length Integer: "))      #Gets integer of how long key should be
        keything = ''                                           #Initializing key storage
        keychain = ''                                           #initializing keychain storage
        asciicode = list(map(chr, range(32, 126)))              #Creates List "asciicode" using Ascii digits
        keychain = (random.choices(asciicode, k=keylong))       #Randomly selects digits from "asciicode", "keylong" amount of times, stores in List "keychain"
        keything = ''.join(map(str,keychain))                   #Turns List "keychain" into a string "keything"
        print("Your Key is ==>"+keything+"<== Please create a text doc and store the key inside.")
        return keything
        
def fileenc():
    import sys
    import os
    import codecs 
    userpath = input("Enter filepath for HTML file you would like to encrypt: ")
    filename = input("What shoiuld the name of the new file be? (Do not add file extension ending, .htm, .html, etc.")
    with codecs.open(userpath,"r") as file:
        fstring = file.read().rstrip()
    flist = list(fstring)
    fjoin = ''.join(flist)
    return flist

    
if (selection == 1):
    key = kquery()

elif (selection == 2):
    kraw = kquery()
    string = fileenc()
    key = generateKey(string,kraw)
    print (cipherText(string, key))
    


